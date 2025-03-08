from abc import ABCMeta
import inspect

class InterfaceMeta(ABCMeta):
    """Metaclass to force implementation of methods in derived classes with the same signature."""
    
    def __new__(mcs, name, bases, namespace):
        # If it is not a base class (Interface), check implementation
        if bases:
            for base in bases:
                if isinstance(base, InterfaceMeta):
                    for attr_name, attr_value in base.__dict__.items():
                        # Checks if the base attribute is a method and not a variable
                        if callable(attr_value) and not attr_name.startswith('__'):
                            if attr_name not in namespace:
                                raise TypeError(f"Class '{name}' must implement method '{attr_name}' of interface '{base.__name__}'")
                            
                            # Compare method signatures
                            base_signature = inspect.signature(attr_value)
                            derived_signature = inspect.signature(namespace[attr_name])

                            if base_signature != derived_signature:
                                raise TypeError(
                                    f"Method '{attr_name}' in class '{name}' does not match the interface signature.\n"
                                    f"Expected: {base_signature}\n"
                                    f"Got: {derived_signature}"
                                )
        return super().__new__(mcs, name, bases, namespace)


class Interface(metaclass=InterfaceMeta):
    """Base for all interfaces."""
    pass
