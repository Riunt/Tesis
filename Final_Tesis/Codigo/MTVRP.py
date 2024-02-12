import numpy as np
from time import time
import copy
import math
import tempfile
from array import array
import random

class Vehiculo:
    def __init__(self, Numero,Nodo_Final,Menor):
        self.Numero = Numero
        self.Nodo_Actual = 0
        self.Nodo_Final = Nodo_Final
        self.Menor = Menor
        self.Capacidad_Vehiculo = Capacidad_Vehiculos
        self.Tiempo_Utilizado = 0
        self.Estado = True
        self.Ruta = 1
class Sol:
    def __init__(self, Numero,Nodo_Actual,Costo,Ruta):
        self.Numero = Numero
        self.Nodo_Actual = Nodo_Actual
        self.Costo = Costo
        self.Ruta = Ruta
"""
def Lectura_De_Archivo():

    # Guardado cantidad de codos, cantidad de vehículos, capacidad máxima de los vehículos y tiempo máximo de los vehículos
    archivo=open("instancias creadas/CMT1-4VTH1.txt","r")
    instancia=open("instancias creadas/Matriz-CMT1-4VTH1.txt","w")
    N = int(archivo.readline())
    v = int(archivo.readline())
    Capacidad_Vehiculos = int(archivo.readline())
    Tiempo_Maximo_Vehiculo = int(archivo.readline())
    Requerimientos=np.loadtxt("instancias creadas/CMT1-4VTH1.txt",skiprows=4+N)
    Matriz_Coordenadas=np.loadtxt("instancias creadas/CMT1-4VTH1.txt",skiprows=4,max_rows=N)
    Matriz=np.zeros((N,N))

    for i in range (N):
        for j in range (N):      
            x1 = Matriz_Coordenadas[i][1]
            y1 = Matriz_Coordenadas[i][2]
            x2 = Matriz_Coordenadas[j][1]
            y2 = Matriz_Coordenadas[j][2]
            distancia = int(math.sqrt((x2-x1)**2+(y2-y1)**2))
            
            Matriz[i][j]=distancia
    archivo.close()

    return(N,v,Capacidad_Vehiculos,Tiempo_Maximo_Vehiculo,Matriz,Requerimientos,Matriz_Coordenadas)
"""
def Lectura_De_Archivo():

    # Guardado cantidad de codos, cantidad de vehículos, capacidad máxima de los vehículos y tiempo máximo de los vehículos
    archivo=open("instancias creadas/Instancia10N_5V.txt","r")
    instancia=open("instancias creadas/Instancia10N_5V.txt-Matriz.txt","w")
    N = int(archivo.readline())
    v = int(archivo.readline())
    Capacidad_Vehiculos = int(archivo.readline())
    Tiempo_Maximo_Vehiculo = int(archivo.readline())
    Requerimientos=np.loadtxt("instancias creadas/Instancia10N_5V.txt",skiprows=4+N)
    Matriz_Coordenadas=np.loadtxt("instancias creadas/Instancia10N_5V.txt",skiprows=4,max_rows=N)
    Matriz=np.zeros((N,N))

    for i in range (N):
        for j in range (N):      
            x1 = Matriz_Coordenadas[i][1]
            y1 = Matriz_Coordenadas[i][2]
            x2 = Matriz_Coordenadas[j][1]
            y2 = Matriz_Coordenadas[j][2]
            distancia = int(math.sqrt((x2-x1)**2+(y2-y1)**2))
            Matriz[i][j]=distancia
    archivo.close()

    return(N,v,Capacidad_Vehiculos,Tiempo_Maximo_Vehiculo,Matriz,Requerimientos,Matriz_Coordenadas)

def verificar_visitados():
    i=1   
    while i<N:
        if Visitados[i]==0:
            return False
        i=i+1

    return True
def Separar_Vehiculos(lista,v):
    i=1
    separador=0
    ruta_vehiculo=list()
    ruta_separada=list()

    for elements in lista:
        if elements.Numero==v:
            ruta_vehiculo.append(elements.Nodo_Actual)
    Cantidad_Nodos=len(ruta_vehiculo)

    for i in range (1,Cantidad_Nodos):
        if ruta_vehiculo[i] == 0:
            ruta=list()
            for j in range (separador,i+1):
                ruta.append(ruta_vehiculo[j])
            ruta_separada.append(ruta)
            separador=i

    return [ruta_separada]    
def Contar_Rutas(lista,v):
    Numero_Rutas=0    
    for elements in lista:
        if elements.Nodo_Actual==0:
            Numero_Rutas=Numero_Rutas+1
    Numero_Rutas=Numero_Rutas-v

    return Numero_Rutas
def Contar_Rutas_Unidas(solucion_por_vehiculo):
    numero_rutas=0
    for vehiculo in range (len(solucion_por_vehiculo)):
        Cantidad_Rutas_Vehiculo=len(solucion_por_vehiculo[vehiculo][0])
        for ruta in range (Cantidad_Rutas_Vehiculo):
            numero_rutas=numero_rutas+1

    return numero_rutas
