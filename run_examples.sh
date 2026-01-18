#!/usr/bin/env bash
set -e
python3 examples/basics/hello_world.py
python3 examples/basics/variables_and_types.py
python3 examples/data_structures/list_demo.py
python3 examples/algorithms/sort_demo.py
python3 examples/projects/simple_cli/calculator.py add 2 3 || true

echo "Ejemplos ejecutados correctamente"
