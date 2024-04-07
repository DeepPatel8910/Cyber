# importing the required libraries
import hashlib
# making a message
print("MD5 Algorithm")
inputstring = input("Enter a message:")
# encoding the message using the library function
output = hashlib.md5(inputstring.encode())
# printing the hash function
print("Hash of input message:")
print(output.hexdigest())
