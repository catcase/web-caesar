import string

def caesar(text, num):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    secret = ''

    for char in text:
        if char not in lower and char not in upper:
            secret = secret + str(char)
        elif char in upper:
            rotated = upper.index(char) + num
            rotated = rotated % 26
            secret = secret + upper[rotated]
        else:
            rotated = lower.index(char) + num  
            rotated = rotated % 26
            secret = secret + lower[rotated]
    return secret

def main():
    message = input("What is your secret message? ")
    num_rot = int(input("How many times would you like to rotate? "))
    print(caesar(message, num_rot))

if __name__ == "__main__":
    main()