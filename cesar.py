message=input("enter the message \n")
key=input("enter the key\n")
def encrypt(message,key):
    cipher=""
    if message.isupper():
        for i in message:
            cipher+=chr(((ord(i)+int(key)-65)%26)+65)
    else:
        for i in message:
            cipher+=chr(((ord(i)+int(key)-97)%26)+97)
    print(cipher)

def decrypt(message, key):
    cipher = ""
    if message.isupper():
          for i in message:
              cipher += chr(((ord(i) - int(key) - 65) % 26) + 65)
    else:
        for i in message:
            cipher += chr(((ord(i) - int(key) - 97) % 26) + 97)
    print(cipher)
user=input("what do you want encrypt or decrypt")
s=0
while s<3:

    if user=='d':
        decrypt(message,key)
        s=3
    elif user=='e':
        encrypt(message,key)
        s=3
    else:
         user=input("i don't understand try again")
         s+=1





