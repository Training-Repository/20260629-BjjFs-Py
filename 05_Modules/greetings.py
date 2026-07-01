__all__ = ['greet']
# __all__ = ['greet', 'greetName']

def greet():
    print("Hi there")

def greetName(name):
    salutation = "Hello"
    final_greet = prepMsg(salutation, name)
    print(final_greet)

def prepMsg(salutaion, name):
    return salutaion + " " + name + "!"

# def Test():
#     greet()
#     greetName("John")

# print(f"Greetings - {__name__ = }")
# if __name__ == '__main__':
#     Test()

if __name__ == '__main__':
    greet()
    greetName("John")
