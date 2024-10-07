import numpy as np
from scipy import stats

# Generar 100 números aleatorios entre 0 y 1 (distribución uniforme)
datos = np.random.uniform(0, 1, 100)

# Realizar la prueba de Kolmogorov-Smirnov
k, p = stats.kstest(datos, 'uniform')

# Imprimir los resultados
print("Estadístico de prueba de Kolmogorov-Smirnov:", k)
print("p-valor:", p)

# Interpretar los resultados
alpha = 0.05  # Nivel de significancia
if p > alpha:
    print("Los datos no rechazan la hipótesis nula de que provienen de una distribución uniforme.")
else:
    print("Los datos rechazan la hipótesis nula de que provienen de una distribución uniforme.")