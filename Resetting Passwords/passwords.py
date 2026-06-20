pass1 = str(input("Enter your New Password: "))
pass2 = str(input("Enter again to confirm: "))

if pass1 == pass2:
    print("Password changed successfully")
else:
    if pass1.casefold() == pass2.casefold():
        print("Check cases and try again")
    else:
        print("Passwords do not match")
        exit