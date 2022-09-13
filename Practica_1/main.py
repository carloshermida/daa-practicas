###############################
# P  R  Á  C  T  I  C  A  (1) #
###############################

import math
import time
import pandas as pd

#########################################
# IMPLEMENTACIÓN ALGORITMOS EJERCICIO(1)#
#########################################

# Implementamos las funciones de fibonaccide forma recursiva, iterativa y binet

def fib_recursive(n):
    if n < 2:
        return n
    else:
        return fib_recursive(n-1)+fib_recursive(n-2)
    
def fib_iterative(n):
    if n == 0:
        return 0
    a = 0
    b = 1
    i = 2
    while i < n:
        aux = a
        a = b
        b = b + aux
        i += 1
    return a + b

def fibBinet(n):
    phi = (1 + math.sqrt(5))/2
    tau = (1 - math.sqrt(5))/2
    return round((math.pow(phi, n) - math.pow(tau,n))/math.sqrt(5))


###################
# FUNCIÓN DE TEST #
###################

#Creamos una función tester par comprobar que los algoritmos creados tengan 
#implementado de forma correcta la funcion de fibonnaci.

def tester(n):
    '''Dado un número (n) establece iteraciones para testear los algoritmos'''
    for i in range(n):
        print('ITERACIÓN: ',i)
        print('TESTER FIBONACCI RECURSIVE: ',fib_recursive(i) )
        print('TESTER FIBONACCI ITERATIVE: ', fib_iterative(i))
        print('TESTER FIBONACCI BINET: ', fibBinet(i))
        print('\n\n\n')
        time.sleep(0.6)
  

####################
# GENERAR SUCESIÓN #
####################

# Generar sucesiones de orden 2( es decir 2^0, 2^1.... ) 

def generar_sucesion(tamano):
    '''Genera una sucesión de orden 2'''
    s = []
    for i in range(1,tamano):
        n = int(math.pow(2,i))
        s.append(n)
    return s #devolvemos sucesion


#######################
# FUNCIONES DE TIEMPO #
#######################

# Funciones que miden el tiempo del sistema en ese momento en nanosegundos.

''' Funciones conversoras de las unidades de tiempo '''
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

#Creamos una funcion para calculas el tiempo de ejcucion de cada algoritmo
def medir_tiempos(sizes,algoritmo,k):
    '''Medición de los tiempos de ejecución del algoritmo con diferen-
    tes tamaños de entrada y k repeticiones del bucle de tiempos.'''
    
    print('(n)\t  T(n)')
    t_n=[]
    for i in sizes:              # Recorre la sucesión de orden 2
        t1 = time_functions[0]() #Medimos la hora del sistema
        algoritmo(i)             #Ejecutamos la función
        t2 = time_functions[0]() #Volvemos a calcular la hora del sistema
        t=(t2-t1)                #Calculamos el tiempo de ejecución
        
        if t<500000:# Fijación del umbral(en nanosegundos)para tiempos pequeños
            t12 = time_functions[0]()#Medimos la hora del sistema
            n = 0
            while n<k:#Hacemos un bucle k veces para hacer la media de tiempos
                algoritmo(i)
                n+=1
            t22 = time_functions[0]()#Calculamos la hora del sistema
            
            t_loop_1 = time_functions[0]()# Medimos la ejecución de bucle
            n = 0
            while n<k:
                n += 1
            t_loop_2 = time_functions[0]()#Hora del sistema al acabar el bucle

            resultado = ((t22-t12) - (t_loop_2-t_loop_1)) / k 
            #Calculamos la media de los tiempos pequeños restandole el tiempo
            #que dura el bucle y dividiendolo entre k.                
            t_total = round(resultado,3)
            t_n.append(t_total)#Añadimos dicho tiempo a la lista de tiempos
            print(str(i),'\t ',str(t_total),'* ns')
            time.sleep(0.5)
        
        else:
            t_n.append(t)#Los tiempos mayores que el umbral se añaden a t_n
            print(str(i),'\t ',str(t),'* ns')  
            time.sleep(0.5)

    print('\n\n')
    return t_n # Se devuelven la lista de los tiempos correspondiente algoritmo


########################
# FUNCIÓN DE ACOTACIÓN #
########################

