import matplotlib.pyplot as plt

import os as os
import sys

sys.path.insert(0, './')

import Individual as Individual
import copy as copy
import operator as operator
import random as random
import Timer as Timer

sys.path.insert(0, '../')

import GraphicMotor.InitFileNotSI2_PlanningRange as IF
# import GraphicMotor.InitFileNotSI2_PlanningRange_LCG as IF
# import GraphicMotor.InitFileNotSI2_PlanningRange_VCG as IF


class Population():
    
    #docstring
    """(docstring) Classe Population"""
    
    def __init__ (self, initialIndividual, fitnessFunctionNameString, args=(), mutationRate=0.5, populationSize = 100, nbMaxGeneration=10):
        self.populationSize = populationSize
        self.mutationRate = mutationRate
        
        self.nbMaxGeneration = nbMaxGeneration
        self.initialIndividual = initialIndividual
        
        self.fitnessFunctionNameString = fitnessFunctionNameString
        self.args = args
        
        self.population = [None]*self.populationSize
        self.initiatePopulation()
        
        #print(self.population)
        
        self.bestIndividual = self.population[self.populationSize-1]
    
    
        
    def __str__(self):
        rep = ""
        for i in range(0, self.populationSize):
            print("\n\n\n\n\n\n                                             #####################   Individual n°{}   ###########################".format(i))
            print(self.population[i])
        return rep
    
    
    def initiatePopulation (self):
        #comment faire, garder l'indiv initial et random pour les autres ??
        
        print("\nInitialization of Population")
        
        self.population[0] = copy.deepcopy(self.initialIndividual)
        self.population[0].calc(getattr(self.population[0], self.fitnessFunctionNameString), self.args)
        
        for i in range (1, self.populationSize):
            self.population[i] = self.initiateIndividual()
            self.population[i].calc(getattr(self.population[i], self.fitnessFunctionNameString), self.args)
        self.sort(True)
        self.bestIndividual = self.population[self.populationSize - 1]
        #self.population = sorted(self.population, key=operator.attrgetter("fitness"), reverse=True)
        for i in range(self.populationSize):
            print("fitness : {}".format(self.population[i].fitness))
            
    def initiateIndividual(self):
        indiv = copy.deepcopy(self.initialIndividual)
        indiv.randomize(self.initialIndividual.inputParametersAll)
        res = indiv.checkTheta()
        if (not res):
            while(not res):
                indiv.randomize(self.initialIndividual.inputParametersAll)
                res = indiv.checkTheta()
        return indiv
    
    def initiateIndividual2(self):    #test si ca modifie pas 2 trucs   #creates an individual with random values in the range of the model possibles values
        indiv = copy.deepcopy(self.initialIndividual)
        for key in indiv.inputParametersVariable.keys():
            var = random.randint(0, 100 * self.initialIndividual.inputParametersAll[key]['variation'] - 1 )
            var = var / 10000   #random variation pourcentage
            sign = random.randint(0,1)  #random sign since we allow the range of + or - the initial variation percentage
            if (sign):
                indiv.inputParametersVariable[key]['value']  = (1 + var) * self.initialIndividual.inputParametersVariable[key]['value']
            else:
                indiv.inputParametersVariable[key]['value']  = (1 - var) * self.initialIndividual.inputParametersVariable[key]['value']
        return indiv
    
    def mutateIndividual(self, indiv):     #check
        rand = random.random()
        if (rand<=self.mutationRate):
            indiv.mutate(self.initialIndividual.inputParametersAll)
        #return indiv
    
    def rankSelection(self):   #for rank selection, individuals must be sorted so that the best individuals have the highest ranks (from 1 to N / attention, in the population tab, goes from 0 to N-1)
        #as in our case, we only want to minimize values (drag, thrust, required power and vertical motion), we need to sort in reverse order
        
        childrenIndividuals = [None]*self.populationSize
        
        sumOfRanks = self.populationSize*(self.populationSize+1)/2
        selectionProbability = [None]*self.populationSize
        selectionValueRange = [None]*self.populationSize
        selectionValueRange[0] = 1
        for i in range(1, self.populationSize):
            selectionValueRange[i] = selectionValueRange[i-1] + (i + 1)
        totalOfRanksForSelection = 0
        for i in range(self.populationSize):
            totalOfRanksForSelection = totalOfRanksForSelection + selectionValueRange[i]
        for i in range(self.populationSize):
            selectionProbability[i] = selectionValueRange[i]/totalOfRanksForSelection
            
        def temp_function(randomNumber, selectionValueRangeTab):
            j=0
            while (j < (self.populationSize - 1)):
                if (selectionValueRangeTab[j]<= randomNumber and randomNumber < selectionValueRangeTab[j+1]):
                    break
                else:
                    j = j+1
            return j
          
        print(selectionProbability)
        print(selectionValueRange)
        print(sumOfRanks)
        print(totalOfRanksForSelection)
        
        for i in range(self.populationSize):     #selection of 2 individuals each time to cross them together -> creation of as many children as parents
            rand1 = random.randint(1,totalOfRanksForSelection)
            rand2 = random.randint(1,totalOfRanksForSelection)
            
            #print("rand 1 et 2 : {}    {}".format(rand1,rand2))
            
            indParent1 = temp_function(rand1, selectionValueRange)
            parent1 = self.population[indParent1]
            indParent2 = temp_function(rand2, selectionValueRange)
            print("rand 1 et 2 : {}    {}".format(indParent1,indParent2))
            while(indParent1 == indParent2):
                rand2 = random.randint(1,sumOfRanks)
                indParent2 = temp_function(rand2, selectionValueRange)
                print("rand 2 : {} ".format(indParent2))
            parent2 = self.population[indParent2]
            
            childrenIndividuals[i] = parent1.crossover(parent2)
        
            self.mutateIndividual(childrenIndividuals[i])             #check if it works
            childrenIndividuals[i].calc(getattr(childrenIndividuals[i], self.fitnessFunctionNameString), self.args)
        
            boolTheta = childrenIndividuals[i].checkTheta()
            
            if(not boolTheta):
                while(not boolTheta):
                    rand1 = random.randint(1,totalOfRanksForSelection)
                    rand2 = random.randint(1,totalOfRanksForSelection)
                    
                    #print("rand 1 et 2 : {}    {}".format(rand1,rand2))
                    
                    indParent1 = temp_function(rand1, selectionValueRange)
                    parent1 = self.population[indParent1]
                    indParent2 = temp_function(rand2, selectionValueRange)
                    print("rand 1 et 2 : {}    {}".format(indParent1,indParent2))
                    while(indParent1 == indParent2):
                        rand2 = random.randint(1,sumOfRanks)
                        indParent2 = temp_function(rand2, selectionValueRange)
                        print("rand 2 : {} ".format(indParent2))
                    parent2 = self.population[indParent2]
                    
                    childrenIndividuals[i] = parent1.crossover(parent2)
                
                    self.mutateIndividual(childrenIndividuals[i])             #check if it works
                    childrenIndividuals[i].calc(getattr(childrenIndividuals[i], self.fitnessFunctionNameString), self.args)
                
                    boolTheta = childrenIndividuals[i].checkTheta()
        
        
        
        # for i in range(self.populationSize):
        #     self.mutateIndividual(childrenIndividuals[i])             #check if it works
        #     childrenIndividuals[i].calc(getattr(childrenIndividuals[i], self.fitnessFunctionNameString), self.args)
        
        """
        j=0
        while(j<self.populationSize):
            if (not childrenIndividuals[j].isPlanning):
                del childrenIndividuals[j]
            else:
                j = j+1
        """
            
        print("nbChildren : {}".format(len(childrenIndividuals)))
        
        childrenIndividuals = sorted(childrenIndividuals, key=operator.attrgetter("fitness"), reverse=True)
        return childrenIndividuals
        
        
        
    def tournamentSelection(self, k):   #k is an int
        pass
        
    def newGenerationElitism(self):
        pass
        
        
    def nextGeneration(self, selectionFunction, selectionFunctionArgs = ()):
        
        
        childrenIndividuals = functionWrapper(selectionFunction, selectionFunctionArgs)
        
        #print("nbChildren : {}".format(len(childrenIndividuals)))
        
        rateOfParentsToKeep = 0.25
        
        newGeneration = []
        
        nbParentsKept = int(rateOfParentsToKeep * self.populationSize)
        lastParentToKeep = self.populationSize - 1 - nbParentsKept    #because the best parent is the last element of self.population

        print("lastParentToKeep : {}".format(lastParentToKeep))
        print("nbParentsKept : {}".format(nbParentsKept))

        for i in range(self.populationSize-1, lastParentToKeep-1, -1):
            #print("i : {}".format(i))
            newGeneration.append(self.population[i])
        
        otherIndividuals = self.population[0:lastParentToKeep] + childrenIndividuals       #we keep the non-selected individuals from the parent generation and sort them along with the children
        otherIndividuals = sorted(otherIndividuals, key=operator.attrgetter("fitness"), reverse=False)
        
        #print("otherIndividuals Size : {}".format(len(otherIndividuals)))
        
        newGeneration = newGeneration + otherIndividuals[0:self.populationSize-nbParentsKept]
        #print("nbNewIndiv : {}".format(self.populationSize-nbParentsKept))
        #print("NewGenSize : {}".format(len(newGeneration)))
        
        self.population=newGeneration
        
        self.sort(True)
        
        for i in range(self.populationSize):
            print("fitness : {}".format(self.population[i].fitness))
        
        #print(self.population)
    
    def getGoodRandom(self):
        while(self.bestIndividual.fitness > 8000):
            newIndiv = self.initiateIndividual()
            newIndiv.calc()
            if (newIndiv.fitness < self.bestIndividual.fitness):
                self.bestIndividual = newIndiv
            print("fitness : {}".format(newIndiv.fitness))
        print(self.bestIndividual)
    
    
    def tryOneParameter(self, key, fitnessFunctionName, args=(), nbIndividuals=30):         #only makes one parameters vary for a range of value
        
        firstValue = self.initialIndividual.inputParametersVariable[key]['value']*(1-self.initialIndividual.inputParametersVariable[key]['variation']/100)
        lastValue = self.initialIndividual.inputParametersVariable[key]['value']*(1+self.initialIndividual.inputParametersVariable[key]['variation']/100)
        step = (lastValue - firstValue)/nbIndividuals
        
        xaxis = [firstValue]*nbIndividuals
        yaxis = [None]*nbIndividuals
        
        newIndiv = copy.deepcopy(self.initialIndividual)
        newIndiv.inputParametersVariable[key]['value'] = firstValue
        
        
        with Timer.LoggerTimer("{} {} | Fitness : {} | Computation Time ".format(newIndiv.inputParametersVariable[key]['name'], newIndiv.inputParametersVariable[key]['value'], newIndiv.fitness)):         #bug, la fitness affichée est la fitness d'avant le calcul
            newIndiv.calc(getattr(newIndiv, fitnessFunctionName), args)
            
        yaxis[0] = newIndiv.fitness
        
        for i in range(nbIndividuals - 1):
            newIndiv.inputParametersVariable[key]['value'] = newIndiv.inputParametersVariable[key]['value'] + step            
            with Timer.LoggerTimer("{} {} | Fitness : {} | Computation Time ".format(newIndiv.inputParametersVariable[key]['name'], newIndiv.inputParametersVariable[key]['value'], newIndiv.fitness)):
                newIndiv.calc(getattr(newIndiv, fitnessFunctionName), args)
            
            xaxis[i+1] = newIndiv.inputParametersVariable[key]['value']
            yaxis[i+1] = newIndiv.fitness
            
            if (newIndiv.fitness < self.bestIndividual.fitness):
                self.bestIndividual = newIndiv

        return (xaxis, yaxis)
    
    def geneticAlgorithm(self, selectionFunction, selectionFunctionArgs = ()):
    
        for i in range(self.nbMaxGeneration):
            print("\n\nGen n° {}".format(i+1))
            with Timer.LoggerTimer('Next Generation '):
                self.nextGeneration(selectionFunction, selectionFunctionArgs)
                print(self.bestIndividual)
    
        for i in range(self.populationSize):
            print(self.population[i])
    
        self.bestIndividual = self.population[self.populationSize-1]
        print(self.bestIndividual)
        
        
    def evaluate(self):
        pass
        
    def sort(self, reverse = False):            #if reverse = False, sort in ascendant order, if reverse is True, descendant order
        val = reverse
        self.population = sorted(self.population, key=operator.attrgetter("fitness"), reverse=val)
        
    