def umbral(z,n,r):
    B=3
    u=B*(z/(r+n))
    return int(u)
def Definir_Candidatos_Nodo():
    #Matriz de arcos candidatos
    for i in range (N):
        for j in range(N):
            if Tiempos[i][j]!=0:
                if (Tiempos[i][j]<=Umbral):
                    Candidatos[i][j]=1
            if i==0 or j==0:
                Candidatos[i][j]=1  
def Definir_Candidatos_Ruta():
    for vehiculo in range (len(solucion_por_vehiculo)):        
        Rutas_Vehiculo=list()
        for ruta in range (len(solucion_por_vehiculo[vehiculo][0])):
            Nodos_Candidatos=list()
            for k in range (len(solucion_por_vehiculo[vehiculo][0][ruta])-1):
                for n in range (1,N):
                    if Candidatos[solucion_por_vehiculo[vehiculo][0][ruta][k]][n]==1 and Candidatos[solucion_por_vehiculo[vehiculo][0][ruta][k+1]][n]==1:
                        Nodos_Candidatos.append(n)
            Rutas_Vehiculo.append(Nodos_Candidatos)
        Candidatos_Ruta.append(Rutas_Vehiculo)

    for i in range (len(Candidatos_Ruta)):
        for j in range (len(Candidatos_Ruta[i])):
            Candidatos_Ruta[i][j]=list(set(Candidatos_Ruta[i][j]))       
"""
def Swap_Insert():
    costo_swap=0
    costo_mejorado=0
    mejor_solucion_nueva=0
    Inicial_Pre=solucion_por_vehiculo[Vehiculo_Swap_Ini][0][Ruta_Swap_Ini]
    Final_Pre=solucion_por_vehiculo[Vehiculo_Swap_Dest][0][Ruta_Swap_Dest]
 
    if len(solucion_por_vehiculo[Vehiculo_Swap_Ini][0][Ruta_Swap_Ini])>3:
        Posicion_Inicial=random.randrange(1,len(solucion_por_vehiculo[Vehiculo_Swap_Ini][0][Ruta_Swap_Ini])-2)       
        if solucion_por_vehiculo[Vehiculo_Swap_Ini][0][Ruta_Swap_Ini][Posicion_Inicial] in Candidatos_Ruta[Vehiculo_Swap_Dest][Ruta_Swap_Dest]:
            if Candidatos[solucion_por_vehiculo[Vehiculo_Swap_Ini][0][Ruta_Swap_Ini][Posicion_Inicial-1]][solucion_por_vehiculo[Vehiculo_Swap_Ini][0][Ruta_Swap_Ini][Posicion_Inicial+1]]!=2:
                for n in range(1,len(solucion_por_vehiculo[Vehiculo_Swap_Dest][0][Ruta_Swap_Dest])-1):
                    if Candidatos[n][n+1]==1:
                        solucion_por_vehiculo[Vehiculo_Swap_Dest][0][Ruta_Swap_Dest].insert(n,solucion_por_vehiculo[Vehiculo_Swap_Ini][0][Ruta_Swap_Ini][Posicion_Inicial])
                        solucion_por_vehiculo[Vehiculo_Swap_Ini][0][Ruta_Swap_Ini].remove(solucion_por_vehiculo[Vehiculo_Swap_Ini][0][Ruta_Swap_Ini][Posicion_Inicial])

                        Tiempo_Vehiculo=0
                        for ruta in range (len(solucion_por_vehiculo[Vehiculo_Swap_Dest][0])):
                            for nodo in range (len(solucion_por_vehiculo[Vehiculo_Swap_Dest][0][ruta])-1):
                                Tiempo_Vehiculo=Tiempo_Vehiculo+Tiempos[solucion_por_vehiculo[Vehiculo_Swap_Dest][0][ruta][nodo]][solucion_por_vehiculo[Vehiculo_Swap_Dest][0][ruta][nodo+1]]
                        if Tiempo_Vehiculo>=Tiempo_Maximo_Vehiculo:
                            solucion_por_vehiculo[Vehiculo_Swap_Ini][0][Ruta_Swap_Ini]=Inicial_Pre
                            solucion_por_vehiculo[Vehiculo_Swap_Dest][0][Ruta_Swap_Dest]=Final_Pre
                            return False
                        else:
                            return True
"""
def Swap_Insert_2(Posicion_Inicial):
    costo_swap=0
    costo_mejorado=0
    mejor_solucion_nueva=0
    Inicial_Pre=solucion_por_vehiculo[Vehiculo_Swap_Ini][0][Ruta_Swap_Ini]
    Final_Pre=solucion_por_vehiculo[Vehiculo_Swap_Dest][0][Ruta_Swap_Dest]
    if len(solucion_por_vehiculo[Vehiculo_Swap_Ini][0][Ruta_Swap_Ini])>=3:       
        if solucion_por_vehiculo[Vehiculo_Swap_Ini][0][Ruta_Swap_Ini][Posicion_Inicial] in Candidatos_Ruta[Vehiculo_Swap_Dest][Ruta_Swap_Dest]:
            if Candidatos[solucion_por_vehiculo[Vehiculo_Swap_Ini][0][Ruta_Swap_Ini][Posicion_Inicial-1]][solucion_por_vehiculo[Vehiculo_Swap_Ini][0][Ruta_Swap_Ini][Posicion_Inicial+1]]!=2:
                for n in range(1,len(solucion_por_vehiculo[Vehiculo_Swap_Dest][0][Ruta_Swap_Dest])-2):
                    if Candidatos[n][n+1]==1:
                        solucion_por_vehiculo[Vehiculo_Swap_Dest][0][Ruta_Swap_Dest].insert(n,solucion_por_vehiculo[Vehiculo_Swap_Ini][0][Ruta_Swap_Ini][Posicion_Inicial])
                        solucion_por_vehiculo[Vehiculo_Swap_Ini][0][Ruta_Swap_Ini].remove(solucion_por_vehiculo[Vehiculo_Swap_Ini][0][Ruta_Swap_Ini][Posicion_Inicial])

                        Tiempo_Vehiculo=0
                        for ruta in range (len(solucion_por_vehiculo[Vehiculo_Swap_Dest][0])):
                            for nodo in range (len(solucion_por_vehiculo[Vehiculo_Swap_Dest][0][ruta])-1):
                                Tiempo_Vehiculo=Tiempo_Vehiculo+Tiempos[solucion_por_vehiculo[Vehiculo_Swap_Dest][0][ruta][nodo]][solucion_por_vehiculo[Vehiculo_Swap_Dest][0][ruta][nodo+1]]
                        if Tiempo_Vehiculo>=Tiempo_Maximo_Vehiculo:
                            solucion_por_vehiculo[Vehiculo_Swap_Ini][0][Ruta_Swap_Ini]=Inicial_Pre
                            solucion_por_vehiculo[Vehiculo_Swap_Dest][0][Ruta_Swap_Dest]=Final_Pre
                            return False
                        else:
                            return True
