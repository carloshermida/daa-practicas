###############################
# P  R  Á  C  T  I  C  A  (4) #
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

#Implementamos los algoritmos que se estipulan en la práctica

def isMixtureDP(A,B,C):
    n,m,s = len(A),len(B),len(C)
    if n+m != s:
        return False
    t = np.zeros((n+1,m+1),dtype=bool)
    t[0,0] = True
    for i in range(0,n+1):
        for j in range(0,m+1):    
            t[i,j] = t[max(0,i-1),j] or t[i, max(0,j-1)]
            if t[i,j] and (i<n or j<m):
                k = i+j
                t[i,j] = False
                if i<n:
                    t[i,j] = t[i,j] or (A[i] == C[k])
                if j<m:
                    t[i,j] = t[i,j] or (B[j] == C[k])
    return t[n,m]


#En este algoritmo debemos realizar algunas modificaciones con respecto a el pseudocodigo presentado.
#Debido a que trabajamos con conjuntos se debe realizar la union de los mismos
#Esto de debería hacer con set.union pero al calcular las diferentes cotas pero lo debemos realizar al final mediante 
#un add para que este algoritmo funcione correctamente.

def isMixtureCX(A,B,C):
    n,m,s = len(A),len(B),len(C)
    if n+m != s:
        return False
    Known = set((0,0))#conjunto
    Trial = [(0,0)]#lista
    while len(Trial) > 0:
        i,j = Trial.pop()
        k = i+j
        if k>=s:
            return True 
        if (i<n and A[i]==C[k] and (i+1,j) not in Known):
            Trial.append((i+1,j))
            Known.add((i+1,j))
        if( j<m and B[j] == C[k] and (i,j+1) not in Known):
            Trial.append((i,j+1))
            Known.add((i,j+1))
    return False


##########################################
# VALIDACIÓN DEL ALGORITMO EJERCICIO(2)  #
##########################################

# Realizamos una función test para comprobar el correcto funcionamiento de entrada predeterminada de los algoritmos
def test(case, valid):
    
    word_1 = case[0]
    word_2 = case[1]
    mixes = case[2]
    for i in mixes:
        assert(isMixtureDP(word_1,word_2,i) == valid)
        assert(isMixtureCX(word_1,word_2,i) == valid)
    return 'OK'
#Pasamos la entrada predeterminada de los enunciados del ejercicio 2 tanto los resultados validos como los no válidos

word_1 = 'Hello'
word_2 = 'World'
valid_words = ('HelloWorld', 'WorldHello', 'HWorellldo', 'WorHellold', 'HWeolrllod')
not_valid_words= ('dlroWolleH', 'oHelloWrld', 'HelloWorlds', 'HeloWorld', 'HelloWooorld')

valid_case = (word_1,word_2,valid_words)
not_valid_case = (word_1,word_2,not_valid_words)

#Imprimimos por pantalla los casos válidos y los no válidos
 
print('Casos válidos de ejemplo: ',valid_case)
print('Casos NO válidos de ejemplo: ',not_valid_case)

print('\nComprobación implementación: ')

#Realizamos la comprobación de mediante la función test de los algoritmos 
 
print('Casos válidos: ',test(valid_case, valid = True))
print('Casos NO válidos: ',test(not_valid_case, valid = False))
print('\n')


###############################################
# FUNCIÓN GENERADORA DE PALABRAS EJERCICIO(3) #
###############################################

#Creamos una funcion la cual devuelve una lista de números de 0 a 1

def create_word_binary(n,alphabet=(0,1)):
    a = np.random.randint(low=0, high=len(alphabet), size=(n,))
    word = np.array(alphabet)[a].tolist()
    return word
 
#Creamos una funcion la cual devuelve todos los caracteres del codigo ascii 

def create_word_ascii(n):
    alphabet = range(0, 256)
    a = np.random.randint(low=0, high=len(alphabet), size=(n,))
    word = np.array(alphabet)[a].tolist()
    for i in range(len(word)):
        element= chr(word[i])
        if element == '\x00':
            word[i] = ''
        else:
            word[i] = element
    return word

#Creamos una funcion la cual devuelve una longuitud de vocabulario de igual tamaño entre A y B 

def create_word_same_length(n):
    alphabet = range(0, n)
    a = np.random.randint(low=0, high=len(alphabet), size=(n,))
    word = np.array(alphabet)[a].tolist()
    for i in range(len(word)):
        element = chr(word[i])
        if element == '\x00':
            word[i] = ''
        else:
            word[i] = element
    return word

# Funcion que devuelve la union de los dos elementos mezclados.

