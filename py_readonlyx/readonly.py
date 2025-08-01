"""
ReadOnly decorator implementation for Python properties.
"""


class ReadOnlyError(Exception):
    """Exception raised when trying to modify a read-only property."""
    pass


def readonly(func):
    """
    Decorator that converts a method into a read-only property.
    
    Usage:
        @readonly
        def property_name(self):
            return self._value
    
    This will create a property that can be read but not modified.
    Attempting to set or delete the property will raise ReadOnlyError.
    """
    
    def setter(self, value):
        raise ReadOnlyError(f"Cannot set read-only property '{func.__name__}'")
    
    def deleter(self):
        raise ReadOnlyError(f"Cannot delete read-only property '{func.__name__}'")
    
    return property(fget=func, fset=setter, fdel=deleter, doc=func.__doc__)
