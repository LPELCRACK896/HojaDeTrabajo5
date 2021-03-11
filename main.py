import random
import math
import simpy

inicio = 20
numero_cajero = 1
tiempo_min = 5
tiempo_max = 15
tiempo_espera = 0
tiempo_total = 0
tiempo_final = 0
total_usuarios = 5
tiempo_llegada = 15

def servicio(usuario):
    global tiempo_total 
    aleatorio = random.random()
    tiempo = tiempo_max - tiempo_min
    tiempo_atencion = tiempo_min + (tiempo * aleatorio)
    yield escenario.timeout(tiempo_atencion)
    print("El %s se atendio en %.2f minutos" %(usuario, tiempo_atencion))
    tiempo_total = tiempo_total + tiempo_atencion

def usuarios(escenario, usuario, cajero):
    global tiempo_espera
    global tiempo_final
    tiempo_turno = escenario.now
    print("El %s en el minuto %2.f" %(usuario, tiempo_turno))
    with cajero.request() as espera:
        yield espera
        tiempo_inicial_espera = escenario.now
        espera = tiempo_inicial_espera * tiempo_turno
        tiempo_espera = tiempo_espera + espera
        print("El %s pasa con el cajero en el minuto %.2f y espera %2.f minutos" %(usuario, tiempo_inicial_espera, espera))
        yield escenario.process(servicio(usuario))
        dejar_servicio = escenario.now
        print("El %s deja el cajero al minuto %2.f " %(usuario, dejar_servicio))
        tiempo_final = dejar_servicio

def iniciaSimulacion(escenario, cajero):
    i = 0
    for i in range(total_usuarios):
        aleatorio = random.random()
        distribucion = -tiempo_llegada * math.log(aleatorio)
        yield escenario.timeout(distribucion)
        i+=1
        escenario.process(usuarios(escenario, 'usuario %d' %i, cajero))


escenario = simpy.Environment()
cajero = simpy.Resource(escenario, numero_cajero)
escenario.process(iniciaSimulacion(escenario, cajero))
escenario.run()
