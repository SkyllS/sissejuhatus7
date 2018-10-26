import re

parool = input("pass")

if re.search('[a-z]', parool) and re.search('[0-9]', parool) or re.search('[A-Z]', parool) and re.search('[0-9]', parool):
    loorap=parool[::-1]
    print(loorap)