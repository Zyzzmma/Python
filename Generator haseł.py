import random
znaki =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
dlugosc = int(input("Ile znaków ma zwierać hasło"))
haslo = [None] * dlugosc
for i in range(dlugosc):
    haslo[i] = random.choice(znaki)
haslo_str = ''.join(haslo)
print("Twoje hasło to:", haslo_str)
