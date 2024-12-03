

morse = {
    'A': '.-', 'B': '-...',
                    'C': '-.-.', 'D': '-..',
                    'E': '.', 'F': '..-.', 'G': '--.',
                    'H': '....', 'I': '..', 'J': '.---',
                    'K': '-.-', 'L': '.-..', 'M': '--',
                    'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...',
                    'T': '-', 'U': '..-', 'V': '...-',
                    'W': '.--', 'X': '-..-', 'Y': '-.--',
                    'Z': '--..', '1': '.----', '2': '..---',
                    '3': '...--', '4': '....-', '5': '.....',
                    '6': '-....', '7': '--...', '8': '---..',
                    '9': '----.', '0': '-----', ', ': '--..--',
                    '.': '.-.-.-', '?': '..--..', '/': '-..-.',
                    '-': '-....-', '(': '-.--.', ')': '-.--.-'
}


def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':

            cipher += morse[letter] + ' '
        else:

            cipher += ' '

    return cipher


def decrypt(message):

    message += ' '

    decipher = ''
    citext = ''
    for letter in message:

        if (letter != ' '):

            i = 0

            citext += letter

        else:

            i += 1

            if i == 2:

                decipher += ' '
            else:

                decipher += list(morse.keys()
                                 )[list(morse.values()).index(citext)]
                citext = ''

    return decipher


def main():
    while True:
        user_interact = input("Encrypt or Decrypt:")
        if user_interact == "Encrypt":

            message = input("Enter your string to change morse code:")
            result = encrypt(message.upper())
            print("result:"+result)
        elif user_interact == "Decrypt":

            message = input("Enter a morse code:")
            result = decrypt(message)
            print("result1:"+result)
        else:
            print("use these two names Encrypt (or) Decrypt")


# Executes the main function
if __name__ == '__main__':
    main()
