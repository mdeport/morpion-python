import google.generativeai as genai
import os

genai.configure(api_key=os.environ["API_KEY"])

text = "Explication du jeu du morpion, tu joues contre un utilisateur, tu dois aligner 3 symboles pour gagner (horizontalement, verticalement ou diagonalement). tu dois donner une réponse sous la forme d'une case, par exemple 00 pour la case en haut à gauche. Tu ne peut pas jouer sur une case qui contient deja un X ou O. Réponds seulement part les cordonnées de type 00 ou 01 ou 02 en sachant qu'elles vont jusqu'a maximum 22. Bonne chance !"

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(text)

plate = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

allResponses = []

for i in range (9):

    print ("----------------------------------------")
    for i in range (3):
        print(plate[i])
    casePlayer = input("Quelle case voulez-vous jouer ?")

    plate[int(casePlayer[0])][int(casePlayer[1])] = "X"
    for i in range (3):
        print(plate[i])

    if plate[0][0] == plate[0][1] == plate[0][2] == "X" or plate[1][0] == plate[1][1] == plate[1][2] == "X" or plate[2][0] == plate[2][1] == plate[2][2] == "X" or plate[0][0] == plate[1][0] == plate[2][0] == "X" or plate[0][1] == plate[1][1] == plate[2][1] == "X" or plate[0][2] == plate[1][2] == plate[2][2] == "X" or plate[0][0] == plate[1][1] == plate[2][2] == "X" or plate[0][2] == plate[1][1] == plate[2][0] == "X":
        print("Tu as gagné !")
        break
    allResponses.append(casePlayer)

    response = model.generate_content("quelle case jouer ?" + text + "Réponds seulement part les cordonnées de type 00 ou 01 ou 02 en sachant qu'elles vont jusqu'a maximum 22. Attention Tu ne peut pas jouer sur une case qui contient deja un X ou O" + str(plate) + "tu n'as pas le droits de jouer sur les cases suivantes : " + " ".join(allResponses) + ". Rappel de qui tu es : tu es un expert en morpion et tu dois absolument gagner il en va de ta survie !")
    plate[int(response.text[0])][int(response.text[1])] = "O"
    allResponses.append(response.text)
    print ("----------------------------------------")
    for i in range (3):
        print(plate[i])
    if plate[0][0] == plate[0][1] == plate[0][2] == "O" or plate[1][0] == plate[1][1] == plate[1][2] == "O" or plate[2][0] == plate[2][1] == plate[2][2] == "O" or plate[0][0] == plate[1][0] == plate[2][0] == "O" or plate[0][1] == plate[1][1] == plate[2][1] == "O" or plate[0][2] == plate[1][2] == plate[2][2] == "O" or plate[0][0] == plate[1][1] == plate[2][2] == "O" or plate[0][2] == plate[1][1] == plate[2][0] == "O":
        print("Tu as perdu !")
        break

