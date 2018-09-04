#!/usr/bin/env python3

import tkinter as tk
import tkinter.ttk as tk_ttk



import sys

sys.path.insert(0, './')
import UnitSelection as US
import EntryBoxNumber as EBN

sys.path.insert(0, '../')
import InitFile as IF

sys.path.insert(0, '../../')
import PhysicMotor.Units as Units


class ParameterInitializer (tk.Frame):
    
    def __init__(self, root, key, param, row, column):        #param is a key of the initialInput dictionary in the initFile.py (in the physical motor)
    
                                            #ou donner en paramètre des coord de grille       # ajouter min=0.0, max=100., precision=3  (*2 : one triplet for each entry)   
    
                                                                                 # NO -> better to do a class parameter containing this informations and create a tab/dictionnary of                         
                                                                                 # parameters in the main 
        super().__init__(root)
        
        self.key = key
        self.row = row
        self.column = column
        
        #self.paramValue = tk.StringVar()
        #self.paramVariation = tk.StringVar()
        self.paramUsed = tk.IntVar()

        self.label = tk.Label(self, text = param['name'] + ' : ', width = 14)        
        self.entryParamValue = EBN.EntryBoxNumber(self, param, 'value')                 #rajouter les min/max/precision #passer en paramètre la fonction de validation à la place

        if (param['unitType']!=None):    
            self.unit = US.UnitSelection(self, Units.units[param['unitType']], param, 'unit', self.unitChange)
            
            self.unit.grid(row=self.row,column=2) #self.column*5+2
        else:
            tk.Label(self, text='', width=8).grid(row=self.row,column=2)   #self.column*5+2  #modif ??
            
        
        
        self.checkButton = tk.Checkbutton(self, text=" Used ?",variable = self.paramUsed, command = self.isSelectedCheckButton)  #enlever le texte et le mettre sur la grille
        self.checkButton.select()
        self.entryParamVariation = EBN.EntryBoxNumber(self, param, 'variation')            #rajouter les min/max/var      #passer en paramètre la fonction de validation à la place
        
        self.label.grid(row=self.row,column=0) #self.column*5
        self.entryParamValue.grid(row=self.row,column=1)  #self.column*5+1
        
        self.checkButton.grid(row=self.row,column=3)  #self.column*5+3
        self.entryParamVariation.grid(row=self.row,column=4)  #self.column*5+4
        
        
        """
        self.label.pack(side = tk.LEFT)
        self.entryParamValue.pack(side = tk.LEFT)
        self.checkButton.pack(side = tk.LEFT)
        self.entryParamVariation.pack(side = tk.LEFT)
        """
        #self.grid()   -> useless
    
    #def saveEntry(self, keySecondary):
    
    def unitChange(self, param):
        
        unitTemp = param['unit']
        param['unit'] = self.unit.unitSelected.get()
        print(str(param['value']) + '   ' + param['unit'] + '   ' + Units.units[param['unitType']][0])
        param['value'] = Units.unitConversion(param['unitType'], param['value'], unitTemp, param['unit'])
        print(param['value'])
        
        
    def isSelectedCheckButton(self):
        if (self.paramUsed.get()):
            self.entryParamVariation.configure(state=tk.NORMAL)    #activating the checkButton
            IF.initialInputs[self.key]['usedInGA']=True
            #print(self.paramUsed.get())
        else:
            self.entryParamVariation.configure(state=tk.DISABLED)  #disabling the checkButton
            IF.initialInputs[self.key]['usedInGA']=False
            #print(self.paramUsed.get())
    
        
 

if (__name__ == '__main__'):
    
    initialInputs = {
        'V': {'unitType': 'Speed', 'unit1': 'knot', 'value1': [25,30,35,40], 'unit2': 'ft/s', 'SI': [], 'name': 'V'}, 
        #hull
        'LWL':      {'value': 65 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 10.0, 'usedInGA': False, 'name': 'LWL'},
        'B':        {'value': 14 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 10.0, 'usedInGA': False, 'name': 'B'},
        'VCG':      {'value': 2.849548 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 20.0, 'usedInGA': True, 'name': 'VCG'},
        'LCG':      {'value': 29 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 20.0, 'usedInGA': True, 'name': 'LCG'}
    }
    
    window = tk.Tk()
    param = ParameterInitializer(window, )
    param.pack()
    param.grid()
    window.mainloop()
    window.quit()