def Genera_GML(solucion_por_vehiculo,Nodos,Nombre):

    #Se genera el archivo de salida
    GML=open(Nombre,"w")

    #Se imprime la primera linea fija
    GML.write("graph [ hierarchic 1 directed 1 \n")

    #Se imprimen la Id de los nodos, las posiciones de x e y de los clientes, se definen los parametros de diseño
    for j in range (1,N):
        GML.write("node [ id " + (str(int(Nodos[j][0]))) + " graphics [ x " + (str(int(Nodos[j][1]))) + " y " + (str(int(Nodos[j][2]))) + " ")
        GML.write("w 3  h 3 type \"circle\"] LabelGraphics [text " + " " + "\"" + str(int(Nodos[j][0])) + "\"" + " " + "fontSize 2 ] ]\n")

    #Se imprimen la Id de los nodos, las posiciones de x e y del depósito, se definen los parametros de diseño
    GML.write("node [ id " + str(int(Nodos[0][0])) + " graphics [ x " + str(int(Nodos[0][1])) + " y " + str(int(Nodos[0][2])))
    GML.write(" w 5  h 5 type \"roundrectangle\" fill  \"#FF6600\"] LabelGraphics [text \"" + str(int(Nodos[0][0])) + "\" fontSize 3 ] ] \n")

    #Se imprimen los valores de los nodos pertenecientes a cada arco de la solución, con un color distinto para cada vehículo
    for vehiculo in range (len(solucion_por_vehiculo)):
        Cantidad_Rutas_Vehiculo=len(solucion_por_vehiculo[vehiculo][0])

        c1=random.choice("0123456789ABCDEF")
        c2=random.choice("0123456789ABCDEF")
        c3=random.choice("0123456789ABCDEF")
        c4=random.choice("0123456789ABCDEF")
        c5=random.choice("0123456789ABCDEF")
        c6=random.choice("0123456789ABCDEF")

        for ruta in range (Cantidad_Rutas_Vehiculo):
            cantidad_nodos_ruta=len(solucion_por_vehiculo[vehiculo][0][ruta])

            for nodo in range (cantidad_nodos_ruta-1):
                GML.write("edge [ source " + str(solucion_por_vehiculo[vehiculo][0][ruta][nodo]) + " target " + str(solucion_por_vehiculo[vehiculo][0][ruta][nodo+1]) + " graphics [ fill \"#"+c1+c2+c3+c4+c5+c6+"\" ] ]")
                GML.write("\n")
