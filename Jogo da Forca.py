#This game has pre-specified input
import time
name = input("Qual é o seu nome? ")
print("Olá, " + name, "Hora de jogar forca!")
print("")
time.sleep(1)
print("Comece a adivinhar...")
time.sleep(0.5)
word = "secreto"
guesses = ''
turns = 10
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("Você ganhou")
        break
    print('')
    guess = input("adivinhe um personagem:")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("Errado")
    print("Você tem", + turns, 'mais suposições')
    if turns == 0:
        print("Você perdeu")
