import math as math

class Units ():         #Classe comportant toutes les unités et les fonctions de conversion
        
    #docstring
    """(docstring) Classe Inputs"""

    
    def __init__ (self):
        
        #format    'key' : [value(float), variation pourcentage(int ou float), used in GA or not(boolean), "name printed on the GUI"]
        
        self.dictionary = {    # 'key' : {list of units names}
                              
            'Distance' : ['m', 'ft'],
            'Speed' :    ['m/s', 'ft/s', 'km/h', 'mph', 'knot'],
            'Acceleration' : ['m.s\u207B\u00B2'],
            'Angle' : ['\u00B0', 'rad'],
            'Density' : ['kg.m\u207B\u00B3', 'slug.ft\u207B\u00B3', 'lb.ft\u207B\u00B3'],
            'SpecificWeight' : ['N.m\u207B\u00B3', 'lbf.ft\u207B\u00B3'],
            'KinematicViscosity' : ['m\u00B2/s', 'ft\u00B2/s'],
            'Mass' : ['kg', 'slug', 'lb'],
            'Area' : ['m\u00B2', 'ft\u00B2'],
            'Volume' : ['m\u00B3', 'ft\u00B3'],
            'Force' : ['N', 'lbf'],   # kN ?
            'Power' : ['hp', 'kW']   # + 'ehp', 'ekW' ?
        }



units = {    # 'key' : {list of units names}
                    
    'Distance' : ['m', 'ft'],
    'Speed' :    ['m/s', 'ft/s', 'km/h', 'mph', 'knot'],
    'Acceleration' : ['m.s\u207B\u00B2'],
    'Angle' : ['\u00B0', 'rad'],
    'Density' : ['kg.m\u207B\u00B3', 'slug.ft\u207B\u00B3', 'lb.ft\u207B\u00B3'],
    'SpecificWeight' : ['N.m\u207B\u00B3', 'lbf.ft\u207B\u00B3'],
    'KinematicViscosity' : ['m\u00B2/s', 'ft\u00B2/s'],
    'Mass' : ['kg', 'slug', 'lb'],
    'Area' : ['m\u00B2', 'ft\u00B2'],
    'Volume' : ['m\u00B3', 'ft\u00B3'],
    'Force' : ['N', 'lbf'],   # kN ?
    'Power' : ['hp', 'kW']   # + 'ehp', 'ekW' ?
}


def distanceConversion(value, unitFrom, unitTo,  roundingPrecision=4):             #faire pareil partout
    if(unitFrom=='m'):
        if(unitTo=='ft'):
            return round(3.2808*value,  roundingPrecision)
    if(unitFrom=='ft'):
        if(unitTo=='m'):
            return round(0.3048*value,  roundingPrecision)
    else:
        return value
                
def speedConversion(value, unitFrom, unitTo,  roundingPrecision=4):
    if(unitFrom=='m/s'):
        if(unitTo=='ft/s'):
            return round(3.28084*value,  roundingPrecision)
        if(unitTo=='km/h'):
            return round(3.6*value,  roundingPrecision)
        if(unitTo=='mph'):
            return round(2.23694*value,  roundingPrecision)
        if(unitTo=='knot'):
            return round(1.94384*value,  roundingPrecision)
    if(unitFrom=='ft/s'):
        if(unitTo=='m/s'):
            return round(0.3048*value,  roundingPrecision)
        if(unitTo=='km/h'):
            return round(1.09728*value,  roundingPrecision)
        if(unitTo=='mph'):
            return round(0.681818*value,  roundingPrecision)
        if(unitTo=='knot'):
            return round(0.592484*value,  roundingPrecision)
    if(unitFrom=='km/h'):
        if(unitTo=='m/s'):
            return round(0.277778*value,  roundingPrecision)
        if(unitTo=='ft/s'):
            return round(0.911344*value,  roundingPrecision)
        if(unitTo=='mph'):
            return round(0.621371*value,  roundingPrecision)
        if(unitTo=='knot'):
            return round(0.539957*value,  roundingPrecision)
    if(unitFrom=='mph'):
        if(unitTo=='m/s'):
            return round(0.44704*value,  roundingPrecision)
        if(unitTo=='ft/s'):
            return round(1.46667*value,  roundingPrecision)
        if(unitTo=='km/h'):
            return round(1.60934*value,  roundingPrecision)
        if(unitTo=='knot'):
            return round(0.868976*value,  roundingPrecision)
    if(unitFrom=='knot'):
        if(unitTo=='m/s'):
            return round(0.514444*value,  roundingPrecision)
        if(unitTo=='ft/s'):
            return round(1.688*value,  roundingPrecision)   #1.68781
        if(unitTo=='km/h'):
            return round(1.852*value,  roundingPrecision)
        if(unitTo=='mph'):
            return round(1.15078*value,  roundingPrecision)
    else:
        return value


def accelerationConversion(value, unitFrom, unitTo,  roundingPrecision=4):
    pass

def angleConversion(value, unitFrom, unitTo,  roundingPrecision=10):
    if(unitFrom=='\u00B0'):
        if(unitTo=='rad'):
            #print(3.1415/180*value)
            return round(math.pi/180*value,  roundingPrecision)
    if(unitFrom=='rad'):
        if(unitTo=='\u00B0'):
            return round(180/math.pi*value,  roundingPrecision)
    else:                                                                   #mettre un pass ou un message
        return value


