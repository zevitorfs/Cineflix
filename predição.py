import numpy as np
from scipy.spatial import distance

# Função diff para calcular a diferença entre os valores preditos ou características
def diff(attribute, instance1, instance2):
    return abs(attribute[instance1] - attribute[instance2])

# Função para calcular a distância euclidiana entre duas instâncias
def calcular_distancia(instancia1, instancia2):
    return distance.euclidean(instancia1, instancia2)

# Função RReliefF
def RReliefF(X, y, k):
    """
    Parâmetros:
    - X: Matriz de características (instâncias x características)
    - y: Vetor de valores preditos (variável dependente)
    - k: Número de vizinhos mais próximos a serem considerados

    Retorna:
    - W: Vetor de relevância para cada característica
    """
    m, f = X.shape  # m = número de instâncias, f = número de características
    N_AC = 0  # Inicializa o contador N_AC
    N_AF = np.zeros(f)  # Inicializa N_AF para cada característica F
    N_AC_AF = np.zeros(f)  # Inicializa N_AC&AF para cada característica F
    W = np.zeros(f)  # Inicializa vetor de relevância W para cada característica

    # Loop sobre todas as instâncias
    for i in range(m):
        # Seleciona uma instância aleatória R_i
        R_i = X[i]

        # Calcula as distâncias para todas as outras instâncias e ordena os vizinhos
        distancias = [calcular_distancia(R_i, X[j]) for j in range(m)]
        vizinhos_mais_proximos = np.argsort(distancias)[1:k+1]  # Seleciona os k vizinhos mais próximos

        # Loop sobre os vizinhos mais próximos
        for j in vizinhos_mais_proximos:
            I_j = X[j]  # Vizinhos mais próximos

            # Atualiza N_AC com base na diferença entre os valores preditos
            N_AC += diff(y, i, j) * distancias[j]

            # Loop sobre todas as características
            for F in range(f):
                # Atualiza N_AF para a característica F
                N_AF[F] += diff(X[:, F], i, j) * distancias[j]
                
                # Atualiza N_AC&AF para a característica F (correlação entre a diferença de predição e a característica)
                N_AC_AF[F] += diff(y, i, j) * diff(X[:, F], i, j) * distancias[j]

    # Calcula o vetor de relevância W para cada característica
    for F in range(f):
        if N_AC != 0 and (m - N_AC) != 0:
            W[F] = (N_AC_AF[F] / N_AC) - ((N_AF[F] - N_AC_AF[F]) / (m - N_AC))
        else:
            W[F] = 0

    return W

# Exemplo de uso:
# Suponha que temos 4 instâncias e 3 características, com valores preditos y
X = np.array([[1.2, 2.3, 3.1],
              [1.8, 2.0, 2.9],
              [0.9, 2.7, 3.3],
              [1.1, 2.5, 3.0]])

y = np.array([2.1, 1.9, 2.4, 2.2])  # Valores preditos

# Rodar o algoritmo RReliefF com k = 2 vizinhos mais próximos
W = RReliefF(X, y, k=2)

print("Relevância das características: ", W)