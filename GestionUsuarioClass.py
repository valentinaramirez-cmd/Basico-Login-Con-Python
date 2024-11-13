class GestionUsuarios: 

    def __init__(self):
        self.listaUsuarios=[]

    def buscarUsuario(self, user): 

        aux= 0

        for us in self.listaUsuarios : 
            if (us.user == user) :
                aux = us
    
        return aux

    def buscarGmail(self, gmail): 
        
        aux= 0

        for us in self.listaUsuarios : 
            if (us.gmail == gmail) :
                aux = us
    
        return aux
            
            
    def guardarUsuario(self, usuario): 
        self.listaUsuarios.append(usuario); 
    
    def visualizarListaUsuarios(self): 
        return self.listaUsuarios