def acotar(sizes,lista_tn,f,g,h):
    '''Función que dada una lista (sizes) de tamaños y determinados 
    tiempos de ejecución (lista_tn),prueba diferentes cotas (f,g,h)
    para el algoritmo.'''

    cota_sub=[]     # Valores de las cotas subestimadas
    cota_aj=[]      # Valores de las cotas ajustadas
    cota_sobre=[]   # Valores de las cotas sobrestimadas
    
    for i in range(len(sizes)): # Recorro la lista de tamaños 
        n=sizes[i]              # Tamaño de los vectores
        t_n=lista_tn[i]         # Tiempo de ejecución para el tamaño
        
        # ASIGNACIÓN DE COTAS:
        #Calculamos las cotas mas ajustada en cada caso     
        cota_sub.append(round(t_n/f(n),3))#Tiende a infinito
        cota_aj.append(round(t_n/g(n),3)) #Tiende a una constante 
        cota_sobre.append(round(t_n/h(n),3))#Tiende a 0
    
    # IMPRESIÓN DEL DATA FRAME:
    # Imprimimos por pantalla los datos en forma de tabla 
    datos={'n':sizes,'t(n)':lista_tn,'f(n)sub ':cota_sub,
           'g(n)aj':cota_aj,'h(n)sobre':cota_sobre}
    df=pd.DataFrame(datos)
    print(df)
    print('\n\n') 


######################################
# VALIDACIÓN ALGORITMOS EJERCICIO(2) #
######################################

# Introducimos un enunciado para preguntar al usuario si desea testear los 
# algoritmos de fibonacci o no
a=input("Introduce un 1 si desea testear todas los algoritmos de fibonacci: ")
n = 10 # Rango de la sucesión que se exige en el ejercicio que debemos testear
if a=="1": 
# Validación de los algoritmos de la práctica en caso de que se desee
    tester(n)
else:
    print("No se desea testear los algoritmos")
#En el caso que no se desea testear los algoritmos se mostrará este mensaje 


####################################
# MEDICIÓN DE TIEMPOS EJERCICIO(3) #
####################################

# Vector de tamaños de entradas (sucesión de orden 2)
n1 = generar_sucesion(6) #Vector función recursiva
n2 = generar_sucesion(8) #Vector función iterativa y versión binet

# Repeticiones del bucle de medición
k = 100000

# Lista de mediciones de tiempos para cada algoritmo
print('Algoritmo recursivo de Fibonacci  con n=[2, 4, 8, 16, 32]\n')
tn_fibrec = medir_tiempos(n1,fib_recursive,k)
print('Algoritmo iterativo de Fibonacci con n=[2, 4, 8, 16, 32, 64, 128]\n')
tn_fibiter = medir_tiempos(n2,fib_iterative,k)
print('Algoritmo Binet de Fibonacci con n=[2, 4, 8, 16, 32, 64, 128]\n')
tn_fibBin = medir_tiempos(n2,fibBinet,k)


####################################
# ESTIMACIÓN DE COTAS EJERCICIO(4) #
####################################

#Calculamos las cotas que mejor se ajustan segun el algoritmo

print('Algoritmo recursivo de Fibonacci\n')
acotar(n1,tn_fibrec,f = (lambda n: n**2.0), # La que más tiende a infinito
                    g = (lambda n: 1.618**n),#La que más ajusta a una constante
                    h = (lambda n: 2**n)) # La más se ajusta a 0

print('Algoritmo iterativo de Fibonacci\n')
acotar(n2,tn_fibiter,f = (lambda n: 1),# La que más tiende a infinito
                     g = (lambda n: n),# La que más se ajusta a una constante
                     h = (lambda n: n**2))# La que más se ajusta a 0

print('Algoritmo Binet de Fibonacci\n')
acotar(n2,tn_fibBin,f = (lambda n: 1), # No tiene cota subestimada
                    g = (lambda n: 1), #La que más se ajusta a una constante
                    h = (lambda n: n)) # La que más se ajusta a 0

#Este algoritmo no tiene una cota subestimada ya que la ajustada es 1
#Le añadimos la columna aun así para dejar reflejado este hecho
#Calculamos una cota lijeramente subestimada y en la que más se apreciaba era n
#ya que se aprecia claramente la tendencia a disminuir hasta 0
    
    