def Inicializa_Visitados_Vehiculos_Ruta():
    #Inicializa como ningún nodo visitado
    Visitados=list()
    for i in range(N):
        Visitados.append(0)
    #Inicializa los datos iniciales de los veehículos
    Vehiculos=list()
    i=0
    while (i<v):
        auto=Vehiculo(i+1,0,0)
        Vehiculos.append(auto)
        Vehiculos[i].Nodo_Actual
        i=i+1
    #Inicializa la lista de soluciones en el depósito
    Ruta=list()
    Trayecto=Sol(1,0,0,0)
    Ruta.append(Trayecto)

    return(Visitados,Vehiculos,Ruta)
def Unir_Rutas(solucion_por_vehiculo):
    Lista_Unida=list()
    Listas_Cortas=list()
    for i in range (cantidad_vehiculos):
        k=0
        for j in range (len(solucion_por_vehiculo[i][k])):
            numero=len(solucion_por_vehiculo[i][0][j])
            if(numero<=4):
                Lista_Unida.extend(solucion_por_vehiculo[i][0][j])
                Listas_Cortas.append([i,j])
            k=k+1

    Lista_Unida=list(filter((0).__ne__, Lista_Unida))
    Lista_Unida.insert(0,0)
    Lista_Unida.append(0)

    for i in range (len(Listas_Cortas)):
        solucion_por_vehiculo[Listas_Cortas[i][0]][0].pop(Listas_Cortas[0][1])
    solucion_por_vehiculo.append(Lista_Unida)
        
    Tiempo_Utilizado=0
    Menor_Tiempo_Utilizado=0
    Vehiculo_Menor_Tiempo_Utilizado=0
    for vehiculo in range (cantidad_vehiculos):
        Cantidad_Rutas_Vehiculo=len(solucion_por_vehiculo[vehiculo][0])
        for ruta in range (Cantidad_Rutas_Vehiculo):
            cantidad_nodos_ruta=len(solucion_por_vehiculo[vehiculo][0][ruta])
            for nodo in range (cantidad_nodos_ruta-1):
                Tiempo_Utilizado=Tiempo_Utilizado+Tiempos[solucion_por_vehiculo[vehiculo][0][ruta][nodo]][solucion_por_vehiculo[vehiculo][0][ruta][nodo+1]]
        if Menor_Tiempo_Utilizado==0:
            Menor_Tiempo_Utilizado=Tiempo_Utilizado
            Vehiculo_Menor_Tiempo_Utilizado=vehiculo
        else:
            if Tiempo_Utilizado<Menor_Tiempo_Utilizado:
                Menor_Tiempo_Utilizado=Tiempo_Utilizado
                Vehiculo_Menor_Tiempo_Utilizado=vehiculo
    
    solucion_por_vehiculo[0][0].insert(0,Lista_Unida)
    solucion_por_vehiculo.pop()