def mix_words(a, b, valid=True): 
    new_word = []
    a_array = np.array(a) 
    b_array = np.array(b) 
    if not valid:
        np.random.shuffle(a_array)
        np.random.shuffle(b_array)
    a_index = 0
    b_index = 0
    while len(new_word) < len(a) + len(b):
        p = np.random.randint(2)
        if (p and a_index < len(a_array)) or b_index >= len(b_array):
            new_word.append(a_array[a_index])
            a_index += 1 
        else:
            new_word.append(b_array[b_index])
            b_index += 1 
    return new_word

#################
# GENERAR CASOS #
#################

#Esta función genera los diferentes casos segun las funciones anteriores de la mezcla de palabras (3 casos posibles)
#Segun el enunciado de este ejercicio los escenarios posibles son :un algoritmo en binario, caracteres del código asciii y
#misma longitud del vocabulario-palabra.

def case_generator(scenary,n):

    word_1 = scenary(n)
    word_2 = scenary(n)
    mix = mix_words(word_1,word_2)

    return (word_1, word_2, mix)

####################
# GENERAR SUCESIÓN #
####################

# Generar sucesiones para los algoritmos que se nos piden en el ejercicio: [20, 40, 80, 160, 320, 640, 1280, 2560]

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

def medir_tiempos(algoritmo,scenary,k,f,g,h):
    '''Medición de los tiempos de ejecución del algoritmo con diferentes
    tamaños de entrada, k repeticiones del bucle de tiempos.'''

    df_final = pd.DataFrame(columns=['n','t(n)',f[1],g[1],h[1]])
    n_values = generar_sucesion()
    for n in n_values:                      # Recorre la sucesión de orden correspondiente
        estimacion = False                  # Inicializamos el booleano estimación
        case = case_generator(scenary,n)            
        t1 = time_functions[0]()            # Medimos la hora del sistema
        algoritmo(case[0],case[1],case[2])  # Ejecutamos la función
        t2 = time_functions[0]()            # Volvemos a calcular la hora del sistema
        t = (t2-t1)                         # Calculamos el tiempo de ejecución
        if t<500000:                        # Fijación del umbral(en nanosegundos)para tiempos pequeños
            estimacion = True               # Al ejecutar el algortimo k veces, se trata de una estimación
            t12 = time_functions[0]()       # Medimos la hora del sistema
            i = 0
            while i<k:                      # Hacemos un bucle k veces para hacer la media de tiempos
                algoritmo(case[0],case[1],case[2])
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

print('Algoritmo DP (binario)\n')
medir_tiempos(isMixtureDP, create_word_binary,k,
             ((lambda n: n),     			         't(n)/n'),            # La que más tiende a infinito
             ((lambda n: n**2),                      't(n)/n^2'),          # La que más ajusta a una constante
             ((lambda n: n**2.7),				     't(n)/n^2.7')) 	   # La más se ajusta a 0

print('Algoritmo DP (ascii)\n')
medir_tiempos(isMixtureDP, create_word_ascii,k,
             ((lambda n: n),                         't(n)/n'),            # La que más tiende a infinito
             ((lambda n: n**2),                       't(n)/n^2'),          # La que más ajusta a una constante
             ((lambda n: n**2.7),                    't(n)/n^2.7'))        # La más se ajusta a 0

print('Algoritmo DP (misma longitud vocabulario-palabra)\n')
medir_tiempos(isMixtureDP, create_word_same_length,k,
             ((lambda n: n),                         't(n)/n'),            # La que más tiende a infinito
             ((lambda n: n**2),                      't(n)/n^2'),          # La que más ajusta a una constante
             ((lambda n: n**2.7),                    't(n)/n^2.7'))        # La más se ajusta a 0

print('Algoritmo CX (binario)\n')
medir_tiempos(isMixtureCX, create_word_binary,k,
             ((lambda n: math.log(n)),               't(n)/log(n)'),        # La que más tiende a infinito
             ((lambda n: n),                         't(n)/n'),             # La que más ajusta a una constante
             ((lambda n: n**2),                      't(n)/n^2'))           #La más se ajusta a 0

print('Algoritmo CX (ascii)\n')
medir_tiempos(isMixtureCX, create_word_ascii,k,
             ((lambda n: math.log(n)),                't(n)/log(n)'),     # La que más tiende a infinito
             ((lambda n: n),                          't(n)/n'),          # La que más ajusta a una constante
             ((lambda n: n**2),                       't(n)/n^2'))        # La más se ajusta a 0

print('Algoritmo CX (misma longitud vocabulario-palabra)\n')
medir_tiempos(isMixtureCX, create_word_same_length,k,
             ((lambda n: math.log(n)),                     't(n)/log(n)'),   # La que más tiende a infinito
             ((lambda n: n),                               't(n)/n'),        # La que más ajusta a una constante
             ((lambda n: n**2),                            't(n)/n^2'))      # La más se ajusta a 0




