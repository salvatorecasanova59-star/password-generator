lunghezza_testo = input("Quanto lunga vuoi che sia la tua password? ")
Numeri = ""
for carattere in lunghezza_testo:
    if carattere.isdigit():
        Numeri =  Numeri + carattere
       

lunghezza_vera = int(Numeri)

if (lunghezza_vera > 100):
    print("La lunghezza massima della password è 100 caratteri.")
    exit()
print("La tua password è lunga",lunghezza_vera, "caratteri.")

import string
Lettere = string.ascii_letters
Numeri = string.digits
Simboli = string.punctuation
tutti_caratteri = Lettere + Numeri + Simboli
import secrets
password = ''.join(secrets.choice(tutti_caratteri) for _ in range(lunghezza_vera))
print("La tua password è:", password)