#password generator
import string,secrets
karakter = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(karakter) for i in range(12))
print("Password kamu = " + password)
