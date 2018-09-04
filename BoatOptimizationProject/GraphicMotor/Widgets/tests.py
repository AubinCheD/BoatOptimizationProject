import tkinter as tk
import EntryBoxNumber as EBN
import tests2 as ET

class VariationFluctuationInterval(tk.Frame):
    
    def __init__(self, root):
        
        super().__init__(root)
        
        self.labelMin = tk.Label(self, text="Min :")
        self.labelMax = tk.Label(self, text="Max :")
        
        #self.entryVariationMin = EBN.EntryBoxNumber(self)
        self.entry = tk.Entry(self)
        self.entryTest = ET.EntryTest(self)

    def grid2(self):
        self.labelMin.grid(row=0,column=0)
        
        #self.entryVariationMin.grid(row=0,column=1)
        #self.entry.grid(row=0,column=1)
        self.entryTest.grid(row=0,column=1)
        
        self.labelMax.grid(row=0,column=2)


if (__name__ == '__main__'):

    window = tk.Tk()
    unitCombo = VariationFluctuationInterval(window)
    
    unitCombo.grid2()    
    unitCombo.grid(row=0,column=0)
    
    window.mainloop()
    window.quit()