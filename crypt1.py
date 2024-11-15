import argparse
from cryptography.fernet import Fernet 

def generateKey(path):
    with open(path, "wb+") as file:
        file.write(Fernet.generate_key())

def encryptFile(keyPath, encryptPath):
    keyFile = open(keyPath, "rb")
    key = Fernet(keyFile.read())
    keyFile.close()

    ffile = open(encryptPath, "rb")
    normalFileContent = ffile.readlines()
    ffile.close()

    with open(encryptPath, "wb+") as file:
        for normalContent in normalFileContent:
            file.write(key.encrypt(normalContent))

def decryptFile(keyPath, decryptPath):
    keyFile = open(keyPath, "rb")
    key = Fernet(keyFile.read())
    keyFile.close()

    ffile = open(decryptPath, "rb")
    encryptedFileContent = ffile.readlines()
    ffile.close()

    with open(decryptPath, "wb+") as file:
        for encryptedContent in encryptedFileContent:
            file.write(key.decrypt(encryptedContent))

def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--generate-key", action = "store_true", help = "Generate a symetric key")
    argparser.add_argument("--filnamn", required = True, help = "File to use for argument")
    argparser.add_argument("--key-file", "-k", help = "File path for new key")
    argparser.add_argument("--encrypt", "-e", action = "store_true", help = "Encrypt file from path")
    argparser.add_argument("--decrypt", "-d", action = "store_true", help = "Decrypt file from path")
    arguments = vars(argparser.parse_args())

    try: 
        if (arguments["generate_key"] == True):
            generateKey(arguments["filnamn"])
        elif (arguments["key_file"] != None and arguments["encrypt"] == True):
            encryptFile(arguments["key_file"], arguments["filnamn"])
        elif (arguments["key_file"] != None and arguments["decrypt"] == True):
            decryptFile(arguments["key_file"], arguments["filnamn"])
    except FileNotFoundError as error:
        print("File not found!")
    except Exception as error:
        print("Something went wrong!")

if __name__ == "__main__":
    main()


