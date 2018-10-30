message = input("Enter some message: ")
m = int(input("Number of positions down the alphabet? "))
caesar_cipher = ''

for char in message:

    if not char.isalpha():

        caesar_cipher += char

    else:

        num = ord(char)

        num += m

        if char.isupper():

            if num > ord('Z'):

                num -= 26

            elif num < ord('A'):

                num += 26

        elif char.islower():

            if num > ord('z'):

                num -= 26

            elif num < ord('a'):

                num += 26

        caesar_cipher += chr(num)


print(caesar_cipher)
