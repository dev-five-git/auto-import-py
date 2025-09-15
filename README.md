# Auto Import Py

A Python library for automatically importing modules from a directory structure.

English | [한국어](README_ko.md)

## Features

- 📁 Automatically imports all Python modules from a directory structure
- 🔄 Recursively traverses subdirectories
- ⚙️ Returns a list of imported module objects
- 🚀 Simple and lightweight implementation
- 🛣️ Works with any directory structure

## Installation

```bash
pip install auto-import-py
uv add auto-import-py
```

## Usage

### Basic Usage

```python
from auto_import import auto_import
from pathlib import Path

# Import all modules from the current directory
modules = auto_import()

# Import all modules from a specific directory
modules = auto_import("my_modules")

# Import all modules from a Path object
modules = auto_import(Path("src/components"))
```

### Directory Structure Example

```
my_modules/
├── users.py          # Will be imported
├── items.py          # Will be imported
├── __init__.py       # Will be filtered out
└── v1/
    ├── admin.py      # Will be imported
    └── __init__.py   # Will be filtered out
```

### Module File Example

```python
# my_modules/users.py
def get_users():
    return {"users": []}

def create_user(name: str):
    return {"name": name, "id": 1}

# my_modules/items.py
class Item:
    def __init__(self, name: str):
        self.name = name

def get_items():
    return [Item("item1"), Item("item2")]
```

### Using Imported Modules

```python
from auto_import import auto_import

# Import all modules
modules = auto_import("my_modules")

# Access functions and classes from imported modules
for module in modules:
    print(f"Module: {module.__name__}")
    
    # Get all functions from the module
    functions = [attr for attr in dir(module) if callable(getattr(module, attr)) and not attr.startswith('_')]
    print(f"Functions: {functions}")
    
    # Get all classes from the module
    classes = [attr for attr in dir(module) if isinstance(getattr(module, attr), type) and not attr.startswith('_')]
    print(f"Classes: {classes}")
```

### Advanced Usage

```python
from auto_import import auto_import
import inspect

# Import modules and inspect their contents
modules = auto_import("src")

for module in modules:
    print(f"\n=== {module.__name__} ===")
    
    # Get all callable objects
    for name, obj in inspect.getmembers(module, callable):
        if not name.startswith('_'):
            print(f"Callable: {name}")
    
    # Get all classes
    for name, obj in inspect.getmembers(module, inspect.isclass):
        if not name.startswith('_'):
            print(f"Class: {name}")
```

## API Reference

### `auto_import(dir_path: Path | str = ".") -> list[ModuleType]`

Automatically imports all Python modules from the specified directory.

**Parameters:**
- `dir_path` (Path | str): Directory path to import modules from (default: ".")

**Returns:**
- `list[ModuleType]`: List of imported module objects

**Behavior:**
1. Recursively traverses the specified directory
2. Finds all `.py` files
3. Imports each module using `importlib.import_module`
4. Returns a list of successfully imported modules

**Note:** The function will return an empty list if the directory doesn't exist.

## Development

### Install Dependencies

```bash
# Install development dependencies
uv sync
```

### Run Tests

```bash
# Run all tests
uv run pytest
```

### Code Quality Checks

```bash
# Linting
ruff check src/ tests/

# Formatting
ruff format src/ tests/
```

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

## Contributing

Bug reports, feature requests, and pull requests are welcome! Please create an issue first before contributing.

## Author

- **owjs3901** - *Initial work* - [owjs3901@gmail.com](mailto:owjs3901@gmail.com)