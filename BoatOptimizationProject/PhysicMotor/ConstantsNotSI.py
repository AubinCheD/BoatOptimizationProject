import copy
import math as math

  ##                   FAIRE : DEUX DICO DE CONSTANTES, UN SI, LAUTRE NON ET METTRE LES MEMES NOMS DE CLE

constants = {    # 'key' : [value:float, unitType: string, unit: string]

    'pi':   {'value': 3.1415, 'unitType': None,           'unit': None,              'name': '\u03C0'},                                        #pi
    'g_SI': {'value': 32.174,  'unitType': 'Acceleration', 'unit': 'm.s\u207B\u00B2', 'name': 'g'},                      #gravity   
    
    'gammaWater_SI': {'value': 1.025, 'unitType': None, 'unit': None, 'name': '\03B3 Water'},
     
    'rhoWater_SI':   {'value': 1.9888109342,    'unitType': 'Density',          'unit': 'kg.m\u207B\u00B3',         'name': '\03F1 Water'},      #density of water
    'rhogWater_SI':  {'value': 63.9880029966, 'unitType': 'SpecificWeight',   'unit': 'N.m\u207B\u00B3',          'name': '\03F1g Water'},     #specific weight of water
    'muWater_SI':    {'value': 0.000012615,    'unitType': 'KinematicViscosity', 'unit': 'm\u00B2.s\u207B\u009B',    'name': '\03BD'},            #viscosity of water at 25°C
    'rhoAir_SI':     {'value': 0.0023769,    'unitType': 'Density',          'unit': 'slug.ft\u207B\u00B3',         'name': '\03F1 Air'}, #density of air at 30°C
    'rhogAir_SI':    {'value': 0.0764743806,    'unitType': 'SpecificWeight',   'unit': 'lbf.ft\u207B\u00B3',          'name': '\03F1g Air'}        #specific weight of air at 30°C
} 


dico = {
    'V': {'unitType': 'Speed', 'unit1': 'knot', 'value1': [7,8,10,15,20,25,30,35,40,45,50,55,60,65,70], 'unit2': 'km/h', 'SI': [], 'name': 'V'},


    #hull
    'LWL':      {'value': 0.0 , 'unitType': 'Distance', 'unit': '', 'variationType': None, 'variation': 0.0, 'usedInGA': True, 'name': 'LWL'},
    'B':        {'value': 0.0 , 'unitType': 'Distance', 'unit': '', 'variationType': None, 'variation': 0.0, 'usedInGA': True, 'name': 'B'}
}


#dico2 = dico
"""
dico2 = copy.deepcopy(dico)


V=[10 for i in range(0,10)]
B=5
g=10


f = lambda x : x+2
g = map(f, V)

f
print(V)
V=list(g)
print(V)
"""
#calcul = {'Cv': {'value': [0 for i in range(0,10)], 'Function': lambda V, B, g : for i in range (0,len(V)): v[i]*math.sqrt(B*g) } }