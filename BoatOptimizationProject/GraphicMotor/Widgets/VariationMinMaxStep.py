import tkinter as tk
import tkinter.ttk as tk_ttk

import EntryBoxNumber as EBN

class UnitSelection(tk_ttk.Combobox):
    #docstring
    """(docstring) Classe UnitSelection"""
    
    unitDictionary = {'distance':['m', 'ft'], 'speed':['m/s', 'ft/s', 'km/h', 'mph', 'knot'], 'acceleration':['m.s' + '\u207B' + '\u00B2'], 'power':['hp', 'kW']}    #à compléter
    
    def __init__(self, root, unitType):     #unitType is a key of the class dictionary (unitDictionary)
        self.unitSelected = tk.StringVar()
        
        super().__init__(root)
        self.configure(textvariable = self.unitSelected, values = UnitSelection.unitDictionary[unitType], state = 'readonly')


if (__name__ == '__main__'):
     
    #print ('X' + '\u207B'+ '\u00B2')
    
    window = tk.Tk()
    unitCombo = UnitSelection(window, 'speed')
    unitCombo.pack()
    
    window.mainloop()
    window.quit()
    """
    window = Window()
    window.mainloop()
    window.quit()
    """