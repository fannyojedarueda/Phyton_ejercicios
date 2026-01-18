# Phyton_ejercicios

Este repositorio contiene ejemplos organizados de Python para aprendizaje y pruebas rápidas.

Estructura propuesta:
- examples/
  - basics/        Ejemplos introductorios (hello world, variables, funciones)
  - data/          Ejemplos con manejo de datos (pandas, csv)
  - algorithms/    Algoritmos y estructuras
  - projects/      Proyectos pequeños organizados por carpetas
- scripts/         Scripts de mantenimiento y ejecución
- tests/           Tests automatizados con pytest
- requirements.txt Dependencias opcionales

Cómo usar (localmente)
1. Clona el repositorio (si no está ya en tu máquina).
2. Crea y activa un entorno virtual:
   python -m venv .venv
   source .venv/bin/activate   # macOS/Linux
   .venv\Scripts\activate      # Windows
3. Instala dependencias:
   pip install -r requirements.txt
4. Ejecuta todos los ejemplos:
   python scripts/run_all.py
5. Ejecuta tests:
   pytest -q

Automatización para reorganizar archivos existentes
- Hay un script interactivo `scripts/organize_repo.py` que lista los archivos `.py` en el repo (excepto tests y scripts) y te permite moverlos a la carpeta que elijas (basics, data, algorithms, projects).

Si quieres que yo haga los cambios directamente en GitHub
