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