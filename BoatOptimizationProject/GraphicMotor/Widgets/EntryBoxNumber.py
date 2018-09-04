import tkinter as tk
        
                                            #pouvoir insérer un caractère en milieu de string : ex 1.1515 -> 1.15315 sans avoir à supprimer tout
                                            #pouvoir se déplacer avec les flèches dans la string

        
class EntryBoxNumber (tk.Entry):          #PRENDRE UN INTERVALLE EN PARAM DE CE WIDGET ( min et max autorisés -> 2 attributs d'instance)
                                            # + une variable pour le nombre de chiffres après la virgule
                                            # ameliorer pour tenir compte des nombres négatifs ??
                                            # selectionner le texte lors d'un appui sur tab
    #docstring
    """(docstring) Classe Fenetre"""
    

    def __init__ (self, root, param, key, size=7 ,min=0.0, max=100., precision=3, type=None):  #precision = nb digits after comma
                                                                #type : "float" or "string", if string no need for validation
                                                                
                                                                
                                                                
                                                                #faire en sorte que si min ou max spécifié sans l'autre, alors pas de limite haute ou basse
        self.min = min
        self.max = max
        self.precision = precision
            
        if (type == None or type != 'string'):
            self.type = "float"
        #self.root = window
        
        self.entryRealValue = self.initEntryValue(param, key)
        self.entryTkValue = self.entryRealValue
        param[key] = float(self.entryRealValue.get())
                
        super().__init__(root, textvariable = self.entryTkValue, text = self.entryTkValue, validate='focus', width = size, justify='right')  #, padx=(0,1)
        cmd = self.register(lambda : self.entryFloatValidation(param, key))
        self.configure(validatecommand=cmd)
        
                                                        #when enter button pressed and entry is beeing focused
        
        #self.config(command=self.entryFloatValidation)
        #self.bind('<Return>',self.entryFloatValidation())
        self.bind("<Return>", (lambda event: self.entryFloatValidation(param, key)))
        self.bind("<KP_Enter>", (lambda event: self.entryFloatValidation(param, key)))
        self.bind("Tab", (lambda event : self.selectionOnTab(param, key)))                 #change the function ?
        #self.bind("<Key>", (lambda event : self.entryFloatValidation(param, key)))             #si activé problème cités lignes 3/4

    
    def getText(self):
        return self.entryRealValue
    
    def initEntryValue(self, param, key):
        if (param[key]!=''):
            initVal = param[key]
        else:
            initVal = "0"
            if (self.precision > 0):
                initVal += "."
                for i in range(0,self.precision):
                    initVal += "0"
        return tk.StringVar(value=initVal)
    
 
    def entryFloatValidation(self, param, key):                 #améliorer pour les cas "50" -> "50.0000"
        
        """
        Cas : - pas de "." dans la chaine, si c'est que des entiers c'est bon
               - caractères non autorisés
               - plus d'un point
               - chaine correcte mais valeur en dehors de l'intervalle de valeur
               - s'il rentre "," instead of '.', change it
        
        """

        tempString = self.entryTkValue.get()
        n = len(tempString)
        nbPoints = 0
        res = True
        i=0
            
        while (i<n):
            if (tempString[i] < '0' or tempString[i] > '9'):
                if (tempString[i] == ',' or tempString[i] == ';'):
                    tempString = tempString[0:i] + '.' + tempString[i+1:]

                if (tempString[i] == '.'):
                    nbPoints += 1
                    if (nbPoints > 1):
                        res = False
                else:
                    res = False
            i += 1
        
        if (res):                 #correct string, checking if min<value<max
            res = self.checkString(tempString)
            if (res and (float(tempString) < self.min or float(tempString) > self.max)):
                res = False
        
        if (res):                #string correct
            i=0
            test = True
            while(test):
                n = len(tempString)
                if (i<(n-1) and tempString[i]=='0' and tempString[i+1]=='0'):
                    tempString = tempString[1:]
                else:
                    test=False            

            #self.entryRealValue.set(tempString)
            self.entryRealValue = tempString
            self.delete(0,tk.END)
            self.insert(0,tempString)
            #print(self.entryRealValue.get())
            
            #param[key]=float(self.entryRealValue.get())
            param[key]=float(self.entryRealValue)
        else:
            self.delete(0,tk.END)
            self.insert(0,self.entryRealValue)
            #print(self.entryRealValue.get())
            #param[key]=float(self.entryRealValue.get())
        
        
        print(param)
        
        return res
     
     
    def selectionOnTab(self):               #need to change tab behaviour instead or when focus changed
        #n = len(self.entryRealValue)
        self.entryFloatValidation.select_range(0,tk.END)            
    
    def onEnterKey(event=None):             #useless
        self.EntryFloatValidation()            

    def checkString(self, string):
        n = len(string)
        res = True
        if (string == ''):
            res = False
        else:
            for i in range(0,n):
                if (string[i] not in ',;.0123456789'):
                    res = False
        return res



if (__name__ == '__main__'):


    initialInputs = {
        'V': {'unitType': 'Speed', 'unit1': 'knot', 'value1': [25,30,35,40], 'unit2': 'ft/s', 'SI': [], 'name': 'V'}, 
        #hull
        'LWL':      {'value': 65 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 10.0, 'usedInGA': False, 'name': 'LWL'},
        'B':        {'value': 14 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 10.0, 'usedInGA': False, 'name': 'B'},
        'VCG':      {'value': 2.849548 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 20.0, 'usedInGA': True, 'name': 'VCG'},
        'LCG':      {'value': 29 , 'unitType': 'Distance', 'unit': 'ft', 'variationType': None, 'variation': 20.0, 'usedInGA': True, 'name': 'LCG'}
    }

    #pass
    #print(tk.StringVar().configure())
    
    window = tk.Tk()  
    entry = EntryBoxNumber(window, initialInputs['LWL'], 'value',20) 
    entry.grid()
    entry2 = EntryBoxNumber(window, initialInputs['VCG'], 'value',20)
    entry2.grid() 
    window.mainloop()
    window.quit()
    