def functionWrapper(func, args): # without star
    return func(*args)
    


def variationTest(population, testName, fitnessFunctionName, args=(), key=None, testSize = 41):
    nbFigures = 0 
    
    if(key!=None):
        print("\n\n##########      {}       ##########".format(key))
        xaxis, yaxis = population.tryOneParameter(key, fitnessFunctionName, args, testSize)
        nbFigures = nbFigures + 1
        plt.figure(nbFigures)
        plt.grid(True)
        plt.plot(xaxis, yaxis, "r+", marker="+")
        plt.xlabel(population.initialIndividual.inputParametersVariable[key]['name'])
        plt.ylabel(testName)
        pathName = "../Results/VariationTests/"+testName
        os.makedirs(pathName, exist_ok=True)
        fileName = "{}_variationTest_{}.png".format(key, testName)
        plt.figure(nbFigures).savefig(pathName + '/' + fileName)
        #plt.show()
    
    else:
        for key in population.initialIndividual.inputParametersVariable.keys():
            print("\n\n##########      {}       ##########".format(key))
            xaxis, yaxis = population.tryOneParameter(key, fitnessFunctionName, args, testSize)
            nbFigures = nbFigures + 1
            plt.figure(nbFigures)
            plt.grid(True)
            plt.plot(xaxis, yaxis, "r+", marker="+")
            plt.xlabel(population.initialIndividual.inputParametersVariable[key]['name'])
            plt.ylabel(testName)
            pathName = "../Results/VariationTests/"+testName
            os.makedirs(pathName, exist_ok=True)
            fileName = "{}_variationTest_{}.png".format(key, testName)
            plt.figure(nbFigures).savefig(pathName + '/' + fileName)
            #plt.show()

