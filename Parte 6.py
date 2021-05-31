        filemenu2.add_command(label= "Ficha do Cliente", command= self.geraRelatCliente)
    def validaEntradas(self):
        self.vcmd2= (self.root.register(self.validate_entry2), '%P')

# Programa Principal
App()