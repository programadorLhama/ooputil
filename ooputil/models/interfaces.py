from abc import ABCMeta

class InterfaceMeta(ABCMeta):
    """Metaclass to force implementation of methods in derived classes."""
    
    def __new__(mcs, name, bases, namespace):
        # If it is not a base class (Interface), check implementation
        if bases:
            for base in bases:
                if isinstance(base, InterfaceMeta):
                    for attr_name, attr_value in base.__dict__.items():
                        # Checks if the base attribute is a method (not a variable) and if the derived class has not implemented it
                        if callable(attr_value) and not attr_name.startswith('__'):
                            if attr_name not in namespace:
                                raise TypeError(f"Class '{name}' must implement method '{attr_name}' of interface '{base.__name__}'")
        return super().__new__(mcs, name, bases, namespace)


class Interface(metaclass=InterfaceMeta):
    """Base for all interfaces."""
    pass