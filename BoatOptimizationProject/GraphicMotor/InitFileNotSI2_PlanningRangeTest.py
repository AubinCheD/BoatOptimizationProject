#https://fr.wikipedia.org/wiki/Table_des_caract%C3%A8res_Unicode_(0000-0FFF)
#https://www.technologyuk.net/physics/measurement-and-units/physical-quantities-and-si-units.shtml
#https://en.wikipedia.org/wiki/List_of_physical_quantities
#https://www.google.com.br/search?q=lbf%2Fft%5E3+to+N%2Fm%5E3&oq=lbf%2Fft%5E3+to+N%2Fm%5E3&aqs=chrome..69i57j6j69i58.17710j0j7&sourceid=chrome&ie=UTF-8
#https://www.google.com.br/search?q=lfb+to+lb&oq=lfb+to+lb&aqs=chrome..69i57j0l5.2815j0j7&sourceid=chrome&ie=UTF-8
#https://fr.wikipedia.org/wiki/Exposants_et_indices_Unicode
#https://fr.wikipedia.org/wiki/Table_des_caract%C3%A8res_Unicode_(2000-2FFF)
#https://www.engineeringtoolbox.com/water-dynamic-kinematic-viscosity-d_596.html


#conversions d'unités à faire au debut

import sys

sys.path.insert(0, '../')
import PhysicMotor.Units as Units


constants = {    # 'key' : [value:float, unitType: string, unit: string]

    'pi':   {'value': 3.1415, 'unitType': None,           'unit': None,              'name': '\u03C0'},                                        #pi
    'g_SI': {'value': 9.807,  'unitType': 'Acceleration', 'unit': 'm.s\u207B\u00B2', 'name': 'g'},                      #gravity   
    
    'gammaWater_SI': {'value': 1.025, 'unitType': None, 'unit': None, 'name': '\03B3 Water'},
     
    'rhoWater_SI':   {'value': 1025,    'unitType': 'Density',          'unit': 'kg.m\u207B\u00B3',         'name': '\03F1 Water'},      #density of water
    'rhogWater_SI':  {'value': 10051.7, 'unitType': 'SpecificWeight',   'unit': 'N.m\u207B\u00B3',          'name': '\03F1g Water'},     #specific weight of water
    'muWater_SI':    {'value': None,    'unitType': 'KinematicViscosity', 'unit': 'm\u00B2.s\u207B\u009B',    'name': '\03BD'},            #viscosity of water
    'rhoAir_SI':     {'value': None,    'unitType': 'Density',          'unit': 'kg.m\u207B\u00B3',         'name': '\03F1 Air'},        #density of air
    'rhogAir_SI':    {'value': None,    'unitType': 'SpecificWeight',   'unit': 'N.m\u207B\u00B3',          'name': '\03F1g Air'}        #specific weight of air
} 

"""
'rhoWater_SI' = {}     #density of water
'g_SI'= {}              #gravity
'rhogWater_SI' = {}           #specific weight of water
'muWater_SI' = {}             #viscosity of water
'pi' = {} 
'rhoAir_SI' = {}        #density of air
'rhogAir_SI' = {}       #specific weight of air
"""










