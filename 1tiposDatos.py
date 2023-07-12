print("Hola mundo")

print("Bienvenido al 1er programa")
print("------------------------------")
print("tipo entero")
print(type(23))
print("------------------------------")
print("Tipo decimal")
print(type(12.32))
print("------------------------------")
print("tipo cadena")
print(type("saludo"))
print("------------------------------")
print("tipo booleano")
print(type(True))

#ejemplos con las cadenas
print("Hola, " + "amigos!!!")#solo las suma
print("saludos "*4)#nos la enseña la palabra 4 veces
variable = "cadena en variable"
variable = "sumo esto a "+variable
print(variable)#imprime todo
print(variable[3])#la letra en dicha posicion de la cadena
print(variable[-1])
print(variable[2:6])#un rango del 2 al 6 sin imprimir esta ultima
print(len(variable))#cantidad de letras incluyendo espacios en blanco
print("hola".upper())#todo en mayuscula
print("HOLA".lower())#todo en minuscula
print(variable.capitalize())#solo la 1ra en mayuscula
cadena = "   Esto es una cadena con                  muchos espacios   "
print(cadena)
print(cadena.strip())#quita los espacios de los extremos

#reemplazar valor
cadena2= "Hola esto es un texto sin reemplazar"
print(cadena2)
print(cadena2.replace("sin reemplazar","reemplazada"))#(parte por reemplazar, por que queremos reemplazarlo)

#operaciones
print(7*2)
print(7+2)