"""
def Busca_Mejora (v,N,Tiempos,mejor_solucion,Necesidad,Capacidad_Maxima,Tiempo_Maximo,Candidatos,solucion_por_vehiculo):
    mejor_solucion_nueva=mejor_solucion
    contador_iteraciones=0
    mejor_ruta=list()
    costo_mejorado=mejor_solucion
    while contador_iteraciones<=1000:
        
        if len(solucion_por_vehiculo[vehiculo][0][ruta])>=5:
            numero1 = random.randint(1,len(solucion_por_vehiculo[vehiculo][0][ruta])-2)
            numero2 = random.choice([i for i in range(1,len(solucion_por_vehiculo[vehiculo][0][ruta])-2) if i not in [numero1]])

            if Candidatos[solucion_por_vehiculo[vehiculo][0][ruta][numero1-1]][solucion_por_vehiculo[vehiculo][0][ruta][numero2]] == 1 and Candidatos[solucion_por_vehiculo[vehiculo][0][ruta][numero1+1]][solucion_por_vehiculo[vehiculo][0][ruta][numero2]] == 1 and Candidatos[solucion_por_vehiculo[vehiculo][0][ruta][numero2-1]][solucion_por_vehiculo[vehiculo][0][ruta][numero1]] == 1 and Candidatos[solucion_por_vehiculo[vehiculo][0][ruta][numero2+1]][solucion_por_vehiculo[vehiculo][0][ruta][numero1]] == 1:
                costo_mejorado=costo_mejorado-Tiempos[solucion_por_vehiculo[vehiculo][0][ruta][numero1]][solucion_por_vehiculo[vehiculo][0][ruta][numero1-1]]-Tiempos[solucion_por_vehiculo[vehiculo][0][ruta][numero1]][solucion_por_vehiculo[vehiculo][0][ruta][numero1+1]]-Tiempos[solucion_por_vehiculo[vehiculo][0][ruta][numero2]][solucion_por_vehiculo[vehiculo][0][ruta][numero2-1]]-Tiempos[solucion_por_vehiculo[vehiculo][0][ruta][numero2]][solucion_por_vehiculo[vehiculo][0][ruta][numero2+1]]
                auxiliar=solucion_por_vehiculo[vehiculo][0][ruta][numero1]
                solucion_por_vehiculo[vehiculo][0][ruta][numero1]=solucion_por_vehiculo[vehiculo][0][ruta][numero2]
                solucion_por_vehiculo[vehiculo][0][ruta][numero2]=auxiliar;
                costo_mejorado=costo_mejorado+Tiempos[solucion_por_vehiculo[vehiculo][0][ruta][numero1]][solucion_por_vehiculo[vehiculo][0][ruta][numero1-1]]+Tiempos[solucion_por_vehiculo[vehiculo][0][ruta][numero1]][solucion_por_vehiculo[vehiculo][0][ruta][numero1+1]]+Tiempos[solucion_por_vehiculo[vehiculo][0][ruta][numero2]][solucion_por_vehiculo[vehiculo][0][ruta][numero2-1]]+Tiempos[solucion_por_vehiculo[vehiculo][0][ruta][numero2]][solucion_por_vehiculo[vehiculo][0][ruta][numero2+1]]
                
                if costo_mejorado<mejor_solucion_nueva:
                    mejor_solucion_nueva=costo_mejorado
                    contador_iteraciones=0
                    mejor_ruta=solucion_por_vehiculo
                    Genera_GML(solucion_por_vehiculo,Coordenadas,"Grafico_Final.GML")
                
                else:
                    auxiliar=solucion_por_vehiculo[vehiculo][0][ruta][numero1]
                    solucion_por_vehiculo[vehiculo][0][ruta][numero1]=solucion_por_vehiculo[vehiculo][0][ruta][numero2]
                    solucion_por_vehiculo[vehiculo][0][ruta][numero2]=auxiliar
                    contador_iteraciones=contador_iteraciones+1
            else:
                contador_iteraciones=contador_iteraciones+1
    solucion_por_vehiculo=mejor_ruta
    return mejor_solucion_nueva
"""
"""
def Busca_Mejora (v,N,Tiempos,mejor_solucion,Necesidad,Capacidad_Maxima,Tiempo_Maximo,Candidatos,solucion_por_vehiculo):
    mejor_solucion_nueva=mejor_solucion
    contador_iteraciones=0
    nodo=1
    mejor_ruta=solucion_por_vehiculo[vehiculo][0][ruta]
    costo_mejorado=mejor_solucion
    iteraciones=0
    reiniciar=0
    nodos_movidos=list()
    while iteraciones<20:
        reiniciar=0
        while (nodo<=len(mejor_ruta)-1):
            nodo_a_mover=mejor_ruta[1]
            
            if len(mejor_ruta)>=5:
                if nodo_a_mover not in nodos_movidos:
                    for i in range (1,len(mejor_ruta)-1):
                        costo_mejorado=costo_mejorado-Tiempos[mejor_ruta[0]][mejor_ruta[1]]-Tiempos[mejor_ruta[i]][mejor_ruta[i+1]]-Tiempos[mejor_ruta[i]][mejor_ruta[i-1]]            
                        mejor_ruta.insert(i,nodo_a_mover)
                        mejor_ruta.remove(nodo_a_mover)
                        print( solucion_por_vehiculo[vehiculo][0][ruta])
                        costo_mejorado=costo_mejorado+Tiempos[mejor_ruta[0]][mejor_ruta[1]]+Tiempos[mejor_ruta[i]][mejor_ruta[i+1]]+Tiempos[mejor_ruta[i]][mejor_ruta[i-1]]            
                        if costo_mejorado<mejor_solucion:
                            mejor_solucion=costo_mejorado
                            mejor_ruta=solucion_por_vehiculo[vehiculo][0][ruta]
                            print(costo_mejorado)
                            reiniciar=1
                            nodos_movidos.append(nodo_a_mover)
                    if reiniciar==1:
                        iteraciones=0
                    else:
                        iteraciones=iteraciones+1   
                    nodo+=1
                else:
                    nodo+=1
                print ("nodos movidos",nodos_movidos)               
            
                
    return mejor_solucion
"""