initialInputs = {    # 'key' : [value:float, unitType: string, unit: string, variationType, variation, displayedName: string, usedInGA: boolean]
                        #depending on variationType, variation is either a float or a tab [min: float, max: float, step: float]
                        #maybe don't need variationType and unitType
    
                #mettre un pointeur de fonction pour la conversion d'unité ?
                
                #pas besoin de variationType / seul V changera  / du moins pour l'instant 
                
    #Speed Values   [25,30,32,34,36,38,40]
    'V': {'unitType': 'Speed', 'unit1': 'knot', 'value1': [25,30,35,40], 'unit2': 'ft/s', 'SI': [], 'name': 'V'},  # [ou faire un autre tableau intermédiaire ?]
    
    #'LCG': {'unitType': 'Distance', 'unit1': 'ft', 'value1': [], 'unit2': 'm', 'SI': [], 'name': 'LCG'},   pour l'instant constant, voir plus bas
    
    #hull
    'LWL':      {'value': 65 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 10.0, 'usedInGA': False, 'name': 'LWL'},
    'B':        {'value': 14 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 10.0, 'usedInGA': False, 'name': 'B'},
    'VCG':      {'value': 1.97 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 20.0, 'usedInGA': True, 'name': 'VCG'},
    'LCG':      {'value': 25.46 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 20.0, 'usedInGA': True, 'name': 'LCG'},
    'DELTA':    {'value': 60000 , 'unitType': 'Mass',    'unit': 'lb', 'variationType': None, 'variation': 10.0, 'usedInGA': False, 'name': '\u0394'},    ##CHECK UNIT
    'beta':     {'value': 8.07 , 'unitType': 'Angle',    'unit': '\u00B0', 'variationType': None, 'variation': 20.0, 'usedInGA': True, 'name': '\u03B2_transom'},
    'beta_x':   {'value': 11.53 , 'unitType': 'Angle',    'unit': '\u00B0', 'variationType': None, 'variation': 20.0, 'usedInGA': True, 'name': '\u03B2\u208E\u2080\u208D'},
    #'L_x': {'value': 0.0 , 'unitType': 'Distance', 'unit': '', 'variationType': None, 'variation': None, 'usedInGA': True, 'name': 'L\u208E\u2080\u208D'},    #not input
    #'theta': {'value': 0.0 , 'unitType': 'Angle', 'unit': '\u00B0', 'variationType': None, 'variation': 20.0, 'usedInGA': True, 'name': '\u03B8'},        #not input ?
    'e':        {'value': 4.59 , 'unitType': 'Angle',    'unit': '\u00B0', 'variationType': None, 'variation': 20.0, 'usedInGA': True, 'name': '\u03E8'},
    'f':        {'value': 0.5 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 10.0, 'usedInGA': False, 'name': 'f'},
          
    #'Vmin': {'value': 0.0 , 'unitType': 'Speed', 'unit': '', 'variationType': None, 'variation': None, 'usedInGA': True, 'name': 'B'},         #not input
    #'Vmax': {'value': 0.0 , 'unitType': 'Speed', 'unit': '', 'variationType': None, 'variation': None, 'usedInGA': True, 'name': 'B'},       #not input

    #S/str
    'LOA':  {'value': 70 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 10.0, 'usedInGA': False, 'name': 'LOA'},
    'Bmax': {'value': 14 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 10.0, 'usedInGA': False, 'name': 'Bmax'},
    'Z':    {'value': 3 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 10.0, 'usedInGA': False, 'name': 'Z'},
    'Hss':  {'value': 5 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 10.0, 'usedInGA': False, 'name': 'Hss'},
    'Bss':  {'value': 7 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 10.0, 'usedInGA': False, 'name': 'Bss'},
    #'Ass': {'value': 0.0 , 'unitType': 'Area', 'unit': '', 'variationType': None, 'variation': None, 'usedInGA': True, 'name': 'Ass'},       #not input

    #Propulsion System

    'propellersNumber': {'value': 2.0 , 'unitType': None, 'unit': '', 'variationType': None, 'variation': 10.0, 'usedInGA': False, 'name': 'NbPropellers'},
    
    #trim tabs
    'TrimTab_chord': {'value': 0.0 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 10.0, 'usedInGA': False, 'name': 'Chord'},
    'TrimTab_sigma': {'value': 0.0 , 'unitType': None,       'unit': '', 'variationType': None, 'variation': 10.0, 'usedInGA': False, 'name': '\u03C3'},
    'TrimTab_delta': {'value': 0.0 , 'unitType': 'Angle',    'unit': '\u00B0', 'variationType': None, 'variation': 10.0, 'usedInGA': False, 'name': '\u03B4'},
    #Rudder
    'Rudder_chord':     {'value': 0.0 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 10.0, 'usedInGA': False, 'name': 'Chord'},
    'Rudder_thickness': {'value': 0.0 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 10.0, 'usedInGA': False, 'name': 'Thickness'},
    'Rudder_area':      {'value': 0.0 , 'unitType': 'Area',     'unit': 'ft\u00B2', 'variationType': None, 'variation': 10.0, 'usedInGA': False, 'name': 'Area'},
    'Rudder_xc':        {'value': 0.0 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 10.0, 'usedInGA': False, 'name': 'Xc'},
    'Rudder_yc':        {'value': 0.0 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 10.0, 'usedInGA': False, 'name': 'Yc'},
    #Shaft
    'Shaft_diameter': {'value': 0.0 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 10.0, 'usedInGA': False, 'name': '\u03A6'},
    'Shaft_length':   {'value': 0.0 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 10.0, 'usedInGA': False, 'name': 'l'},
    'Shaft_xc':       {'value': 0.0 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 10.0, 'usedInGA': False, 'name': 'Xc'},
    'Shaft_yc':       {'value': 0.0 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 10.0, 'usedInGA': False, 'name': 'Yc'},
    #Strut
    'Strut_chord':      {'value': 0.0 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 10.0, 'usedInGA': False, 'name': 'Chord'},
    'Strut_thickness':  {'value': 0.0 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 10.0, 'usedInGA': False, 'name': 'Thickness'},
    'Strut_area':       {'value': 0.0 , 'unitType': 'Area',     'unit': 'ft\u00B2', 'variationType': None, 'variation': 10.0, 'usedInGA': False, 'name': 'Area'},
    'Strut_xc':         {'value': 0.0 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 10.0, 'usedInGA': False, 'name': 'Xc'},
    'Strut_yc':         {'value': 0.0 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 10.0, 'usedInGA': False, 'name': 'Yc'}
    
    
}



#fonction qui convertit tous les param, normalement fait au binding


"""
def findParamFromPrintedName(name):
    test = True
    
    while(test):
"""

def showDict(dict):
    for param in dict.values():
        print(param)

def initSpeed(param):                            #    à appeler dans une fonction d'init
    n = len(param['value1'])
    for i in range (0,n):
        param['SI'].append(round(Units.unitConversion(param['unitType'],param['value1'][i], param['unit1'], param['unit2']), 4))  #3 = precision

def initLCG(dico):                #not to use anymore
    n=len(dico['V']['value1'])
    for i in range (0,n):
        dico['LCG']['value1'].append(29)
    for i in range (0,n):
        dico['LCG']['SI'].append(round(Units.unitConversion(dico['LCG']['unitType'], dico['LCG']['value1'][i], dico['LCG']['unit1'], dico['LCG']['unit2']), 4))

def truncate(number, precision):    #to improve -> see https://stackoverflow.com/questions/783897/truncating-floats-in-python
    return round(number, precision)


if (__name__ == '__main__'):
    
    
    print(initialInputs['LCG'])
    initSpeed(initialInputs['V'])
    initLCG(initialInputs)
    print(initialInputs)
    
    
    '''
    print(initialInputs['LWL'])
    print(initialInputs['LWL']['unitType'])
    print(constants['pi']['value'])
    
    dict  =  initialInputs['LWL']
    print(dict['unitType'])
    
    #print(initialInputs.values())
    
    
            
    showDict(initialInputs)
    
    '''