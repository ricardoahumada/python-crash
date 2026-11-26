# VENV en VC

## **Ventajas de hacerlo en VS Code**
- Detecta automáticamente entornos virtuales.
- Permite seleccionar el intérprete correcto con un clic.
- Integra terminal, depuración y linting usando el entorno aislado.
- Todo se hace sin salir del editor.


---

## Resumen rápido

| Paso | Comando / Acción |
|------|------------------|
| Crear entorno | `python -m venv .venv` |
| Seleccionar intérprete | `Ctrl+Shift+P` → `Python: Select Interpreter` → elige `.venv/.../python` |
| Instalar librerías | `pip install numpy` |
| Guardar dependencias | `pip freeze > requirements.txt` |
| Ignorar en Git | Añade `.venv/` al `.gitignore` |

---
## Detalle

# Instalar uv (una sola vez en tu sistema)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Crear entorno
uv venv .venv

# Activar (opcional, pero útil en terminal)
source .venv/bin/activate  # o .venv\Scripts\Activate.ps1

# Instalar desde requirements.txt
uv pip install -r requirements.txt

# Compilar dependencias (como pip-compile)
uv pip compile requirements.in > requirements.txt

# Sincronizar entorno (elimina paquetes no en el archivo)
uv pip sync requirements.txt

# Listar paquetes
uv pip list

# Actualizar uv
uv self update