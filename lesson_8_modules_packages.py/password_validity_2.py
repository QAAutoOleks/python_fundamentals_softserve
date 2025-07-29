import re


def validity_checking():
    print("Password must contain:\n"
        "- At least 1 lowercase letter [a-z]\n"
        "- At least 1 uppercase letter [A-Z]\n"
        "- At least 1 digit [0-9]\n"
        "- At least 1 special character from [$#@]\n"
        "- Length between 7 and 15 characters (inclusive)")
    
    given_password = str(input("Please enter your password: \n"))

    if (
        6 < len(given_password) < 16 and 
        re.findall("[a-z]", given_password) and
        re.findall("[A-Z]", given_password) and
        re.findall("[0-9]", given_password) and
        re.findall("[$#@]", given_password)
    ):
        print("Password meets requirements")
    else:
        print("Password does not meet requirements")

validity_checking()