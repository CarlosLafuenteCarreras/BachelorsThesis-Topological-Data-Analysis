import numpy as np
import matplotlib.pyplot as plt
from ripser import ripser
from persim import plot_diagrams
from sklearn.neighbors import NearestNeighbors
from persim import bottleneck

def generar_toro(n_puntos=500, ruido=0.02, n_outliers=10):
    R, r = 2, 1
    theta = 2 * np.pi * np.random.rand(n_puntos)
    phi = 2 * np.pi * np.random.rand(n_puntos)
    x = (R + r * np.cos(theta)) * np.cos(phi)
    y = (R + r * np.cos(theta)) * np.sin(phi)
    z = r * np.sin(theta)
    toro = np.vstack([x, y, z]).T
    ruido_gaussiano = np.random.normal(scale=ruido, size=toro.shape)
    toro_ruidoso = toro + ruido_gaussiano
    outliers = np.random.uniform(low=-4, high=4, size=(n_outliers, 3))
    return np.vstack([toro_ruidoso, outliers])


def filtrar_por_impacto_topologico(puntos, epsilon, max_iter=5):
    S = puntos.copy()
    for iter in range(max_iter):
        D = ripser(S, maxdim=2)['dgms'][2]  # Calcula hasta la dimensión 2
        eliminar = []
        for i in range(len(S)):
            S_i = np.delete(S, i, axis=0)
            D_i = ripser(S_i, maxdim=2)['dgms'][2]  # Calcula hasta la dimensión 2 también
            if len(D) > 2 and len(D_i) > 2:  # Asegura que hay diagramas de persistencia en dim 2
                d = bottleneck(D, D_i)
                if d < epsilon:
                    eliminar.append(i)
        if not eliminar:
            break
        S = np.delete(S, eliminar, axis=0)
    return S

def comparar_persistencia(puntos1, puntos2, dim):
    dgms1 = ripser(puntos1, maxdim=2)['dgms']
    dgms2 = ripser(puntos2, maxdim=2)['dgms']
    
    if len(dgms1) > dim and len(dgms2) > dim:
        dist = bottleneck(dgms1[dim], dgms2[dim])
    
        # Verificar si los diagramas no están vacíos
        if len(dgms1[dim]) > 0 and len(dgms2[dim]) > 0:
            # Visualización
            plt.figure(figsize=(10,4))
            plt.subplot(1,2,1)
            plt.title(f'Diagrama persistencia original (dim {dim})')
            plt.scatter(dgms1[dim][:,0], dgms1[dim][:,1])
            plt.plot([0, max(dgms1[dim][:,1])], [0, max(dgms1[dim][:,1])], 'k--')
            plt.subplot(1,2,2)
            plt.title(f'Diagrama persistencia filtrado (dim {dim})')
            plt.scatter(dgms2[dim][:,0], dgms2[dim][:,1])
            plt.plot([0, max(dgms2[dim][:,1])], [0, max(dgms2[dim][:,1])], 'k--')
            plt.show()
        
            print(f"Distancia bottleneck dimensión {dim}: {dist:.4f}")
        else:
            print(f"No hay elementos en el diagrama de persistencia de dimensión {dim}.")
    else:
        print(f"No se pudo calcular el diagrama de persistencia para la dimensión {dim}")

def main():
    puntos = generar_toro()
    print(f"Puntos originales: {len(puntos)}")
    
    # Filtrar por densidad
    puntos_filtrados = filtrar_por_impacto_topologico(puntos,0.0008,5)
    print(f"Puntos tras filtrado: {len(puntos_filtrados)}")

    # Mostrar nubes de puntos 3D
    fig = plt.figure(figsize=(12, 6))
    
    ax1 = fig.add_subplot(121, projection='3d')
    ax1.scatter(puntos[:,0], puntos[:,1], puntos[:,2], s=10, )
    ax1.set_title("Conjunto original")
    
    ax2 = fig.add_subplot(122, projection='3d')
    ax2.scatter(puntos_filtrados[:,0], puntos_filtrados[:,1], puntos_filtrados[:,2], s=10, c="#ff7f0e")
    ax2.set_title("Conjunto filtrado")
    
    plt.show()

    # Calcular diagramas de persistencia
    resultados = ripser(puntos, maxdim=2)
    diagramas = resultados['dgms']

    # Mostrar diagramas de persistencia
    plot_diagrams(diagramas, show=True)
    comparar_persistencia(puntos, puntos_filtrados, dim=0) 
    comparar_persistencia(puntos, puntos_filtrados, dim=1) 
    comparar_persistencia(puntos, puntos_filtrados, dim=2)  # Aquí comparamos el grado 2

if __name__ == "__main__":
    main()



    #prueba a usar la metrica de gromov-haussdorf!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!