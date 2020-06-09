import math # Funciones matematicas
import tkinter as tk # interfaz Grafica
import tkinter.scrolledtext as tkst

#Definicion de Variables

# Ejemplo Practico

"""UUna compañía se abastece actualmente de cierto producto solicitando una
 cantidad suficiente para satisfacer la demanda de un mes. La demanda anual
  del artículo es de 1500 unidades. Se estima que cada vez que hace un pedido
   se incurre en un costo de $20. El costo de almacenamiento por inventario 
   unitario por mes es de $2 y no se admite escasez.
Determinar la cantidad de pedido óptima y el tiempo entre pedidos.

"""
class TeoriaInventarios():
    def __init__(self):
        #Definicion de Variables
        self.costoTotal=0 # CostoAnual total  tambien definido como TC o CTAQ
        self.demandaA=0 # Demanda Anual tambien definido como D
        self.demandaP=0 # Demanda Promedio dia tambien definido como d
        self.costoUnid=0 #Costo por unidad tambien definido como C
        self.cantidad=0 # Cantidada que debe ordenarse Q
        self.costoSepara=0 # costo de separacion  o costo de pedido S o Cp
        self.nuePedido=0  # Nuevo pedido R
        self.plazoRepo=0 # plazo reposicion L
        self.costoAManten=0 # costo mantenimiento y almacen por unidad H
        self.tasaMan=0 #tasa de mantenimineto
        self.tiempo=0
        self.cantEcon=0
        self.costoTendencia=0
        
    def setTiempo(self,tiempo):
            self.tiempo=tiempo
    def setCostoTotal(self,costoTotal):
            self.costoTotal=costoTotal
    def setDemandaA(self,demandaA):
            self.demandaA=demandaA
    def setDemandaP(self,demandaP):
            self.demandaP=demandaP
    def setCostoUnid(self,costoUnid):
            self.costoUnid=costoUnid
    def setCantidad(self,cantidad):
            self.cantidad=cantidad
    def setCostoSepara(self,costoSepara):
            self.costoSepara=costoSepara
    def setNuePedido(self,nuePedido):
            self.nuePedido=nuePedido
    def setPlazoRepo(self,plazoRepo):
            self.plazoRepo=plazoRepo
    def setCostoAManten(self,costoAManten):
            self.costoAManten=costoAManten
    def setTasaMan(self,tasaMan):
            self.tasaMan=tasaMan
                
   
    def eoqFija(self,costoTendencia,tiempo,costoTotal,demandaA,demandaP,costoUnid,cantidad,costoSepara,nuePedido,plazoRepo,costoAManten,tasaMan):
        self.tiempo=tiempo
        self.costoTotal=costoTotal
        self.demandaA=demandaA
        self.demandaP=demandaP
        self.costoUnid=costoUnid
        self.cantidad=cantidad
        self.costoSepara=costoSepara
        self.nuePedido=nuePedido
        self.plazoRepo=plazoRepo
        self.costoAManten=costoAManten
        self.tasaMan=tasaMan
        self.costoTendencia=costoTendencia

                
    
    def catidadEconmica (self):
        if self.demandaA==0 or self.costoSepara ==0 or  self.costoAManten==0:
            if self.costoAManten==0:
                self.costoMantenimiento();
        self.cantEcon=math.ceil(math.sqrt((2*self.demandaA*self.costoSepara)/self.costoAManten))
        return "•La cantidad que debe ordenarse es de "+str(self.cantEcon)+" unidades"

    def costoMantenimiento(self):
        self.costoAManten=self.costoTendencia*self.tiempo;
        

    def nuevoPedido(self,demandaP,plazoRepo):
       if demandaP==0:
           demandaP=self.demandaA/self.tiempo
       return "•El nuevo pedido se debe hacer cundo haya minimo " +str(math.ceil(demandaP*plazoRepo))+ " unidades"

    def plazoReemplazo(self,demandaA):
       self.plazoRepo= math.ceil(demandaA/self.cantEcon)
       return "•Numero de pedidos por año es de " +str(self.plazoRepo)

    def tiempoPedidos(self):
        return self.cantEcon/self.demandaA

    def costeTotal(self):
        self.costoTotal=self.costoUnid*self.demandaA+(self.costoSepara*self.plazoRepo)+self.costoAManten*(self.cantEcon/2)
        return self.costoTotal
        
            

