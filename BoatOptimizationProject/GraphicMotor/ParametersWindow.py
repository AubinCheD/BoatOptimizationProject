import sys
sys.path.insert(0, './Widgets')

import tkinter as tk
import tkinter.messagebox as tk_mb
import tkinter.ttk as tk_ttk

import Widgets.ParameterInitializer as PI

import InitFileNotSI2_temp as IF

#sys.path.insert(0, '../')

import PhysicMotor.Units as Units

#tableau à double entrée / test avec grilles
class ParametersWindow (tk.Frame):
    
    def __init__(self, root):

        super().__init__(root)
        
        self.paramWidgets = [] 
        
        i=0
        j=0
        # for key in IF.initialInputs.keys():
        #     if (IF.initialInputs[key]['name'] != 'V'):
        #         
        #         #print("temp : {}, i : {}, j : {}, k : {}".format(k+int(i/15), i, j, k))
        #         # if ((j+int(i/16))>j):
        #         #     j = j+1
        #         #     i=0
        #         print("i : {}, j : {}".format( i, j))
        #         self.paramWidgets.append(PI.ParameterInitializer(self, key, IF.initialInputs[key], i, 0))
        #         self.paramWidgets[i].grid(row = i, column=j)
                    # i += 1
        
        nbKeys = len(list(IF.initialInputs.keys()))
        print(nbKeys)
        
        self.labelName = tk.Label(self, text = 'Parameter:', width = 0)
        self.labelValue = tk.Label(self, text = 'Value:', width = 0)
        self.labelUnit = tk.Label(self, text = 'Unit:', width = 0)
        self.labelUsedInGA = tk.Label(self, text = 'UsedInGA:', width = 0)
        self.labelVariation = tk.Label(self, text = 'Variation:', width = 0)
        
        # self.labelName.grid(row = 0, column=0)
        # self.labelValue.grid(row = 0, column=1)
        # self.labelUnit.grid(row = 0, column=2)
        # self.labelUsedInGA.grid(row = 0, column=3)
        # self.labelVariation.grid(row = 0, column=4)
        
        for key in IF.initialInputs.keys():
            if (IF.initialInputs[key]['name'] != 'V'):
                
                #print("temp : {}, i : {}, j : {}, k : {}".format(k+int(i/15), i, j, k))
                # if ((j+int(i/16))>j):
                #     j = j+1
                #     i=0
                # if (i>=nbKeys/2):
                #     i = 0
                #     j = 1
                print("i : {}, j : {}".format( i, j))
                self.paramWidgets.append(PI.ParameterInitializer(self, key, IF.initialInputs[key], i, j))
                self.paramWidgets[i].grid(row = i+1, column=1)
                #i = i + 1
                
        
        
        
        """
        self.paramWidgets.append(PI.ParameterInitializer(self, 'LWL', IF.initialInputs['LWL']))
        self.paramWidgets[i].grid(row = 1, column=0)
        """
        
        #si l'unité selectionnée n'est pas l'unité SI, faire la conversion
        
        
        self.buttonValidation = tk.Button(self, text='Validate')     #might need to put the button in another window
        self.buttonValidation.bind('<Button-1>', (lambda event: self.validateParameters()))
        #   self.buttonValidation.grid(row = 1+16, column = 5*j+1)
        
    def validateParameters(self):
        for w in self.paramWidgets:
            #for param in IF.initialInputs.values():
            for key in IF.initialInputs.keys():
                #print(w.label['text'])
                #if (param['name']==w.label['text'][:-3]):    # on enlève le " : " de la fin du label
                if (key == w.key):
                    pass
                    #print(IF.initialInputs[key]['name'])
                    #print(IF.initialInputs[key])
                    #IF.initialInputs[key][value] = w.
                    
    
    

if (__name__ == '__main__'):
    
    window = tk.Tk()
    
    params = ParametersWindow(window)

    params.grid()
    
    window.mainloop()
    window.quit()