def Busca_Mejora (v,N,Tiempos,mejor_solucion,Necesidad,Capacidad_Maxima,Tiempo_Maximo,Candidatos,solucion_por_vehiculo):
    mejor_solucion_nueva=mejor_solucion
    contador_iteraciones=0
    nodo=1
    mejor_ruta=solucion_por_vehiculo[vehiculo][0][ruta]
    costo_mejorado=mejor_solucion
    iteraciones=0
    reiniciar=0
    nodos_movidos=list()
    while iteraciones<2:
        reiniciar=0
        nodo=1
        while (nodo<=len(mejor_ruta)-2):
            nodo_a_mover=mejor_ruta.index(nodo)
            #print("nodo a mover",nodo_a_mover)           
            if len(mejor_ruta)>=5:
                for i in range (1,len(mejor_ruta)-1):
                    costo_mejorado=costo_mejorado-Tiempos[mejor_ruta[nodo_a_mover]][mejor_ruta[nodo_a_mover-1]]-Tiempos[mejor_ruta[nodo_a_mover]][mejor_ruta[nodo_a_mover+1]]-Tiempos[mejor_ruta[i]][mejor_ruta[i-1]]            
                    mejor_ruta.insert(i,nodo_a_mover)
                    mejor_ruta.remove(nodo_a_mover)
                    #print( solucion_por_vehiculo[vehiculo][0][ruta])
                    if i<nodo_a_mover:
                        costo_mejorado=costo_mejorado+Tiempos[mejor_ruta[i-1]][mejor_ruta[i]]+Tiempos[mejor_ruta[i]][mejor_ruta[i+1]]+Tiempos[mejor_ruta[nodo_a_mover]][mejor_ruta[nodo_a_mover+1]]   
                        print("sumar")
                    if i>nodo_a_mover:
                        costo_mejorado=costo_mejorado+Tiempos[mejor_ruta[i-1]][mejor_ruta[i]]+Tiempos[mejor_ruta[i]][mejor_ruta[i+1]]+Tiempos[mejor_ruta[nodo_a_mover-1]][mejor_ruta[nodo_a_mover]]   
                    print("costo mejorado",costo_mejorado)
                    if costo_mejorado<mejor_solucion:
                        mejor_solucion=costo_mejorado
                        mejor_ruta=solucion_por_vehiculo[vehiculo][0][ruta]
                        #print(costo_mejorado)
                        reiniciar=1
                        nodos_movidos.append(nodo)
                        #print("nodos movidos",nodos_movidos)
                if reiniciar==1:
                    iteraciones=0
                else:
                    iteraciones=iteraciones+1   
                nodo+=1
                                 
    return mejor_solucion

(N,v,Capacidad_Vehiculos,Tiempo_Maximo_Vehiculo,Tiempos,Requerimientos,Coordenadas)=Lectura_De_Archivo()
Candidatos = [[0 for col in range(N)] for row in range(N)]
(Visitados,Vehiculos,Ruta)=Inicializa_Visitados_Vehiculos_Ruta()
Candidatos_Ruta=list()
menor=0
Nodo_Final=0
Nodo_Actual=0
Nodo_Aux=1
vehiculo=Vehiculo(1,1,10)
Todos_visitados=False

cantidad_vehiculos=1
vehiculos_sin_servicio=0
nodos_visitados=0

