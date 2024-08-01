msg = "Hello World"
print(msg)

msg = "Hello World"
print(msg)

#um zu sehen ob code funktioniert zuerst 'run' im Terminal

# #Aufgabe 1

# name = "Melissa"
# alter = 29
# geburtsort = "Erding"

# name = input("Wie heißt du? ")
# alter = int(input("Wie alt bist du? "))
# geburtsort = input("Wo bist du geboren? ")

# # Ausgabe
# print(f"\nName: {name}\nAlter: {alter}\nGeburtsort: {geburtsort}")

# # Check
# if alter > 18:
#     print("Du bist älter als 18.")
# else:
#     print("Du bist 18 Jahre alt oder jünger.")

#ValueError: invalid literal for int() with base 10



#AUFGABE 1:

#Frage nach Name, Alter und Geburtsort
name = input("Wie heißt du? ")

#while Schleife mit Aufforderung zur Eingabe
while True:
    alter_input = input("Wie alt bist du? ")
    try:
        alter = int(alter_input)
        break
    except ValueError:
        print("Bitte gib eine gültige Zahl für das Alter ein.")
#Frage wo du geboren bist
geburtsort = input("Wo bist du geboren? ")

#Ausgabe
print(f"\nName: {name}\nAlter: {alter}\nGeburtsort: {geburtsort}")

# Check ob Alter > als 18 sonst Fehlermeldung
if alter > 18:
    print("Du bist älter als 18 Jahre.")
else:
    print("Du bist 18 Jahre oder jünger.")



#AUFGABE 2:

text = input("Hier kommt der Text: ")

neuer_text = ""

vokal_anzahl = 0

vokale = "aeiouAEIOU"

# Alle Vokale durch * ersetzen und Vokale zählen
for buchstabe in text:
    if buchstabe in vokale:
        neuer_text += "*"
        vokal_anzahl += 1
    else:
        neuer_text += buchstabe

# Ausgabe 
print(f"Der neue Text ist: {neuer_text}")
print(f"Anzahl der Vokale im Text: {vokal_anzahl}")




#AUFGABE:3

import random

#liste random zahlen
randomnumber = [random.randint(1, 100) for _ in range(10)]

sorted_numbers = sorted(randomnumber)

largest_numb = max(sorted_numbers)
smallest_numb = min(sorted_numbers)

#ausgabe
print(f"Sortierte liste: {sorted_numbers}")
print(f"Größte Zahl: {largest_numb}")
print(f"Kleinste Zahl: {smallest_numb}")

#tuple
result = (sorted_numbers, largest_numb, smallest_numb)

print(f"Ergebnis Tuple: {result}")



#AUFGABE 4:

#Dictionary
friends = {
    "Franzi": 1995,
    "Svea": 1994,
    "Jule": 1995,
    "Maria": 1993,
    "Kathi": 1990
}
name = input("Namen eines Freundes: ")

if name in friends:
    geburtsjahr = friends[name]
    print(f"{name} ist {geburtsjahr} geboren.")
else:
    print(f"Der Name {name} existiert nicht.")

# 3. Ein Set aller Geburtsjahre erstellen und die Anzahl der einzigartigen Geburtsjahre ausgeben
gebjahre = set(friends.values())
einzigartige_geburtsjahre = len(gebjahre)

# Ausgabe des Sets und der Anzahl der einzigartigen Geburtsjahre
print(f"Set der Geb.jahre: {gebjahre}")
print(f"Anzahl der einzigartigen Geb.jahre: {einzigartige_geburtsjahre}")





#AUFGABE 5 loops
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#loop summe
summe = 0
for number in numbers:
    summe += number

print(f"Die Summe aller Zahlen in der Liste ist: {summe}")

# 3. Eine weitere Schleife verwenden, um das Produkt aller Zahlen in der Liste zu berechnen und auszugeben
product = 1
for number in numbers:
    product *= number

print(f"Produkt aller zahlen in liste: {product}")



#AUFGABE 6
number1 = int(input("Eingabe erste Zahl: "))
number2 = int(input("Eingabe zweite Zahl: "))
number3 = int(input("Eingabe dritte Zahl: "))

# welche der 3 zahlen ist größer
if number1 >= number2 and number1 >= number3:
    biggestnumb = number1
elif number2 >= number1 and number2 >= number3:
    biggestnumb = number2
else:
    biggestnumb = number3

print(f"Die größte Zahl ist: {biggestnumb}")

# Überprüfe ob die größte Zahl gerade oder ungerade ist
if biggestnumb % 2 == 0:
    print(f"Die größte zahl {biggestnumb} ist gerade.")
else:
    print(f"Die größte zahl {biggestnumb} ist ungerade.")



#AUFGABE 7

#function fakultaet definieren, die die Fakultät einer zahl berechnet
def fakultaet(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fakultaet(n - 1)

# Eingabe einer Zahl
number = int(input("Eigabe Zahl: "))

#fakultät dieser Zahl mithilfe der function berechnen, dann ausgabe
result = fakultaet(number)
print(f"Die Fakultät von {number} ist {result}.")

