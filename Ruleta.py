#LIBRERIAS USADAS
import matplotlib.pyplot as plt
import numpy as np

#FUNCIONES DADA UNA LISTA CON NUMEROS PSEUDOALEATORIOS DEL 0 AL 36 COMO PARAMETRO NOS DEVUELVE SU ESTADISTICO
def relativefrequency(numero,data):
    count = 0
    rf = []
    for x in range(len(data)):
        if data[x] == numero:
            count += 1
        a = count / (x + 1)
        rf.append(a)
    return rf


def promedio(data):
    avg = []
    sum = 0
    for x in range(len(data)):
        sum = sum + data[x]
        aux = sum / (x + 1)
        avg.append(aux)
    return avg


def varianza(data):
    varlist = []
    var = 0.0
    auxlist = []
    for x in range(len(data)):
        auxlist.append(data[x])
        v = np.var(auxlist)
        varlist.append(v)
    return varlist


def desviacion(data):
    auxlist = []
    desvlist = []
    for x in range(len(data)):
        auxlist.append(data[x])
        v = np.std(auxlist)
        desvlist.append(v)
    return desvlist

#FUNCION QUE PLOTEA LOS PARAMETROS ESTADISTICOS DE UNA DISTRIBUCION
def ploteograficas(numero,tiradas):
    data = np.random.randint(0, 37, tiradas)

    plt.plot(relativefrequency(numero,data), 'g', label="Frecuencia relativa del número X respecto a n")
    plt.hlines((1/36), 0, tiradas, label="Frecuencia relativa esperada del número X")
    plt.xlabel("Número de tiradas")
    plt.ylabel("Frecuencia relativa")
    plt.title("Gráfica de frecuencias relativas")
    plt.legend()
    plt.show()

    plt.plot(promedio(data), 'b', label="Valor promedio de las tiradas con respecto a n")
    plt.hlines((666/36), 0, tiradas, label="Valor promedio esperado")
    plt.xlabel("Número de tiradas")
    plt.ylabel("Promedio")
    plt.title("Gráfica de promedios")
    plt.legend()
    plt.show()

    plt.plot(varianza(data), 'y', label="Valor de la varianza del número X con respecto a n")
    plt.hlines((1296/12), 0, tiradas, label="Valor esperado de la varianza")
    plt.xlabel("Número de tiradas")
    plt.ylabel("Varianza")
    plt.title("Gráfica de las varianzas")
    plt.legend(loc="lower right")
    plt.show()

    plt.plot(desviacion(data), 'm', label="Valor del desvío del número X con respecto a n")
    plt.hlines(np.sqrt((1296/12)), 0, tiradas, label="Valor del desvío esperado")
    plt.xlabel("Número de tiradas")
    plt.ylabel("Desvío")
    plt.title("Gráfica de los desvíos")
    plt.legend()
    plt.show()

#FUNCION QUE PLOTEA EL PROMEDIO DE LOS PARAMETROS ESTADISTICOS DE 10 DISTRIBUCIONES EN UNA GRAFICA
def plotpromedios(numero, tiradas):
    avgfrec = []
    avgavg = []
    avgdesv = []
    avgvar = []
    for x in range(10):
        np.random.seed()
        data = np.random.randint(0,37,tiradas)
        avgfrec.append(relativefrequency(numero, data))
        avgavg.append(promedio(data))
        avgdesv.append(desviacion(data))
        avgvar.append(varianza(data))

    plt.plot(np.mean(avgavg,axis=-1), 'b', label="Valor promedio de los promedios de n tiradas")
    plt.xlabel("Número de tiradas")
    plt.ylabel("Promedio")
    plt.hlines((666 / 36), 0, 10, label="Valor promedio esperado")
    plt.title("Gráfica promedio de promedios de n distribuciones")
    plt.legend()
    plt.show()

    plt.plot(np.mean(avgfrec, axis=-1), 'g', label="Valor promedio de las frecuencias relativas de n tiradas ")
    plt.xlabel("Número de tiradas")
    plt.ylabel("Frecuencia relativa")
    plt.hlines((1 / 36), 0, 10, label="Frecuencia relativa esperada del número X")
    plt.title("Gráfica promedio de frecuencias relativas de n distribuciones")
    plt.legend(loc="lower right")
    plt.show()

    plt.plot(np.mean(avgdesv, axis=-1), 'm', label="Valor promedio de los desvios de n tiradas")
    plt.xlabel("Número de tiradas")
    plt.ylabel("Desvio")
    plt.title("Gráfica promedio de los devíos de n distribuciones")
    plt.hlines(np.sqrt((1296 / 12)), 0, 10, label="Valor del desvío esperado")
    plt.legend()
    plt.show()

    plt.plot(np.mean(avgvar, axis=-1), 'y', label="Valor promedio de las varianzas de n tiradas")
    plt.xlabel("Número de tiradas")
    plt.ylabel("Varianza")
    plt.hlines((1296 / 12), 0, 10)
    plt.title("Gráfica promedio de las varianzas de n distribuciones")
    plt.legend()
    plt.show()

#FUNCION QUE PLOTEA LOS PARAMETROS ESTADISTICOS DE 10 DISTRIBUCIONES EN UNA MISMA GRAFICA
def ploteotog(numero,tiradas):
    for x in range(10):
        frec = []
        np.random.seed()
        data = np.random.randint(0, 37, tiradas)
        frec = relativefrequency(numero,data)
        plt.plot(frec)
    plt.xlabel("Número de tiradas")
    plt.ylabel("Frecuencia relativa")
    plt.hlines((1 / 36), 0, tiradas)
    plt.title("Gráfica de frecuencias relativas")
    plt.show()
    for x in range(10):
        desv = []
        np.random.seed()
        data = np.random.randint(0, 37, tiradas)
        desv = desviacion(data)
        plt.plot(desv)
    plt.xlabel("Número de tiradas")
    plt.ylabel("Desvio")
    plt.hlines(np.sqrt((1296 / 12)), 0, tiradas)
    plt.title("Gráfica de desvíos")
    plt.show()
    for x in range(10):
        var = []
        np.random.seed()
        data = np.random.randint(0, 37, tiradas)
        var = varianza(data)
        plt.plot(var)
    plt.xlabel("Número de tiradas")
    plt.ylabel("Varianza")
    plt.hlines((1296 / 12), 0, tiradas)
    plt.title("Gráfica de varianzas")
    plt.show()
    for x in range(10):
        prom = []
        np.random.seed()
        data = np.random.randint(0, 37, tiradas)
        prom = promedio(data)
        plt.plot(prom)
    plt.xlabel("Número de tiradas")
    plt.ylabel("Promedio")
    plt.hlines((666 / 36), 0, tiradas)
    plt.title("Gráfica de promedios")
    plt.show()

# # MAIN SECTION
# numero = int(input("Ingrese un numero"))
# tiradas = int(input("Ingrese tiradas"))
# plotpromedios(numero, tiradas)
# ploteograficas(numero, tiradas)
# ploteotog(numero, tiradas)