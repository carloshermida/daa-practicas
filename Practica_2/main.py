###############################
# P  R  Á  C  T  I  C  A  (2) #
###############################

# Patricia Da Concepción Sarrate
# Alba González Mallo
# Carlos Hermida Mayán

import time
import math
import pandas as pd
import numpy as np

##########################################
# IMPLEMENTACIÓN ALGORITMOS EJERCICIO(1) #
##########################################

# Creamos la funcion de insertionSort
# Esta funcion es reliza una ordenación de una lista de elementos introducida 
# comparando el elemento de la lista con todos los anteriores intercambiando los
# valores si es necesario en función de si es ascendiente o descendiente.

def insertionSort(v):
    n = len(v)
    for i in range(1,n):
        x = v[i]
        j = i-1
        while j >= 0 and v[j] > x:
            v[j+1] = v[j]
            j = j-1
            v[j+1] = x
            
# Creamos la funcion de bubbleSort  
# Esta funcion se realiza una ordenacion de una lista de elementos introducida
# comparando los elementos de la lista en parejas y intercambiando sus elementos
# si es necesario en funcion si es ascendiente o descendiente.
     
def bubbleSort(v):
    n = len(v)
    for i in range(1,n):
        for j in range(n-i):
                if v[j+1] < v[j]:
                    v[j],v[j+1] = v[j+1],v[j]


###################
# FUNCIÓN DE TEST #
###################

# Creamos una función test en la cual comprobamos que las listas introducidas se
# ordenan correctamente mediante una aserción y imprimiendolas por pantalla.

def test(function, arrays, ordered_arrays):
    for i in range(len(arrays)):
        print ("Input: {}".format(arrays[i]))
        function(arrays[i])
        assert(arrays[i] == ordered_arrays[i])
        print("Output: {} \n".format(arrays[i]))


######################################
# VALIDACIÓN ALGORITMOS EJERCICIO(2) #
######################################

# Creamos la validación del algortimo tanto de una lista predeterminada por
# nosotros como de un lista de vectores aleatorios

np.random.seed(1)

sizes =[5,10,15] # Dimensiones de los vectores aleatorios

for function in [insertionSort, bubbleSort]: # Comprobar las dos funciones de ordenación
    # La lista de los arrays que queremos ordenar   
    lista = [ [-9,4,13,-1,-5], [6,-3,-15,5,4,5,2], [13,4], [9],
              [7,6,6,5,4,3,2,1], [1,2,3,4,4,5,6,7] ]
    # La lista de los arrays ordenados
    lista_ordenada = [ [-9,-5,-1,4,13], [-15,-3,2,4,5,5,6], [4,13],
                       [9], [1,2,3,4,5,6,6,7], [1,2,3,4,4,5,6,7] ]                    
    print("SECUENCIA CONOCIDA ({})\n".format(function.__name__))
    # Comprobando que la ordenación es correcta
    test(function, lista, lista_ordenada)
    # La lista de arrays aleatorios
    print("SECUENCIA ALEATORIA ({})\n".format(function.__name__))
    for size in sizes:
        lista_aleatoria = list(np.random.randint(-10, 10, size))
        # Utilizamos la función sorted de python en este caso para comprobar la 
        # ordenación correcta
        test(function, [lista_aleatoria], [sorted(lista_aleatoria)])


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


################################
# FUNCIÓN GENERADORA DE LISTAS #
################################

# Función que genera un conjunto de vectores ordenados de diferentes formas:
# ascendentes,descendentes o aleatorios.

def array_generator(way, length):
        """Genera vectores aleatorios ordenados de diferentes formas"""

        if way == 'aleatorio':
            return list(np.random.randint(-10, 10,length))
        elif way == 'ascendente':
            return sorted(list(np.random.randint(-10, 10,length)))
        elif way == 'descendente':
            return sorted(list(np.random.randint(-10, 10,length)),reverse=True)


####################
# GENERAR SUCESIÓN #
####################

# Generar sucesiones de orden 2 ( es decir 2^1, 2^2.... ) 

def generar_sucesion(tamano):
    '''Genera una sucesión de orden 2'''
    s = []
    for i in range(1,tamano):
        n = int(math.pow(2,i))
        s.append(n)
    return s


#######################
# FUNCIÓN DE MEDICIÓN #
#######################

