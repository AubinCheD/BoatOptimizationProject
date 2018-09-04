import math as math

from threading import Thread

import _thread

import sys
sys.path.insert(0, './')

import Timer as Timer
import ConstantsNotSI as Constants
import Units as Units

sys.path.insert(0, '../')
import GraphicMotor.InitFileNotSI2_PlanningRange as IF


class ParallelCalculation(Thread):
    
    def __init__(self):
        
        super().init(self)
        
        pass
        
    def run():
        
        pass



class Computation ():
        
    #docstring
    """(docstring) Class Computation"""

    
    def __init__ (self, inputDictionary, size):   #size = size of the vector of speeds
        
        #format    'key' : [value(float), variation pourcentage(int ou float), used in GA or not(boolean), "name printed on the GUI"]
        
        self.size = size
        
        self.inputDictionary = inputDictionary      #just a reference  // faire le test pour check que ca modifie pas le dico en param
        
        self.dictionary = {    # 'key' : [value:float, unitType: string, unit: string, variationType, variation, displayedName: string, usedInGA: boolean]
                              #depending on variationType, variation is either a float or a tab [min: float, max: float, step: float]
                              #maybe don't need variationType and unitType
         
        
        #on pourrait créer un sous dictionnaire avec comme clés les noms des catégories pour une création automatique de l'interface, à essayer un jour

        #intermediate calculation
            
            'M': {'value': None, 'constant': False, 'output': True},    #needs Nt, c, Df, T first
            
            'Ass': {'value': None, 'constant': True, 'output': False},
            
            ##une solution: {value: [], 'Fun': f, args: [list of args]}
            
            
            #15
            'Cv': {'value': None, 'constant': True, 'output': False},                      #une lambda ?
            'CLb': {'value': None, 'constant': True, 'output': False},
            'trim': {'value': None, 'constant': False, 'output': True},
            'trim_eL': {'value': None, 'constant': False, 'output': False},
            'trim_eD': {'value': None, 'constant': False, 'output': False},
            'beta_e': {'value': None, 'constant': False, 'output': False},
            'CL0': {'value': None, 'constant': True, 'output': False},

            'lambda': {'value': None, 'constant': False, 'output': False},
            'CL0d': {'value': None, 'constant': False, 'output': False},
            'CL_beta_d': {'value': None, 'constant': False, 'output': False},               #problem with line 131
            'Vm': {'value': None, 'constant': False, 'output': False},
            'Re': {'value': None, 'constant': False, 'output': False},
            'Cf': {'value': None, 'constant': False, 'output': False},
            'Sf': {'value': None, 'constant': False, 'output': False},
            'Df': {'value': None, 'constant': False, 'output': False},
            'D': {'value': None, 'constant': False, 'output': False},
            'Mfactor': {'value': None, 'constant': False, 'output': False},
            'D_romp': {'value': None, 'constant': False, 'output': False},
            
            #Trim Tabs
            'trimTabs_DELTA': {'value': None, 'constant': True, 'output': False},
            'trimTabs_Re': {'value': None, 'constant': False, 'output': False},
            'trimTabs_Cf': {'value': None, 'constant': False, 'output': False},
            'trimTabs_Df': {'value': None, 'constant': False, 'output': False},
            'trimTabs_D_L': {'value': None, 'constant': False, 'output': False},
            'trimTabs_D': {'value': None, 'constant': False, 'output': False},
            'trimTabs_M': {'value': None, 'constant': False, 'output': False},
            'trimTabs_H': {'value': None, 'constant': True, 'output': False},
            
            #shaft
            'shaft_Re_D': {'value': None, 'constant': True, 'output': False},
            'shaft_Re_L': {'value': None, 'constant': True, 'output': False},
            'shaft_Cf_L': {'value': None, 'constant': True, 'output': False},
            'shaft_D': {'value': None, 'constant': True, 'output': False},
            'shaft_N': {'value': None, 'constant': True, 'output': False},
            'shaft_f': {'value': None, 'constant': True, 'output': False},
            'shaft_e': {'value': None, 'constant': True, 'output': False},
            'shaft_M': {'value': None, 'constant': True, 'output': False},
            
            #strut
            'strut_Re_c': {'value': None, 'constant': True, 'output': False},
            'strut_CD': {'value': None, 'constant': True, 'output': False},
            'strut_D': {'value': None, 'constant': True, 'output': False},
            'strut_f': {'value': None, 'constant': True, 'output': False},
            'strut_e': {'value': None, 'constant': True, 'output': False},
            'strut_M': {'value': None, 'constant': True, 'output': False},            
            
            #rudder
            'rudder_Re_c': {'value': None, 'constant': True, 'output': False},
            'rudder_CD': {'value': None, 'constant': True, 'output': False},
            'rudder_D': {'value': None, 'constant': True, 'output': False},
            'rudder_f': {'value': None, 'constant': True, 'output': False},
            'rudder_e': {'value': None, 'constant': True, 'output': False},
            'rudder_M': {'value': None, 'constant': True, 'output': False},
                        
            
            #Air Resistance
            'Zprim': {'value': None, 'constant': False, 'output': False},  #?
            'A_romp': {'value': None, 'constant': False, 'output': False},  #?
            'A_voorkant': {'value': None, 'constant': False, 'output': False}, #?
            'D_air': {'value': None, 'constant': False, 'output': False},
            'f_air': {'value': None, 'constant': False, 'output': False},
            'M_air': {'value': None, 'constant': False, 'output': False},
            
            #total resistance
            'Fh': {'value': None, 'constant': False, 'output': True},
            'Fv': {'value': None, 'constant': False, 'output': True},
            'T': {'value': None, 'constant': False, 'output': True},
            'Nt': {'value': None, 'constant': False, 'output': False},
            'Cp': {'value': None, 'constant': False, 'output': False},
            'Lp': {'value': None, 'constant': False, 'output': False},
            'c': {'value': None, 'constant': False, 'output': False},
            'a': {'value': None, 'constant': False, 'output': False},
            'Fn_vol': {'value': None, 'constant': True, 'output': False},
            #99
            'lambda_k': {'value': None, 'constant': False, 'output': False},
            'Lk': {'value': None, 'constant': False, 'output': False},
            'Lc': {'value': None, 'constant': False, 'output': False},
            'h': {'value': None, 'constant': False, 'output': True},
            
            #ROLSTABILITEIT    #using another article
            'lt': {'value': None, 'constant': False, 'output': False},
            'DELTA_s': {'value': None, 'constant': False, 'output': False},
            'KB': {'value': None, 'constant': False, 'output': False},
            'BG': {'value': None, 'constant': False, 'output': False},
            'a_one_s': {'value': None, 'constant': False, 'output': False},
            'CL_beta_d2': {'value': None, 'constant': False, 'output': False},          #problem with line 54
            'drukpt': {'value': None, 'constant': False, 'output': False},      #meaning ?
            'arm': {'value': None, 'constant': False, 'output': False},
            
            'F': {'value': None, 'constant': True, 'output': False},
        
            #Outputs
            'Peff': {'value': None, 'constant': False, 'output': True},
            'trim_critical_lewandowski': {'value': None, 'constant': True, 'output': True},
            'trim_critical_angeli': {'value': None, 'constant': True, 'output': True},
            'planning': {'value': None, 'constant': True, 'output': True}
            
        
        }
        
        
        self.initAll()
        
        
        
        
       
                    
                    
                    ##                                                    modifier les n=len() .. par self.size
    
    #Calculation functions
    
    
    def calc(self, roundingPrecision = 10):
        with Timer.LoggerTimer('Trim '):
            self.calc_trim(roundingPrecision)
    
    def calc_M(self, NbPropellers, f, roundingPrecision = 10, index = -1):          #need Nt, c ..., to put in the end of calculation, see..                #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['Ass']['value'][i])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(firstIndex, lastIndex):
        temp = self.dictionary['Nt']['value'][index] * self.dictionary['c']['value'][index]+ self.dictionary['trimTabs_M']['value'][index]
        temp = temp + NbPropellers*(self.dictionary['shaft_M']['value'][index]+self.dictionary['rudder_M']['value'][index]+self.dictionary['strut_M']['value'][index])
        temp = temp + self.dictionary['Df']['value'][index]*self.dictionary['a']['value'][index] 
        temp = temp - self.dictionary['T']['value'][index]*f
        temp = temp - self.dictionary['M_air']['value'][index] 
        self.dictionary['M']['value'][index] = round(temp, roundingPrecision)
    
    
    def calc_Ass(self, Hss, Bss, roundingPrecision = 10, index = -1):   #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0 lastIndex =
        #     len(self.dictionary['trim']['value'])
        # else :
        #     firstIndex = index lastIndex = index + 1
        for i in range(self.size):
            self.dictionary['Ass']['value'][i] = round(Hss*Bss, roundingPrecision)
    
    
    def calc_trim(self, roundingPrecision = 10):
        
        #with Timer.LoggerTimer('Constants '):
        self.calcAllConstants()
        
        n = len(self.dictionary['trim']['value'])
        j=-1
        tabA = [0]*n       #tester les valeurs des tableaux
        tabTemp = [0]*n
        
        nbTourDeBoucles = 0
        
        mat = [[0 for i in range(n)] for j in range(n)]                     #???

        #print('calc_trim : Entrée boucle 1')
        for i in range (0,n):
            
            nbTourDeBoucles = nbTourDeBoucles+1
            
            self.dictionary['trim']['value'][i] = 0.0001
            self.calcAll(roundingPrecision, i)
            if (self.dictionary['M']['value'][i] > 0):  
                j = i
        
        #print('calc_trim : Entrée boucle 2')
        for i in range (j+1, n):
            trim = 0.1
            while (trim < 15.1):
                nbTourDeBoucles = nbTourDeBoucles+1
                
                self.dictionary['trim']['value'][i] = trim
                self.calcAll(roundingPrecision, i)
                if (self.dictionary['M']['value'][i] < 0):
                    tabTemp[i] = self.dictionary['trim']['value'][i]
                    trim = trim + 1
                else:
                    break
            
            self.dictionary['trim']['value'][i] = tabTemp[i]
            self.calcAll(roundingPrecision, i)
            tabA[i] = tabTemp[i]
        
        #print('calc_trim : Entrée boucle 3')
        for i in range (j+1, n):
            trim = tabA[i]
            while (trim < 15.1):
                nbTourDeBoucles = nbTourDeBoucles+1
                
                self.dictionary['trim']['value'][i] = trim
                self.calcAll(roundingPrecision, i)
                if (self.dictionary['M']['value'][i] < 0):
                    tabTemp[i] = self.dictionary['trim']['value'][i]
                    trim = trim + 0.1
                else:
                    break
            self.dictionary['trim']['value'][i] = tabTemp[i]
            self.calcAll(roundingPrecision, i)
            tabA[i] = tabTemp[i]
        
        #print('calc_trim : Entrée boucle 4')
        for i in range (j+1, n):
            trim = tabA[i]
            while (trim < 15.01):
                nbTourDeBoucles = nbTourDeBoucles+1
                
                self.dictionary['trim']['value'][i] = trim
                self.calcAll(roundingPrecision, i)
                if (self.dictionary['M']['value'][i] < 0):
                    tabTemp[i] = self.dictionary['trim']['value'][i]
                    trim = trim + 0.01
                else:
                    break
            self.dictionary['trim']['value'][i] = tabTemp[i]
            self.calcAll(roundingPrecision, i)
            tabA[i] = tabTemp[i]
                    
        #print('calc_trim : Entrée boucle 5')
        for i in range (j+1, n):
            trim = tabA[i]
            while (trim < 15.001):
                nbTourDeBoucles = nbTourDeBoucles+1
                
                self.dictionary['trim']['value'][i] = trim
                self.calcAll(roundingPrecision, i)
                if (self.dictionary['M']['value'][i] < 0):
                    tabTemp[i] = self.dictionary['trim']['value'][i]
                    trim = trim + 0.001
                else:
                    break
            if (self.dictionary['trim']['value'][i] > 13):
                break
            self.dictionary['trim']['value'][i] = tabTemp[i]
            self.calcAll(roundingPrecision, i)
            tabA[i] = tabTemp[i]
        
        #print('calc_trim : Entrée boucle 6')
        for i in range (j+1, n):
            trim = tabA[i]
            while (trim < 15.0001):
                nbTourDeBoucles = nbTourDeBoucles+1
                
                self.dictionary['trim']['value'][i] = trim
                self.calcAll(roundingPrecision, i)
                if (self.dictionary['M']['value'][i] >= 0):
                    break
                trim = trim + 0.0001
            if (self.dictionary['trim']['value'][i] > 13):
                break
        
        #print('calc_trim : Entrée boucle 7')
        if (j != -1):
            for i in range (0,j+1):
                self.dictionary['trim']['value'][i] = 0   # ou = '-'
                self.calcAll(roundingPrecision, i)
        
        #showAll(self.dictionary)
        '''
        for i in range (j+1, n):
            if (self.dictionary['trim']['value'][i] > 15):
                self.dictionary['trim']['value'][i] = ' > 15'
        '''
        
        print("nbToursBoucle : {}".format(nbTourDeBoucles))
    
    
    def calc_Cv(self, V, B, roundingPrecision = 10, index = -1):         #if index == -1, calculate the all tab, otherwise calcultate only tab[index]           #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(V)
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        for i in range(self.size):
            self.dictionary['Cv']['value'][i] = round(V[i]/math.sqrt(Constants.constants['g_SI']['value']*B),  roundingPrecision)
    
    def calc_CLb(self, V, B, delta, roundingPrecision = 10, index = -1):    #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(V)
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        for i in range(self.size):
            self.dictionary['CLb']['value'][i] = round(delta/(0.5*Constants.constants['rhoWater_SI']['value']*B*B*V[i]*V[i]),  roundingPrecision)

    def calc_trim_eL(self, theta, roundingPrecision = 10, index = -1):      #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['trim']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(firstIndex, lastIndex):
        self.dictionary['trim_eL']['value'][index] = round(self.dictionary['trim']['value'][index] + 0.12*theta,  roundingPrecision)
        
    def calc_trim_eD(self, theta, roundingPrecision = 10, index = -1):      #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['trim']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(firstIndex, lastIndex):
        self.dictionary['trim_eD']['value'][index] = round(self.dictionary['trim']['value'][index] + 0.5*theta,  roundingPrecision)
    
    def calc_CL0(self, beta, roundingPrecision = 10, index = -1):       #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['CLb']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        for i in range(self.size): #init CL0 with CLb
            self.dictionary['CL0']['value'][i] = round(self.dictionary['CLb']['value'][i], roundingPrecision)            #round not necesssary
        for k in range (0,11):
            for i in range (self.size):
                self.dictionary['CL0']['value'][i] = round(self.dictionary['CLb']['value'][i] + 0.0065*beta*math.pow(self.dictionary['CL0']['value'][i],0.6),  roundingPrecision)
            
    def calc_lambda(self, roundingPrecision = 10, index = -1):                    #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['Cv']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(firstIndex, lastIndex):
        lam = 0
        while (lam < 10):
            temp = 0.0055/self.dictionary['Cv']['value'][index]/self.dictionary['Cv']['value'][index] * math.pow(lam, 2.5)
            temp = temp + 0.012 * math.pow(lam, 0.5) 
            temp = temp - self.dictionary['CL0']['value'][index] / math.pow(self.dictionary['trim_eL']['value'][index], 1.1)     #CLO/trim_eL^1.1
            if (temp >= 0):
                break
            lam = lam + 0.0001
        self.dictionary['lambda']['value'][index] = round(lam,  roundingPrecision)
    
    
    def calc_beta_e(self, beta, theta, roundingPrecision = 10, index = -1):   #need lambda first        #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['lamda']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        beta_temp =  math.radians(beta)
        theta_temp =  math.radians(theta)
        #for i in range(firstIndex, lastIndex):
        temp = math.degrees ( math.atan(   math.tan(beta_temp) + self.dictionary['lambda']['value'][index]*math.tan(theta_temp)  ))
        self.dictionary['beta_e']['value'][index] = round( 0.5*(beta + temp) ,  roundingPrecision)
    
    def calc_CL0d(self, roundingPrecision = 10, index = -1):        #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['lambda']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(firstIndex, lastIndex):
        temp = 0.012*math.sqrt(self.dictionary['lambda']['value'][index])*math.pow(self.dictionary['trim_eL']['value'][index],1.1)         #rajouter variable trim^1.1 pour opti/voir si c'est plus rentable
        self.dictionary['CL0d']['value'][index] = round(temp, roundingPrecision)
        
    def calc_CL_beta_d(self, beta, roundingPrecision = 10, index = -1):     #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['CL0d']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(firstIndex, lastIndex):
        temp = self.dictionary['CL0d']['value'][index] - 0.0065*beta*pow(self.dictionary['CL0d']['value'][index],0.6)
        self.dictionary['CL_beta_d']['value'][index] = round(temp, roundingPrecision)
        
    def calc_Vm(self, V, beta, roundingPrecision = 10, index = -1):         #ok    
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(V)
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(firstIndex, lastIndex):
        temp = self.dictionary['lambda']['value'][index] * math.cos(math.radians(beta)) * math.cos(math.radians(self.dictionary['trim']['value'][index]))
        temp =V[index] * math.sqrt(1 - self.dictionary['CL_beta_d']['value'][index]/temp)
        self.dictionary['Vm']['value'][index] = round(temp, roundingPrecision)
        
    def calc_Re(self, B, roundingPrecision = 10, index = -1):       #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['Re']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(firstIndex, lastIndex):
        self.dictionary['Re']['value'][index] = round(self.dictionary['Vm']['value'][index]*self.dictionary['lambda']['value'][index]*B/Constants.constants['muWater_SI']['value'], roundingPrecision)
    
    def calc_Cf(self, roundingPrecision = 10, index = -1):          #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['Re']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(firstIndex, lastIndex):
        self.dictionary['Cf']['value'][index] = round(0.455/pow(math.log10(self.dictionary['Re']['value'][index]),2.58) + 0.0004,  roundingPrecision)
        
    def calc_Sf(self, B, roundingPrecision = 10, index = -1):            #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['lambda']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(firstIndex, lastIndex):
        self.dictionary['Sf']['value'][index] = round(self.dictionary['lambda']['value'][index]*B*B/math.cos(math.radians(self.dictionary['beta_e']['value'][index])),  roundingPrecision)
        
    def calc_Df(self, roundingPrecision = 10, index = -1):          #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['Vm']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(firstIndex, lastIndex):
        self.dictionary['Df']['value'][index] = round(0.97*self.dictionary['Vm']['value'][index]*self.dictionary['Vm']['value'][index]*self.dictionary['Sf']['value'][index]*self.dictionary['Cf']['value'][index],  roundingPrecision)
            
    def calc_D(self, delta, roundingPrecision = 10, index = -1):            #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['Df']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(firstIndex, lastIndex):
        self.dictionary['D']['value'][index] = round(delta*math.tan(math.radians(self.dictionary['trim_eD']['value'][index])) + self.dictionary['Df']['value'][index]/math.cos(math.radians(self.dictionary['trim_eD']['value'][index])),  roundingPrecision)
        
    def calc_Mfactor(self, LCG, B, roundingPrecision = 10, index = -1):            #ok        #need fn_vol               #deplacer LCG ici ou le rendre constant
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['Fn_vol']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(firstIndex, lastIndex):
        temp = 2*math.pow(LCG/B, 1.45) * math.exp(-2*(self.dictionary['Fn_vol']['value'][index] - 0.85))
        temp = temp - 3 * LCG/B * math.exp(-3*(self.dictionary['Fn_vol']['value'][index] - 0.85))
        temp = 0.98 + 0.5 * temp
        if (temp > 0.5):
            self.dictionary['Mfactor']['value'][index] = round(temp,  roundingPrecision)
        else:
            self.dictionary['Mfactor']['value'][index] = 0.5
        
    def calc_D_romp(self, roundingPrecision = 10, index = -1):          #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['Mfactor']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(firstIndex, lastIndex):
        self.dictionary['D_romp']['value'][index] = round(self.dictionary['Mfactor']['value'][index]*self.dictionary['D']['value'][index],  roundingPrecision)
        
    ## TRIM TABS
    
    def calc_trimTabs_DELTA (self, V, B, beta, trimChord, trimSigma, trimDelta, roundingPrecision = 10, index = -1):            #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(V)
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        for i in range(self.size):
            self.dictionary['trimTabs_DELTA']['value'][i] = round(0.046*trimChord*trimSigma*trimDelta*B*0.5*Constants.constants['rhoWater_SI']['value']*V[i]*V[i] * math.cos(math.radians(beta)),  roundingPrecision)

    def calc_trimTabs_Re (self, trimChord, roundingPrecision = 10, index = -1):         #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['Vm']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(firstIndex, lastIndex):
        self.dictionary['trimTabs_Re']['value'][index] = round(self.dictionary['Vm']['value'][index]*trimChord/Constants.constants['muWater_SI']['value'],  roundingPrecision)
        
    def calc_trimTabs_Cf (self, trimChord, roundingPrecision = 10, index = -1):         #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['trimTabs_Re']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(firstIndex, lastIndex):
        if (trimChord > 0):
            self.dictionary['trimTabs_Cf']['value'][index] = round(0.455/math.pow(math.log10(self.dictionary['trimTabs_Re']['value'][index]), 2.58),  roundingPrecision)  
        else:
            self.dictionary['trimTabs_Cf']['value'][index] = 0
        
    def calc_trimTabs_Df (self, B, trimChord, trimSigma, roundingPrecision = 10, index = -1):           #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['trimTabs_Cf']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(firstIndex, lastIndex):
        self.dictionary['trimTabs_Df']['value'][index] = round(self.dictionary['trimTabs_Cf']['value'][index]*0.5*Constants.constants['rhoWater_SI']['value']*self.dictionary['Vm']['value'][index]*self.dictionary['Vm']['value'][index]*B*trimSigma*trimChord,  roundingPrecision)
        
    def calc_trimTabs_D_L (self, trimDelta, roundingPrecision = 10, index = -1):                  #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['trim']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(firstIndex, lastIndex):
        self.dictionary['trimTabs_D_L']['value'][index] = round(0.0052*self.dictionary['trimTabs_DELTA']['value'][index]*(self.dictionary['trim']['value'][index] + trimDelta),  roundingPrecision)
        
    def calc_trimTabs_D (self, trimDelta, roundingPrecision = 10, index = -1):              #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['trim']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(firstIndex, lastIndex):
        self.dictionary['trimTabs_D']['value'][index] = round(self.dictionary['trimTabs_Df']['value'][index]*math.cos(math.radians(self.dictionary['trim']['value'][index] + trimDelta)) + self.dictionary['trimTabs_D_L']['value'][index],  roundingPrecision)
        
    def calc_trimTabs_M (self, LCG, VCG, B, trimChord, trimSigma, trimDelta, roundingPrecision = 10, index = -1):       #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['trimTabs_DELTA']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(firstIndex, lastIndex):
        temp = LCG - 0.6*B - trimChord*(1-trimSigma-math.cos(math.radians(trimDelta)))
        self.dictionary['trimTabs_M']['value'][index] = round(self.dictionary['trimTabs_DELTA']['value'][index]*temp + self.dictionary['trimTabs_D']['value'][index]*VCG,  roundingPrecision)
        
    def calc_trimTabs_H (self, trimChord, roundingPrecision = 10, index = -1):                  #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['trim']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        for i in range(self.size):
            self.dictionary['trimTabs_H']['value'][i] = round(0.139*self.dictionary['trimTabs_DELTA']['value'][i]*trimChord,  roundingPrecision)
        
        
    ## SHAFT
    
    def calc_shaft_Re_D (self, V, shaftDiameter, roundingPrecision = 10, index = -1):               #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(V)
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        for i in range(self.size):
            self.dictionary['shaft_Re_D']['value'][i] = round(V[i]*shaftDiameter/Constants.constants['muWater_SI']['value'],  roundingPrecision)
            
    def calc_shaft_Re_L (self, V, shaftLength, roundingPrecision = 10, index = -1):                 #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(V)
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        for i in range(self.size):
            self.dictionary['shaft_Re_L']['value'][i] = round(V[i]*shaftLength/Constants.constants['muWater_SI']['value'],  roundingPrecision)
        
    def calc_shaft_Cf_L (self, shaftLength, roundingPrecision = 10, index = -1):                    #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['shaft_Re_L']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        for i in range(self.size):
            if(shaftLength > 0):
                self.dictionary['shaft_Cf_L']['value'][i] = round(0.455/math.pow(math.log10(self.dictionary['shaft_Re_L']['value'][i]), 2.58),  roundingPrecision)
            else:
                self.dictionary['shaft_Cf_L']['value'][i] = 0
                
    def calc_shaft_D (self, V, shaftDiameter, shaftLength, e, roundingPrecision = 10, index = -1):          #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['shaft_Cf_L']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        for i in range(self.size):
            temp = Constants.constants['rhoWater_SI']['value']/2*shaftLength*shaftDiameter*V[i]*V[i]
            temp = temp *(1.1 * math.pow(math.sin(math.radians(e)), 3) + math.pi*self.dictionary['shaft_Cf_L']['value'][i])
            self.dictionary['shaft_D']['value'][i] = round(temp,  roundingPrecision)
        
    def calc_shaft_N (self, V, shaftDiameter, shaftLength, e, roundingPrecision = 10, index = -1):          #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['shaft_Cf_L']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        for i in range(self.size):
            temp = Constants.constants['rhoWater_SI']['value']/2*shaftLength*shaftDiameter*V[i]*V[i]*1.1
            temp = temp * math.pow(math.sin(math.radians(e)), 2) * math.cos(math.radians(e))
            self.dictionary['shaft_N']['value'][i] = round(temp,  roundingPrecision)
        
    def calc_shaft_f (self, VCG, shaft_yc, roundingPrecision = 10, index = -1):        #ok              #should not be a tab
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['shaft_Cf_L']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        for i in range(self.size):
            self.dictionary['shaft_f']['value'][i] = round(VCG - shaft_yc,  roundingPrecision)
        
    def calc_shaft_e (self, LCG, shaft_xc, roundingPrecision = 10, index = -1):           #ok           #should not be a tab
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['shaft_Cf_L']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        for i in range(self.size):
            self.dictionary['shaft_e']['value'][i] = round(LCG - shaft_xc,  roundingPrecision)
        
    def calc_shaft_M (self, roundingPrecision = 10, index = -1):                        #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['shaft_N']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        for i in range(self.size):
            self.dictionary['shaft_M']['value'][i] = round(self.dictionary['shaft_N']['value'][i]*self.dictionary['shaft_e']['value'][i] + self.dictionary['shaft_D']['value'][i]*self.dictionary['shaft_f']['value'][i],  roundingPrecision)
    
    ## STRUT
    
    def calc_strut_Re_c (self, V, strutChord, roundingPrecision = 10, index = -1):              
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(V)
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        for i in range(self.size):
            self.dictionary['strut_Re_c']['value'][i] = round(V[i]*strutChord/Constants.constants['muWater_SI']['value'], roundingPrecision)
        
    def calc_strut_CD (self, strutChord, strutThickness, roundingPrecision = 10, index = -1):
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['Cv']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        for i in range(self.size):
            if (strutChord == 0):            #faire le test avant la boucle est plus opti
                self.dictionary['strut_CD']['value'][i] = 0
            else:
                self.dictionary['strut_CD']['value'][i] = self.profiel(self.dictionary['strut_Re_c']['value'][i], strutThickness, strutChord)     #faire le test
        
    def calc_strut_D (self, V, strutArea, roundingPrecision = 10, index = -1):
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(V)
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        for i in range(self.size):
            self.dictionary['strut_D']['value'][i] = round(self.dictionary['strut_CD']['value'][i]*0.5*Constants.constants['rhoWater_SI']['value']*V[i]*V[i]*2*strutArea,  roundingPrecision)
        
    def calc_strut_f (self, VCG, strut_yc, roundingPrecision = 10, index = -1):             #should not be a tab
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['Cv']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        for i in range(self.size):
            self.dictionary['strut_f']['value'][i] = round(VCG-strut_yc,  roundingPrecision)
        
    def calc_strut_e (self, LCG, strut_xc, roundingPrecision = 10, index = -1):
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['Cv']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        for i in range(self.size):                    
            self.dictionary['strut_e']['value'][i] = round(LCG-strut_xc,  roundingPrecision)
        
    def calc_strut_M (self, roundingPrecision = 10, index = -1):
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['strut_D']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        for i in range(self.size):
            self.dictionary['strut_M']['value'][i] = round(self.dictionary['strut_D']['value'][i]*self.dictionary['strut_f']['value'][i],  roundingPrecision)
        
    ## RUDDER
    
    def calc_rudder_Re_c (self, V, rudderChord, roundingPrecision = 10, index = -1):
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(V)
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        for i in range(self.size):
            self.dictionary['rudder_Re_c']['value'][i] = round(V[i]*rudderChord/Constants.constants['muWater_SI']['value'], roundingPrecision)
        
    def calc_rudder_CD (self, rudderChord, rudderThickness, roundingPrecision = 10, index = -1):
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['Cv']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        for i in range(self.size):
            if (rudderChord == 0):            #faire le test avant la boucle est plus opti
                self.dictionary['rudder_CD']['value'][i] = 0
            else:
                self.dictionary['rudder_CD']['value'][i] = self.CD_profiel(self.dictionary['rudder_Re_c']['value'][i], rudderThickness, rudderChord)
        
    def calc_rudder_D (self, V, rudderArea, roundingPrecision = 10, index = -1):
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(V)
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        for i in range(self.size):
            self.dictionary['rudder_D']['value'][i] = round(self.dictionary['rudder_CD']['value'][i]*0.5*Constants.constants['rhoWater_SI']['value']*V[i]*V[i]*2*rudderArea,  roundingPrecision)
        
    def calc_rudder_f (self, VCG, rudder_yc, roundingPrecision = 10, index = -1):             #should not be a tab
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['Cv']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        for i in range(self.size):
            self.dictionary['rudder_f']['value'][i] = round(VCG-rudder_yc,  roundingPrecision)
        
    def calc_rudder_e (self, LCG, rudder_xc, roundingPrecision = 10, index = -1):
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['Cv']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        for i in range(self.size):                     
            self.dictionary['rudder_e']['value'][i] = round(LCG-rudder_xc,  roundingPrecision)
        
    def calc_rudder_M (self, roundingPrecision = 10, index = -1):
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['rudder_D']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        for i in range(self.size):
            self.dictionary['rudder_M']['value'][i] = round(self.dictionary['rudder_D']['value'][i]*self.dictionary['rudder_f']['value'][i],  roundingPrecision)
        
    ## RESITANCE TO AIR
    
    def calc_Zprim(self, Z, LOA, roundingPrecision = 10, index = -1):     #need h                #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['trim']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(self.size):
        self.dictionary['Zprim']['value'][index] = round(Z/math.cos(math.radians(self.dictionary['trim']['value'][index])) + LOA*math.sin(math.radians(self.dictionary['trim']['value'][index])) - self.dictionary['h']['value'][index],  roundingPrecision)
        
    def calc_A_romp(self, Bmax, roundingPrecision = 10, index = -1):                                #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['Zprim']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(self.size):
        self.dictionary['A_romp']['value'][index] = round(Bmax * self.dictionary['Zprim']['value'][index],  roundingPrecision)
        
    def calc_A_voorkant(self, roundingPrecision = 10, index = -1):                              #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['A_romp']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(self.size):
        self.dictionary['A_voorkant']['value'][index] = round(self.dictionary['A_romp']['value'][index] + self.dictionary['Ass']['value'][index],  roundingPrecision)
        
    def calc_D_air(self, V, roundingPrecision = 10, index = -1):
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(V)
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(self.size):
        self.dictionary['D_air']['value'][index] = round(0.6*Constants.constants['rhoAir_SI']['value']*V[index]*V[index]*self.dictionary['A_voorkant']['value'][index],  roundingPrecision)
        
    def calc_f_air(self, LCG, VCG, roundingPrecision = 10, index = -1):        #need h and Zprim              #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(V)
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(self.size):
        temp = self.dictionary['Zprim']['value'][index]/2 + self.dictionary['h']['value'][index]
        temp = temp - VCG * math.cos(math.radians(self.dictionary['trim']['value'][index]))
        temp = temp + LCG * math.sin(math.radians(self.dictionary['trim']['value'][index]))
        self.dictionary['f_air']['value'][index] = round(temp, roundingPrecision)
        
    def calc_M_air(self, roundingPrecision = 10, index = -1):                   #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['D_air']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(self.size):
        self.dictionary['M_air']['value'][index] = round(self.dictionary['D_air']['value'][index]* self.dictionary['f_air']['value'][index],  roundingPrecision)
    
    ## TOTAL RESITANCE
    
        
    def calc_Fh(self, nbPropellers, roundingPrecision = 10, index = -1):                #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['trim_eD']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(self.size):
        temp = self.dictionary['D_romp']['value'][index] + self.dictionary['D_air']['value'][index] + self.dictionary['trimTabs_D']['value'][index]
        temp2 = nbPropellers * (self.dictionary['shaft_D']['value'][index] + self.dictionary['strut_D']['value'][index] + self.dictionary['rudder_D']['value'][index]) * math.cos(math.radians(self.dictionary['trim_eD']['value'][index]))
        temp3 = nbPropellers * self.dictionary['shaft_N']['value'][index] * math.sin(math.radians(self.dictionary['trim_eD']['value'][index]))
        self.dictionary['Fh']['value'][index] = round(temp + temp2 + temp3,  roundingPrecision)
        
    def calc_Fv(self, nbPropellers, delta, roundingPrecision = 10, index = -1):                 #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['trim_eD']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(self.size):
        temp = delta - self.dictionary['trimTabs_DELTA']['value'][index]
        temp2 = nbPropellers * (self.dictionary['shaft_D']['value'][index] + self.dictionary['strut_D']['value'][index] + self.dictionary['rudder_D']['value'][index]) * math.sin(math.radians(self.dictionary['trim_eD']['value'][index]))
        temp3 = nbPropellers * self.dictionary['shaft_N']['value'][index] * math.cos(math.radians(self.dictionary['trim_eD']['value'][index]))
        self.dictionary['Fv']['value'][index] = round(temp + temp2 - temp3,  roundingPrecision)
        
    def calc_T(self, e, roundingPrecision = 10, index = -1):                #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['Fh']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(self.size):
        self.dictionary['T']['value'][index] = round(self.dictionary['Fh']['value'][index]/math.cos(math.radians(self.dictionary['trim_eD']['value'][index]+e)),  roundingPrecision)
        
    def calc_Nt(self, e, roundingPrecision = 10, index = -1):              #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['Fv']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(self.size):
        self.dictionary['Nt']['value'][index] = round(self.dictionary['Fv']['value'][index]*math.cos(math.radians(self.dictionary['trim_eD']['value'][index] + e)) + self.dictionary['Fh']['value'][index]*math.sin(math.radians(self.dictionary['trim_eD']['value'][index] + e)),  roundingPrecision)
        
    def calc_Cp(self, roundingPrecision = 10, index = -1):                  #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['Cv']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(self.size):
        self.dictionary['Cp']['value'][index] = round(0.75 - 1/(5.21*self.dictionary['Cv']['value'][index]*self.dictionary['Cv']['value'][index]/self.dictionary['lambda']['value'][index]/self.dictionary['lambda']['value'][index] + 2.39),  roundingPrecision)
        
    def calc_Lp(self, B, roundingPrecision = 10, index = -1):               #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['Cp']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(self.size):
        self.dictionary['Lp']['value'][index] = round(self.dictionary['Cp']['value'][index]*self.dictionary['lambda']['value'][index]*B,  roundingPrecision)
        
    def calc_c(self, LCG, roundingPrecision = 10, index = -1):                  #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['Lp']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(self.size):                                                        #deplacer LCG ici ou le rendre constant
        self.dictionary['c']['value'][index] = round(LCG - self.dictionary['Lp']['value'][index],  roundingPrecision)
            
    def calc_a(self, VCG, B, beta, roundingPrecision = 10, index = -1):            #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['Cv']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        for i in range(self.size):
            self.dictionary['a']['value'][i] = round(VCG - 0.25*B*math.tan(math.radians(beta)),  roundingPrecision)
            
    def calc_Fn_vol(self, V, delta, roundingPrecision = 10, index = -1):            #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['Cv']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        for i in range(self.size):
            self.dictionary['Fn_vol']['value'][i] = round(V[i]/math.sqrt(Constants.constants['g_SI']['value']*math.pow(delta/Constants.constants['rhogWater_SI']['value'], 1/3)),  roundingPrecision)
        
    def calc_lambda_k(self, roundingPrecision = 10, index = -1):                    #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['lambda']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(firstIndex, lastIndex):
        temp = 1.8/math.pi + self.dictionary['beta_e']['value'][index]/1000
        temp2 = math.tan(math.radians(self.dictionary['beta_e']['value'][index])) / 2
        temp2 = temp2 / math.tan(math.radians(self.dictionary['trim']['value'][index])) 
        temp2 = temp2 - self.dictionary['beta_e']['value'][index]/167
        self.dictionary['lambda_k']['value'][index] = round(self.dictionary['lambda']['value'][index] - 0.03 + temp*temp2/2,  roundingPrecision)
        
    def calc_Lk(self, B, roundingPrecision = 10, index = -1):           #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['lambda_k']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(firstIndex, lastIndex):
        self.dictionary['Lk']['value'][index] = round(self.dictionary['lambda_k']['value'][index]*B,  roundingPrecision)
        
    def calc_Lc(self, B, roundingPrecision = 10, index = -1):           #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['lambda_k']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(firstIndex, lastIndex):
        self.dictionary['Lc']['value'][index] = round(B*(2*(self.dictionary['lambda']['value'][index] - 0.03) - self.dictionary['lambda_k']['value'][index]),  roundingPrecision)
        
    def calc_h(self, B, roundingPrecision = 10, index = -1):            #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == - 1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['lambda_k']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(firstIndex, lastIndex):
        self.dictionary['h']['value'][index] = round(self.dictionary['lambda_k']['value'][index]*B*math.sin(math.radians(self.dictionary['trim']['value'][index])),  roundingPrecision)
        
    def calc_lt(self, B, roundingPrecision = 10, index = -1):           #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['Lk']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(firstIndex, lastIndex):
        self.dictionary['lt']['value'][index] = round(1/48*B*B*B*(self.dictionary['Lk']['value'][index] + 3*self.dictionary['Lc']['value'][index]), roundingPrecision)
        
    def calc_DELTA_s(self, B, roundingPrecision = 10, index = -1):              #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['lambda']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(firstIndex, lastIndex):
        temp = 0.25*Constants.constants['rhogWater_SI']['value']*B*B*B*self.dictionary['lambda']['value'][index]*self.dictionary['lambda']['value'][index]
        temp = temp * math.sin(math.radians(2*self.dictionary['trim']['value'][index]))
        temp1 = self.dictionary['Lk']['value'][index] - self.dictionary['Lc']['value'][index]
        temp2 = self.dictionary['Lk']['value'][index] + self.dictionary['Lc']['value'][index]
        self.dictionary['DELTA_s']['value'][index] = round(temp * (1 + temp1*temp1/(3*temp2*temp2)),  roundingPrecision)
        
    def calc_KB(self, B, roundingPrecision = 10, index = -1):                   #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['Lc']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(firstIndex, lastIndex):
        temp = B/6*math.tan(math.radians(self.dictionary['beta_e']['value'][index]))
        self.dictionary['KB']['value'][index] = round(temp * (1 + self.dictionary['Lc']['value'][index]/self.dictionary['Lk']['value'][index]),  roundingPrecision)
        
    def calc_BG(self, VCG, roundingPrecision = 10, index = -1):                #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['KB']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(firstIndex, lastIndex):
        self.dictionary['BG']['value'][index] = round(VCG - self.dictionary['KB']['value'][index],  roundingPrecision)
        
    def calc_a_one_s(self, roundingPrecision = 10, index = -1):                 #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['BG']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(firstIndex, lastIndex):
        self.dictionary['a_one_s']['value'][index] = round(0.624 * (-Constants.constants['rhogWater_SI']['value']*self.dictionary['lt']['value'][index] + self.dictionary['BG']['value'][index]*self.dictionary['DELTA_s']['value'][index]),  roundingPrecision)
        
    def calc_CL_beta_d2(self, roundingPrecision = 10, index = -1):                  #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['BG']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(firstIndex, lastIndex):
        temp = math.pi/4*(1-math.sin(math.radians(self.dictionary['beta_e']['value'][index])))*math.cos(math.radians(self.dictionary['trim_eL']['value'][index]))*self.dictionary['lambda']['value'][index]/(1+self.dictionary['lambda']['value'][index])
        temp = temp + 1.33/4*self.dictionary['lambda']['value'][index]*math.cos(math.radians(self.dictionary['trim_eL']['value'][index]))*math.sin(math.radians(2*self.dictionary['trim_eL']['value'][index]))*math.cos(math.radians(self.dictionary['beta_e']['value'][index]))
        self.dictionary['CL_beta_d2']['value'][index] = round(math.sin(math.radians(2*self.dictionary['trim_eL']['value'][index]))*temp,  roundingPrecision)
        
    def calc_drukpt(self, B, roundingPrecision = 10, index = -1):               #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['BG']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(firstIndex, lastIndex):
        self.dictionary['drukpt']['value'][index] = round(0.8*math.pi/4*B/2/math.cos(math.radians(self.dictionary['beta_e']['value'][index])),  roundingPrecision)
        
    def calc_arm(self, VCG, roundingPrecision = 10, index = -1):                #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = len(self.dictionary['dkrupt']['value'])
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(firstIndex, lastIndex):
        self.dictionary['arm']['value'][index] = round(self.dictionary['drukpt']['value'][index] - VCG*math.sin(math.radians(self.dictionary['beta_e']['value'][index])),  roundingPrecision)
            
    def calc_F(self, roundingPrecision = 10, index = -1):                #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = self.size
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        for i in range(self.size):
            self.dictionary['F']['value'][i] = round(self.dictionary['CLb']['value'][i]/self.dictionary['CL0']['value'][i], roundingPrecision)
    

    ##outputs
    
    def calc_Peff(self, V, roundingPrecision = 10, index = -1):                #ok
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = self.size
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        # for i in range(firstIndex, lastIndex):
        self.dictionary['Peff']['value'][index] = round(self.dictionary['Fh']['value'][index]*V[index]/550, roundingPrecision)
            
    def calc_trim_critical_angeli(self, LCG, B, DELTA, beta, beta_x, roundingPrecision = 10, index = -1):                #ok         #donner slmt les valeurs, même pour les angles
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = self.size
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
            
        x_temp = LCG / math.pow(DELTA/Constants.constants['rhogWater_SI']['value'], 1/3)
        y_temp = B / math.pow(DELTA / Constants.constants['rhogWater_SI']['value'], 1/3)
        k_temp = (106 + 85) * (1 + 0.2*(beta_x - beta)/beta_x) * math.pow(x_temp/y_temp, 0.25)
            
        for i in range(self.size):
            temp = math.pow(self.dictionary['Fn_vol']['value'][i], 2) * x_temp * y_temp * self.dictionary['F']['value'][i]
            
            self.dictionary['trim_critical_angeli']['value'][i] = round(math.pow(k_temp/temp, 0.75), roundingPrecision)
            
            
    def calc_planning(self, B, LWL, roundingPrecision = 10, index = -1):
        #assert (index >= -1), 'Out Of range Index given as parameter'
        #assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        # if index == -1:
        #     firstIndex = 0
        #     lastIndex = self.size
        # else :
        #     firstIndex = index
        #     lastIndex = index + 1
        #     
        # for i in range(firstIndex, lastIndex):
        if(LWL/B < self.dictionary['lambda_k']['value'][index]):
            self.dictionary['planning']['value'][index] =False
        else:
            self.dictionary['planning']['value'][index] = True
            
    ##fonctions de calcul annexes
    
    def CD_profiel(self, re, t, c, roundingPrecision = 10):
        ratio = t/c
        if (re < 50000):
            temp = 1.46*math.pow(re, -0.507)
            temp2 = 0.466*math.pow(re, -0.259)
            return round((temp2 - temp)/0.2*ratio + temp, roundingPrecision)
        elif (50000 <= re <= 500000):
            temp = 0.172*math.pow(re, -0.31)
            temp2 = 181*math.pow(re, -0.81)
            return round((temp2 - temp)/0.2*ratio + temp, roundingPrecision)
        elif (500000 < re <= 10000000):
            return round(0.00293 * (1 + 2*ratio+ 60 * math.pow(ratio, 4)), roundingPrecision)
        else:
            return round(0.03*math.pow(re, -0.143) * (1 + 2*ratio + 60* math.pow(ratio, 4)), roundingPrecision)


    ## Global Calculation

    def calcAllConstants(self, roundingPrecision = 10, index = -1):
        #add V
        """
        thread0 = Thread(target = self.calc_Ass, args = (self.inputDictionary['Hss']['value'], self.inputDictionary['Bss']['value'], roundingPrecision, index) ).start()     #ok   #constant
        thread1 = Thread(target = self.calc_Fn_vol, args = (self.inputDictionary['V']['SI'], self.inputDictionary['DELTA']['value'], roundingPrecision, index) ).start()    #ok   #constant
        
        thread2 = Thread(target = self.calc_Cv, args = (self.inputDictionary['V']['SI'], self.inputDictionary['B']['value'], roundingPrecision, index) ).start()       #ok         #constant
        thread3 = Thread(target = self.calc_CLb, args = (self.inputDictionary['V']['SI'], self.inputDictionary['B']['value'], self.inputDictionary['DELTA']['value'], roundingPrecision, index) ).start()   #ok   #constant
        """
        self.calc_Ass(self.inputDictionary['Hss']['value'], self.inputDictionary['Bss']['value'], roundingPrecision, index)      #ok   #constant
        self.calc_Fn_vol(self.inputDictionary['V']['SI'], self.inputDictionary['DELTA']['value'], roundingPrecision, index)     #ok   #constant
        
        self.calc_Cv(self.inputDictionary['V']['SI'], self.inputDictionary['B']['value'], roundingPrecision, index)       #ok         #constant
        self.calc_CLb(self.inputDictionary['V']['SI'], self.inputDictionary['B']['value'], self.inputDictionary['DELTA']['value'], roundingPrecision, index)   #ok   #constant
        
        #CL0 doit attendre CLb
        self.calc_CL0(self.inputDictionary['beta']['value'], roundingPrecision, index)   #ok    #constant  #need CLb
        
        self.calc_trimTabs_DELTA(self.inputDictionary['V']['SI'], self.inputDictionary['B']['value'], self.inputDictionary['beta']['value'], self.inputDictionary['TrimTab_chord']['value'], self.inputDictionary['TrimTab_sigma']['value'], self.inputDictionary['TrimTab_delta']['value'], roundingPrecision, index)      #ok        #constant
        self.calc_trimTabs_H(self.inputDictionary['TrimTab_chord']['value'], roundingPrecision, index) #need trimTabs_DELTA   -> constant        #ok
        
        self.calc_shaft_Re_D(self.inputDictionary['V']['SI'], self.inputDictionary['Shaft_diameter']['value'], roundingPrecision, index) #contant           #ok
        self.calc_shaft_Re_L(self.inputDictionary['V']['SI'], self.inputDictionary['Shaft_length']['value'], roundingPrecision, index) #constant        #ok
        self.calc_shaft_Cf_L(self.inputDictionary['Shaft_length']['value'], roundingPrecision, index) #need shaft_Re_L    #constant         #ok
        self.calc_shaft_D(self.inputDictionary['V']['SI'], self.inputDictionary['Shaft_diameter']['value'], self.inputDictionary['Shaft_length']['value'], self.inputDictionary['e']['value'], roundingPrecision, index) #need shaft_Cf    #constant        #ok
        self.calc_shaft_N(self.inputDictionary['V']['SI'], self.inputDictionary['Shaft_diameter']['value'], self.inputDictionary['Shaft_length']['value'], self.inputDictionary['e']['value'], roundingPrecision, index) #constant          #ok
        self.calc_shaft_f(self.inputDictionary['VCG']['value'], self.inputDictionary['Shaft_yc']['value'], roundingPrecision, index) #constant, should not be a tab         #ok
        self.calc_shaft_e(self.inputDictionary['LCG']['value'], self.inputDictionary['Shaft_xc']['value'], roundingPrecision, index)   #constant, should not be a tab           #ok
        self.calc_shaft_M(roundingPrecision, index) #need shaft_N, shaft_e, shaft_D, shaft_f     #constant         #ok
        
        
        self.calc_strut_Re_c(self.inputDictionary['V']['SI'], self.inputDictionary['Strut_chord']['value'], roundingPrecision, index) #constant         #ok
        self.calc_strut_CD(self.inputDictionary['Strut_chord']['value'], self.inputDictionary['Strut_thickness']['value'], roundingPrecision, index) #constant normally         #ok
        self.calc_strut_D(self.inputDictionary['V']['SI'], self.inputDictionary['Strut_area']['value'], roundingPrecision, index) #constant normally        #ok
        self.calc_strut_f(self.inputDictionary['VCG']['value'], self.inputDictionary['Strut_yc']['value'], roundingPrecision, index) #constant          #ok
        self.calc_strut_e(self.inputDictionary['LCG']['value'], self.inputDictionary['Strut_xc']['value'], roundingPrecision, index) #constant      #ok
        self.calc_strut_M(roundingPrecision, index) #constant normally          #ok
        
        self.calc_rudder_Re_c(self.inputDictionary['V']['SI'], self.inputDictionary['Rudder_chord']['value'], roundingPrecision, index) #constant           #ok
        self.calc_rudder_CD(self.inputDictionary['Rudder_chord']['value'], self.inputDictionary['Rudder_thickness']['value'], roundingPrecision, index) #constant normally      #ok
        self.calc_rudder_D(self.inputDictionary['V']['SI'], self.inputDictionary['Rudder_area']['value'], roundingPrecision, index) #constant normally      #ok
        self.calc_rudder_f(self.inputDictionary['VCG']['value'], self.inputDictionary['Rudder_yc']['value'], roundingPrecision, index) #constant        #ok
        self.calc_rudder_e(self.inputDictionary['LCG']['value'], self.inputDictionary['Rudder_xc']['value'], roundingPrecision, index) #constant    #ok
        self.calc_rudder_M(roundingPrecision, index) #constant normally         #ok
        
        self.calc_a(self.inputDictionary['VCG']['value'], self.inputDictionary['B']['value'], self.inputDictionary['beta']['value'], roundingPrecision, index) #constant        #ok
        
        self.calc_F(roundingPrecision, index)
        self.calc_trim_critical_angeli(self.inputDictionary['LCG']['value'], self.inputDictionary['B']['value'], self.inputDictionary['DELTA']['value'], self.inputDictionary['beta']['value'], self.inputDictionary['beta_x']['value'], roundingPrecision, index)
    
    
    def calcAll(self, roundingPrecision = 10, index = -1):
        
        self.calc_trim_eL(self.inputDictionary['theta']['value'], roundingPrecision, index)     #ok
        self.calc_trim_eD(self.inputDictionary['theta']['value'], roundingPrecision, index)     #ok

        self.calc_lambda(roundingPrecision, index)  #need trim_eL
        
        self.calc_beta_e(self.inputDictionary['beta']['value'], self.inputDictionary['theta']['value'], roundingPrecision, index)  #need lambda         #ok
        
        self.calc_CL0d(roundingPrecision, index) #need lambda et trim_eL        #ok
        self.calc_CL_beta_d(self.inputDictionary['beta']['value'], roundingPrecision, index) #need CL0d     #ok
        self.calc_Vm(self.inputDictionary['V']['SI'], self.inputDictionary['beta']['value'], roundingPrecision, index) #need lambda         #ok
        self.calc_Re(self.inputDictionary['B']['value'], roundingPrecision, index) #need Vm, lambda     #ok
        self.calc_Cf(roundingPrecision, index) #need Re         #ok
        self.calc_Sf(self.inputDictionary['B']['value'], roundingPrecision, index) #need lam, beta_e        #ok
        self.calc_Df(roundingPrecision, index) #need Vm, Sf, Cf         #ok
        self.calc_D(self.inputDictionary['DELTA']['value'], roundingPrecision, index) #need trim_eD, Df  #ok
        
        self.calc_Mfactor(self.inputDictionary['LCG']['value'],self.inputDictionary['B']['value'], roundingPrecision, index) #need Fn_vol  #LCG not a tab for now                 #constant       #ok
        
        self.calc_D_romp(roundingPrecision, index) #need Mfactor, D         #ok
        
        self.calc_trimTabs_Re(self.inputDictionary['TrimTab_chord']['value'], roundingPrecision, index) #need Vm           #ok
        self.calc_trimTabs_Cf(self.inputDictionary['TrimTab_chord']['value'], roundingPrecision, index) #need trimTabs_Re       #ok
        self.calc_trimTabs_Df(self.inputDictionary['B']['value'],self.inputDictionary['TrimTab_chord']['value'],self.inputDictionary['TrimTab_sigma']['value'], roundingPrecision, index) #need Vm, trimTabs_Cf         #ok
        self.calc_trimTabs_D_L(self.inputDictionary['TrimTab_delta']['value'], roundingPrecision, index) #need trimTabs_DELTA, trim         #ok
        self.calc_trimTabs_D(self.inputDictionary['TrimTab_delta']['value'], roundingPrecision, index) #need trimTabs_Df, trimTabs_D_L, trim        #ok
        self.calc_trimTabs_M(self.inputDictionary['LCG']['value'], self.inputDictionary['VCG']['value'],self.inputDictionary['B']['value'], self.inputDictionary['TrimTab_chord']['value'], self.inputDictionary['TrimTab_sigma']['value'], self.inputDictionary['TrimTab_delta']['value'], roundingPrecision, index) #need trimTabs_DELTA, trimTabs_D              #ok
        
        
        self.calc_Cp(roundingPrecision, index)  #need Cv, lambda        #ok
        self.calc_Lp(self.inputDictionary['B']['value'], roundingPrecision, index) #need Cp, lambda  #ok
        self.calc_c(self.inputDictionary['LCG']['value'], roundingPrecision, index) #need Lp  #ok
        
        
        self.calc_lambda_k(roundingPrecision, index) #need lambda, beta_e, trim     #ok
        self.calc_planning(self.inputDictionary['B']['value'], self.inputDictionary['LWL']['value'], roundingPrecision, index) #need lambda_k  
        self.calc_Lk(self.inputDictionary['B']['value'], roundingPrecision, index) #need lambda_k  #ok
        self.calc_Lc(self.inputDictionary['B']['value'], roundingPrecision, index) #need lambda, lambda_k       #ok

        self.calc_h(self.inputDictionary['B']['value'], roundingPrecision, index) #need lambda_k, trim    #ok
        
        #resistance to air
        self.calc_Zprim(self.inputDictionary['Z']['value'], self.inputDictionary['LOA']['value'], roundingPrecision, index)      #need trim, h first        #ok
        self.calc_A_romp(self.inputDictionary['Bmax']['value'], roundingPrecision, index) #need Zprim    #ok
        self.calc_A_voorkant(roundingPrecision, index) #need A_romp         #ok
        self.calc_D_air(self.inputDictionary['V']['SI'], roundingPrecision, index) #need A_voorkant         #ok
        self.calc_f_air(self.inputDictionary['LCG']['value'], self.inputDictionary['VCG']['value'], roundingPrecision, index) #need Zprim, h, trim          #ok
        self.calc_M_air(roundingPrecision, index) #need D_air, f_air        #ok
        
        #total resistance
        self.calc_Fh(self.inputDictionary['propellersNumber']['value'], roundingPrecision, index)    #need D_romp, D_F, ***D_air***, shaft_D, strut_D, rudder_D, trim_eD, shaft_N           #ok
        self.calc_Fv(self.inputDictionary['propellersNumber']['value'], self.inputDictionary['DELTA']['value'], roundingPrecision, index) #need trimTabs_DELTA, shaft_D, strut_D, rudder_D, trim_eD, shaft_N         #ok
        self.calc_T(self.inputDictionary['e']['value'], roundingPrecision, index) #need Fh, trim_eD             #ok
        self.calc_Nt(self.inputDictionary['e']['value'], roundingPrecision, index) #need Fh, Fv, trim_eD        #ok
        
        
        
        self.calc_lt(self.inputDictionary['B']['value'], roundingPrecision, index) #need Lk, Lc    #ok
        self.calc_DELTA_s(self.inputDictionary['B']['value'], roundingPrecision, index) #need Lk, Lc, lambda, trim          #ok
        self.calc_KB(self.inputDictionary['B']['value'], roundingPrecision, index) #need Lk, Lc, beta_e     #ok
        self.calc_BG(self.inputDictionary['VCG']['value'], roundingPrecision, index) #need KB       #ok
        self.calc_a_one_s(roundingPrecision, index) #need BG, DELTA_s       #ok
        
        #calc_CL_beta_d2 ?????
        
        self.calc_drukpt(self.inputDictionary['B']['value'], roundingPrecision, index) #need beta_e     #ok
        self.calc_arm(self.inputDictionary['VCG']['value'], roundingPrecision, index) #need drukpt, beta_e      #ok
        
        
        self.calc_M(self.inputDictionary['propellersNumber']['value'], self.inputDictionary['f']['value'], roundingPrecision, index)  #need Nt, c, trimTabs_M, shaft_M, strut_M, rudder_M, Df, a, T, M_air    #ok

        self.calc_Peff(self.inputDictionary['V']['SI'], roundingPrecision, index)
        

    ##other functions

    
    def initArray(self):
        return [0]*self.size
    
    def initSpeed(self):                            #    à appeler dans une fonction d'init
        n = len(self.inputDictionary['V']['value1'])
        n2 = len(self.inputDictionary['V']['SI'])
        if(n2<n):
            for i in range (0,n):
                self.inputDictionary['V']['SI'].append(round(Units.unitConversion(self.inputDictionary['V']['unitType'],self.inputDictionary['V']['value1'][i], self.inputDictionary['V']['unit1'], self.inputDictionary['V']['unit2']), 4))  #3 = precision
    
    def initAll(self):
        for key in self.dictionary.keys():
            self.dictionary[key]['value']=self.initArray()
        self.initSpeed()

    


