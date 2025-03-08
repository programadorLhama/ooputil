from ooputil import Interface

def test_interface_ok():
    class FooInterface(Interface):
        def do_something(self, elem: str) -> None: pass

    class Foo(FooInterface):
        def do_something(self, elem: str) -> None:
            print(elem)
            
    foo = Foo()
    foo.do_something("Test OK! :)")
    assert True

def test_interface_raise_if_method_not_equal():
    class FooInterface(Interface):
        def do_something(self, elem: str) -> None: pass

    try:
        class Foo(FooInterface):
            def do_error(self, elem: str) -> None:
                print(elem)
    except Exception as e:
        assert str(e) == "Class 'Foo' must implement method 'do_something' of interface 'FooInterface'"
        assert True

def test_interface_raise_if_signature_not_equal():
    class FooInterface(Interface):
        def do_something(self, elem: str) -> None: pass

    try:
        class Foo(FooInterface):
            def do_something(self, elem: int) -> None:
                print(elem)
    except Exception as e:
        assert "Method 'do_something' in class 'Foo' does not match the interface signature" in str(e)
        assert "Expected: (self, elem: str) -> None" in str(e)
        assert "Got: (self, elem: int) -> None" in str(e)
        assert True

