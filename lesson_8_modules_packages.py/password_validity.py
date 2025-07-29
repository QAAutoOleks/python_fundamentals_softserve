import re


# make a function which return a 'bool', but indirectly
# because a 'match' object is truthy / None is falsy

def checking_validity_conditions(password: str) -> bool:
    return (
        6 < len(password) < 16 and
        re.search(r"[a-z]", password) and
        re.search(r"[A-Z]", password) and
        re.search(r"[0-9]", password) and
        re.search(r"[$#@]", password)
        )

def getting_password_and_printing_result():
    print("Password must contain:\n"
        "- At least 1 lowercase letter [a-z]\n"
        "- At least 1 uppercase letter [A-Z]\n"
        "- At least 1 digit [0-9]\n"
        "- At least 1 special character from [$#@]\n"
        "- Length between 7 and 15 characters (inclusive)")
    
    given_password = str(input("Please enter your password: \n"))
    if checking_validity_conditions(given_password):
        print("Password meets requirements")
    else:
        print("Password does not meet requirements")

getting_password_and_printing_result()