def variationTest2(population, testName, fitnessFunctionName, args=(), key=None, testSize = 41):
    
    if(key!=None):
        fig = plt.figure(nbFigures)
        
        ax1 = plt.subplot()
        color = 'tab:red'
        # color = "r+"
        ax1.set_xlabel("LCG with set Deadrise Angle of {}°".format(deadrise))
        ax1.set_ylabel("EffectivePower", color = color)
        ax1.tick_params(axis='y', labelcolor=color)
        ax1.plot(xaxis, yaxis_effectivePower, color, marker="+")
        
        ax2 = ax1.twinx()
        color = 'tab:blue'
        # color = "b+"
        ax2.set_ylabel("Stability", color = color)
        ax2.tick_params(axis='y', labelcolor=color)
        ax2.plot(xaxis, yaxis_stability, color, marker="+")
        
        fig.tight_layout()
        
        plt.grid(True)                
        fileName = "{}_variationTest_{}_{}.png".format('beta', fileNameEnd, testSize)
        plt.figure(nbFigures).savefig(pathName + '/' + fileName)
        plt.close()

    else:
        for key in population.initialIndividual.inputParametersVariable.keys():
            
            fig = plt.figure(nbFigures)
            
            ax1 = plt.subplot()
            color = 'tab:red'
            # color = "r+"
            ax1.set_xlabel("LCG with set Deadrise Angle of {}°".format(deadrise))
            ax1.set_ylabel("EffectivePower", color = color)
            ax1.tick_params(axis='y', labelcolor=color)
            ax1.plot(xaxis, yaxis_effectivePower, color, marker="+")
            
            ax2 = ax1.twinx()
            color = 'tab:blue'
            # color = "b+"
            ax2.set_ylabel("Stability", color = color)
            ax2.tick_params(axis='y', labelcolor=color)
            ax2.plot(xaxis, yaxis_stability, color, marker="+")
            
            fig.tight_layout()
            
            plt.grid(True)                
            fileName = "{}_variationTest_{}_{}.png".format('beta', fileNameEnd, testSize)
            plt.figure(nbFigures).savefig(pathName + '/' + fileName)
            plt.close()