# Creamos una funcion para calcular el tiempo de ejecucion de cada algoritmo

def medir_tiempos(algoritmo, way,k,f,fs,g,gs,h,hs):
    '''Medición de los tiempos de ejecución del algoritmo con diferentes
    tamaños de entrada, diferentes ordenaciones y k repeticiones
    del bucle de tiempos.'''

    df_final = pd.DataFrame(columns=['n','t(n)',fs,gs,hs])
    n_values = generar_sucesion(10)
    for n in n_values:                      # Recorre la sucesión de orden 2
        estimacion = False                  # Inicializamos el booleano estimación
        v = array_generator(way,n)
        t1 = time_functions[0]()            # Medimos la hora del sistema
        algoritmo(v)                        # Ejecutamos la función
        t2 = time_functions[0]()            # Volvemos a calcular la hora del sistema
        t = (t2-t1)                         # Calculamos el tiempo de ejecución
        if t<500000:                        # Fijación del umbral(en nanosegundos)para tiempos pequeños
            estimacion = True               # Al ejecutar el algortimo k veces, se trata de una estimación
            t12 = time_functions[0]()       # Medimos la hora del sistema
            i = 0
            while i<k:                      # Hacemos un bucle k veces para hacer la media de tiempos
                v = array_generator(way,n)
                algoritmo(v)
                i+=1
            t22 = time_functions[0]()       # Calculamos la hora del sistema
            t_loop_1 = time_functions[0]()  # Medimos la ejecución de bucle
            i = 0
            while i<k:
                v = array_generator(way,n)
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
            np.array([[str(n),t_n,round(t/f(n),3),round(t/g(n),3),round(t/h(n),3)]]),
            columns=['n','t(n)',fs,gs,hs])
        df_final = pd.concat([df_final,df_aux], ignore_index=True)
    print(df_final)
    print('\n\n')


######################################
# ESTIMACIÓN DE COTAS EJERCICIO(3-4) #
######################################

# Calculamos las cotas que mejor se ajustan segun el algoritmo

k = 10000

print('Algoritmo insertionSort [aleatorio]\n')
medir_tiempos(insertionSort,'aleatorio',k,(lambda n: 1),     't(n)/1',     # La que más tiende a infinito
                                          (lambda n: n**2.), 't(n)/n^2',   # La que más ajusta a una constante
                                          (lambda n: n**2.7),'t(n)/n^2.7') # La más se ajusta a 0

print('Algoritmo BubbleSort [aleatorio]\n')
medir_tiempos(bubbleSort,'aleatorio',k,(lambda n: 1),     't(n)/1',     # La que más tiende a infinito
                                       (lambda n: n**2),  't(n)/n^2',   # La que más ajusta a una constante
                                       (lambda n: n**2.7),'t(n)/n^2.7') # La más se ajusta a 0

print('Algoritmo insertionSort [ascendente]\n')
medir_tiempos(insertionSort,'ascendente',k,(lambda n: 1),   't(n)/1',   # La que más tiende a infinito
                                           (lambda n: n),   't(n)/n',   # La que más ajusta a una constante
                                           (lambda n: n**2),'t(n)/n^2') # La más se ajusta a 0

print('Algoritmo bubbleSort [ascendente]\n')
medir_tiempos(bubbleSort,'ascendente',k,(lambda n: 1),     't(n)/1',     # La que más tiende a infinito
                                        (lambda n: n**2),  't(n)/n^2',   # La que más se ajusta a una constante
                                        (lambda n: n**2.7),'t(n)/n^2.7') # La que más se ajusta a 0

print('Algoritmo insertionSort [descendente]\n')
medir_tiempos(insertionSort,'descendente',k,(lambda n: 1),    't(n)/1',      # La que más tiende a infinito
                                            (lambda n: n**2), 't(n)/n^2',    # La que más ajusta a una constante
                                            (lambda n: n**2.8),'t(n)/n^2.8') # La más se ajusta a 0

print('Algoritmo bubbleSort [descendente]\n')
medir_tiempos(bubbleSort,'descendente',k,(lambda n: 1),     't(n)/1',     # La que más tiende a infinito
                                         (lambda n: n**2),  't(n)/n^2',   # La que más se ajusta a una constante
                                         (lambda n: n**2.8),'t(n)/n^2.8') # La que más se ajusta a 0
    
    

    
