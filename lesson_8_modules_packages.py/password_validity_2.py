import re


def validity_checking():
    print("Password must contain:\n"
        "- At least 1 lowercase letter [a-z]\n"
        "- At least 1 uppercase letter [A-Z]\n"
        "- At least 1 digit [0-9]\n"
        "- At least 1 special character from [$#@]\n"
        "- Length between 7 and 15 characters (inclusive)")
    
    given_password = str(input("Please enter your password: \n"))
    
    checking_length = 6 < len(given_password) < 16
    checking_lowercase = re.findall("[a-z]", given_password)
    checking_uppercase = re.findall("[A-Z]", given_password)
    checking_numbers = re.findall("[0-9]", given_password)
    checking_characters = re.findall("[$#@]", given_password)
   
    if (checking_length and 
    len(checking_characters) > 0 and
    len(checking_lowercase) > 0 and
    len(checking_numbers) > 0 and
    len(checking_uppercase) > 0):
        print("Password meets requirements")
    else:
        print("Password does not meet requirements")

validity_checking()