def testBetaBetaX(population, testName, fitnessFunctionName, args = (), testSize = 41):
    nbFigures = -1
    
    beta_x_first = population.initialIndividual.inputParametersVariable['beta_x']['value'] - population.initialIndividual.inputParametersVariable['beta_x']['value']*population.initialIndividual.inputParametersVariable['beta_x']['variation']/100
    beta_x_last = population.initialIndividual.inputParametersVariable['beta_x']['value'] + population.initialIndividual.inputParametersVariable['beta_x']['value']*population.initialIndividual.inputParametersVariable['beta_x']['variation']/100
    beta_x_step = (beta_x_last - beta_x_first)/10      #10 = nbValues of beta_x we want to try
    
    beta_x_first = beta_x_first + beta_x_step
    
    print("{} {} {}".format(beta_x_first, beta_x_last, beta_x_step))

    
    beta_init_first = population.initialIndividual.inputParametersVariable['beta']['value'] - population.initialIndividual.inputParametersVariable['beta']['value']*population.initialIndividual.inputParametersVariable['beta']['variation']/100
    
    
    xaxis = [beta_init_first]*(testSize+1)
    yaxis = [None]*(testSize+1)
    
    newIndiv = copy.deepcopy(population.initialIndividual)

    pathName = "../Results/VariationTests/" + testName
    os.makedirs(pathName, exist_ok=True)
    
    while(beta_x_first <= beta_x_last):
        
        i=0
        fileNameEnd = testName + "__{}_{}".format('beta_x', round(beta_x_first,2))
        newIndiv.inputParametersVariable['beta_x']['value'] = round(beta_x_first,2)
        newIndiv.inputParametersVariable['beta']['value'] = round(beta_init_first,2)
        beta_first = beta_init_first
        beta_last = beta_x_first
        beta_step = (beta_last - beta_first) / testSize
        
        while(i<testSize+1 and beta_first <= beta_x_first): # and beta_first <= beta_x_first ?
            
            
            with Timer.LoggerTimer("{} {} | {} {} | Fitness : {} | Computation Time ".format(newIndiv.inputParametersVariable['beta_x']['name'], newIndiv.inputParametersVariable['beta_x']['value'],  newIndiv.inputParametersVariable['beta']['name'], newIndiv.inputParametersVariable['beta']['value'], newIndiv.fitness)):
                newIndiv.calc(getattr(newIndiv, fitnessFunctionName), args)
            
            xaxis[i] = newIndiv.inputParametersVariable['beta']['value']
            yaxis[i] = newIndiv.fitness
            
            beta_first = round(beta_first + beta_step, 2)
            newIndiv.inputParametersVariable['beta']['value'] = beta_first
            i = i+1
            
        nbFigures = nbFigures + 1
        plt.figure(nbFigures)
        #plt.subplot(2,1,nbFigures+1)
        plt.plot(xaxis, yaxis, "r+", marker="+")
        plt.xlabel(population.initialIndividual.inputParametersVariable['beta']['name'])
        plt.ylabel(fileNameEnd)
        plt.grid(True)                
        fileName = "{}_variationTest_{}_{}.png".format('beta', fileNameEnd, testSize)
        plt.figure(nbFigures).savefig(pathName + '/' + fileName)
        
        beta_x_first = beta_x_first + beta_x_step
    
    

