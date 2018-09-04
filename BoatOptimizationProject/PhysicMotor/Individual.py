
#https://saladtomatonion.com/blog/2014/12/16/mesurer-le-temps-dexecution-de-code-en-python/

import sys
import copy as copy
import random as random

import ComputationMathRad_initDico_thread_noTests as Computation

sys.path.insert(0, '../')
import GraphicMotor.InitFileNotSI2_PlanningRange as IF
# import GraphicMotor.InitFileNotSI2_PlanningRangeTest as IF

class Individual ():
        
    #docstring
    """(docstring) Classe Individual"""

    
    def __init__ (self, inputDictionary):
        
        #format    'key' : [value(float), variation pourcentage(int ou float), used in GA or not(boolean), "name printed on the GUI"]
        
        self.fitness = 0.0
        
        self.fitnessEffectivePower = 0.0
        self.fitnessStability = 0.0
        
        self.firstPlanningSpeed = 0.0
        
        self.inputParametersAll = copy.deepcopy(inputDictionary)   #genes of the individual
        self.inputParametersVariable = {}  #genes allowed to change
        self.inputParametersFixed = {}  #genes not allowed to change
        
        self.fillParametersGA()
        
        self.computation = Computation.Computation(self.inputParametersAll, len(self.inputParametersAll['V']['value1']))  #intermediate calculation to get the outputs 
        
        self.outputParametersAll = {}   #outputs
        self.fillParametersOutputs()

    def __str__(self):
        rep = ""
        
        print("\n\n#####################   Fitness | Drag : {}  | Stability ###########################".format(self.fitnessDrag, self.fitnessStability))
        print("                firstPlanningSpeed : {}".format(self.firstPlanningSpeed))
        print("\n#####################   ParametersFixed    ###########################")
        print("{} = {} ({})".format(self.inputParametersFixed['V']['name'], self.inputParametersFixed['V']['value1'], self.inputParametersFixed['V']['unit1']))
        for key in self.inputParametersFixed.keys():
            if (key != 'V'):
                print("{} = {} ({})".format(self.inputParametersFixed[key]['name'], self.inputParametersFixed[key]['value'], self.inputParametersFixed[key]['unit']))
                
        
        print("\n#####################   ParametersVariable   ###########################")
        for key in self.inputParametersVariable.keys():
            print("{} = {} ({})".format(self.inputParametersVariable[key]['name'], self.inputParametersVariable[key]['value'], self.inputParametersVariable[key]['unit']))

        
        print("\n#####################   Computation   ###########################")
        print(self.computation)
        
        return rep 
    


    def fillParametersGA(self):         #sans les deepcopy, pas besoin de reconstruire le dico inputParametersAll, il est mis à jour automatiquement
                                        #car les dicos associés aux clés ne contiennent au plus que des tableaux
        for key in self.inputParametersAll.keys():
            if (key == 'V'):
                self.inputParametersFixed[key] = self.inputParametersAll[key]
            else:
                if (self.inputParametersAll[key]['usedInGA']):
                    self.inputParametersVariable[key] = self.inputParametersAll[key] 
                else:
                    self.inputParametersFixed[key] = self.inputParametersAll[key]
            
    
    def fillParametersOutputs(self):        
        for key in self.computation.dictionary.keys():
            if (self.computation.dictionary[key]['output']):
                self.outputParametersAll[key] = self.computation.dictionary[key]
                

    def fillParametersGA_deepcopy(self):                #useless now
        for key in self.inputParametersAll.keys():  
            if (self.inputParametersAll[key]['usedInGA']):
                self.inputParametersVariable[key] = copy.deepcopy(self.inputParametersAll[key])   
            else:
                self.inputParametersFixed[key] = copy.deepcopy(self.inputParametersAll[key]) 
    
    def fillParametersOutputs_deepcopy(self):        #useless now
        for key in self.computation.dictionary.keys():
            if (self.computation.dictionary[key]['output']):
                self.outputParametersAll[key] = copy.deepcopy(self.computation.dictionary[key])

    """def inversion():
        size = self.inputParametersAll.keys().size()   #seulement les param variables ??  -> fonction qui actualise le tableau contenant l'ensemble des paramètres (possible de la faire slmt à la fin de l'algo -> non car computation en a besoin et son dico init doit être actualisé)
        
        tab = [0]*size
        for i in range (0,size):
            for j in range (0,i):
                tab[i] + = 
                
    """
    
    def randomize(self, initialIndividualDictionary, key=None):  #the initialIndividual is necessary to check that the values obtained via mutation are still in the good range of values
                                                #if a key is scpecified, it only randomizes the value for this key, otherwise for all
        temp = 0
        if (key != None):
            if(key != 'V'):
                var = random.randint(0, 100 * initialIndividualDictionary[key]['variation'] - 1 )
                print(var)
                var = var / 10000 #random variation pourcentage
                print(var)
                sign = random.randint(0,1)  #random sign since we allow the range of + or - the initial variation percentage
                if (sign):
                    temp = round((1 + var) * initialIndividualDictionary[key]['value'],2)
                else:
                    temp = round((1 - var) * initialIndividualDictionary[key]['value'],2)
                    
                if(temp<=0):
                    self.inputParametersVariable[key]['value'] = 0
                else:
                    self.inputParametersVariable[key]['value'] = temp
                    
        else:
            for key in self.inputParametersVariable.keys():
                if (key != 'V'):
                    var = random.randint(0, 100 * initialIndividualDictionary[key]['variation'] - 1 )
                    var = var / 10000   #random variation pourcentage   /   (divided by 10000 cause divided two times by 100, once to compensate the multiplication by 100 right before and once more to put 10% as 0.1)
                    sign = random.randint(0,1)  #random sign since we allow the range of + or - the initial variation percentage
                    if (sign):
                        temp = round((1 + var) * initialIndividualDictionary[key]['value'],2)
                    else:
                        temp = round((1 - var) * initialIndividualDictionary[key]['value'],2)
                        
                    if(temp<=0):
                        self.inputParametersVariable[key]['value'] = 0
                    else:
                        self.inputParametersVariable[key]['value'] = temp
            
    
    def reconstructIndividual(self, dicoFixedParam, dicoVariableParam):  #useless now
        #le resultat sera un dico contenant les mêmes clés que le dico init complet mais avec les clés potentiellement dans un ordre différent  -> aucune incidence
        
        child = {}
        for key in dicoFixedParam.keys():
            child[key] = copy.deepcopy(dicoFixedParam[key])
        for key in dicoVariableParam.keys():
            child[key] = copy.deepcopy(dicoVariableParam[key])
            
        return child                #returns the main dictionary of an Individual, to create the individual, do indiv = Individual(recontructIndividual(dicoFixed, dicoVariable))
        
        
    """"
    def inversion():
        pass
        
    def reversion():
        pass
    """
    
    def mutate(self, initialIndividualDictionary):   #the initialIndividual is necessary to check that the values obtained via mutation are still in the good range of values
        
        #mutationRate determined by the population
        
        nbKeys = len(self.inputParametersVariable.keys())
        nbMutations = random.randint(0,nbKeys - 1)
        #print(nbMutations)
        tabTemp = [i for i in range(0,nbKeys) ]
        for i in range(0, nbKeys - nbMutations):
            ind = random.randint(0, nbKeys - 1 - i)
            del tabTemp[ind]
        #random.shuffle(tabTemp)
        #tabTemp.sort()
        print(tabTemp)
        keys = list(self.inputParametersVariable.keys())
        print(keys[0])
        for i in range(len(tabTemp)):
            key = keys[tabTemp[i]]
            if (key == 'beta' or key == 'beta_x'):
                self.randomize(initialIndividualDictionary, key)
                while(self.inputParametersVariable['beta']['value'] > self.inputParametersVariable['beta_x']['value']):
                    self.randomize(initialIndividualDictionary, key)
                
        #print(tabTemp)
        
        
        
        
        
    def crossover(self, individualB, nbPoints = 1):  #cette fonction garde #childA1 + ChildB2 
    
        #crossover points multiples ?
        #childA1 + ChildB2   
        #childB1 + ChildA2
        
        childVariable = copy.deepcopy(individualB.inputParametersVariable)
    
        size  = len(self.inputParametersVariable.keys()) - 1
        
        pointIndex  = random.randint(1, size)
        print("crossover point : {}".format(pointIndex))
        temp = -1
        
        for key in self.inputParametersVariable:
            temp += 1
            if (temp == pointIndex):
                break
            childVariable[key] = copy.deepcopy(self.inputParametersVariable[key])

        return( Individual(self.reconstructIndividual(self.inputParametersFixed, childVariable)))
    
    def isPlanning(self):
        speedIndice = 0
        for i in range(len(self.inputParametersFixed['V']['SI'])):
            if (self.inputParametersFixed['V']['SI'][i] == 35):
                break
            speedIndice = speedIndice + 1
        return self.outputParametersAll['planning']['value'][speedIndice]
    
    def checkTheta(self):
        self.computation.calc_theta(self.inputParametersAll['B']['value'], self.inputParametersAll['LWL']['value'], self.inputParametersAll['beta']['value'], self.inputParametersAll['beta_x']['value'], 10, -1)
        temp = True
        if (self.computation.dictionary['theta']['value'][0] < 0):
            temp = False
        return temp
    
    def calcFitnessEffectivePower(self):
        average = self.outputParametersAll['Peff']['value'][0]
        size = self.computation.size
        k=1
        for i in range(1, size):
            average = average + self.outputParametersAll['Peff']['value'][i]
            k = k+1

        self.fitness = average / k
        self.fitnessEffectivePower = average / k
    
    
    def calcFirstPlanningSpeed(self):
        
        for i in range(0, self.computation.size):
            if(self.outputParametersAll['planning']['value'][i]):
                self.firstPlanningSpeed = self.inputParametersAll['V']['value1'][i]
                break
    
    
    def calcFitnessDrag(self):
        average = self.outputParametersAll['Fh']['value'][0]
        size = self.computation.size
        k=1
        for i in range(1, size):
            average = average + self.outputParametersAll['Fh']['value'][i]
            k = k+1

        self.fitness = average / k
            
            
    def calcFitnessDrag2(self):
        average = self.outputParametersAll['Fh']['value'][0]
        size = self.computation.size
        k=1
        for i in range(1, size):
            if (self.outputParametersAll['planning']['value'][i]):
                average = average + self.outputParametersAll['Fh']['value'][i]
                k = k+1
        self.fitness = average / k
        self.fitnessDrag = average / k
           
    
    def calcFitnessStability(self):
        average = self.outputParametersAll['verticalAcceleration']['value'][0]
        size = self.computation.size
        k=1
        for i in range(1, size):
            average = average + self.outputParametersAll['verticalAcceleration']['value'][i]
            k = k+1

        self.fitness = average / k
        self.fitnessStability = average / k
        for i in range(0, size):
            print(self.outputParametersAll['verticalAcceleration']['value'][i])
        
           
    def calcFitnessStability2(self):
        average = self.outputParametersAll['Fh']['value'][0]
        size = self.computation.size
        k=1
        for i in range(1, size):
            if (self.outputParametersAll['planning']['value'][i]):
                average = average + self.outputParametersAll['Fv']['value'][i]
                k = k+1

        self.fitness = average / k
            
            
    def calc(self, fitnessFunction, args=()):
        self.computation.calc()
        #self.calcFitnessDrag()
        self.calcFirstPlanningSpeed()
        functionWrapper(fitnessFunction, args)
        
        self.calcFitnessEffectivePower()
        self.calcFitnessStability()
        
        #self.calcFitnessStability()
        
        #print("fitness : {}".format(self.fitness))
    