class Ventana():

    def  __init__(self):
        self.teoriaInventarios=TeoriaInventarios()
        self.window=tk.Tk()
        self.window.geometry("500x400")
        self.window.title("Teoria de Inventarios")
        #self.window.configure(bg='black')
        self.frame=tk.Frame(self.window)
        self.contVariables()
        self.window.mainloop()

    def contVariables(self):
        #Creando un label para el campo de texto "answer"
        lbTitulo = tk.Label(self.window, text="Defina las Variables", padx=10 )
        lbTitulo.place(x=10,y=10)

        #Creando un label para el campo de texto "question"
        lbcostoTotal = tk.Label(self.frame, text="Costo Total", padx=10 )
        lbcostoTotal.grid(row=1, column=0, sticky=tk.W)
        lbdemandaA = tk.Label(self.frame, text="Demanda Anual", padx=10 )
        lbdemandaA.grid(row=2, column=0, sticky=tk.W)
        lbdemandaP = tk.Label(self.frame, text="Demanda Promedio", padx=10 )
        lbdemandaP.grid(row=3, column=0, sticky=tk.W)
        lbcostoUnid = tk.Label(self.frame, text="Costo Unitario", padx=10 )
        lbcostoUnid.grid(row=4, column=0, sticky=tk.W)
        lbcantidad = tk.Label(self.frame, text="Cantidad", padx=10 )
        lbcantidad.grid(row=5, column=0, sticky=tk.W)
        lbcostoSepara = tk.Label(self.frame, text="Costo de Orden", padx=10 )
        lbcostoSepara.grid(row=6, column=0, sticky=tk.W)
        lbplazoRepo = tk.Label(self.frame, text="PlazoRepo", padx=10 )
        lbplazoRepo.grid(row=8, column=0, sticky=tk.W)
        lbcostoAManten = tk.Label(self.frame, text="Costo mantenimiento", padx=10 )
        lbcostoAManten.grid(row=9, column=0, sticky=tk.W)
        lbtasaMan = tk.Label(self.frame, text="tasa mantenimiento", padx=10 )
        lbtasaMan.grid(row=10, column=0, sticky=tk.W)
        lbtiempo = tk.Label(self.frame, text="tiempo", padx=10 )
        lbtiempo.grid(row=11, column=0, sticky=tk.W)
        lbcantEcon = tk.Label(self.frame, text="cantidad economica", padx=10 )
        lbcantEcon.grid(row=12, column=0, sticky=tk.W)
        lbcostoTendencia = tk.Label(self.frame, text="costo Tendencia", padx=10 )
        lbcostoTendencia.grid(row=13, column=0, sticky=tk.W)

       
         #Creando un txt para el campo de texto "answer"
        self.entrycostoTotal=tk.StringVar()
        self.entrycostoTotal.set("0")
        txtcostoTotal=tk.Entry(self.frame,textvariable=self.entrycostoTotal)
        txtcostoTotal.grid(row=1, column=1)
        self.entrydemandaA=tk.StringVar()
        self.entrydemandaA.set("1500")
        txtdemandaA=tk.Entry(self.frame,textvariable=self.entrydemandaA)
        txtdemandaA.grid(row=2, column=1)
        self.entrydemandaP=tk.StringVar()
        self.entrydemandaP.set("0")
        txtdemandaP=tk.Entry(self.frame,textvariable=self.entrydemandaP)
        txtdemandaP.grid(row=3, column=1)
        self.entrycostoUnid=tk.StringVar()
        self.entrycostoUnid.set("0")
        txtcostoUnid=tk.Entry(self.frame,textvariable=self.entrycostoUnid)
        txtcostoUnid.grid(row=4, column=1)
        self.entrycantidad=tk.StringVar()
        self.entrycantidad.set("0")
        txtcantidad=tk.Entry(self.frame,textvariable=self.entrycantidad)
        txtcantidad.grid(row=5, column=1)
        self.entrycostoSepara=tk.StringVar()
        self.entrycostoSepara.set("20")
        txtcostoSepara=tk.Entry(self.frame,textvariable=self.entrycostoSepara)
        txtcostoSepara.grid(row=6, column=1)
        self.entryplazoRepo=tk.StringVar()
        self.entryplazoRepo.set("0")
        txtplazoRepo=tk.Entry(self.frame,textvariable=self.entryplazoRepo)
        txtplazoRepo.grid(row=8, column=1)
        self.entrycostoAManten=tk.StringVar()
        self.entrycostoAManten.set("24")
        txtcostoAManten=tk.Entry(self.frame,textvariable=self.entrycostoAManten)
        txtcostoAManten.grid(row=9, column=1)
        self.entrytasaMan=tk.StringVar()
        self.entrytasaMan.set("0")
        txttasaMan=tk.Entry(self.frame,textvariable=self.entrytasaMan)
        txttasaMan.grid(row=10, column=1)
        self.entrytiempo=tk.StringVar()
        self.entrytiempo.set("1")
        txttiempo=tk.Entry(self.frame,textvariable=self.entrytiempo)
        txttiempo.grid(row=11, column=1)
        self.entrycantEcon=tk.StringVar()
        self.entrycantEcon.set("0")
        txtcantEcon=tk.Entry(self.frame,textvariable=self.entrycantEcon)
        txtcantEcon.grid(row=12, column=1)
        self.entrycostoTendencia=tk.StringVar()
        self.entrycostoTendencia.set("0")
        txtcostoTendencia=tk.Entry(self.frame,textvariable=self.entrycostoTendencia)
        txtcostoTendencia.grid(row=13, column=1) 

        self.editArea = tkst.ScrolledText(
       master = self.window,
       wrap   = tk.WORD,
       width  = 25,
       height = 15.5
)

        self.editArea.place(x=275,y=50)


        #Definimos un tamaño mínimo de la fila central delgrid para que quede un espacio entre cada entry y posicionamos el frame
        self.frame.grid_rowconfigure(1, minsize=10)
        self.frame.place(x=8,y=50)
        




        #Creando un botón para guardar pregunta y respuesta
        btnSave=tk.Button(self.window,text="Resolver",command=self.acciones,font=("Agency FB",14))
        btnSave.place(x=50,y=310)