def variationTestMultiple(population, testNamesTab, fitnessFunctionNamesTab, args=(), key=None, testSize = 41):
    nbFigures = 0
    nbSubPlots = len (fitnessFunctionNamesTab)
    
    fileNameEnd = ""
    
    if(key!=None):
        print("\n\n##########      {}       ##########".format(key))
        nbFigures = nbFigures + 1
        plt.figure(nbFigures)
        for i in range(nbSubPlots):
            xaxis, yaxis = population.tryOneParameter(key, fitnessFunctionNamesTab[i], args, testSize)
            plt.subplot(2,1,i+1)
            plt.plot(xaxis, yaxis, "r+", marker="+")
            plt.xlabel(population.initialIndividual.inputParametersVariable[key]['name'])
            plt.ylabel(testNamesTab[i])
            plt.grid(True)
            fileNameEnd = fileNameEnd + "_" + testNamesTab[i]
        pathName = "../Results/VariationTests/Multiple"
        os.makedirs(pathName, exist_ok=True)
        fileName = "{}_variationTest{}_{}.png".format(key, fileNameEnd, testSize)
        plt.figure(nbFigures).savefig(pathName + '/' + fileName)
        #plt.show()
    
    else:
        for i in range(nbSubPlots):
            fileNameEnd = fileNameEnd + "_" + testNamesTab[i]
        for key in population.initialIndividual.inputParametersVariable.keys():
            print("\n\n##########      {}       ##########".format(key))
            nbFigures = nbFigures + 1
            plt.figure(nbFigures)
            for i in range(nbSubPlots):
                xaxis, yaxis = population.tryOneParameter(key, fitnessFunctionNamesTab[i], args, testSize)
                plt.subplot(2,1,i+1)
                plt.plot(xaxis, yaxis, "r+", marker="+")
                plt.xlabel(population.initialIndividual.inputParametersVariable[key]['name'])
                plt.ylabel(testNamesTab[i])
                plt.grid(True)
            pathName = "../Results/VariationTests/Multiple"
            os.makedirs(pathName, exist_ok=True)
            fileName = "{}_variationTest{}_{}.png".format(key, fileNameEnd, testSize)
            plt.figure(nbFigures).savefig(pathName + '/' + fileName)
            #plt.show()   



