import subprocess
import sys

def run(script_path):
    completed = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
    return completed.returncode, completed.stdout.strip(), completed.stderr.strip()

def test_hello_world():
    rc, out, err = run('examples/basics/hello_world.py')
    assert rc == 0
    assert 'Hola, mundo' in out

def test_variables_types():
    rc, out, err = run('examples/basics/variables_and_types.py')
    assert rc == 0
    assert 'entero=' in out

def test_sort_demo():
    rc, out, err = run('examples/algorithms/sort_demo.py')
    assert rc == 0
    assert 'Ordenado (built-in sorted):' in out
