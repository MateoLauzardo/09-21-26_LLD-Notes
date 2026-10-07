def d ():
    animal = "elephant"
    def e():
        nonlocal animal #NOTE (nonlocal) lets a nested function modify a varaible  that lives outside of it / in its parent
        animal = "Girafee"
        print(f"inside string is {animal}") #! second thing being called 
    
    print("before calling function " + animal) #! first thing being called 
    e()
    print("after calling function " + animal) #! third thing being called 
    
animal = "camel"
d()
print("global name: " + animal) #! last thing being called 