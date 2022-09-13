###############################
# P  R  Á  C  T  I  C  A  (3) #
###############################

# Patricia Da Concepción Sarrate
# Alba González Mallo
# Carlos Hermida Mayán

import time
import math
import pandas as pd
import numpy as np


##########################################
# IMPLEMENTACIÓN ALGORITMO EJERCICIO(1) #
##########################################

#Creamos una funcion para buscar los elementos en un conjunto 
#Si encontramos dicho valor lo devolvemos 

def find(lista, valor):    
	for item in lista:
		if valor in item:
			return item

#Creamos una funcion para unir lo diferentes elementos del conjunto
#Pasamos diferentes elementos, los unimos por la funcion set.union, eliminamos
#los elementos individualmente y añadimos la unión

def merge(S, Uset, Vset):
	union = set.union(Uset, Vset)
	S.remove(Uset)
	S.remove(Vset)
	S.append(union)
	return S

# Creamos la funcion de kruskal para ordenar un grafo.

def kruskal(V,E):
#Creamos una funcion con la finalidad de ordenar las aristas de menos a mayor 

	weight = lambda x: x[2]
	E = sorted(E, key=weight)
	n = len(V)
	T = set()
	S = []
# Una vez que tengamos ordenadas las aristas añadimos los vertices en un 
#conjunto independiente	
	for vertice in V:
		S.append({vertice})
        
# Recorremos las aristas ordenadas con anterioridad		
	for arista in E:
		u = arista[0]
		v = arista[1]

		Uset = find(S, u) #Realizamos la busqueda de dicho vertice en S
		Vset = find(S, v) #Realizamos la busqueda de dicho vertice en S

		if Uset != Vset:
        #Si los elementos buscados son diferentes se hace la union de los mismos 
        #Con la función anteriormente creada
			S = merge(S, Uset, Vset)
			T.add(arista)
		if len(T) == n-1:
			break
		#El objetivo crear el grafo uniendo todos los vertices con las aristas de menor peso			
	return T


##########################################
# VALIDACIÓN DEL ALGORITMO EJERCICIO(2)  #
##########################################

#Realizamos las compromaciones de que el algoritmo de kruskal funcione correctamente
#para esta utilizamos una funcion test 

V1 = {0,1,2,3}
E1 = {(0, 2, 9), (2, 3, 2), (0, 3, 6), (1, 2, 4), (0, 1, 5), (1, 3, 3)}
MST1_gold = {(2, 3, 2), (0, 1, 5), (1, 3, 3)}

V2 = {0,1,2,3,4}
E2 = {(3, 4, 6), (1, 2, 1), (0, 2, 9), (1, 4, 7), (0, 3, 4), (1, 3, 2), (2, 3, 3), (2, 4, 9), (0, 4, 8), (0, 1, 5)}
MST2_gold = {(3, 4, 6), (1, 2, 1), (0, 3, 4), (1, 3, 2)}

def test(grafos):
#Introducimos por pantalla los vertices, las aristas y la solución correcta de arbol de expandido minimo
    for grafo in grafos:
        V = grafo[0]
        E = grafo[1]
        MST_gold = grafo[2]
# Realizamos kruskal con las aristas y los vertices 
        print ("Input: {}".format(E))
        MST = kruskal(V,E)
#Comprobamos que la longitud de la solución de aplicar el algoritmo de kruskal
# y la solución del arbol expandido minimo tienen los mismos elementos y el mismo número de los mismos 
        assert(len(MST)==len(MST_gold))
 
        for arista in MST:
        	assert(arista in MST_gold)
#Si estas dos cosas no se cumplen se produce la asserción correspondiente
        
        print("Output: {} \n".format(MST))


print('Algoritmo Kruskal (test)\n')
grafos = [(V1,E1,MST1_gold),(V2,E2,MST2_gold)]
test(grafos)
#Aqui comprobamos el funcionamiento de la función test

#############################################
# FUNCIÓN GENERADORA DE GRAFOS EJERCICIO(3) #
#############################################


#Introducimos una función para crear el gráfico y devuelve los vertices y las aristas

