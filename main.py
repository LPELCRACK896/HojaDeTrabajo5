import random
import math
import simpy
#Simulacion de corrida de programas
escenario=simpy.Environment()

memoria_ram_disponible== simpy.Container(escenario, init=100, capacity=100)
registros_para_instrucciones_disponible = 15

def onNew(): #Manda a siguiente proceso o asigna tiempo de espera
    global memoria_ram_disponible
    aleatorio_ram= random.randint(1,10)
    if(aleatorio_ram<=memoria_ram_disponible):
        memoria_ram_disponible=memoria_ram_disponible-aleatorio_ram

    else:
        pass


def onReady(): #Manda a siguiente proceso o asigna tiempo de espera
    global registros_para_instrucciones_disponible
    aleatorio_instrucciones = random.randint(1, 10)
    if(aleatorio_instrucciones<=registros_para_instrucciones_disponible):
        pass
def onRunning():
    pass
def onSimulation():
    pass
def terminated():#Posible proceso post onRunnning
    pass