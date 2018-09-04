class Outputs ():
        
    #docstring
    """(docstring) Classe Outputs"""

    
    def __init__ (self):
        
        #format    'key' : [value(float), variation pourcentage(int ou float), used in GA or not(boolean), "name printed on the GUI"]
        
        self.dictionary = {    # 'key' : [value:float, unitType: string, unit: string, variationType, variation, displayedName: string, usedInGA: boolean]
                              #depending on variationType, variation is either a float or a tab [min: float, max: float, step: float]
                              #maybe don't need variationType and unitType
         
        
        #on pourrait créer un sous dictionnaire avec comme clés les noms des catégories pour une création automatique de l'interface, à essayer un jour
        
        #
            '':[]

            
        }    
       