import json as js

print("Willkommen!")

# JSON-Datei einlesen oder Dictionary initialisieren
try:
    with open("users.json", "r") as file:
        users = js.load(file)
except FileNotFoundError:
    users = {}  # Falls Datei nicht existiert, leeres Dictionary

# Funktionen
def login(username, password):
    if username in users and users[username]["password"] == password:
        print("Eingeloggt!")
    else:
        print("Fehler: Benutzername oder Passwort falsch!")

def register(username, password):
    if username in users:
        print("Fehler: Benutzername existiert bereits!")
    else:
        users[username] = {"password": password}  # Speichere Passwort als Schlüssel-Wert-Paar
        with open("users.json", "w") as file:
            js.dump(users, file, indent=4)
        print("Registrierung erfolgreich!")

# Aktionen
print("1 : Einloggen")
print("2 : Registrieren")

action = input("Aktion auswählen: ")

if action == "1":
    login(input("Benutzername: "), input("Passwort: "))
elif action == "2":
    register(input("Benutzername: "), input("Passwort: "))
else:
    print("Fehler: Ungültige Auswahl!")