def testDeadriseLCG(population, testName, fitnessFunctionName, args = (), testSize = 41):
    #nbFigures = -1
    nbFigures = 0
    deadrise = 5
    LCG = 24
    stepLCG = (30-24)/testSize

    pathName = "../Results/VariationTests/" + testName
    os.makedirs(pathName, exist_ok=True)

    xaxis = [LCG]*(testSize+1)
    yaxis_effectivePower = [None]*(testSize+1)
    yaxis_stability = [None]*(testSize+1)
    

    while (deadrise <= 25):
        i=0
        LCG = 24
        population.initialIndividual.inputParametersVariable['beta']['value'] = deadrise
        population.initialIndividual.inputParametersVariable['beta_x']['value'] = deadrise
        fileNameEnd = testName + "__{}_{}".format('Deadrise', deadrise)
        while(LCG <= 30):
        
            population.initialIndividual.inputParametersVariable['LCG']['value']= LCG
            
            with Timer.LoggerTimer("{} {} |{} {} | {} | FitnessEffectivePower : {} | FitnessStability : {}| Computation Time ".format(population.initialIndividual.inputParametersVariable['beta_x']['name'], population.initialIndividual.inputParametersVariable['beta_x']['value'],  population.initialIndividual.inputParametersVariable['beta']['name'], population.initialIndividual.inputParametersVariable['beta']['value'],
population.initialIndividual.inputParametersVariable['LCG']['value'],
population.initialIndividual.fitnessEffectivePower, population.initialIndividual.fitnessStability)):
                population.initialIndividual.calc(getattr(population.initialIndividual, fitnessFunctionName), args)
            
            xaxis[i] = population.initialIndividual.inputParametersVariable['LCG']['value']
            yaxis_effectivePower[i] = population.initialIndividual.fitnessEffectivePower
            yaxis_stability[i] = population.initialIndividual.fitnessStability
            
            LCG = LCG + stepLCG
            i = i+1
            
        #nbFigures = nbFigures + 1
        fig = plt.figure(nbFigures)
        
        ax1 = plt.subplot()
        color = 'tab:red'
        # color = "r+"
        ax1.set_xlabel("LCG with set Deadrise Angle of {}°".format(deadrise))
        ax1.set_ylabel("EffectivePower", color = color)
        ax1.tick_params(axis='y', labelcolor=color)
        ax1.plot(xaxis, yaxis_effectivePower, color, marker="+")
        
        ax2 = ax1.twinx()
        color = 'tab:blue'
        # color = "b+"
        ax2.set_ylabel("Stability", color = color)
        ax2.tick_params(axis='y', labelcolor=color)
        ax2.plot(xaxis, yaxis_stability, color, marker="+")
        
        fig.tight_layout()
        
        plt.grid(True)                
        fileName = "{}_variationTest_{}_{}.png".format('beta', fileNameEnd, testSize)
        plt.figure(nbFigures).savefig(pathName + '/' + fileName)
        plt.close()

        deadrise = deadrise + 1
    
    