size = 10            
        
def initArray(size):
    return [0]*size
    
def initAll(dict, size):
    for key in dict:
        dict[key]['value']=initArray(size)

def roundAll(dict, precision):
    for key in dict:
        n = len (dict[key]['value'])
        for i in range(0,n):
            dict[key]['value'][i] = round(dict[key]['value'][i], precision)




def showParam(dict, key, key2):
    string = ''
    for i in range (len(dict[key][key2])):
        string = string + str(dict[key][key2][i]) + ';  '
    print(key + ' : ' + string)
        
def showAll(dict, roundingPrecision = 5):
    print ('       ################       CONSTANT VALUES           #############       \n')
    for key in dict:
        string = ''
        if (dict[key]['constant']):
            for i in range (len(dict[key]['value'])):
                string = string + str(round(dict[key]['value'][i], roundingPrecision)) + ';  '
            print(key + ' : ' + string)
    print ('\n\n       ################      NON CONSTANT VALUES           #############       \n')
    for key in dict:
        string = ''
        if (not(dict[key]['constant'])):
            for i in range (len(dict[key]['value'])):
                string = string + str(round(dict[key]['value'][i], roundingPrecision)) + ';  '
            print(key + ' : ' + string)
    
def calcTrim(size):
    pass
    

def printMatrix(matrix):
    n = len(matrix[0])
    for i in range(0,n):
        print (matrix[i])


            