start_time = time()
while Todos_visitados==False:
    menor=0
    num_auto=1
    Vehiculo_Trayecto_Menor=num_auto
    
    while num_auto<=cantidad_vehiculos:

        #inicializa el primer numero distinto de 0 como el menor        OK primer vehiculo
        for i in range (N):
            if Tiempos[Vehiculos[num_auto-1].Nodo_Actual][i]!=0 and Visitados[i]==0:
                menor=Tiempos[Vehiculos[num_auto-1].Nodo_Actual][i]
                numero_auto_guardado=num_auto-1
                i=N

        if cantidad_vehiculos==1:
            Trayecto_Menor=Tiempo=menor

        #busca el nodo de destino con menor costo
        for j in range(N):
            if Tiempos[Vehiculos[num_auto-1].Nodo_Actual][j]<=menor and Tiempos[Vehiculos[num_auto-1].Nodo_Actual][j]!=0 and Visitados[j]==0 and Nodo_Aux!=Nodo_Actual:
                menor=Tiempos[Vehiculos[num_auto-1].Nodo_Actual][j]
                Nodo_Actual=j
                Nodo_Aux=menor

        if menor<Trayecto_Menor and cantidad_vehiculos>1:
            Vehiculo_Trayecto_Menor=num_auto
            num_auto=num_auto+1
        num_auto=num_auto+1

    menor_deposito=0
    if nodos_visitados>0 and v!=1:
        #inicializa el primer numero distinto de 0 como el menor desde el depósito
        for i in range (N):
            if Tiempos[0][i]!=0 and Visitados[i]==0:
                menor_deposito=Tiempos[0][i]
                k=N

        #buscar trayecto menor desde el depósito
        for j in range(N):
            if Tiempos[0][j]<=menor_deposito and Tiempos[0][j]!=0 and Visitados[j]==0:
                menor_deposito=int(Tiempos[0][j])
                Nodo_Actual_Deposito=j

        if menor_deposito<Nodo_Aux and cantidad_vehiculos<v:
            cantidad_vehiculos=cantidad_vehiculos+1
            menor=menor_deposito
            Nodo_Actual=Nodo_Actual_Deposito
            numero_auto_guardado=cantidad_vehiculos-1
            Trayecto=Sol(numero_auto_guardado+1,Vehiculos[numero_auto_guardado].Nodo_Actual,0,Vehiculos[numero_auto_guardado].Ruta)
            Ruta.append(Trayecto)

    #actualizar valores
    if Tiempo_Maximo_Vehiculo>=Vehiculos[numero_auto_guardado].Tiempo_Utilizado+Tiempos[Vehiculos[numero_auto_guardado].Nodo_Actual][j]+Tiempos[Vehiculos[numero_auto_guardado].Nodo_Actual][0] and Vehiculos[numero_auto_guardado].Estado==True:
        if 0<=Vehiculos[numero_auto_guardado].Capacidad_Vehiculo-Requerimientos[Vehiculos[numero_auto_guardado].Nodo_Actual]:
            Nodo_inicial=Vehiculos[numero_auto_guardado].Nodo_Actual
            Vehiculos[numero_auto_guardado].menor=menor
            Vehiculos[numero_auto_guardado].Nodo_Actual=Nodo_Actual
            Vehiculos[numero_auto_guardado].Tiempo_Utilizado=Vehiculos[numero_auto_guardado].Tiempo_Utilizado+menor
            Candidatos[Nodo_inicial][Nodo_Actual]=1

            if Vehiculos[numero_auto_guardado].Nodo_Actual!=0:
                Visitados[Vehiculos[numero_auto_guardado].Nodo_Actual]=1

        else:
            Vehiculos[numero_auto_guardado].Nodo_Actual=0
            Vehiculos[numero_auto_guardado].Capacidad_Vehiculo=Capacidad_Vehiculos
            print("al deposito por falta de capacidad")
    else:
        Vehiculos[numero_auto_guardado].Estado=False
        Vehiculos[numero_auto_guardado].Nodo_Actual=0
        vehiculos_sin_servicio=vehiculos_sin_servicio+1;

    if vehiculos_sin_servicio==cantidad_vehiculos and cantidad_vehiculos<v:
        cantidad_vehiculos=cantidad_vehiculos+1

    #Marca los nodos distintos de 0 como visitados
    if Vehiculos[numero_auto_guardado].Nodo_Actual!=0:
        Visitados[Vehiculos[numero_auto_guardado].Nodo_Actual]=1

    if Vehiculos[numero_auto_guardado].Nodo_Actual==0:
        Vehiculos[numero_auto_guardado].Capacidad_Vehiculo=Capacidad_Vehiculos
        Vehiculos[numero_auto_guardado].Ruta=Vehiculos[numero_auto_guardado].Ruta+1
    else:
        Vehiculos[numero_auto_guardado].Capacidad_Vehiculo=Vehiculos[numero_auto_guardado].Capacidad_Vehiculo-Requerimientos[Vehiculos[numero_auto_guardado].Nodo_Actual]
    
    #Se agregan los datos del trayecto a la ruta
    Trayecto=Sol(numero_auto_guardado+1,Vehiculos[numero_auto_guardado].Nodo_Actual,menor,Vehiculos[numero_auto_guardado].Ruta)
    Ruta.append(Trayecto)
    Todos_visitados=verificar_visitados()
    nodos_visitados=nodos_visitados+1

    #devuelve vehículos al depósito
    if Todos_visitados==True:
        for i in range (cantidad_vehiculos):
            if Vehiculos[i].Nodo_Actual!=0:
                Trayecto=Sol(i+1,0,Tiempos[Vehiculos[i].Nodo_Actual][0],Vehiculos[numero_auto_guardado].Ruta)
                Ruta.append(Trayecto)
                Vehiculos[i].Nodo_Actual=0

costo_inicial=0
for elements in Ruta:
    costo_inicial=costo_inicial+elements.Costo
print("Costo Inicial = ", costo_inicial)

solucion_por_vehiculo=list()
Genera_GML(solucion_por_vehiculo,Coordenadas,"Grafico_Vacio.GML")

for i in range (1,cantidad_vehiculos+1):
    solucion_por_vehiculo.append(Separar_Vehiculos(Ruta,i))

Cantidad_Rutas=Contar_Rutas(Ruta,cantidad_vehiculos)
Genera_GML(solucion_por_vehiculo,Coordenadas,"Grafico_inicial.GML")

Unir_Rutas(solucion_por_vehiculo)
solucion_por_vehiculo = [x for x in solucion_por_vehiculo if x != [[]]]
Cantidad_Rutas_Unidas=Contar_Rutas_Unidas(solucion_por_vehiculo)
print("cantidad rutas:",Cantidad_Rutas)
Umbral=umbral(costo_inicial,N,Cantidad_Rutas_Unidas)
Definir_Candidatos_Nodo()

costo=0
for vehiculo in range (len(solucion_por_vehiculo)):
        Cantidad_Rutas_Vehiculo=len(solucion_por_vehiculo[vehiculo][0])
        for ruta in range (Cantidad_Rutas_Vehiculo):
            cantidad_nodos_ruta=len(solucion_por_vehiculo[vehiculo][0][ruta])
            for nodo in range (cantidad_nodos_ruta-1):
                costo=costo+Tiempos[solucion_por_vehiculo[vehiculo][0][ruta][nodo]][solucion_por_vehiculo[vehiculo][0][ruta][nodo+1]]

