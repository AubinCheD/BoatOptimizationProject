import tkinter as tk
import tkinter.ttk as tk_ttk

import EntryBoxNumber as EBN

class VariationFluctuationInterval(tk.Frame):        #ou une seule classe VariationInterval ?
    #docstring
    """(docstring) Classe """
    
    def __init__(self, root, variationType):     #unitType is a key of the class dictionary (unitDictionary)    #variationType = 'pourcentage' or 'minmax' or 0 and 1
        
        super().__init__(root)
        
        if (variationType == 0):
            self.entryVariationFluctuation = EBN.EntryBoxNumber(self)
            self.entryVariationFluctuation.grid(row=0,column=1)
        elif (variationType == 1):
            self.labelMin = tk.Label(self, text="Min :")
            self.labelMax = tk.Label(self, text="Max :")
            self.labelStep = tk.Label(self, text="Step :")

            self.entryVariationMin = EBN.EntryBoxNumber(self)
            self.entryVariationMax = EBN.EntryBoxNumber(self)
            self.entryVariationStep = EBN.EntryBoxNumber(self)

            
            self.labelMin.grid(row=0,column=0)
            self.entryVariationMin.grid(row=0,column=1)
            self.labelMax.grid(row=0,column=2)
            self.entryVariationMax.grid(row=0,column=3)
            self.labelStep.grid(row=0,column=4)
            self.entryVariationStep.grid(row=0,column=5)


if (__name__ == '__main__'):
     
     
    initialInputs = {
        'V': {'unitType': 'Speed', 'unit1': 'knot', 'value1': [25,30,35,40], 'unit2': 'ft/s', 'SI': [], 'name': 'V'}, 
        #hull
        'LWL':      {'value': 65 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 10.0, 'usedInGA': False, 'name': 'LWL'},
        'B':        {'value': 14 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 10.0, 'usedInGA': False, 'name': 'B'},
        'VCG':      {'value': 2.849548 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 20.0, 'usedInGA': True, 'name': 'VCG'},
        'LCG':      {'value': 29 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 20.0, 'usedInGA': True, 'name': 'LCG'}
    }
    #print ('X' + '\u207B'+ '\u00B2')
    
    window = tk.Tk()
    #frame = tk.Frame(window)
    
    unitCombo = VariationFluctuationInterval(window, 1)
    
    #unitCombo.grid2()
    unitCombo.grid()
    
    #unitCombo.grid(row=0,column=0)
    
    
    #unitCombo2 = VariationFluctuationInterval(window, 1)
    #unitCombo3 = VariationFluctuationInterval(frame, 1)
    
    
    
    #unitCombo2.grid()
    #unitCombo3.grid()
    #frame.grid()
    
    window.mainloop()
    window.quit()
    """
    window = Window()
    window.mainloop()
    window.quit()
    """