def functionWrapper(func, args): # without star
    return func(*args)
    


"""        
indiv = Individual()

indiv.inputParametersAll['key'] = 1
indiv.inputParametersAll['key1'] = 2
indiv.inputParametersAll['key2'] = 3
indiv.inputParametersAll['key3'] = [4,False,"uhuih",1.254]

tab = {
    'uigi' : 54,
    'hohdof' : 546
}
"""
#print(indiv.dict)

#print(indiv.dict.values())



"""
tab = {
    'V' : {'value1' : [1,2,3,4,5,6]},
    'V2' : {'value1' : [1,2,3,4,5,6]},
    'uigi' : {'val' : 0.0, 'val2' : 'uhgouho'},
    'hohdof' : 546
}

indiv  = Individual(tab)

print(tab)
print(indiv.computation.inputDictionary)

indiv.computation.inputDictionary['hohdof'] = 5
indiv.computation.inputDictionary['V']['value1'][2] = 9999

print(tab)
print(indiv.computation.inputDictionary)



tab2 = {}

tab2['V'] = tab['V']
tab2['V2'] = copy.deepcopy(tab['V2'])

tab2['V']['value1'][0] = 0
tab2['V2']['value1'][0] = 0

tab['V']['value1'][5] = 0
tab['V2']['value1'][5] = 0

print('tab')
print (tab)
print('tab2')
print (tab2)       #pas besoin de deepcopy ni copy dans les fonction fill car dico[key] ne contient au plus que des tableaux en sous-niveau / une modif dans l'un entraine la modif dans l'autre

"""