Genera_GML(solucion_por_vehiculo,Coordenadas,"Grafico_inicial.GML")

print("Costo inicial = ",costo)
print("Ruta inicial\n",solucion_por_vehiculo)
costo=0
for nodo in range (len(solucion_por_vehiculo[0][0][0])-1):
    costo=costo+Tiempos[solucion_por_vehiculo[0][0][0][nodo]][solucion_por_vehiculo[0][0][0][nodo+1]]

#Busca mejoras dentro de una ruta
nuevo_costo=0

for vehiculo in range (len(solucion_por_vehiculo)):
    Cantidad_Rutas_Vehiculo=len(solucion_por_vehiculo[vehiculo][0])
    for ruta in range (Cantidad_Rutas_Vehiculo):
        cantidad_nodos_ruta=len(solucion_por_vehiculo[vehiculo][0][ruta])
        costo=0
        for nodo in range (cantidad_nodos_ruta-1):
            costo=costo+Tiempos[solucion_por_vehiculo[vehiculo][0][ruta][nodo]][solucion_por_vehiculo[vehiculo][0][ruta][nodo+1]]            
        nuevo_costo=nuevo_costo+Busca_Mejora(v,N,Tiempos,costo,Requerimientos,Capacidad_Vehiculos,Tiempo_Maximo_Vehiculo,Candidatos,solucion_por_vehiculo)
costo_mejorado=nuevo_costo

print("Costo luego de buscar mejoras dentro de las rutas: ",nuevo_costo)

print("solucion por vehiculo despues de buscar mejora: \n", solucion_por_vehiculo)

mejor_ruta=[]
Candidatos_Ruta=list()
swap_realizado=True


#Swap

for i in range (100):
    for vehiculo in range (len(solucion_por_vehiculo)):
        
        Vehiculo_Swap_Ini=vehiculo
        Cantidad_Rutas_Vehiculo=len(solucion_por_vehiculo[vehiculo][0])
        for ruta in range (Cantidad_Rutas_Vehiculo):
            Ruta_Swap_Ini=ruta
            for vehiculo_fin in range(len(solucion_por_vehiculo)):
                Vehiculo_Swap_Dest=vehiculo_fin
                for ruta_fin in range (Cantidad_Rutas_Vehiculo):
                    if (Ruta_Swap_Ini==ruta_fin and Vehiculo_Swap_Ini==Vehiculo_Swap_Dest):
                        break
                    else:
                        if len(solucion_por_vehiculo[vehiculo][0][Ruta_Swap_Ini])>2:
                            Ruta_Swap_Dest=ruta_fin
                            Definir_Candidatos_Ruta()
                            #print("Vehiculo inicio ",Vehiculo_Swap_Ini," ruta inicio: ", Ruta_Swap_Ini," vehiculo fin: ",Vehiculo_Swap_Dest,"Ruta fin: ",Ruta_Swap_Dest)
                            i=0

                            for posicion_inicial in range (1,len(solucion_por_vehiculo[Vehiculo_Swap_Ini][0][Ruta_Swap_Ini])-2):
                                swap_realizado=Swap_Insert_2(posicion_inicial)
                                if swap_realizado==True:            
                                    costo_swap=0
                                    for vehiculo in range (len(solucion_por_vehiculo)):
                                        Cantidad_Rutas_Vehiculo=len(solucion_por_vehiculo[vehiculo][0])
                                        for ruta in range (Cantidad_Rutas_Vehiculo):
                                            cantidad_nodos_ruta=len(solucion_por_vehiculo[vehiculo][0][ruta])
                                            for nodo in range (cantidad_nodos_ruta-1):
                                                costo_swap=costo_swap+Tiempos[solucion_por_vehiculo[vehiculo][0][ruta][nodo]][solucion_por_vehiculo[vehiculo][0][ruta][nodo+1]]            
                                    if costo_swap<costo_mejorado:
                                        costo_mejorado=costo_swap
                                        contador_iteraciones=0
                                        mejor_ruta=solucion_por_vehiculo
                                        Genera_GML(solucion_por_vehiculo,Coordenadas,"Grafico_Final_SWAP.GML")
                                        i=0
                                    else:
                                        i=i+1
                                else:
                                    i=i+1

print(mejor_ruta)
solucion_por_vehiculo=mejor_ruta
print(solucion_por_vehiculo)
print("costo despues de 100 swaps: ",costo_mejorado)
elapsed_time = time() - start_time
print("Elapsed time: %.10f seconds." % elapsed_time)
#Genera_GML(solucion_por_vehiculo,Coordenadas,"Grafico_Final_SWAP.GML")
