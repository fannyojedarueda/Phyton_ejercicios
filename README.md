# Phyton_ejercicios

Este repositorio contiene ejemplos organizados de Python para aprender y ejecutar. Estructura:

- examples/
  - basics/       # scripts básicos (hola mundo, tipos, variables)
  - data_structures/ # listas, diccionarios, conjuntos
  - algorithms/    # ejemplos de algoritmos simples (ordenamiento)
  - projects/      # pequeños proyectos ejecutables (CLI)
- tests/           # pruebas básicas usando pytest
- requirements.txt # dependencias opcionales
- run_examples.sh  # script para ejecutar todos los ejemplos

Cómo usar:

1. Clona el repositorio y sitúate en la carpeta:
   git clone https://github.com/fannyojedarueda/Phyton_ejercicios.git
   cd Phyton_ejercicios

2. (Opcional) Crea y activa un entorno virtual:
   python3 -m venv .venv
   source .venv/bin/activate

3. Instala dependencias (si lo deseas):
   pip install -r requirements.txt

4. Ejecuta un ejemplo:
   python examples/basics/hello_world.py

5. Ejecuta todas las pruebas:
   pytest -q

---