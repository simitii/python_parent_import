# Parent Import

Unfortunately, importing from parent directory is problematic in Python. 

This package makes it easier to import from parent directory.

## Install
```
pip install parent_import
```


## Example Usage:
file structure:
```
project_name/
    dir1/
        importer.py
    dir2/
        dir3/
            module_to_import.py
```

`module_to_import.py`:
```python
print("Module Imported")
def method1():
    print("Hello World")
```


`importer.py`:
```python
from parent_import import parentdir

module = parentdir.dir2.dir3.module_to_import
# Output: "Module Imported"

module.method1()
# Output: "Hello World"
```

Note: Accesing parent of parent is also possible as follows:
```python
from parent_import import parentdir

module = parentdir.parentdir.another_dir.module_to_import
```

Another Usage - Import From Parent Directory:
```python
from parent_import import add_ancestor_dir_to_path

add_ancestor_dir_to_path(level=1)

import dir2.dir3.module_to_import
```

Another Usage - Import From Parent of Parent Directory:
```python
from parent_import import add_ancestor_dir_to_path

add_ancestor_dir_to_path(level=2)

import another_dir.module_to_import
```


## TODO
* Get rid of `sys.path.insert(0, self.dir_path)` statements in order to speed up module search. (possible?)
* Override or extend `import` statement to use the Pythonic syntax for importing from parent directory. (possible?)