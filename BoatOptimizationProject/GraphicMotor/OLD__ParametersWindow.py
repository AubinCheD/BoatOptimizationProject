import tkinter as tk
import tkinter.messagebox as tk_mb
import tkinter.ttk as tk_ttk

class Window(tk.Tk):
    #docstring
    """(docstring) Classe Fenetre"""
    
    def __init__(self):
        tk.Tk.__init__(self)	# On dérive de Tk, on reprend sa méthode d'instanciation
        
        self.param = ParameterPanedWindow(self, tk.HORIZONTAL)
        self.param.pack()
        
    def initCombobox(self, root, varType, listOfAttributes, visibilityState):
        
        return tk_ttk.Combobox(root, textvariable = varType, values = listOfAttributes, state = visibilityState)
        

#tableau à double entrée / test avec grilles
class ParameterPanedWindow (tk.PanedWindow):  # WARNING ! USE PanedWindow from tkinter, not tkinter.ttk
    
    def __init__(self, root, orientation):  #ou donner en paramètre des coord de grille

        super().__init__(orient=orientation)
        #self.configure(orient=tk.HORIZONTAL)
        
        #super.__self__.
        #tk_ttk.Panedwindow.configure(self, None, orient=tk.VERTICAL)
        
        #tk_ttk.Panedwindow.config(self, None, orient=tk.VERTICAL)
        
        self.paramValue = tk.StringVar()
        self.paramVariation = tk.StringVar()
        self.paramUsed = tk.IntVar()
        
        self.label = tk_ttk.Label(self, text = "ParamName : ")
        self.entryParamValue = tk_ttk.Entry(self, textvariable = self.paramValue)
        self.checkButton = tk.Checkbutton(self, text=" Used ?",variable = self.paramUsed, command = self.isSelectedCheckButton)
        self.checkButton.select()
        self.entryParamVariation = tk_ttk.Entry(self, textvariable = self.paramVariation)
        
        #self.checkButton.bind('<<Enter>>', self.isSelectedCheckButton)
        
        
        self.add(self.label)
        self.add(self.entryParamValue)
        self.add(self.checkButton)
        self.add(self.entryParamVariation)
        
        #self.pack()
        
        
        #faire les binding ?
        
        #format des entry box
            
    def isSelectedCheckButton(self):
        if (self.paramUsed.get()):
            self.entryParamVariation.configure(state=tk.HIDDEN)
            print("on")
            print(self.paramUsed.get())
        else:
            self.entryParamVariation.configure(state=tk.DISABLED)
            print("off")
            print(self.paramUsed.get())
    
        
 

if (__name__ == '__main__'):
    

    
    pane = tk_ttk.Panedwindow
    #pane = tk_ttk.Panedwindow()
    #print(pane.configure())
    
    window = Window()
    

    checkButton = tk.Checkbutton(window, text='oih')
    print(checkButton.bind())
    entry = tk.Entry(window, text='oih')
    print(checkButton.bind())
    
    window.mainloop()
    window.quit()