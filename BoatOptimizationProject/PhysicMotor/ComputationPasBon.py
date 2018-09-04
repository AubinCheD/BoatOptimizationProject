import math as math

import sys
sys.path.insert(0, './')

import ConstantsNotSI as Constants
import Units as Units

sys.path.insert(0, '../')
import GraphicMotor.InitFileNotSI2 as IF


class Computation ():            #rename en classe individu ?? + prendre 3 dicos : inputs / outputs / calcul
        
    #docstring
    """(docstring) Classe Inputs"""

    
    def __init__ (self, size):   #size = size of the vector of speeds
        
        #format    'key' : [value(float), variation pourcentage(int ou float), used in GA or not(boolean), "name printed on the GUI"]
        
        self.size = size
        
        self.dictionary = {    # 'key' : [value:float, unitType: string, unit: string, variationType, variation, displayedName: string, usedInGA: boolean]
                              #depending on variationType, variation is either a float or a tab [min: float, max: float, step: float]
                              #maybe don't need variationType and unitType
         
        
        #on pourrait créer un sous dictionnaire avec comme clés les noms des catégories pour une création automatique de l'interface, à essayer un jour

        #intermediate calculation
            
            'M': {'value': None, 'constant': False},       #dans quel ordre faire le calcul par rapport à trim ?          #une output ??    needs Nt, c, Df, T first
            
            'Ass': {'value': None, 'constant': True},
            
            ##une solution: {value: [], 'Fun': f, args: [list of args]}
            
            
            #15
            'Cv': {'value': None, 'constant': True},                      #une lambda ?
            'CLb': {'value': None, 'constant': True},
            'trim': {'value': None, 'constant': False},                                                  #18 trim is an output ?                to calculate
            'trim_eL': {'value': None, 'constant': False},
            'trim_eD': {'value': None, 'constant': False},
            'beta_e': {'value': None, 'constant': False},
            'CL0': {'value': None, 'constant': True},
            # 'CL0_on_trim_eL_1_1':
            'lambda': {'value': None, 'constant': False},
            'CL0d': {'value': None, 'constant': False},
            'CL_beta_d': {'value': None, 'constant': False},               #problem with line 123
            'Vm': {'value': None, 'constant': False},
            'Re': {'value': None, 'constant': False},
            'Cf': {'value': None, 'constant': False},
            'Sf': {'value': None, 'constant': False},
            'Df': {'value': None, 'constant': False},
            'D': {'value': None, 'constant': False},
            'Mfactor': {'value': None, 'constant': False},
            'D_romp': {'value': None, 'constant': False},
            
            #Trim Tabs
            'trimTabs_DELTA': {'value': None, 'constant': True},
            'trimTabs_Re': {'value': None, 'constant': False},
            'trimTabs_Cf': {'value': None, 'constant': False},
            'trimTabs_Df': {'value': None, 'constant': False},
            'trimTabs_D_L': {'value': None, 'constant': False},
            'trimTabs_D': {'value': None, 'constant': False},
            'trimTabs_M': {'value': None, 'constant': False},
            'trimTabs_H': {'value': None, 'constant': True},
            
            #shaft
            'shaft_Re_D': {'value': None, 'constant': True},
            'shaft_Re_L': {'value': None, 'constant': True},
            'shaft_Cf_L': {'value': None, 'constant': True},
            'shaft_D': {'value': None, 'constant': True},
            'shaft_N': {'value': None, 'constant': True},
            'shaft_f': {'value': None, 'constant': True},
            'shaft_e': {'value': None, 'constant': True},
            'shaft_M': {'value': None, 'constant': True},
            
            #strut
            'strut_Re_c': {'value': None, 'constant': True},
            'strut_CD': {'value': None, 'constant': True},
            'strut_D': {'value': None, 'constant': True},
            'strut_f': {'value': None, 'constant': True},
            'strut_e': {'value': None, 'constant': True},
            'strut_M': {'value': None, 'constant': True},            
            
            #rudder
            'rudder_Re_c': {'value': None, 'constant': True},
            'rudder_CD': {'value': None, 'constant': True},
            'rudder_D': {'value': None, 'constant': True},
            'rudder_f': {'value': None, 'constant': True},
            'rudder_e': {'value': None, 'constant': True},
            'rudder_M': {'value': None, 'constant': True},
                        
            
            #Air Resistance
            'Zprim': {'value': None, 'constant': False},  #?
            'A_romp': {'value': None, 'constant': False},  #?
            'A_voorkant': {'value': None, 'constant': False}, #?
            'D_air': {'value': None, 'constant': False},
            'f_air': {'value': None, 'constant': False},
            'M_air': {'value': None, 'constant': False},
            
            #total resistance
            'Fh': {'value': None, 'constant': False},
            'Fv': {'value': None, 'constant': False},
            'T': {'value': None, 'constant': False},
            'Nt': {'value': None, 'constant': False},
            'Cp': {'value': None, 'constant': False},
            'Lp': {'value': None, 'constant': False},
            'c': {'value': None, 'constant': False},
            'a': {'value': None, 'constant': False},
            'Fn_vol': {'value': None, 'constant': True},
            #99
            'lambda_k': {'value': None, 'constant': False},
            'Lk': {'value': None, 'constant': False},
            'Lc': {'value': None, 'constant': False},
            'h': {'value': None, 'constant': False},
            
            #ROLSTABILITEIT    #using another article
            'lt': {'value': None, 'constant': False},
            'DELTA_s': {'value': None, 'constant': False},
            'KB': {'value': None, 'constant': False},
            'BG': {'value': None, 'constant': False},
            'a_one_s': {'value': None, 'constant': False},
            'CL_beta_d2': {'value': None, 'constant': False},          #problem with line 30
            'drukpt': {'value': None, 'constant': False},      #???
            'arm': {'value': None, 'constant': False}
        
        }    
       
                    
                    
                    ##                                                    modifier les n=len() .. par self.size
    
    #Calculation functions
    
    def calc_M(self, NbPropellers, f, roundingPrecision = 10, index = -1):          #need Nt, c ..., to put in the end of calculation, see..                #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['Ass']['value'][i])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            temp = self.dictionary['Nt']['value'][i] * self.dictionary['c']['value'][i]+ self.dictionary['trimTabs_M']['value'][i]
            temp = temp + NbPropellers*(self.dictionary['shaft_M']['value'][i]+self.dictionary['rudder_M']['value'][i]+self.dictionary['strut_M']['value'][i])
            temp = temp + self.dictionary['Df']['value'][i]*self.dictionary['a']['value'][i] 
            temp = temp - self.dictionary['T']['value'][i]*f
            temp = temp - self.dictionary['M_air']['value'][i] 
            self.dictionary['M']['value'][i] = round(temp, roundingPrecision)
    
    
    def calc_Ass(self, Hss, Bss, roundingPrecision = 10, index = -1):   #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['trim']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['Ass']['value'][i] = round(Hss*Bss, roundingPrecision)
    
    
    def calc_trim(self, roundingPrecision = 10):
        self.calcAllConstants()
        
        n = len(self.dictionary['trim']['value'])
        trim = 0.
        j = -1
        tabA = [0]*n
        tabTijdelijk = [0]*n
        
        print('calc_trim : Entrée boucle initialization')
        for i in range(0, n):
            self.dictionary['trim']['value'][i] = 0.0001
            self.calcAll(roundingPrecision, i)
            if (self.dictionary['M']['value'][i] > 0):
                j = i
        
        showAll(self.dictionary)
        
        print('calc_trim : Entrée boucle 1 : step 1')
        for i in range(j+1, n):
            trim = 0.1
            while(trim < 2.2):
                self.dictionary['trim']['value'][i] = trim
                self.calcAll(roundingPrecision, i)
                if (self.dictionary['M']['value'][i] < 0):
                    tabTijdelijk[i] = trim
                    trim = trim + 1
                else:
                    break
            self.dictionary['trim']['value'][i] = tabTijdelijk[i]
            self.calcAll(roundingPrecision, i)              #au cas où
            tabA[i] = tabTijdelijk[i]
            
            #print('\n\n               tour numéro ' + str(i))
        showAll(self.dictionary)
        
    
    def calc_trim2(self, roundingPrecision = 10):
        self.calcAllConstants()
        
        n = len(self.dictionary['trim']['value'])
        j=-1
        tabA = [0]*n       #tester les valeurs des tableaux
        tabTemp = [0]*n
        
        mat = [[0 for i in range(n)] for j in range(n)]
            
        indL = 0
        indC = 0
        
        print('calc_trim : Entrée boucle 1')
        for i in range (0,n):
            self.dictionary['trim']['value'][i] = 0.0001
            self.calcAll(roundingPrecision, i)                                              #modifier pour avoir un calcAll par colonne
            #showAll(calcul.dictionary)
            if (self.dictionary['M']['value'][i] > 0):  
                j = i
        """
        for i in range (0,n):
            print ('trim : ' + str(self.dictionary['trim']['value'][i]))
        """
        
        print('calc_trim : Entrée boucle 2')
        for i in range (j+1, n):
            trim = 0.1
            #indC=0
            while (trim < 15.1):
                self.dictionary['trim']['value'][i] = trim
                #print("i : " + str(i) +"  trim1 : " + str(self.dictionary['trim']['value'][i]))
                
                #mat[i][indC] = trim
                
                self.calcAll(roundingPrecision, i)
                #showAll(calcul.dictionary) 
                
                #print ('boucle1 trim : ' + str(self.dictionary['trim']['value'][i]))
                
                if (self.dictionary['M']['value'][i] < 0):
                    tabTemp[i] = self.dictionary['trim']['value'][i]
                    #print("i : " + str(i) +"  tabtemp : " + str(tabTemp[i]))
                    trim = trim + 1
                else:
                    break
                
                #indC = indC + 1
            
            self.dictionary['trim']['value'][i] = tabTemp[i]
            self.calcAll(roundingPrecision, i)
            #print("i : " + str(i) +"  trim2 : " + str(self.dictionary['trim']['value'][i]))
            tabA[i] = tabTemp[i]
            
        #printMatrix(mat)
        
        
        print('calc_trim : Entrée boucle 3')
        for i in range (j+1, n):
            trim = tabA[i]
            while (trim < 15.1):
                self.dictionary['trim']['value'][i] = trim
                self.calcAll(roundingPrecision, i)
                #showAll(calcul.dictionary)
                if (self.dictionary['M']['value'][i] < 0):
                    tabTemp[i] = self.dictionary['trim']['value'][i]
                    trim = trim + 0.1
                else:
                    break
            self.dictionary['trim']['value'][i] = tabTemp[i]
            self.calcAll(roundingPrecision, i)
            tabA[i] = tabTemp[i]
        
        print('calc_trim : Entrée boucle 4')
        for i in range (j+1, n):
            trim = tabA[i]
            while (trim < 15.01):
                self.dictionary['trim']['value'][i] = trim
                self.calcAll(roundingPrecision, i)
                #showAll(calcul.dictionary) 
                if (self.dictionary['M']['value'][i] < 0):
                    tabTemp[i] = self.dictionary['trim']['value'][i]
                    trim = trim + 0.01
                else:
                    break
            self.dictionary['trim']['value'][i] = tabTemp[i]
            self.calcAll(roundingPrecision, i)
            tabA[i] = tabTemp[i]
                    
        print('calc_trim : Entrée boucle 5')
        for i in range (j+1, n):
            trim = tabA[i]
            while (trim < 15.001):
                self.dictionary['trim']['value'][i] = trim
                self.calcAll(roundingPrecision, i)
                #showAll(calcul.dictionary) 
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
        
        print('calc_trim : Entrée boucle 6')
        for i in range (j+1, n):
            trim = tabA[i]
            while (trim < 15.0001):
                self.dictionary['trim']['value'][i] = trim
                self.calcAll(roundingPrecision, i)
                #showAll(calcul.dictionary) 
                if (self.dictionary['M']['value'][i] >= 0):
                    break
                trim = trim + 0.0001
            if (self.dictionary['trim']['value'][i] > 13):
                break
        
        print('calc_trim : Entrée boucle 7')
        if (j != -1):
            for i in range (0,j+1):
                #print('test boucle')
                self.dictionary['trim']['value'][i] = 0   # ou = '-'
                self.calcAll(roundingPrecision, i)
        
        
        '''
        for i in range (j+1, n):
            if (self.dictionary['trim']['value'][i] > 15):
                self.dictionary['trim']['value'][i] = ' > 15'
        '''
    
    
    def calc_Cv(self, V, B, roundingPrecision = 10, index = -1):         #if index == -1, calculate the all tab, otherwise calcultate only tab[index]           #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(V)
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['Cv']['value'][i] = round(V[i]/math.sqrt(Constants.constants['g_SI']['value']*B),  roundingPrecision)
    
    def calc_CLb(self, V, B, delta, roundingPrecision = 10, index = -1):    #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(V)
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['CLb']['value'][i] = round(delta/(0.5*Constants.constants['rhoWater_SI']['value']*B*B*V[i]*V[i]),  roundingPrecision)

        
    def calc_trim_eL(self, theta, roundingPrecision = 10, index = -1):      #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['trim']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['trim_eL']['value'][i] = round(self.dictionary['trim']['value'][i] + 0.12*theta,  roundingPrecision)
            #print('trim_eL = ' + str(self.dictionary['trim_eL']['value'][i]))
        
    def calc_trim_eD(self, theta, roundingPrecision = 10, index = -1):      #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['trim']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['trim_eD']['value'][i] = round(self.dictionary['trim']['value'][i] + 0.5*theta,  roundingPrecision)
            #print('trim_eD = ' + str(self.dictionary['trim_eD']['value'][i]))
    
    def calc_CL0(self, beta, roundingPrecision = 10, index = -1):       #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['CLb']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex): #init CL0 with CLb
            self.dictionary['CL0']['value'][i] = round(self.dictionary['CLb']['value'][i], roundingPrecision)            #round not necesssary
        for k in range (0,11):
            for i in range (firstIndex, lastIndex):
                self.dictionary['CL0']['value'][i] = round(self.dictionary['CLb']['value'][i] + 0.0065*beta*math.pow(self.dictionary['CL0']['value'][i],0.6),  roundingPrecision)
            
    
    def calc_lambda(self, roundingPrecision = 10, index = -1):                    #ok         #division par zéro, à check
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['Cv']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            lam = 0
            while (lam < 10):
                temp = 0.0055/self.dictionary['Cv']['value'][i]/self.dictionary['Cv']['value'][i]
                temp = temp + 0.012 * math.pow(lam, 0.5) 
                temp = temp - self.dictionary['CL0']['value'][i] / math.pow(self.dictionary['trim_eL']['value'][i], 1.1)     #CLO/trim_eL^1.1
                """print('lambda temp = ' + str(temp))
                print('CL0 =  ' + str(self.dictionary['CL0']['value'][i]))
                print('Cl0/trim_eL^1.1  =  ' + str(self.dictionary['CL0']['value'][i] / math.pow(self.dictionary['trim_eL']['value'][i], 1.1)))
                print('positive part =  ' + str(0.0055/self.dictionary['Cv']['value'][i]/self.dictionary['Cv']['value'][i] + 0.12 * math.pow(lam, 0.5)))"""
                if (temp >= 0):
                    break
                lam = lam + 0.0001
            self.dictionary['lambda']['value'][i] = round(lam,  roundingPrecision)
    
    
    def calc_beta_e(self, beta, theta, roundingPrecision = 10, index = -1):   #need lambda first        #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['lamda']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        beta_temp =  Units.angleConversion(beta,'\u00B0','rad')
        theta_temp =  Units.angleConversion(theta,'\u00B0','rad')
        for i in range(firstIndex, lastIndex):
            temp = Units.angleConversion(   math.atan(   math.tan(beta_temp) + self.dictionary['lambda']['value'][i]*math.tan(theta_temp)  )  ,'rad','\u00B0'  )
            self.dictionary['beta_e']['value'][i] = round( 0.5*(beta + temp) ,  roundingPrecision)
        
   
    #def calc_CL0_on_trim_e:
    #    pass
        
    
    def calc_CL0d(self, roundingPrecision = 10, index = -1):        #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['lambda']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            temp = 0.012*math.sqrt(self.dictionary['lambda']['value'][i])*math.pow(self.dictionary['trim_eL']['value'][i],1.1)         #rajouter variable trim^1.1 pour opti/voir si c'est plus rentable
            self.dictionary['CL0d']['value'][i] = round(temp, roundingPrecision)
        
    def calc_CL_beta_d(self, beta, roundingPrecision = 10, index = -1):     #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['CL0d']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            #print('CL0d : ' + str(self.dictionary['CL0d']['value'][i]))
            #print('test : ' + str(0.0065*beta*pow(self.dictionary['CL0d']['value'][i],0.6)))
            temp = self.dictionary['CL0d']['value'][i] - 0.0065*beta*pow(self.dictionary['CL0d']['value'][i],0.6)
            self.dictionary['CL_beta_d']['value'][i] = round(temp, roundingPrecision)
        
    def calc_Vm(self, V, beta, roundingPrecision = 10, index = -1):         #ok    
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(V)
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            temp = self.dictionary['lambda']['value'][i] * math.cos(Units.angleConversion(beta,'\u00B0','rad')) * math.cos(Units.angleConversion(self.dictionary['trim']['value'][i],'\u00B0','rad'))
            '''print('temp = ' + str(temp))
            print('lambda =  ' + str(self.dictionary['lambda']['value'][i] ))
            print('cos beta  =  ' + str(math.cos(Units.angleConversion(beta,'\u00B0','rad'))))
            print('cos trim  =  ' + str(math.cos(Units.angleConversion(self.dictionary['trim']['value'][i],'\u00B0','rad'))))'''
            temp =V[i] * math.sqrt(1 - self.dictionary['CL_beta_d']['value'][i]/temp)  #division par 0
            self.dictionary['Vm']['value'][i] = round(temp, roundingPrecision)
        
    def calc_Re(self, B, roundingPrecision = 10, index = -1):       #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['Re']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['Re']['value'][i] = round(self.dictionary['Vm']['value'][i]*self.dictionary['lambda']['value'][i]*B/Constants.constants['muWater_SI']['value'], roundingPrecision)
    
    def calc_Cf(self, roundingPrecision = 10, index = -1):          #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['Re']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            #print('value  = ' + str(self.dictionary['Re']['value'][i]))
            #if self.dictionary['Re']['value'][i] != 0:
             #   self.dictionary['Cf']['value'][i] = round(0.455/pow(math.log10(self.dictionary['Re']['value'][i]),2.58) + 0.0004, 4)
            #else:
             #   self.dictionary['Cf']['value'][i] = 0.0004
            #print('Re = ' + str(self.dictionary['Re']['value'][i]))
            #print( 'log Re = ' + str(math.log10(self.dictionary['Re']['value'][i])))
            self.dictionary['Cf']['value'][i] = round(0.455/pow(math.log10(self.dictionary['Re']['value'][i]),2.58) + 0.0004,  roundingPrecision)
        
    def calc_Sf(self, B, roundingPrecision = 10, index = -1):            #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['lambda']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['Sf']['value'][i] = round(self.dictionary['lambda']['value'][i]*B*B/math.cos(Units.angleConversion(self.dictionary['beta_e']['value'][i],'\u00B0','rad')),  roundingPrecision)
        
    def calc_Df(self, roundingPrecision = 10, index = -1):          #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['Vm']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['Df']['value'][i] = round(0.97*self.dictionary['Vm']['value'][i]*self.dictionary['Vm']['value'][i]*self.dictionary['Sf']['value'][i]*self.dictionary['Cf']['value'][i],  roundingPrecision)
            
    def calc_D(self, delta, roundingPrecision = 10, index = -1):            #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['Df']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            #print('D neg : ' + str(Units.angleConversion(self.dictionary['trim_eD']['value'][i],'\u00B0','rad')))
            self.dictionary['D']['value'][i] = round(delta*math.tan(Units.angleConversion(self.dictionary['trim_eD']['value'][i],'\u00B0','rad')) + self.dictionary['Df']['value'][i]/math.cos(Units.angleConversion(self.dictionary['trim_eD']['value'][i],'\u00B0','rad')),  roundingPrecision)
        
    def calc_Mfactor(self, LCG, B, roundingPrecision = 10, index = -1):            #ok        #need fn_vol               #deplacer LCG ici ou le rendre constant
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['Fn_vol']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            temp = 2*math.pow(LCG/B, 1.45) * math.exp(-2*(self.dictionary['Fn_vol']['value'][i] - 0.85))
            temp = temp - 3 * LCG/B * math.exp(-3*(self.dictionary['Fn_vol']['value'][i] - 0.85))
            temp = 0.98 + 0.5 * temp
            if (temp > 0.5):
                self.dictionary['Mfactor']['value'][i] = round(temp,  roundingPrecision)
            else:
                self.dictionary['Mfactor']['value'][i] = 0.5
        
    def calc_D_romp(self, roundingPrecision = 10, index = -1):          #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['Mfactor']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['D_romp']['value'][i] = round(self.dictionary['Mfactor']['value'][i]*self.dictionary['D']['value'][i],  roundingPrecision)
        
    ## TRIM TABS
    
    def calc_trimTabs_DELTA (self, V, B, beta, trimChord, trimSigma, trimDelta, roundingPrecision = 10, index = -1):            #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(V)
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['trimTabs_DELTA']['value'][i] = round(0.046*trimChord*trimSigma*trimDelta*B*0.5*Constants.constants['rhoWater_SI']['value']*V[i]*V[i] * math.cos(Units.angleConversion(beta,'\u00B0','rad')),  roundingPrecision)

    def calc_trimTabs_Re (self, trimChord, roundingPrecision = 10, index = -1):         #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['Vm']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['trimTabs_Re']['value'][i] = round(self.dictionary['Vm']['value'][i]*trimChord/Constants.constants['muWater_SI']['value'],  roundingPrecision)
        
    def calc_trimTabs_Cf (self, trimChord, roundingPrecision = 10, index = -1):         #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['trimTabs_Re']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            if (trimChord > 0):
                self.dictionary['trimTabs_Cf']['value'][i] = round(0.455/math.pow(math.log10(self.dictionary['trimTabs_Re']['value'][i]), 2.58),  roundingPrecision)  
            else:
                self.dictionary['trimTabs_Cf']['value'][i] = 0
        
    def calc_trimTabs_Df (self, B, trimChord, trimSigma, roundingPrecision = 10, index = -1):           #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['trimTabs_Cf']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['trimTabs_Df']['value'][i] = round(self.dictionary['trimTabs_Cf']['value'][i]*0.5*Constants.constants['rhoWater_SI']['value']*self.dictionary['Vm']['value'][i]*self.dictionary['Vm']['value'][i]*B*trimSigma*trimChord,  roundingPrecision)
        
        
    def calc_trimTabs_D_L (self, trimDelta, roundingPrecision = 10, index = -1):                  #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['trim']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['trimTabs_D_L']['value'][i] = round(0.0052*self.dictionary['trimTabs_DELTA']['value'][i]*(self.dictionary['trim']['value'][i] + trimDelta),  roundingPrecision)
        
        
    def calc_trimTabs_D (self, trimDelta, roundingPrecision = 10, index = -1):              #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['trim']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['trimTabs_D']['value'][i] = round(self.dictionary['trimTabs_Df']['value'][i]*math.cos(Units.angleConversion(self.dictionary['trim']['value'][i] + trimDelta,'\u00B0','rad')) + self.dictionary['trimTabs_D_L']['value'][i],  roundingPrecision)
        
        
    def calc_trimTabs_M (self, LCG, VCG, B, trimChord, trimSigma, trimDelta, roundingPrecision = 10, index = -1):       #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['trimTabs_DELTA']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            temp = LCG - 0.6*B - trimChord*(1-trimSigma-math.cos(Units.angleConversion(trimDelta,'\u00B0','rad')))
            self.dictionary['trimTabs_M']['value'][i] = round(self.dictionary['trimTabs_DELTA']['value'][i]*temp + self.dictionary['trimTabs_D']['value'][i]*VCG,  roundingPrecision)
        
    def calc_trimTabs_H (self, trimChord, roundingPrecision = 10, index = -1):                  #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['trim']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['trimTabs_H']['value'][i] = round(0.139*self.dictionary['trimTabs_DELTA']['value'][i]*trimChord,  roundingPrecision)
        
        
    ## SHAFT
    
    def calc_shaft_Re_D (self, V, shaftDiameter, roundingPrecision = 10, index = -1):               #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(V)
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['shaft_Re_D']['value'][i] = round(V[i]*shaftDiameter/Constants.constants['muWater_SI']['value'],  roundingPrecision)
            
    def calc_shaft_Re_L (self, V, shaftLength, roundingPrecision = 10, index = -1):                 #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(V)
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['shaft_Re_L']['value'][i] = round(V[i]*shaftLength/Constants.constants['muWater_SI']['value'],  roundingPrecision)
        
    def calc_shaft_Cf_L (self, shaftLength, roundingPrecision = 10, index = -1):                    #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['shaft_Re_L']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            if(shaftLength > 0):
                self.dictionary['shaft_Cf_L']['value'][i] = round(0.455/math.pow(math.log10(self.dictionary['shaft_Re_L']['value'][i]), 2.58),  roundingPrecision)
            else:
                self.dictionary['shaft_Cf_L']['value'][i] = 0
                
        
    def calc_shaft_D (self, V, shaftDiameter, shaftLength, e, roundingPrecision = 10, index = -1):          #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['shaft_Cf_L']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            temp = Constants.constants['rhoWater_SI']['value']/2*shaftLength*shaftDiameter*V[i]*V[i]
            temp = temp *(1.1 * math.pow(math.sin(Units.angleConversion(e,'\u00B0','rad')), 3) + math.pi*self.dictionary['shaft_Cf_L']['value'][i])
            self.dictionary['shaft_D']['value'][i] = round(temp,  roundingPrecision)
        
    def calc_shaft_N (self, V, shaftDiameter, shaftLength, e, roundingPrecision = 10, index = -1):          #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['shaft_Cf_L']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            temp = Constants.constants['rhoWater_SI']['value']/2*shaftLength*shaftDiameter*V[i]*V[i]*1.1
            temp = temp * math.pow(math.sin(Units.angleConversion(e,'\u00B0','rad')), 2) * math.cos(Units.angleConversion(e,'\u00B0','rad'))
            self.dictionary['shaft_N']['value'][i] = round(temp,  roundingPrecision)
        
    def calc_shaft_f (self, VCG, shaft_yc, roundingPrecision = 10, index = -1):        #ok              #should not be a tab
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['shaft_Cf_L']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['shaft_f']['value'][i] = round(VCG - shaft_yc,  roundingPrecision)
        
    def calc_shaft_e (self, LCG, shaft_xc, roundingPrecision = 10, index = -1):           #ok           #should not be a tab
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['shaft_Cf_L']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['shaft_e']['value'][i] = round(LCG - shaft_xc,  roundingPrecision)
        
    def calc_shaft_M (self, roundingPrecision = 10, index = -1):                        #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['shaft_N']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['shaft_M']['value'][i] = round(self.dictionary['shaft_N']['value'][i]*self.dictionary['shaft_e']['value'][i] + self.dictionary['shaft_D']['value'][i]*self.dictionary['shaft_f']['value'][i],  roundingPrecision)
    
    ## STRUT
    
    def calc_strut_Re_c (self, V, strutChord, roundingPrecision = 10, index = -1):              
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(V)
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['strut_Re_c']['value'][i] = round(V[i]*strutChord/Constants.constants['muWater_SI']['value'], roundingPrecision)
        
    def calc_strut_CD (self, strutChord, strutThickness, roundingPrecision = 10, index = -1):
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['Cv']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            if (strutChord == 0):            #faire le test avant la boucle est plus opti
                self.dictionary['strut_CD']['value'][i] = 0
            else:
                self.dictionary['strut_CD']['value'][i] = self.profiel(self.dictionary['strut_Re_c']['value'][i], strutThickness, strutChord)     #faire le test
        
    def calc_strut_D (self, V, strutArea, roundingPrecision = 10, index = -1):
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(V)
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['strut_D']['value'][i] = round(self.dictionary['strut_CD']['value'][i]*0.5*Constants.constants['rhoWater_SI']['value']*V[i]*V[i]*2*strutArea,  roundingPrecision)
        
    def calc_strut_f (self, VCG, strut_yc, roundingPrecision = 10, index = -1):             #should not be a tab
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['Cv']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['strut_f']['value'][i] = round(VCG-strut_yc,  roundingPrecision)
        
    def calc_strut_e (self, LCG, strut_xc, roundingPrecision = 10, index = -1):
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['Cv']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):                    
            self.dictionary['strut_e']['value'][i] = round(LCG-strut_xc,  roundingPrecision)
        
    def calc_strut_M (self, roundingPrecision = 10, index = -1):
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['strut_D']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['strut_M']['value'][i] = round(self.dictionary['strut_D']['value'][i]*self.dictionary['strut_f']['value'][i],  roundingPrecision)
        
    ## RUDDER
    
    def calc_rudder_Re_c (self, V, rudderChord, roundingPrecision = 10, index = -1):
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(V)
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['rudder_Re_c']['value'][i] = round(V[i]*rudderChord/Constants.constants['muWater_SI']['value'], roundingPrecision)
        
    def calc_rudder_CD (self, rudderChord, rudderThickness, roundingPrecision = 10, index = -1):
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['Cv']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            if (rudderChord == 0):            #faire le test avant la boucle est plus opti
                self.dictionary['rudder_CD']['value'][i] = 0
            else:
                self.dictionary['rudder_CD']['value'][i] = self.CD_profiel(self.dictionary['rudder_Re_c']['value'][i], rudderThickness, rudderChord)
        
    def calc_rudder_D (self, V, rudderArea, roundingPrecision = 10, index = -1):
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(V)
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['rudder_D']['value'][i] = round(self.dictionary['rudder_CD']['value'][i]*0.5*Constants.constants['rhoWater_SI']['value']*V[i]*V[i]*2*rudderArea,  roundingPrecision)
        
    def calc_rudder_f (self, VCG, rudder_yc, roundingPrecision = 10, index = -1):             #should not be a tab
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['Cv']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['rudder_f']['value'][i] = round(VCG-rudder_yc,  roundingPrecision)
        
    def calc_rudder_e (self, LCG, rudder_xc, roundingPrecision = 10, index = -1):
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['Cv']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):                     
            self.dictionary['rudder_e']['value'][i] = round(LCG-rudder_xc,  roundingPrecision)
        
    def calc_rudder_M (self, roundingPrecision = 10, index = -1):
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['rudder_D']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['rudder_M']['value'][i] = round(self.dictionary['rudder_D']['value'][i]*self.dictionary['rudder_f']['value'][i],  roundingPrecision)
        
    ## RESITANCE TO AIR
    
    def calc_Zprim(self, Z, LOA, roundingPrecision = 10, index = -1):     #need h                #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['trim']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['Zprim']['value'][i] = round(Z/math.cos(Units.angleConversion(self.dictionary['trim']['value'][i],'\u00B0','rad')) + LOA*math.sin(Units.angleConversion(self.dictionary['trim']['value'][i],'\u00B0','rad')) - self.dictionary['h']['value'][i],  roundingPrecision)
        
    def calc_A_romp(self, Bmax, roundingPrecision = 10, index = -1):                                #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['Zprim']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['A_romp']['value'][i] = round(Bmax * self.dictionary['Zprim']['value'][i],  roundingPrecision)
        
    def calc_A_voorkant(self, roundingPrecision = 10, index = -1):                              #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['A_romp']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['A_voorkant']['value'][i] = round(self.dictionary['A_romp']['value'][i] + self.dictionary['Ass']['value'][i],  roundingPrecision)
        
    def calc_D_air(self, V, roundingPrecision = 10, index = -1):
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(V)
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['D_air']['value'][i] = round(0.6*Constants.constants['rhoAir_SI']['value']*V[i]*V[i]*self.dictionary['A_voorkant']['value'][i],  roundingPrecision)
        
    def calc_f_air(self, LCG, VCG, roundingPrecision = 10, index = -1):        #need h and Zprim       #a rajouter              #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(V)
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            temp = self.dictionary['Zprim']['value'][i]/2 + self.dictionary['h']['value'][i]
            temp = temp - VCG * math.cos(Units.angleConversion(self.dictionary['trim']['value'][i],'\u00B0','rad'))
            temp = temp - LCG * math.sin(Units.angleConversion(self.dictionary['trim']['value'][i],'\u00B0','rad'))
            self.dictionary['f_air']['value'][i] = round(temp, roundingPrecision)
        
    def calc_M_air(self, roundingPrecision = 10, index = -1):                   #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['D_air']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['M_air']['value'][i] = round(self.dictionary['D_air']['value'][i]* self.dictionary['f_air']['value'][i],  roundingPrecision)
    
    ## TOTAL RESITANCE
    
        
    def calc_Fh(self, nbPropellers, roundingPrecision = 10, index = -1):                #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['trim_eD']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            temp = self.dictionary['D_romp']['value'][i] + self.dictionary['D_air']['value'][i] + self.dictionary['trimTabs_D']['value'][i]
            temp2 = nbPropellers * (self.dictionary['shaft_D']['value'][i] + self.dictionary['strut_D']['value'][i] + self.dictionary['rudder_D']['value'][i]) * math.cos(Units.angleConversion(self.dictionary['trim_eD']['value'][i],'\u00B0','rad'))
            temp3 = nbPropellers * self.dictionary['shaft_N']['value'][i] * math.sin(Units.angleConversion(self.dictionary['trim_eD']['value'][i],'\u00B0','rad'))
            self.dictionary['Fh']['value'][i] = round(temp + temp2 + temp3,  roundingPrecision)
        
    def calc_Fv(self, nbPropellers, delta, roundingPrecision = 10, index = -1):                 #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['trim_eD']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            temp = delta - self.dictionary['trimTabs_DELTA']['value'][i]
            temp2 = nbPropellers * (self.dictionary['shaft_D']['value'][i] + self.dictionary['strut_D']['value'][i] + self.dictionary['rudder_D']['value'][i]) * math.sin(Units.angleConversion(self.dictionary['trim_eD']['value'][i],'\u00B0','rad'))
            temp3 = nbPropellers * self.dictionary['shaft_N']['value'][i] * math.cos(Units.angleConversion(self.dictionary['trim_eD']['value'][i],'\u00B0','rad'))
            self.dictionary['Fv']['value'][i] = round(temp + temp2 - temp3,  roundingPrecision)
        
    def calc_T(self, e, roundingPrecision = 10, index = -1):                #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['Fh']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['T']['value'][i] = round(self.dictionary['Fh']['value'][i]/math.cos(Units.angleConversion(self.dictionary['trim_eD']['value'][i]+e,'\u00B0','rad')),  roundingPrecision)
        
    def calc_Nt(self, e, roundingPrecision = 10, index = -1):              #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['Fv']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['Nt']['value'][i] = round(self.dictionary['Fv']['value'][i]*math.cos(Units.angleConversion(self.dictionary['trim_eD']['value'][i] + e,'\u00B0','rad')) + self.dictionary['Fh']['value'][i]*math.sin(Units.angleConversion(self.dictionary['trim_eD']['value'][i] + e,'\u00B0','rad')),  roundingPrecision)
        
    def calc_Cp(self, roundingPrecision = 10, index = -1):                  #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['Cv']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['Cp']['value'][i] = round(0.75 - 1/(5.21*self.dictionary['Cv']['value'][i]*self.dictionary['Cv']['value'][i]/self.dictionary['lambda']['value'][i]/self.dictionary['lambda']['value'][i] + 2.39),  roundingPrecision)
        
    def calc_Lp(self, B, roundingPrecision = 10, index = -1):               #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['Cp']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['Lp']['value'][i] = round(self.dictionary['Cp']['value'][i]*self.dictionary['lambda']['value'][i]*B,  roundingPrecision)
        
    def calc_c(self, LCG, roundingPrecision = 10, index = -1):                  #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['Lp']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):                                                        #deplacer LCG ici ou le rendre constant
            self.dictionary['c']['value'][i] = round(LCG - self.dictionary['Lp']['value'][i],  roundingPrecision)
            
    def calc_a(self, VCG, B, beta, roundingPrecision = 10, index = -1):            #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['Cv']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['a']['value'][i] = round(VCG - 0.25*B*math.tan(Units.angleConversion(beta,'\u00B0','rad')),  roundingPrecision)
            
    def calc_Fn_vol(self, V, delta, roundingPrecision = 10, index = -1):            #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['Cv']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['Fn_vol']['value'][i] = round(V[i]/math.sqrt(Constants.constants['g_SI']['value']*math.pow(delta/Constants.constants['rhogWater_SI']['value'], 1/3)),  roundingPrecision)
        
    def calc_lambda_k(self, roundingPrecision = 10, index = -1):                    #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['lambda']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            #print('lambda_k trim= ' + str(self.dictionary['trim']['value'][i]))
            #print('lambda_k tan(trim) = ' + str(Units.angleConversion(self.dictionary['trim']['value'][i],'\u00B0','rad')))
            
            print('lam - 0.03 = ' +str(self.dictionary['lambda']['value'][i] - 0.03) )
            temp = 1.8/math.pi + self.dictionary['beta_e']['value'][i]/1000
            print('1) = ' + str(temp))
            
            ######           Units.angleConversion(self.dictionary['beta_e']['value'][i],'\u00B0','rad')
            
            temp2 = math.tan(math.radians(self.dictionary['beta_e']['value'][i])) / 2
            temp2 = temp2 / math.tan(math.radians(self.dictionary['trim']['value'][i])) 
            print('3) = ' + str(temp2))
            temp2 = temp2 - self.dictionary['beta_e']['value'][i]/167
            print('2) = ' + str(temp2))
            
            print('4) = ' + str(self.dictionary['beta_e']['value'][i]/167))
            
            print('5) = ' + str(math.tan(Units.angleConversion(self.dictionary['beta_e']['value'][i],'\u00B0','rad'))))
            print('6) = ' + str(math.tan(Units.angleConversion(self.dictionary['trim']['value'][i],'\u00B0','rad'))))
            
            print(math.tan(Units.angleConversion(0.0001,'\u00B0','rad')))
            print(math.tan(math.radians(0.0001)))
            print(math.pi)
            
            self.dictionary['lambda_k']['value'][i] = round(self.dictionary['lambda']['value'][i] - 0.03 + temp*temp2/2,  roundingPrecision)
        
    def calc_Lk(self, B, roundingPrecision = 10, index = -1):           #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['lambda_k']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['Lk']['value'][i] = round(self.dictionary['lambda_k']['value'][i]*B,  roundingPrecision)
        
    def calc_Lc(self, B, roundingPrecision = 10, index = -1):           #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['lambda_k']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['Lc']['value'][i] = round(B*(2*(self.dictionary['lambda']['value'][i] - 0.03) - self.dictionary['lambda_k']['value'][i]),  roundingPrecision)
        
    def calc_h(self, B, roundingPrecision = 10, index = -1):            #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == - 1:
            firstIndex = 0
            lastIndex = len(self.dictionary['lambda_k']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['h']['value'][i] = round(self.dictionary['lambda_k']['value'][i]*B*math.sin(Units.angleConversion(self.dictionary['trim']['value'][i],'\u00B0','rad')),  roundingPrecision)
        
    def calc_lt(self, B, roundingPrecision = 10, index = -1):           #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['Lk']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['lt']['value'][i] = round(1/48*B*B*B*(self.dictionary['Lk']['value'][i] + 3*self.dictionary['Lc']['value'][i]), roundingPrecision)
        
    def calc_DELTA_s(self, B, roundingPrecision = 10, index = -1):              #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['lambda']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            temp = 0.25*Constants.constants['rhogWater_SI']['value']*B*B*B*self.dictionary['lambda']['value'][i]*self.dictionary['lambda']['value'][i]
            temp = temp * math.sin(Units.angleConversion(2*self.dictionary['trim']['value'][i],'\u00B0','rad'))
            temp1 = self.dictionary['Lk']['value'][i] - self.dictionary['Lc']['value'][i]
            temp2 = self.dictionary['Lk']['value'][i] + self.dictionary['Lc']['value'][i]
            self.dictionary['DELTA_s']['value'][i] = round(temp * (1 + temp1*temp1/(3*temp2*temp2)),  roundingPrecision)
        
    def calc_KB(self, B, roundingPrecision = 10, index = -1):                   #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['Lc']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            temp = B/6*math.tan(Units.angleConversion(self.dictionary['beta_e']['value'][i],'\u00B0','rad'))
            self.dictionary['KB']['value'][i] = round(temp * (1 + self.dictionary['Lc']['value'][i]/self.dictionary['Lk']['value'][i]),  roundingPrecision)
        
    def calc_BG(self, VCG, roundingPrecision = 10, index = -1):                #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['KB']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['BG']['value'][i] = round(VCG - self.dictionary['KB']['value'][i],  roundingPrecision)
        
    def calc_a_one_s(self, roundingPrecision = 10, index = -1):                 #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['BG']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['a_one_s']['value'][i] = round(0.624 * (-Constants.constants['rhogWater_SI']['value']*self.dictionary['lt']['value'][i] + self.dictionary['BG']['value'][i]*self.dictionary['DELTA_s']['value'][i]),  roundingPrecision)
        
    def calc_CL_beta_d2(self, roundingPrecision = 10, index = -1):                  #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['BG']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            temp = math.pi/4*(1-math.sin(Units.angleConversion(self.dictionary['beta_e']['value'][i],'\u00B0','rad')))*math.cos(Units.angleConversion(self.dictionary['trim_eL']['value'][i],'\u00B0','rad'))*self.dictionary['lambda']['value'][i]/(1+self.dictionary['lambda']['value'][i])
            temp = temp + 1.33/4*self.dictionary['lambda']['value'][i]*math.cos(Units.angleConversion(self.dictionary['trim_eL']['value'][i],'\u00B0','rad'))*math.sin(Units.angleConversion(2*self.dictionary['trim_eL']['value'][i],'\u00B0','rad'))*math.cos(Units.angleConversion(self.dictionary['beta_e']['value'][i],'\u00B0','rad'))
            self.dictionary['CL_beta_d2']['value'][i] = round(math.sin(Units.angleConversion(2*self.dictionary['trim_eL']['value'][i],'\u00B0','rad'))*temp,  roundingPrecision)
        
    def calc_drukpt(self, B, roundingPrecision = 10, index = -1):               #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['BG']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['drukpt']['value'][i] = round(0.8*math.pi/4*B/2/math.cos(Units.angleConversion(self.dictionary['beta_e']['value'][i],'\u00B0','rad')),  roundingPrecision)
        
    def calc_arm(self, VCG, roundingPrecision = 10, index = -1):                #ok
        assert (index >= -1), 'Out Of range Index given as parameter'
        assert (isinstance(index, int)), 'Type Error for Index : given ' + str(type(index)) + ', must be ' + str(type(int()))
        if index == -1:
            firstIndex = 0
            lastIndex = len(self.dictionary['dkrupt']['value'])
        else :
            firstIndex = index
            lastIndex = index + 1
        for i in range(firstIndex, lastIndex):
            self.dictionary['arm']['value'][i] = round(self.dictionary['drukpt']['value'][i] - VCG*math.sin(Units.angleConversion(self.dictionary['beta_e']['value'][i],'\u00B0','rad')),  roundingPrecision)
            
            
            
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


## some calc are constant in time
    def calcAllConstants(self, roundingPrecision = 10, index = -1):
        #add V
        
        self.calc_Ass(IF.initialInputs['Hss']['value'], IF.initialInputs['Bss']['value'], roundingPrecision, index)      #ok   #constant
        self.calc_Fn_vol(IF.initialInputs['V']['SI'], IF.initialInputs['DELTA']['value'], roundingPrecision, index)     #ok   #constant
        
        self.calc_Cv(IF.initialInputs['V']['SI'], IF.initialInputs['B']['value'], roundingPrecision, index)       #ok         #constant
        self.calc_CLb(IF.initialInputs['V']['SI'], IF.initialInputs['B']['value'], IF.initialInputs['DELTA']['value'], roundingPrecision, index)   #ok   #constant
        
        self.calc_CL0(IF.initialInputs['beta']['value'], roundingPrecision, index)   #ok    #constant
        
        self.calc_trimTabs_DELTA(IF.initialInputs['V']['SI'], IF.initialInputs['B']['value'], IF.initialInputs['beta']['value'], IF.initialInputs['TrimTab_chord']['value'], IF.initialInputs['TrimTab_sigma']['value'], IF.initialInputs['TrimTab_delta']['value'], roundingPrecision, index)      #ok        #constant
        self.calc_trimTabs_H(IF.initialInputs['TrimTab_chord']['value'], roundingPrecision, index) #need trimTabs_DELTA   -> constant        #ok
        
        self.calc_shaft_Re_D(IF.initialInputs['V']['SI'], IF.initialInputs['Shaft_diameter']['value'], roundingPrecision, index) #contant           #ok
        self.calc_shaft_Re_L(IF.initialInputs['V']['SI'], IF.initialInputs['Shaft_length']['value'], roundingPrecision, index) #constant        #ok
        self.calc_shaft_Cf_L(IF.initialInputs['Shaft_length']['value'], roundingPrecision, index) #need shaft_Re_L    #constant         #ok
        self.calc_shaft_D(IF.initialInputs['V']['SI'], IF.initialInputs['Shaft_diameter']['value'], IF.initialInputs['Shaft_length']['value'], IF.initialInputs['e']['value'], roundingPrecision, index) #need shaft_Cf    #constant        #ok
        self.calc_shaft_N(IF.initialInputs['V']['SI'], IF.initialInputs['Shaft_diameter']['value'], IF.initialInputs['Shaft_length']['value'], IF.initialInputs['e']['value'], roundingPrecision, index) #constant          #ok
        self.calc_shaft_f(IF.initialInputs['VCG']['value'], IF.initialInputs['Shaft_yc']['value'], roundingPrecision, index) #constant, should not be a tab         #ok
        self.calc_shaft_e(IF.initialInputs['LCG']['value'], IF.initialInputs['Shaft_xc']['value'], roundingPrecision, index)   #constant, should not be a tab           #ok
        self.calc_shaft_M(roundingPrecision, index) #need shaft_N, shaft_e, shaft_D, shaft_f     #constant         #ok
        
        
        self.calc_strut_Re_c(IF.initialInputs['V']['SI'], IF.initialInputs['Strut_chord']['value'], roundingPrecision, index) #constant         #ok
        self.calc_strut_CD(IF.initialInputs['Strut_chord']['value'], IF.initialInputs['Strut_thickness']['value'], roundingPrecision, index) #constant normally         #ok
        self.calc_strut_D(IF.initialInputs['V']['SI'], IF.initialInputs['Strut_area']['value'], roundingPrecision, index) #constant normally        #ok
        self.calc_strut_f(IF.initialInputs['VCG']['value'], IF.initialInputs['Strut_yc']['value'], roundingPrecision, index) #constant          #ok
        self.calc_strut_e(IF.initialInputs['LCG']['value'], IF.initialInputs['Strut_xc']['value'], roundingPrecision, index) #constant      #ok
        self.calc_strut_M(roundingPrecision, index) #constant normally          #ok
        
        self.calc_rudder_Re_c(IF.initialInputs['V']['SI'], IF.initialInputs['Rudder_chord']['value'], roundingPrecision, index) #constant           #ok
        self.calc_rudder_CD(IF.initialInputs['Rudder_chord']['value'], IF.initialInputs['Rudder_thickness']['value'], roundingPrecision, index) #constant normally      #ok
        self.calc_rudder_D(IF.initialInputs['V']['SI'], IF.initialInputs['Rudder_area']['value'], roundingPrecision, index) #constant normally      #ok
        self.calc_rudder_f(IF.initialInputs['VCG']['value'], IF.initialInputs['Rudder_yc']['value'], roundingPrecision, index) #constant        #ok
        self.calc_rudder_e(IF.initialInputs['LCG']['value'], IF.initialInputs['Rudder_xc']['value'], roundingPrecision, index) #constant    #ok
        self.calc_rudder_M(roundingPrecision, index) #constant normally         #ok
        
    
    def calcAll(self, roundingPrecision = 10, index = -1):        ## séparer en 2 fonctions -> certaines valeurs n'ont pas besoin d'être recalculées
    
        #self.calc_Ass(IF.initialInputs['Hss']['value'], IF.initialInputs['Bss']['value'], index)       #constante
        
        #self.calc_Fn_vol(IF.initialInputs['V']['SI'], IF.initialInputs['DELTA']['value'], index)        #constante
        
        #self.calc_Cv(IF.initialInputs['V']['SI'], IF.initialInputs['B']['value'], index)                #constante
        #self.calc_CLb(IF.initialInputs['V']['SI'], IF.initialInputs['B']['value'], IF.initialInputs['DELTA']['value'], index)      #constante
        
        #self.calc_CL0(IF.initialInputs['beta']['value'], index)       #constant
        
        #self.calc_trim()
        self.calc_trim_eL(IF.initialInputs['theta']['value'], roundingPrecision, index)     #ok
        self.calc_trim_eD(IF.initialInputs['theta']['value'], roundingPrecision, index)     #ok

        self.calc_lambda(roundingPrecision, index)  
        
        self.calc_beta_e(IF.initialInputs['beta']['value'], IF.initialInputs['theta']['value'], roundingPrecision, index)  #need lambda         #ok
        
        self.calc_CL0d(roundingPrecision, index) #need lambda et trim_eL        #ok
        self.calc_CL_beta_d(IF.initialInputs['beta']['value'], roundingPrecision, index) #need CL0d     #ok
        self.calc_Vm(IF.initialInputs['V']['SI'], IF.initialInputs['beta']['value'], roundingPrecision, index) #need lambda         #ok
        self.calc_Re(IF.initialInputs['B']['value'], roundingPrecision, index) #need Vm, lambda     #ok
        self.calc_Cf(roundingPrecision, index) #need Re         #ok
        self.calc_Sf(IF.initialInputs['B']['value'], roundingPrecision, index) #need lam, beta_e        #ok
        self.calc_Df(roundingPrecision, index) #need Vm, Sf, Cf         #ok
        self.calc_D(IF.initialInputs['DELTA']['value'], roundingPrecision, index) #need trim_eD, Df  #ok
        
        self.calc_Mfactor(IF.initialInputs['LCG']['value'],IF.initialInputs['B']['value'], roundingPrecision, index) #need Fn_vol  #LCG not a tab for now                 #constant       #ok
        
        self.calc_D_romp(roundingPrecision, index) #need Mfactor, D         #ok
        
        #tabs
        #self.calc_trimTabs_DELTA(IF.initialInputs['V']['SI'], IF.initialInputs['B']['value'], IF.initialInputs['beta']['value'], IF.initialInputs['TrimTab_chord']['value'], IF.initialInputs['TrimTab_sigma']['value'], IF.initialInputs['TrimTab_delta']['value'], index)         #constante
        
        #print('DELTA fin : ' + str(self.dictionary['trimTabs_DELTA']['value']))
        
        self.calc_trimTabs_Re(IF.initialInputs['TrimTab_chord']['value'], roundingPrecision, index) #need Vm           #ok
        self.calc_trimTabs_Cf(IF.initialInputs['TrimTab_chord']['value'], roundingPrecision, index) #need trimTabs_Re       #ok
        self.calc_trimTabs_Df(IF.initialInputs['B']['value'],IF.initialInputs['TrimTab_chord']['value'],IF.initialInputs['TrimTab_sigma']['value'], roundingPrecision, index) #need Vm, trimTabs_Cf         #ok
        self.calc_trimTabs_D_L(IF.initialInputs['TrimTab_delta']['value'], roundingPrecision, index) #need trimTabs_DELTA, trim         #ok
        self.calc_trimTabs_D(IF.initialInputs['TrimTab_delta']['value'], roundingPrecision, index) #need trimTabs_Df, trimTabs_D_L, trim        #ok
        self.calc_trimTabs_M(IF.initialInputs['LCG']['value'], IF.initialInputs['VCG']['value'],IF.initialInputs['B']['value'], IF.initialInputs['TrimTab_chord']['value'], IF.initialInputs['TrimTab_sigma']['value'], IF.initialInputs['TrimTab_delta']['value'], roundingPrecision, index) #need trimTabs_DELTA, trimTabs_D              #ok
        #self.calc_trimTabs_H(IF.initialInputs['TrimTab_chord']['value'], index) #need trimTabs_DELTA   -> constant
        
        #shaft
        #self.calc_shaft_Re_D(IF.initialInputs['V']['SI'], IF.initialInputs['Shaft_diameter']['value'], index) #contant
        #self.calc_shaft_Re_L(IF.initialInputs['V']['SI'], IF.initialInputs['Shaft_length']['value'], index) #constant
        #self.calc_shaft_Cf_L(IF.initialInputs['Shaft_length']['value'], index) #need shaft_Re_L    #constant
        #self.calc_shaft_D(IF.initialInputs['V']['SI'], IF.initialInputs['Shaft_diameter']['value'], IF.initialInputs['Shaft_length']['value'], IF.initialInputs['e']['value'], index) #need shaft_Cf    #constant
        #self.calc_shaft_N(IF.initialInputs['V']['SI'], IF.initialInputs['Shaft_diameter']['value'], IF.initialInputs['Shaft_length']['value'], IF.initialInputs['e']['value'], index) #constant
        #self.calc_shaft_f(IF.initialInputs['VCG']['value'], IF.initialInputs['Shaft_yc']['value'], index) #constant, should not be a tab
        #self.calc_shaft_e(IF.initialInputs['LCG']['value'], IF.initialInputs['Shaft_xc']['value'], index)   #constant, should not be a tab
        #self.calc_shaft_M(index) #need shaft_N, shaft_e, shaft_D, shaft_f     #constant
        
        #strut          #faire des tests avec d'autres valeurs; rajouter les need
        #self.calc_strut_Re_c(IF.initialInputs['V']['SI'], IF.initialInputs['Strut_chord']['value'], index) #constant
        #self.calc_strut_CD(IF.initialInputs['Strut_chord']['value'], IF.initialInputs['Strut_thickness']['value'], index) #constant normally
        #self.calc_strut_D(IF.initialInputs['V']['SI'], IF.initialInputs['Strut_area']['value'], index) #constant normally
        #self.calc_strut_f(IF.initialInputs['VCG']['value'], IF.initialInputs['Strut_yc']['value'], index) #constant
        #self.calc_strut_e(IF.initialInputs['LCG']['value'], IF.initialInputs['Strut_xc']['value'], index) #constant
        #self.calc_strut_M(index) #constant normally
        
        #rudder      #faire des tests avec d'autres valeurs; rajouter les need
        #self.calc_rudder_Re_c(IF.initialInputs['V']['SI'], IF.initialInputs['Rudder_chord']['value'], index) #constant
        #self.calc_rudder_CD(IF.initialInputs['Rudder_chord']['value'], IF.initialInputs['Rudder_thickness']['value'], index) #constant normally
        #self.calc_rudder_D(IF.initialInputs['V']['SI'], IF.initialInputs['Rudder_area']['value'], index) #constant normally
        #self.calc_rudder_f(IF.initialInputs['VCG']['value'], IF.initialInputs['Rudder_yc']['value'], index) #constant
        #self.calc_rudder_e(IF.initialInputs['LCG']['value'], IF.initialInputs['Rudder_xc']['value'], index) #constant
        #self.calc_rudder_M(index) #constant normally
        
        #resistance to air
        #self.calc_Zprim(IF.initialInputs['Z']['value'], IF.initialInputs['LOA']['value'], index)      #need h first
        #self.calc_A_romp(IF.initialInputs['Bmax']['value'], index) #need Zprim
        #self.calc_A_voorkant(index) #need A_romp
        #self.calc_D_air(IF.initialInputs['V']['SI'], index) #need A_voorkant
        #self.calc_f_air(index)
        #self.calc_M_air(index)
        
        #total resistance
        #self.calc_Fh(IF.initialInputs['propellersNumber']['value'], index)                                                     
        #self.calc_Fv(IF.initialInputs['propellersNumber']['value'], IF.initialInputs['DELTA']['value'], index)            
        
        #self.calc_T(IF.initialInputs['e']['value'], index)
        #self.calc_Nt(IF.initialInputs['e']['value'], index)
        
        
        self.calc_Cp(roundingPrecision, index)  #need Cv, lambda        #ok
        self.calc_Lp(IF.initialInputs['B']['value'], roundingPrecision, index) #need Cp, lambda  #ok
        self.calc_c(IF.initialInputs['LCG']['value'], roundingPrecision, index) #need Lp  #ok
        self.calc_a(IF.initialInputs['VCG']['value'], IF.initialInputs['B']['value'], IF.initialInputs['beta']['value'], roundingPrecision, index) #constant        #ok
        
        self.calc_lambda_k(roundingPrecision, index) #need lambda, beta_e, trim     #ok
        self.calc_Lk(IF.initialInputs['B']['value'], roundingPrecision, index) #need lambda_k  #ok
        self.calc_Lc(IF.initialInputs['B']['value'], roundingPrecision, index) #need lambda, lambda_k       #ok

        self.calc_h(IF.initialInputs['B']['value'], roundingPrecision, index) #need lambda_k, trim    #ok
        
        #resistance to air
        self.calc_Zprim(IF.initialInputs['Z']['value'], IF.initialInputs['LOA']['value'], roundingPrecision, index)      #need trim, h first        #ok
        self.calc_A_romp(IF.initialInputs['Bmax']['value'], roundingPrecision, index) #need Zprim    #ok
        self.calc_A_voorkant(roundingPrecision, index) #need A_romp         #ok
        self.calc_D_air(IF.initialInputs['V']['SI'], roundingPrecision, index) #need A_voorkant         #ok
        self.calc_f_air(IF.initialInputs['LCG']['value'], IF.initialInputs['VCG']['value'], roundingPrecision, index) #need Zprim, h, trim          #ok
        self.calc_M_air(roundingPrecision, index) #need D_air, f_air        #ok
        
        #total resistance
        self.calc_Fh(IF.initialInputs['propellersNumber']['value'], roundingPrecision, index)    #need D_romp, D_F, ***D_air***, shaft_D, strut_D, rudder_D, trim_eD, shaft_N           #ok
        self.calc_Fv(IF.initialInputs['propellersNumber']['value'], IF.initialInputs['DELTA']['value'], roundingPrecision, index) #need trimTabs_DELTA, shaft_D, strut_D, rudder_D, trim_eD, shaft_N         #ok
        self.calc_T(IF.initialInputs['e']['value'], roundingPrecision, index) #need Fh, trim_eD             #ok
        self.calc_Nt(IF.initialInputs['e']['value'], roundingPrecision, index) #need Fh, Fv, trim_eD        #ok
        
        
        
        self.calc_lt(IF.initialInputs['B']['value'], roundingPrecision, index) #need Lk, Lc    #ok
        self.calc_DELTA_s(IF.initialInputs['B']['value'], roundingPrecision, index) #need Lk, Lc, lambda, trim          #ok
        self.calc_KB(IF.initialInputs['B']['value'], roundingPrecision, index) #need Lk, Lc, beta_e     #ok
        self.calc_BG(IF.initialInputs['VCG']['value'], roundingPrecision, index) #need KB       #ok
        self.calc_a_one_s(roundingPrecision, index) #need BG, DELTA_s       #ok
        
        #calc_CL_beta_d2 ?????
        
        self.calc_drukpt(IF.initialInputs['B']['value'], roundingPrecision, index) #need beta_e     #ok
        self.calc_arm(IF.initialInputs['VCG']['value'], roundingPrecision, index) #need drukpt, beta_e      #ok
        
        
        
        
        self.calc_M(IF.initialInputs['propellersNumber']['value'], IF.initialInputs['f']['value'], roundingPrecision, index)  #need Nt, c, trimTabs_M, shaft_M, strut_M, rudder_M, Df, a, T, M_air    #ok
        #print('M : ' + str(self.dictionary['M']['value']))
        

    ##other functions

       
    def initArray(self):
        return [None]*size
        
    def initAll(self):
        for key in dict:
            self.dictionary[key]['value']=self.initArray()
        #for i in range (0, len(self.dictionary['trim']['value'])):
        #    self.dictionary['trim']['value'][i] = 0.0001

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
    
    calcul = Computation(len(IF.initialInputs['V']['value1']))
    initAll(calcul.dictionary, calcul.size)
    
    IF.initSpeed(IF.initialInputs['V'])                 # add a calc_V ??
    
    showParam(IF.initialInputs, 'V', 'value1')
    showParam(IF.initialInputs, 'V', 'SI')
    
    '''
    calcul.calc_trim()
    
    calcul.calc_Cv(IF.initialInputs['V']['SI'], IF.initialInputs['B']['value'])
    calcul.calc_CLb(IF.initialInputs['V']['SI'], IF.initialInputs['B']['value'], IF.initialInputs['DELTA']['value'])
    '''
    
    
    #calcul.calc_Cv(IF.initialInputs['V']['SI'], IF.initialInputs['B']['value'], 2.0)
    calcul.calc_trim()
    
    #roundAll(calcul.dictionary, 5)
    #showAll(calcul.dictionary)
            
            