if (__name__ == '__main__'):
    '''
    dict = {'Cv': {'value': None, 'Function': None}}
    print(dict)
    initAll(dict)
    print(dict)
    for i in range(0,10):
        dict['Cv']['value'][i]=10.
    print(dict)
    
    a=0.6565
    b = -a
    print (b)
    '''
    
    calcul = Computation(IF.initialInputs, len(IF.initialInputs['V']['value1']))
    """
    initAll(calcul.dictionary, calcul.size)
    
    IF.initSpeed(IF.initialInputs['V'])                 # add a calc_V ??
    """
    
    #calcul.initAll()
    
    showParam(IF.initialInputs, 'V', 'value1')
    showParam(IF.initialInputs, 'V', 'SI')
    
    '''
    calcul.calc_trim()
    
    calcul.calc_Cv(IF.initialInputs['V']['SI'], IF.initialInputs['B']['value'])
    calcul.calc_CLb(IF.initialInputs['V']['SI'], IF.initialInputs['B']['value'], IF.initialInputs['DELTA']['value'])
    '''
    
    
    #calcul.calc_Cv(IF.initialInputs['V']['SI'], IF.initialInputs['B']['value'], 2.0)
    with Timer.LoggerTimer('Trim '):
        for i in range(10):
            calcul.calc_trim()
    
    #roundAll(calcul.dictionary, 5)
    #showAll(calcul.dictionary)
            
            
