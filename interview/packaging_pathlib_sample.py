import pathlib
import inspect
script_dir = pathlib.Path(__file__).parent.resolve()

print(open(str(script_dir/'sample.txt')).read())