def densityConversion(value, unitFrom, unitTo,  roundingPrecision=4):
    if(unitFrom=='kg.m\u207B\u00B3'):
        if(unitTo=='slug.ft\u207B\u00B3'):
            return round(0.00194032*value,  roundingPrecision)
        if(unitTo=='lb.ft\u207B\u00B3'):
            return round(0.062428*value,  roundingPrecision)
    if(unitFrom=='slug.ft\u207B\u00B3'):
        if(unitTo=='kg.m\u207B\u00B3'):
            return round(515.379*value,  roundingPrecision)
        if(unitTo=='lb.ft\u207B\u00B3'):
            return round(32.174*value,  roundingPrecision)
    if(unitFrom=='lb.ft\u207B\u00B3'):
        if(unitTo=='kg.m\u207B\u00B3'):
            return round(16.0185*value,  roundingPrecision)
        if(unitTo=='slug.ft\u207B\u00B3'):
            return round(0.031081*value,  roundingPrecision)
    else:
        return value


def specificWeightConversion(value, unitFrom, unitTo,  roundingPrecision=4):
    if(unitFrom=='N.m\u207B\u00B3'):
        if(unitTo=='lbf.ft\u207B\u00B3'):
            return round(0.224809*value,  roundingPrecision)
    if(unitFrom=='lbf.ft\u207B\u00B3'):
        if(unitTo=='N.m\u207B\u00B3'):
            return round(4.448222*value,  roundingPrecision)
    else:
        return value


def kinematicViscosityConversion(value, unitFrom, unitTo,  roundingPrecision=4):
    if(unitFrom=='m\u00B2/s'):
        if(unitTo=='ft\u00B2/s'):
            return round(10.7639104*value,  roundingPrecision)
    if(unitFrom=='ft\u00B2/s'):
        if(unitTo=='m\u00B2/s'):
            return round(0.09290304*value,  roundingPrecision)
    else:
        return value
 
            
def massConversion(value, unitFrom, unitTo,  roundingPrecision=4):
    if(unitFrom=='kg'):
        if(unitTo=='slug'):
            return round(0.0685218*value,  roundingPrecision)
        if(unitTo=='lb'):
            return round(2.20462*value,  roundingPrecision)
    if(unitFrom=='slug'):
        if(unitTo=='kg'):
            return round(14.5939*value,  roundingPrecision)
        if(unitTo=='lb'):
            return round(32.174*value,  roundingPrecision)
    if(unitFrom=='lb'):
        if(unitTo=='kg'):
            return round(0.453592*value,  roundingPrecision)
        if(unitTo=='slug'):
            return round(0.031081*value,  roundingPrecision)
    else:
        return value

            
def areaConversion(value, unitFrom, unitTo,  roundingPrecision=4):
    if(unitFrom=='m\u00B2'):
        if(unitTo=='ft\u00B2'):
            return round(10.7639104*value,  roundingPrecision)
    if(unitFrom=='ft\u00B2'):
        if(unitTo=='m\u00B2'):
            return round(0.09290304*value,  roundingPrecision)
    else:
        return value
         
            
def volumeConversion(value, unitFrom, unitTo,  roundingPrecision=4):
    if(unitFrom=='m\u00B3'):
        if(unitTo=='ft\u00B3'):
            return round(35.3147*value,  roundingPrecision)
    if(unitFrom=='ft\u00B3'):
        if(unitTo=='m\u00B3'):
            return round(0.0283168*value,  roundingPrecision)
    else:
        return value
  
            
def forceConversion(value, unitFrom, unitTo,  roundingPrecision=4):
    if(unitFrom=='N'):
        if(unitTo=='lbf'):
            return round(0.224809*value,  roundingPrecision)
    if(unitFrom=='lbf'):
        if(unitTo=='N'):
            return round(4.44822*value,  roundingPrecision)
    else:
        return value
 
            
def powerConversion(value, unitFrom, unitTo,  roundingPrecision=4):
    if(unitFrom =='hp'):
        if(unitTo=='kW'):
            return round(0.7457*value,  roundingPrecision)
    if(unitFrom =='kW'):
        if(unitTo =='hp'):
            return round(1.34102*value,  roundingPrecision)
    else:
        return value

            
            
def unitConversion(unitType, value, unitFrom, unitTo,  roundingPrecision=4):
    if (unitType == 'Distance'):
        return distanceConversion(value, unitFrom, unitTo) 
    if (unitType == 'Speed'):
        return speedConversion(value, unitFrom, unitTo) 
    if (unitType == 'Acceleration'):
        return accelerationConversion(value, unitFrom, unitTo) 
    if (unitType == 'Angle'):
        return angleConversion(value, unitFrom, unitTo) 
    if (unitType == 'Density'):
        return densityConversion(value, unitFrom, unitTo) 
    if (unitType == 'SpecificWeight'):
        return specificWeightConversion(value, unitFrom, unitTo) 
    if (unitType == 'KinematicViscosity'):
        return kinematicViscosityConversion(value, unitFrom, unitTo) 
    if (unitType == 'Mass'):
        return massConversion(value, unitFrom, unitTo) 
    if (unitType == 'Area'):
        return areaConversion(value, unitFrom, unitTo) 
    if (unitType == 'Volume'):
        return volumeConversion(value, unitFrom, unitTo)  
    if (unitType == 'Force'):
        return forceConversion(value, unitFrom, unitTo)   
    if (unitType == 'Power'):
        return powerConversion(value, unitFrom, unitTo)             