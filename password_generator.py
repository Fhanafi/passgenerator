#password generator
import string,secrets

karakter = string.ascii_letters + string.digits
password = ''.join(secrets.choice(karakter) for i in range(8))
print("Password kamu = " + password)
