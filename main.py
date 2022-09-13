# Sample taken from pyStrich GitHub repository
# https://github.com/mmulqueen/pyStrich
from pystrich.datamatrix import DataMatrixEncoder
import sys

print(len(sys.argv))
print(str(sys.argv))

match sys.argv[1]:
    case "A":
        encoder = DataMatrixEncoder('This is a DataMatrix.')
        encoder.save('./datamatrix_test.png')
        print(encoder.get_ascii())
    case "B":
        print("!yes, this is a B!!!")
        sys.argv[1]
    case "C":
        print("!yes, this is a C!! frank needs some new function")
    case "D":
        print("!yes, this is a D!!")
    case "D":
        print("!yes, this is a Dragan!!")        

    # If an exact match is not confirmed, this last case will be used if provided
    case _:
        print("Something's wrong with the internet")
        print(sys.argv[1])


