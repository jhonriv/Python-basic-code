import random


def userTests():
    name = input("What is your name? ")
    age = input("How old are you? ")
    print("Hello " + name + ", you are " + age + " years old.")

def aleatoryListNumber():
    numbers = [random.randint(1, 100) for i in range(20)]
    return numbers

def sumNumberPair():
    # Hacer una lista de numeros aleatorios del 1 al 100 y tomar 20
    aleatoryList = aleatoryListNumber()
    print("The list is: " + str(aleatoryList))
    
    # Extraer y sumar los numeros pares de la lista
    evenNumbers = sum([i for i in aleatoryList if i % 2 == 0])
    print("The sum of the even numbers is: " + str(evenNumbers))


def orderStrings():
    # Hacer una lista de palabras aleatorias y ordenarlas alfabeticamente
    words = ["tv", "dog", "glasses", "computer", "code", "friday", "Canada", "Japan", "mom", "learing"]
    words.sort()

    [print(x) for x in words]

def isPair():
    number = int(input("What is the number?"))
    if (number % 2 == 0): print("Is pair")
    else: print("Is not pair")

def orderNumber():
	# Hacer una lista de numeros aleatorios del 1 al 100 y tomar 20
    aleatoryList = aleatoryListNumber()
    print(str(aleatoryList))
    
    aleatoryList.sort()
    print("The list ordered is: " + str(aleatoryList))


userTests()

sumNumberPair()

orderStrings()

isPair()

orderNumber()