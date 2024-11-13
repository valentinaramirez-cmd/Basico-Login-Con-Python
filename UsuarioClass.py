class Usuario: 

    def __init__(self, nombreCompleto, gmail, user, contrasena):
        self.nombreCompleto = nombreCompleto
        self.gmail = gmail
        self.user = user
        self.contrasena = contrasena

    def __str__(self):
        return (f"\n||  Nombre Completo: {self.nombreCompleto} \n||  Usuario: {self.user}  \n||  Gmail: {self.gmail}")

    
