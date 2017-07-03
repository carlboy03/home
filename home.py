import json
from pprint import pprint
import homeYacc as yacc
import homeFunctions




def main():
    homeFunctions.open_home()

    while True:
        try:
            s = input('home >')
        except EOFError:
            break
        if not s: continue
        result = yacc.parser.parse(s)

main()