"""
tab2 = copy.deepcopy(tab)

print(tab)
print(tab2)

tab['hohdof'] = 5
tab['uigi']['val'] = 40

print(tab)
print(tab2)

"""

def printDico(dico):
    for key in dico.keys():
        print (key)
        print(dico[key])


if (__name__ == '__main__'):
    indiv = Individual(IF.initialInputs)
    # indiv2 = Individual(IF.initialInputs)
    initialIndiv= Individual(IF.initialInputs)
    # #print(indiv.inputParametersVariable)
    # 
    # print(indiv)
    # print(initialIndiv)
    # #print(initialIndiv.inputParametersAll)
    # print('\n')
    # 
    # '''
    # indiv.inputParametersVariable['LCG']['value'] = 77777
    # print("\n\n#####################   FIXED   ###########################")
    # printDico(indiv.inputParametersFixed)
    # 
    # print("\n\n#####################   VARIABLE  ###########################")
    # printDico(indiv.inputParametersVariable)
    # 
    # print("\n\n#####################   ALL  ###########################")
    # printDico(indiv.inputParametersAll)
    # '''
    # 
    # #printDico(indiv.inputParametersAll)
    # print("\n\n                                 #####################   000 ###########################")
    # printDico(indiv.inputParametersVariable)
    # print(indiv.computation.inputDictionary)
    # indiv.randomize(initialIndiv.inputParametersAll)
    # printDico(indiv.inputParametersVariable)
    # print(indiv.computation.inputDictionary)
    # #print("\n\n#####################   RANDOMIZED  ###########################")
    # #printDico(indiv.inputParametersAll)
    # 
    # indiv3 = indiv.crossover(indiv2)
    # """
    # print("\n\n#####################   indiv   ###########################")
    # printDico(indiv.inputParametersVariable)
    # 
    # print("\n\n#####################   indiv2  ###########################")
    # printDico(indiv2.inputParametersVariable)
    # 
    # print("\n\n#####################   indiv3 = child of indiv and indiv2  ###########################")
    # printDico(indiv3.inputParametersVariable)
    # """
    # indiv.mutate(initialIndiv.inputParametersAll)
    # 
    # '''
    # print("\n\n                                 #####################   TEST  ###########################")
    # print(indiv3)
    # print(indiv3.computation.inputDictionary)
    # print("\n\n                                 #####################   TEST 2 ###########################")
    # printDico(indiv.inputParametersVariable)
    # print(indiv.computation.inputDictionary)
    # '''
    
    
    
    
    #indiv.calc(indiv.calcFitnessDrag)
    
    print("\n\n\n\n\n\n\n\n")
    print (indiv)

    # indiv.mutate(initialIndiv.inputParametersAll)
    # indiv.mutate(initialIndiv.inputParametersAll)
    # indiv.mutate(initialIndiv.inputParametersAll)
    # indiv.mutate(initialIndiv.inputParametersAll)
    # 
    indiv.calc(getattr(indiv,"calcFitnessStability"))
    
    print (indiv)
