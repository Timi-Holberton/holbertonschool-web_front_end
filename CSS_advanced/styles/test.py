#!/usr/bin/python3

# Générer les fichiers de 7 à 32
for i in range(7, 33):
    filename = f"{i}-style.css"
    with open(filename, "w") as f:
        f.write(f"/* CSS file for style {i} */\n")
    print(f"Fichier créé : {filename}")
