import string
import random

def generate():
    c1 = string.ascii_uppercase
    c2 = string.ascii_lowercase
    c3 = string.digits
    c4 = string.punctuation

    p_len = int(input("Enter the length of the password\n"))

    c = []
    c.extend(list(c1))
    c.extend(list(c2))
    c.extend(list(c3))
    c.extend(list(c4))

    random.shuffle(c)
    password = ("".join(c[0:p_len]))
    print(password)

generate()