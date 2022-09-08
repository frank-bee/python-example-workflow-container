# Sample taken from pyStrich GitHub repository
# https://github.com/mmulqueen/pyStrich
from pystrich.datamatrix import DataMatrixEncoder
import sys

print(len(sys.argv))
print(str(sys.argv))

match sys.argv[1]:
    case "1":
        encoder = DataMatrixEncoder('This is a DataMatrix.')
        encoder.save('./datamatrix_test.png')
        print(encoder.get_ascii())
    case "2":
        print("!yes, this is a 2!!")
    case "3":
        print("!yes, this is a 3!!")

    # If an exact match is not confirmed, this last case will be used if provided
    case _:
        print("Something's wrong with the internet")


