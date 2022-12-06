import hashlib

str = input("Enter a string: ")

result = hashlib.sha512(str.encode())

print("The hexadecimal equivalent of SHA512 is: ")
print(result.hexdigest())