def testDeadriseVCG(population, testName, fitnessFunctionName, args = (), testSize = 25):
    #nbFigures = -1
    nbFigures = 0
    deadrise = 5
    VCG = 1.5
    stepVCG = (2.5-1.5)/testSize

    pathName = "../Results/VariationTests/" + testName
    os.makedirs(pathName, exist_ok=True)

    xaxis = [VCG]*(testSize+1)
    yaxis_effectivePower = [None]*(testSize+1)
    yaxis_stability = [None]*(testSize+1)
    
    i=0
    fileNameEnd = 'EffectivePowerAndStability'
    while(VCG <= 2.5):
    
        population.initialIndividual.inputParametersVariable['VCG']['value']= VCG
        
        with Timer.LoggerTimer("VCG : {} | FitnessEffectivePower : {} | FitnessStability : {}| Computation Time ".format(
population.initialIndividual.inputParametersVariable['VCG']['value'],
population.initialIndividual.fitnessEffectivePower, population.initialIndividual.fitnessStability)):
            population.initialIndividual.calc(getattr(population.initialIndividual, fitnessFunctionName), args)
        
        xaxis[i] = population.initialIndividual.inputParametersVariable['VCG']['value']
        yaxis_effectivePower[i] = population.initialIndividual.fitnessEffectivePower
        yaxis_stability[i] = population.initialIndividual.fitnessStability
        
        VCG = VCG + stepVCG
        i = i+1
            
    #nbFigures = nbFigures + 1
    fig = plt.figure(nbFigures)
    
    ax1 = plt.subplot()
    color = 'tab:red'
    # color = "r+"
    ax1.set_xlabel("VCG")
    ax1.set_ylabel("EffectivePower", color = color)
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.plot(xaxis, yaxis_effectivePower, color, marker="+")
    
    ax2 = ax1.twinx()
    color = 'tab:blue'
    # color = "b+"
    ax2.set_ylabel("Stability", color = color)
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.plot(xaxis, yaxis_stability, color, marker="+")
    
    fig.tight_layout()
    
    plt.grid(True)                
    fileName = "{}_variationTest_{}_{}.png".format('VCG', fileNameEnd, testSize)
    plt.figure(nbFigures).savefig(pathName + '/' + fileName)
    plt.close()



    
def testDeadriseE(population, testName, fitnessFunctionName, args = (), testSize = 25):
    #nbFigures = -1
    nbFigures = 0
    deadrise = 5
    E = 2
    stepE = (6-2)/testSize

    pathName = "../Results/VariationTests/" + testName
    os.makedirs(pathName, exist_ok=True)

    xaxis = [E]*(testSize+1)
    yaxis_effectivePower = [None]*(testSize+1)
    yaxis_stability = [None]*(testSize+1)
    
    i=0
    fileNameEnd = 'EffectivePowerAndStability'
    while(E <= 6):
    
        population.initialIndividual.inputParametersVariable['e']['value']= E
        
        with Timer.LoggerTimer("E : {} | FitnessEffectivePower : {} | FitnessStability : {}| Computation Time ".format(
population.initialIndividual.inputParametersVariable['e']['value'],
population.initialIndividual.fitnessEffectivePower, population.initialIndividual.fitnessStability)):
            population.initialIndividual.calc(getattr(population.initialIndividual, fitnessFunctionName), args)
        
        xaxis[i] = population.initialIndividual.inputParametersVariable['e']['value']
        yaxis_effectivePower[i] = population.initialIndividual.fitnessEffectivePower
        yaxis_stability[i] = population.initialIndividual.fitnessStability
        
        E = E + stepE
        i = i+1
            
    #nbFigures = nbFigures + 1
    fig = plt.figure(nbFigures)
    
    ax1 = plt.subplot()
    color = 'tab:red'
    # color = "r+"
    ax1.set_xlabel("{}".format(population.initialIndividual.inputParametersVariable['e']['name']))
    ax1.set_ylabel("EffectivePower", color = color)
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.plot(xaxis, yaxis_effectivePower, color, marker="+")
    
    ax2 = ax1.twinx()
    color = 'tab:blue'
    # color = "b+"
    ax2.set_ylabel("Stability", color = color)
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.plot(xaxis, yaxis_stability, color, marker="+")
    
    fig.tight_layout()
    
    plt.grid(True)                
    fileName = "{}_variationTest_{}_{}.png".format('e', fileNameEnd, testSize)
    plt.figure(nbFigures).savefig(pathName + '/' + fileName)
    plt.close()


