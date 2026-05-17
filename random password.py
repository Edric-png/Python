import random, string
length = 8
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
password = ""
for _ in range(length):
    password += random.choice(characters)
print(password)