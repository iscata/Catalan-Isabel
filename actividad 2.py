import numpy as np
import matplotlib.pyplot as plt 

#Creación de datos con Numpy a través de random. "Wes Mckinney,'Python for data analysis'", p. 103.
X = np.random.uniform(0,3,1000)

Y = 5 + 2 * X + np.random.uniform (2,4,1000)

#Creación de gráfico de dispersión. https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter
plt.figure(figsize= (8, 6))
plt.scatter (X,Y, color="y", s=50, alpha= 0.7, edgecolors="g")
plt.title("Gráfico de dispersión")
plt.xlabel ("Valor dependiente(X)")
plt.ylabel ("Valor independiente(Y)")


#Función para visualizar datos
def datos_simulados (X,Y, num_datos=1000, guardar = False, nombre="imagen_grafico.png"):
    if guardar:
        plt.savefig(nombre)
        print("Imagen guardada como:", nombre)
    else:
        plt.show()

#num_datos
    X = X[num_datos]
    Y = Y[num_datos]

#ejemplo de input de función
datos_simulados(X, Y, num_datos = 1000, guardar=False)

