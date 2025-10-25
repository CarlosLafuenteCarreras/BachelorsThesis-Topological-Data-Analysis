import numpy as np
import matplotlib.pyplot as plt
from ripser import ripser
from persim import plot_diagrams
from persim import bottleneck

def toro(n_puntos=500, ruido=0.2, n_outliers=10):
    R, r = 2, 1
    theta = 2 * np.pi * np.random.rand(n_puntos)
    phi = 2 * np.pi * np.random.rand(n_puntos)
    x = (R + r * np.cos(theta)) * np.cos(phi)
    y = (R + r * np.cos(theta)) * np.sin(phi)
    z = r * np.sin(theta)
    toro = np.vstack([x, y, z]).T
    ruido_gaussiano = np.random.normal(scale=ruido, size=toro.shape)
    toro_ruidoso = toro + ruido_gaussiano
    outliers = np.random.uniform(low=-6, high=6, size=(n_outliers, 3))
    return np.vstack([toro_ruidoso, outliers])






def filtrar_por_impacto_h1_rapido(puntos, epsilon):
    """
    Filtra puntos basándose únicamente en el impacto en H1 (ciclos).
    Elimina el primer punto encontrado en cada pasada que cumpla la condición.
    """
    S = puntos.copy()
    
    while True:
        punto_eliminado_en_esta_pasada = False
        
        D1_actual = ripser(S)['dgms'][1]
        
        for i in range(len(S)):
            S_i = np.delete(S, i, axis=0)
            D1_i =ripser(S_i)['dgms'][1]
            impacto_h1 = bottleneck(D1_actual, D1_i)
            
            if impacto_h1 < epsilon:
                S = S_i
                punto_eliminado_en_esta_pasada = True
                break
        
        if not punto_eliminado_en_esta_pasada:
            break
            
    return S





def comparar_persistencia(puntos1, puntos2, dim):
    dgms1 = ripser(puntos1, maxdim=2)['dgms']
    dgms2 = ripser(puntos2, maxdim=2)['dgms']
    dist = bottleneck(dgms1[dim], dgms2[dim])
    
   # Representacion visual
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
    puntos = toro()
    print(f"Puntos originales: {len(puntos)}")
    
    # Filtramos el toro
    puntos_filtrados = filtrar_por_impacto_h1_rapido(puntos,0.02)
    print(f"Puntos tras filtrado: {len(puntos_filtrados)}")

    # Muestra nubes de puntos 3D
    fig = plt.figure(figsize=(12, 6))
    
    ax1 = fig.add_subplot(121, projection='3d')
    ax1.scatter(puntos[:,0], puntos[:,1], puntos[:,2], s=10)
    ax1.set_title("Conjunto original")
    
    ax2 = fig.add_subplot(122, projection='3d')
    ax2.scatter(puntos_filtrados[:,0], puntos_filtrados[:,1], puntos_filtrados[:,2], s=10, c="#ff7f0e")
    ax2.set_title("Conjunto filtrado")
    
    plt.show()

    # Calculamos diagramas de persistencia
    resultados = ripser(puntos, maxdim=2)
    diagramas = resultados['dgms']

    # Muestra diagramas de persistencia
    plot_diagrams(diagramas, show=True)


    comparar_persistencia(puntos, puntos_filtrados, dim=0)
    comparar_persistencia(puntos, puntos_filtrados, dim=1)
    comparar_persistencia(puntos, puntos_filtrados, dim=2)

if __name__ == "__main__":
    main()