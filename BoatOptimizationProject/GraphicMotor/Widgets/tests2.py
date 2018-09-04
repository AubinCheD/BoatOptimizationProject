import tkinter as tk
        
class EntryTest (tk.Entry):          #PRENDRE UN INTERVALLE EN PARAM DE CE WIDGET ( min et max autorisés -> 2 attributs d'instance)
                                            # + une variable pour le nombre de chiffres après la virgule
                                            # ameliorer pour tenir compte des nombres négatifs ??
                                            # selectionner le texte lors d'un appui sur tab
    #docstring
    """(docstring) Classe Fenetre"""
    

    def __init__ (self, root, min=0.0, max=100., precision=3):
        self.min = min
        self.max = max
        self.precision = precision
    
        self.entryTkValue = tk.StringVar(value="0.0000")
                
        super().__init__(root, textvariable = self.entryTkValue, text = self.entryTkValue, validate='focus')


if (__name__ == '__main__'):

    #pass
    #print(tk.StringVar().configure())
    window = tk.Tk()  
    entry = EntryTest(window) 
    entry.grid()
    entry2 = EntryTest(window) 
    entry2.grid() 
    window.mainloop()
    window.quit()
