class Integer:
    def __init__(self, val) -> None:
        try:
            self.val = int(val)
        except TypeError as ex: 
            print(f"Not supported for {type(val)} type.")
            print(f"Exception --> {type(ex)}")
            raise
        except ValueError as ex: 
            print(f"Not supported for value - [{val}].")
            print(f"Exception --> {type(ex)}")
            raise

    def __str__(self):
        return f"[{self.val}]"

    def __add__(self, other):
        if isinstance(other, Integer):
            return Integer(self.val + other.val)
        try:
            return Integer(self.val + int(other))
        except (TypeError, ValueError):
            return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

# Example usage:
try:
    i1 = Integer(10)
    i2 = Integer(5)
    i3 = i1 + i2
    print(i1, i2, i3)  # Output: [10] [5] [15]

    i4 = i3 + 15
    print(i3, i4)  # Output: [15] [30]

    i5 = 20 + i1
    print(i5)  # Output: [30]
    
    i6 = i1 + "5"
    print(i1, i5)

    i7 = i1 + "Five"
    print(i1, i7)
except Exception as e:
    print(f"{type(e)} --> {e}")

print("\n\nAttempting an invalid instanciation of Integer type.")
try:
    # This will raise a ValueError and print an error message
    i6 = Integer("not an integer")
except Exception as e:
    print(f"{type(e)} --> {e}")
