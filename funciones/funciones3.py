#registrar las edades de n cantidad de personas.
#Y mostrar la edad mas alta y mas baja y la cantidad de gente registrada.
ages = []

def addAge(age):
   ages.append(age)
   return 0

def getMaxAge():
      return max(ages) if ages else None

def getMinAge():
      return min(ages) if ages else None

def showSize():
   return len(ages)

def showAges():
   return ages.copy()

while True:
   try:
      age = int(input("Ingrese la edad de la persona: "))
      if age > 0:
         addAge(age)
      else:
         print("Porfavor ingrese un numero entero positivo")
         continue

    answer = input("Desea ingresar otra edad? (s/n): ")
       if answer.lower() != "s":
          break
    except ValueError:
      print("Porfavor ingrese un numero entero")
      continue



print("Mostrar edades")
print(f"Cantidad de edades registradas: {showSize()}")
print(showAges())
print(f"Edad mas Vieja: {getMaxAge()}")
print(f"Edad mas Joven: {getMinAge()}")
print(f"Cantidad de personas registradas: {showSize()}")
