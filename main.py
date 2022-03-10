import string
import random


print("Welcome to password generator!")

password_len=int(input("Enter lenth of password:"))


lower=string.ascii_lowercase
upper=string.ascii_uppercase
numbers=string.digits
symbols=string.punctuation

all=lower+upper+numbers+symbols

password=random.sample(all,password_len)
password_1="".join(password)
print(f"The generated password is {password_1}")
