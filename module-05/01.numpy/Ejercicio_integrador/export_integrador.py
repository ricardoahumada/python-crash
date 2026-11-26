# %% [markdown]
# # **Ejercicio Integrador: Análisis de Rendimiento Académico**
# 
# #### Contexto:
# Eres docente de una escuela secundaria y tienes los resultados de exámenes de 4 asignaturas (Matemáticas, Historia, Ciencias, Lengua) de 30 estudiantes. Los datos están organizados en una matriz NumPy de forma `(30, 4)`, donde cada fila representa a un estudiante y cada columna a una asignatura.
# 
# Algunos valores faltan (por ausencias) y se han registrado como `np.nan`.
# 
# 

# %% [markdown]
# #### **Parte 1: Preparación de los datos**
# 1. Genera una matriz `notas` de tamaño `(30, 4)` con valores aleatorios entre 0 y 10 (con un decimal), usando `np.random.uniform`.
# 2. Reemplaza aleatoriamente el **10% de los valores** por `np.nan` para simular ausencias.
# 
# > Pista: puedes usar `np.random.choice` para seleccionar índices.
# 
# 

# %%
import numpy as np

notas = np.round(np.random.uniform(0, 10, size=(30, 4)), 1)
total_vals = notas.size
num_nans = int(0.10 * total_vals)
flat_indices = np.random.choice(total_vals, size=num_nans, replace=False)
rows, cols = np.unravel_index(flat_indices, notas.shape)
print(rows, cols)
notas[rows, cols] = np.nan
notas

# %% [markdown]
# #### **Parte 2: Análisis básico**
# 3. Calcula el **promedio general** de todas las notas **ignorando los `nan`**.
# 4. Calcula el **promedio por asignatura** (una lista de 4 valores).
# 5. Calcula el **promedio por estudiante** (un array de 30 valores). Si un estudiante no tiene ninguna nota válida, su promedio debe ser `np.nan`.
# 
# 

# %%
notas_limpias = notas[~np.isnan(notas)]
mgen = notas_limpias.mean()

mgen = np.nanmean(notas)
masig = np.nanmean(notas, axis=0)
malum = np.nanmean(notas, axis=1)

print(mgen, masig, malum)

# %% [markdown]
# #### **Parte 3: Consultas específicas**
# 6. Determina cuántos estudiantes tienen **promedio ≥ 7.0**.
# 7. Encuentra los índices (números de estudiante) de quienes tienen **menos de 4.0 en Matemáticas**.
# 8. Calcula el **porcentaje de datos faltantes** en la matriz completa.
# 
# 

# %%
eM7 = np.sum(malum >= 7)
print("prom  +7: ", eM7)

iem4 = np.where(notas[:, 0] < 4)[0]
print("mat < 4: ", iem4)

pfaltantes = np.sum(np.isnan(notas)) / notas.size * 100
print("faltantes %: ", pfaltantes)

# %% [markdown]
# #### **Parte 4: Transformación y validación**
# 9. Crea una nueva matriz `notas_completas` donde todos los `np.nan` se reemplacen por el **promedio de su respectiva asignatura** (calculado en punto 4).
# 10. Define una función `es_aprobado(promedio)` que retorne `True` si `promedio >= 6.0`. Aplica esta función al array de promedios por estudiante y cuenta cuántos aprobaron.
# 
# 

# %%
print(masig)

# print(np.isnan(notas))
ind_nan = np.where(np.isnan(notas))
print('indx:', ind_nan)

notas_sin_nan = notas.copy()
print(notas_sin_nan[ind_nan])
print("take:\n",np.take(masig, ind_nan[1]))
notas_sin_nan[ind_nan] = np.take(masig, ind_nan[1])
# print("notas:\n",notas,'\n')
# print("notas_sin_nan:\n",notas_sin_nan,'\n')


def es_aprobado(promedio):
    return promedio >= 6.0

aprobados = es_aprobado(malum)

print("aprobados:\n", aprobados, np.sum(aprobados))

# %% [markdown]
# #### **Parte 5: Búsqueda**
# 11. Identifica al **estudiante con mayor mejora** entre la primera asignatura (Matemáticas) y la última (Lengua), **ignorando casos donde alguna nota sea `nan`**. Devuelve su índice y la diferencia de notas.
# 
# 

# %%
mat = notas[:, 0]
leng = notas[:, 3]
print('mat:', mat)
print('leng:', leng)

dif = leng-mat
print('dif:', dif)

dif_limpia = dif[~np.isnan(dif)]

nmax = np.max(dif_limpia)
nmax

np.where(dif == nmax)[0]

# %% [markdown]
# #### **Parte 6: Bonus**
# 12. Encapsula tu código como una clase python en un módulo para poder reutilizarlo en más proyectos.

# %%



