import numpy as np


class AnalizadorAcademico:
    """
    Analiza el rendimiento académico de estudiantes usando NumPy.
    Asume que los datos están organizados en una matriz (estudiantes x asignaturas).
    """

    ASIGNATURAS = ["Matemáticas", "Historia", "Ciencias", "Lengua"]

    def __init__(self, notas: np.ndarray = None):
        """
        Inicializa el analizador.

        Parámetros:
        - notas: array (n_estudiantes, n_asignaturas). Si no se da, se genera aleatorio.
        - seed: semilla para reproducibilidad (solo si se generan datos aleatorios).
        """

        if notas is None:
            self.notas = self._generar_notas_aleatorias()
        else:
            self.notas = np.array(notas, dtype=float)

        self.n_estudiantes, self.n_asignaturas = self.notas.shape

    def _generar_notas_aleatorias(self, n_estudiantes=30, n_asignaturas=4, missing_pct=0.10):
        """Genera matriz de notas con valores faltantes."""
        notas = np.round(np.random.uniform(
            0, 10, size=(n_estudiantes, n_asignaturas)), 1)
        total = notas.size
        n_nans = int(missing_pct * total)
        flat_idx = np.random.choice(total, size=n_nans, replace=False)
        rows, cols = np.unravel_index(flat_idx, notas.shape)
        notas[rows, cols] = np.nan
        return notas

    @property
    def promedio_general(self):
        """Promedio de todas las notas (ignorando NaN)."""
        return np.nanmean(self.notas)

    @property
    def promedio_por_asignatura(self):
        """Promedio por asignatura (array de longitud n_asignaturas)."""
        return np.nanmean(self.notas, axis=0)

    @property
    def promedio_por_estudiante(self):
        """Promedio por estudiante (array de longitud n_estudiantes)."""
        return np.nanmean(self.notas, axis=1)

    def estudiantes_con_promedio_mayor_o_igual(self, umbral: float = 7.0):
        """Devuelve cantidad de estudiantes con promedio ≥ umbral."""
        return np.sum(self.promedio_por_estudiante >= umbral)

    def indices_baja_en_asignatura(self, asignatura_idx: int = 0, umbral: float = 4.0):
        """Devuelve índices de estudiantes con nota < umbral en una asignatura."""
        return np.where(self.notas[:, asignatura_idx] < umbral)[0]

    @property
    def porcentaje_datos_faltantes(self):
        """Porcentaje de valores NaN en la matriz completa."""
        return (np.isnan(self.notas).sum() / self.notas.size) * 100

    @property
    def notas_limpias(self):
        """Devuelve las notas con NaN reemplazados por promedio de su asignatura."""
        if self.notas is None:
            return None
        else:
            return self.rellenar_nan_con_promedio_asignatura()


    def rellenar_nan_con_promedio_asignatura(self):
        """Devuelve una copia de las notas con NaN reemplazados por promedio de su asignatura."""
        notas_rellenas = self.notas.copy()
        promedios = self.promedio_por_asignatura
        ind_nan = np.where(np.isnan(self.notas))
        notas_rellenas[ind_nan] = np.take(promedios, ind_nan[1])

        return notas_rellenas

    def contar_aprobados(self, umbral_aprobacion: float = 6.0):
        """Cuenta estudiantes con promedio ≥ umbral_aprobacion."""
        return np.sum(self.promedio_por_estudiante >= umbral_aprobacion)

    def estudiante_con_mayor_mejora(self, asignatura_inicial=0, asignatura_final=3):
        """
        Encuentra el estudiante con mayor mejora entre dos asignaturas.
        Devuelve índice.
        """
        col1 = self.notas[:, asignatura_inicial]
        col2 = self.notas[:, asignatura_final]
        dif = col2-col1
        dif_limpia = dif[~np.isnan(dif)]
        nmax = np.max(dif_limpia)
        idx_mejor = np.where(dif == nmax)[0]
        return idx_mejor

    def resumen(self):
        """Imprime un resumen del análisis (útil para depuración o demo)."""
        print("Resumen del análisis académico")
        print(f"- Promedio general: {self.promedio_general:.2f}")
        for i, (asig, prom) in enumerate(zip(self.ASIGNATURAS, self.promedio_por_asignatura)):
            print(f"- Promedio en {asig}: {prom:.2f}")
        print(
            f"- Estudiantes con promedio ≥ 7.0: {self.estudiantes_con_promedio_mayor_o_igual(7.0)}")
        print(
            f"- Estudiantes con <4.0 en Matemáticas: {self.indices_baja_en_asignatura(0, 4.0)}")
        print(f"- % datos faltantes: {self.porcentaje_datos_faltantes:.1f}%")
        print(f"- Aprobados (≥6.0): {self.contar_aprobados(6.0)}")
        idx = self.estudiante_con_mayor_mejora()
        print(f"- Mayor mejora: Estudiante {idx}")
