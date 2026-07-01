from random import randint

def Main():
    print("Main")
    try:
        print("Acquiring resources...")
        print("Performing task...")
        if randint(0, 1):
            raise FloatingPointError("Error in floating point")
        # print("Releasing resources...")
    except ZeroDivisionError as ex:
        print(f"Exception: {ex!r}")
        # print("Releasing resources...")
    except (TypeError, ValueError) as ex:
        print("Exception: Cleanup operations")
        print(f"{ex!r}")
        # print("Releasing resources...")
    except Exception as ex:
        print(f"Exception: {ex!r}")
        # print(f"{str(ex) = }")
        # print(f"{repr(ex) = }")
        # print("Releasing resources...")
    else:
        print("No exceptions were raised!")
    finally:
        print("Releasing resources...")

    
    print("Main exit")

Main()
print("Prog exit")
