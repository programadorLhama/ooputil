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