def create_graph(n, max_distance=50):
	a = np.random.randint(low=1, high=max_distance, size=(n,n)) 
	m = np.tril(a,-1) + np.tril(a, -1).T
	rows, cols = m.shape
	E = set([])
	V = set([])
	for i in range(rows): 
		V.add(i)
		for j in range(i+1, cols): 
			E.add((i,j,m[i][j]))
	return (V,E)


####################
# GENERAR SUCESIÓN #
####################

# Generar sucesiones para los grafos que se nos piden en el ejercicio: [20, 40, 80, 160,320, 640, 1280, 2560]

def generar_sucesion():
    '''Genera una sucesión según el ejercicio 3'''
    s = [20]
    for i in range(7):
        n = int(s[i]*2)
        s.append(n)
    return s


#######################
# FUNCIONES DE TIEMPO #
#######################

# Funciones que miden el tiempo del sistema en ese momento en nanosegundos.

def timetime_ns():
    return time.time() * (10**9)
def perfcounter_ns():
    return time.perf_counter() * (10**9)
def processtime_ns():
    return time.process_time() * (10**9)

# Lista que contiene todas estas funciones del tiempo

time_functions =[time.time_ns, perfcounter_ns, timetime_ns, processtime_ns]


#######################
# FUNCIÓN DE MEDICIÓN #
#######################

# Creamos una funcion para calcular el tiempo de ejecucion de cada algoritmo

def medir_tiempos(k,f,g,h):
    '''Medición de los tiempos de ejecución del algoritmo con diferentes
    tamaños de entrada, k repeticiones del bucle de tiempos.'''

    df_final = pd.DataFrame(columns=['n','t(n)',f[1],g[1],h[1]])
    n_values = generar_sucesion()
    for n in n_values:                      # Recorre la sucesión de orden correspondiente
        estimacion = False                  # Inicializamos el booleano estimación
        graph = create_graph(n)             
        V = graph[0]
        E = graph[1]
        t1 = time_functions[0]()            # Medimos la hora del sistema
        kruskal(V,E)          				# Ejecutamos la función
        t2 = time_functions[0]()            # Volvemos a calcular la hora del sistema
        t = (t2-t1)                         # Calculamos el tiempo de ejecución
        if t<500000:                        # Fijación del umbral(en nanosegundos)para tiempos pequeños
            estimacion = True               # Al ejecutar el algortimo k veces, se trata de una estimación
            t12 = time_functions[0]()       # Medimos la hora del sistema
            i = 0
            while i<k:                      # Hacemos un bucle k veces para hacer la media de tiempos
                kruskal(V,E)
                i+=1
            t22 = time_functions[0]()       # Calculamos la hora del sistema
            t_loop_1 = time_functions[0]()  # Medimos la ejecución de bucle
            i = 0
            while i<k:
                i += 1
            t_loop_2 = time_functions[0]()  # Hora del sistema al acabar el bucle
            # Calculamos la media de los tiempos pequeños restandole el tiempo
            # que dura el bucle y dividiendolo entre k.  
            resultado = ((t22-t12) - (t_loop_2-t_loop_1)) / k               
            t = round(resultado,3)
        if estimacion:                      # Si t es una estimación, le añadimos un asterisco
            t_n = f"*{t}"
        else:
            t_n = t
        # Creamos una tabla con los tiempos asi como con las cotas correspondientes
        df_aux = pd.DataFrame(
            np.array([[str(n),t_n,round(t/f[0](n),3),round(t/g[0](n),3),round(t/h[0](n),3)]]),
            columns=['n','t(n)',f[1],g[1],h[1]])
        df_final = pd.concat([df_final,df_aux], ignore_index=True)

    print(df_final)
    print('\n\n')


####################################
# ESTIMACIÓN DE COTAS EJERCICIO(3) #
####################################

# Calculamos las cotas que mejor se ajustan segun el algoritmo

k = 10000

print('Algoritmo Kruskal (complejidad)\n')
medir_tiempos(k,((lambda n: n),     			        't(n)/n'),            # La que más tiende a infinito
                ((lambda n: math.pow(n,2)*math.log(n)), 't(n)/n^2*log(n)'),   # La que más ajusta a una constante
                ((lambda n: n**2.7),					't(n)/n^2.7')) 		  # La más se ajusta a 0




