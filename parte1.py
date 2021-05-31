from modulos import*
from valida import Validadores
from reports import Relatorios
from funcionalidades import Funcs

root = tix.Tk()

class App(Funcs, Relatorios, Validadores):
def _init_ (self):
self.root = root
self.imagens_base64()
self.validaEntradas()
self.tela()
self.frames_da_tela()
self.widgets_frame1()
self.lista_frame2()
self.monta_tabelas()
self.select_lista()
self.Menus()
root.mainloop()

def tela(self):
self.root.title("cadastro de clientes")
self.root.geometry("700x500")
self.root.state("zoomed")
self.root.resizable(true, true)
self.root.minsize(width = 700, weight = 500)
self.root.iconbitmap("icocli.ico")