# Acciones que  se realizan  al Ejecutar Boton
    def acciones(self):
        #Carga de Datos
        self.editArea.insert(tk.INSERT,"")
        self.editArea.delete(1.0,1.0)
        costoTotal=float(self.entrycostoTotal.get())
        demandaA=float(self.entrydemandaA.get())
        demandaP=float(self.entrydemandaP.get())
        costoUnid=float(self.entrycostoUnid.get())
        cantidad=float(self.entrycantidad.get())
        costoSepara=float(self.entrycostoSepara.get())
        nuePedido=0
        plazoRepo=float(self.entryplazoRepo.get())
        costoAManten=float(self.entrycostoAManten.get())
        tasaMan=float(self.entrytasaMan.get())
        tiempo=float(self.entrytiempo.get())
        cantEcon=float(self.entrycantEcon.get())
        costoTendencia=float(self.entrycostoTendencia.get())
        self.teoriaInventarios.eoqFija(costoTendencia,tiempo,costoTotal,demandaA,demandaP,costoUnid,cantidad,costoSepara,nuePedido,plazoRepo,costoAManten,tasaMan)
        self.editArea.insert(tk.INSERT,
            self.teoriaInventarios.catidadEconmica()+"\n"+
            self.teoriaInventarios.nuevoPedido(demandaP,plazoRepo)+"\n"+
            self.teoriaInventarios.plazoReemplazo(demandaA)+"\n"+
            "• Costo Total "+str(self.teoriaInventarios.costeTotal())+"\n"+
            "• El tiempo entre pedido se debe realizar es de" +str(self.teoriaInventarios.tiempoPedidos())+ "Años"+"\n")

        


             

ventana=Ventana()        



    
