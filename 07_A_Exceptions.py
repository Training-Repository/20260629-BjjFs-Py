from random import randint

def Bar(n1, n2):
    print("Bar")
    select = randint(1, 5)

    match select:
        case 1:
            raise ValueError("Numerator should be positive only")
        case 2:
            raise FileNotFoundError("Where's the file?")
        case 3:
            raise TypeError("Choose the correct type for the data")
     
    # if n1 < 0:
    #     raise ValueError("Numerator should be positive only")
    quotient = n1/n2
    print("Bar exit")
    return quotient

def Foo(num):
    print("Foo")
    res = Bar(num, 2)
    print("Foo exit")
    return res

def Main():
    print("Main")
    try:
        res = Foo(-10)
        print(f"{res = }")
    except ZeroDivisionError as ex:
        print(f"Exception: {ex!r}")
    except (TypeError, ValueError) as ex:
        print("Exception: Cleanup operations")
        print(f"{ex!r}")
    except Exception as ex:
        print(f"Exception: {ex!r}")
        # print(f"{str(ex) = }")
        # print(f"{repr(ex) = }")
    
    print("Main exit")

Main()
print("Prog exit")
