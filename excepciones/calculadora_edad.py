try:
    age = int(input("Edad: "))
    print("Edad registrada:", age  )
except ValueError:
    print("Error: Por favor, introduce un valor numérico válido.")  
