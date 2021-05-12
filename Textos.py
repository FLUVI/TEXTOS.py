
def repetir(a):
      palabra = str(input('Que palabra quieres poner?? '))
      veces = int(input('Numero de veces: '))
      print((palabra)*(veces))

def repetir2(b):
      palabra2 = str(input('Que palabra quieres poner? '))
      veces2 = int(input('Numero de veces: '))
      print((palabra2 + " ") * veces2)
    
def repetir3(c):
      palabra3 = str(input('Que palabra quieres poner? '))
      veces3 = int(input("numero de veces: "))
      for i in range(veces3):
        print(palabra3)

def repetir4(d):
      palabra4 = str(input('Que palabra quieres poner? '))
      veces4 = int(input("numero de veces: "))
      for i in range(veces4):
        print(i + 1, palabra4)

def Piramide(a):
      palabra1 = str(input('Que palabra quieres poner? '))
      veces1 = int(input("numero de veces: "))
      for i in range(veces1 + 1):
        print(i*palabra1)

def Piramide2(b):
      palabra2 = str(input('Que palabra quieres poner? '))
      veces2 = int(input("numero de veces: "))
      for i in range(veces2 + 1):
        print(i ,i*palabra2)

def inversa(a):
      palabra2=""
      palabra = str(input("Que palabra quieres poner? "))
      for x in range(len(palabra),0,-1):
        palabra2+=palabra[x-1]
      print(palabra2)

def mayus(a):  
      a = str(input("Palabra en minusculas: ").upper())
      print(a)

def minus(a):
      b = str(input("Palabra en mayusculas: ").lower())
      print(b)


print('Bienvenido al generador de textos!!')
input('Presiona enter')
clear
print('Elige que tipo de texto quieres generar')
print('-Repetidor de texto: [1]')
print('-Cosas random: [2]')
print("-Editor de textos: [3]")
print('-Se implementaran mas proximamente!!!')
decision1 = int(input('Elige: '))
if decision1 == 1:
  print('Bien!, ahora que subtipo quieres?')
  print('-Repetidor sin espacio: [1]')
  print('-Repetidor con espacio: [2]')
  print('-Reloj de repetición:   [3]')
  decision2= int(input())
  if decision2 == 1:
    repetir('a')

  if decision2 == 3:

    enumerado = int(input("Lo quieres enumerado?                                                           Si[1]               No[2]                                                       "))
    if enumerado == 1:
      repetir4("d")
    if enumerado == 2:
      repetir3("c")

  if decision2 == 2:
    repetir2('b')

if decision1 == 2:
  print('Perfecto!, ahora que quieres hacer?')
  print('-Piramide:              [1]')
  print("-Tomador de decisiones: [2]") 
  print("-Generador de caras:    [3]") 
  decision21 = int(input())
  if decision21 == 1:
    enumerado2 = int(input("Lo quieres enumerado?                                                           Si[1]               No[2]                                       "))
    if enumerado2 == 1:
     Piramide2("b")
    
    if enumerado2 == 2:
     Piramide("a")
  if decision21 == 2:
    str(input("Escribe tu pregunta: "))
    print("no","si")
  
  if decision21 == 3:
    print("-Caras 1  [1]")
    print("-Caras 2  [2]")
    print("-Caras 3  [3]")
    print("-Salir   [4]")
    Caras = int(input("Elige tu numero: "))
    if Caras == 1:
      print("(>u<)")


    
if decision1 == 3:
  print("Bien!!, Ahora selecciona una de estas opciones ")
  print("-Texto a MAYUSCULAS [1]")
  print("-Texto a minusculas [2]")
  print("-Texto a la inversa [3]")
  decision3 = int(input())
  if decision3 == 1:
    mayus("a")

  if decision3 == 2:
    minus("a")

  if decision3 == 3:
    inversa("a")
