# ooputil

This package defines utilities for object-oriented programming in python.

## How to use

### Interfaces

```python
from ooputil import Interface

# Implementing an OOP interface
class MyInterface(Interface):
    def do_something(self, elem: str) -> None: pass

    def do_another_thing(self) -> None: pass


# Creating a class that implements the interface
class MyClass(MyInterface):
    def do_something(self, elem: str) -> None:
        print(elem)

    def do_another_thing(self) -> None:
        print("Using my method :)")
