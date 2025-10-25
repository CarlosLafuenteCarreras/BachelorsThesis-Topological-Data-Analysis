import numpy as np
import matplotlib.pyplot as plt
from ripser import ripser
from persim import plot_diagrams
from sklearn.neighbors import NearestNeighbors
from persim import bottleneck

def generar_toro(n_puntos=500, ruido=0.2, n_outliers=10):
    R, r = 2, 1
    theta = 2 * np.pi * np.random.rand(n_puntos)
    phi = 2 * np.pi * np.random.rand(n_puntos)
    x = (R + r * np.cos(theta)) * np.cos(phi)
    y = (R + r * np.cos(theta)) * np.sin(phi)
    z = r * np.sin(theta)
    toro = np.vstack([x, y, z]).T
    ruido_gaussiano = np.random.normal(scale=ruido, size=toro.shape)
    toro_ruidoso = toro + ruido_gaussiano
    outliers = np.random.uniform(low=-10, high=10, size=(n_outliers, 3))
    return np.vstack([toro_ruidoso, outliers])




def plot_barcode_manual(diagramas):
    plt.figure(figsize=(10, 6))
    colores = ['b', 'g', 'r']  # Colores para dimensiones 0,1,2
    y_pos = 0
    for dim, dgm in enumerate(diagramas):
        for interval in dgm:
            birth, death = interval
            if death == float('inf'):
                death = birth + 3  # Para visualizar las barras infinitas
            if death - birth > 0.3:  # solo dibuja barras suficientemente largas
                 plt.hlines(y_pos, birth, death, colors=colores[dim % len(colores)], linewidth=2)
                 y_pos += 1
            plt.hlines(y_pos, birth, death, colors=colores[dim % len(colores)], linewidth=2)
            y_pos += 1
        y_pos += 2  # Espacio entre dimensiones
    plt.xlabel('Parámetro de filtración')
    plt.ylabel('Intervalos de persistencia')
    plt.title('Barcode manual de persistencia')
    plt.show()



def comparar_persistencia(puntos1, puntos2, dim):
    dgms1 = ripser(puntos1, maxdim=2)['dgms']
    dgms2 = ripser(puntos2, maxdim=2)['dgms']
    dist = bottleneck(dgms1[dim], dgms2[dim])
    
    # Visualización
    plt.figure(figsize=(10,4))
    plt.subplot(1,2,1)
    plt.title('Diagrama persistencia original')
    plt.scatter(dgms1[dim][:,0], dgms1[dim][:,1])
    plt.plot([0, max(dgms1[dim][:,1])], [0, max(dgms1[dim][:,1])], 'k--')
    plt.subplot(1,2,2)
    plt.title('Diagrama persistencia filtrado')
    plt.scatter(dgms2[dim][:,0], dgms2[dim][:,1])
    plt.plot([0, max(dgms2[dim][:,1])], [0, max(dgms2[dim][:,1])], 'k--')
    plt.show()
    
    print(f"Distancia bottleneck dimensión {dim}: {dist:.4f}")


def main():
    puntos = generar_toro()
    print(f"Puntos originales: {len(puntos)}")
    S=ripser(puntos, maxdim=2)
    H0=S['dgms'][0]
    H1=S['dgms'][1]
    H2=S['dgms'][2]
    plot_diagrams(H0, show=True)
    plot_diagrams(H1, show=True)
    plot_diagrams(H2, show=True)
    # Filtrar por densidad


    # Mostrar nubes de puntos 3D
    fig = plt.figure(figsize=(10, 6))
    
    ax1 = fig.add_subplot(111, projection='3d')
    ax1.scatter(puntos[:,0], puntos[:,1], puntos[:,2], s=10)
    ax1.set_title("Conjunto original")
    
    
    plt.show()

    # # Calcular diagramas de persistencia
    # resultados = ripser(puntos, maxdim=2)
    # diagramas = resultados['dgms']

    # # Mostrar diagramas de persistencia
    # plot_diagrams(diagramas, show=True)

    # plot_barcode_manual(diagramas)

if __name__ == "__main__":
    main()