if (__name__ == '__main__'):
    # population = Population(Individual.Individual(IF.initialInputs),"calcFitnessDrag", (), 0.5, 50, 80)
    population = Population(Individual.Individual(IF.initialInputs),"calcFitnessDrag", (), 0.5, 2, 120)
    
    #population.sort(True)
    
    #population.rankSelection()
    
    # with Timer.LoggerTimer('\nGenetic Algorithm : '):
    #      population.tryOneParameter('LCG')
    
    
    
    # with Timer.LoggerTimer('\nVariation Test Stability '):
    #     # variationTestMultiple(population, ["Drag"], ["calcFitnessDrag"])
    #     for key in ['e']:
    #         variationTest(population, "EffectivePower", "calcFitnessEffectivePower", (), key)
    
    
    
    
    # with Timer.LoggerTimer('\nVariation Test Stability '):
    #     variationTest(population, "Stability", "calcFitnessStability", (), 'LCG', 25)
    #     
    with Timer.LoggerTimer('\nVariation Test Stability '):
        variationTest(population, "Stability", "calcFitnessStability", (), 'VCG', 25)
    
    
    with Timer.LoggerTimer('\nVariation Test Stability '):
        variationTest(population, "Stability", "calcFitnessStability", (), 'e', 25)
    
    
    
    
    # with Timer.LoggerTimer('\nTest e'):
    #     testDeadriseE(population, 'EffectivePowerAndStability', 'calcFitnessEffectivePower', ())
    # 
    # 
    # with Timer.LoggerTimer('\nTest VCG'):
    #     testDeadriseVCG(population, 'EffectivePowerAndStability', 'calcFitnessEffectivePower', ())
    
    
    
    
    
    
    
    
    
    
    
    # 
    # with Timer.LoggerTimer('\nTest LCG and DeadriseAngle '):
    #     testDeadriseLCG(population, 'EffectivePowerAndStability', 'calcFitnessEffectivePower', ())
    # 
    
    # with Timer.LoggerTimer('\nTestBetaBeta_x '):
    #     testBetaBetaX(population, 'EffectivePower', 'calcFitnessEffectivePower', ())
    
    
    # with Timer.LoggerTimer('\nGeneticAlgorithm '):
    #     population.geneticAlgorithm(population.rankSelection)
    
        
    #     variationTestMultiple(population, ("Drag", "Stability"), ("calc
    #done
    # with Timer.LoggerTimer('\nVariation Test Stability '):
    #     variationTestMultiple(population, ("Drag", "Stability"), ("calcFitnessDrag","calcFitnessStability"))
    
    # with Timer.LoggerTimer('\nVariation Test Stability '):
    #     variationTest(population, "Stability", "calcFitnessStability")
    
                #plt.show()
    
    
    
    # with Timer.LoggerTimer('\nVariation Test Stability '):
    #     # variationTestMultiple(population, ["Drag"], ["calcFitnessDrag"])
    #    variationTest(population, "Drag", "calcFitnessDrag", (), 'e')
    
    
    
    
    
    # with Timer.LoggerTimer('\nGenetic Algorithm : '):
    #     population.getGoodRandom()
    
    # with Timer.LoggerTimer('\nGenetic Algorithm : '):
    #    population.geneticAlgorithm(population.rankSelection)
    
    #print(population)