#https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html

import tkinter as tk
import tkinter.ttk as tk_ttk

import sys
sys.path.insert(0, '../')

import InitFileNotSI2_PlanningRange as IF

sys.path.insert(0, '../../')
sys.path.insert(0, '../../PhysicMotor')
import Units as Units
import PhysicMotor.Units as Units
#import PhysicMotor.Units as Units

class UnitSelection(tk_ttk.Combobox):          #ajouter la selection auto d'une unité en paramètre, autrement qu'avec self.current(0)
    #docstring
    """(docstring) Classe UnitSelection"""
    
    #unitDictionary = {'distance':['m', 'ft'], 'speed':['m/s', 'km/h', 'mph', 'ft/s'], 'acceleration':['m.s\u207B\u00B2'], 'power':['hp', 'kW']}    #à compléter
    
    def __init__(self, root, unitList, param, key, changeFunction=None):      #unitList is the list of units associated to a unitType of the units dictionnary (Units.py)          
                                             #unitType is a key of the Units file dictionary 
        self.unitSelected = tk.StringVar()
        
        super().__init__(root)
        self.configure(textvariable = self.unitSelected, values = unitList, state = 'readonly', width = 7, justify='center')
        self.current(self.getUnitIndexOfParam(param))
        
        self.bind("<<ComboboxSelected>>", lambda event : changeFunction(param))

    def unitChange(self, param):
        param['unit'] = self.unitSelected.get()
        
    def getUnitIndexOfParam(self, param):
        i=0
        test = True
        n=len(Units.units[param['unitType']])
        while(test and i<n):
            if(Units.units[param['unitType']][i] == param['unit']):
                test = False
            else:
                i+=1
        return i

if (__name__ == '__main__'):
     
    #print ('X' + '\u207B'+ '\u00B2')
    
    
    window = tk.Tk()
    unitCombo = UnitSelection(window, ['kg.m\u207B\u00B3', 'slug.ft\u207B\u00B3', 'lb.ft\u207B\u00B3'], IF.initialInputs['LWL'], 'unit')
    unitCombo.pack()
    
    window.mainloop()
    window.quit()
    """
    window = Window()
    window.mainloop()
    window.quit()
    """