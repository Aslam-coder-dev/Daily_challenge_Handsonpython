
st_id = input("Enter student ID: ")
email = input("Enter email: ")
password = input("Enter password: ")
referral = input("Enter referral: ")
valid = True
if len(st_id) != 7:
    valid = False
elif st_id[0:3] != "CSE":
    valid = False
elif st_id[3] != "-":
    valid = False
elif not (st_id[4].isdigit() and st_id[5].isdigit() and st_id[6].isdigit()):
    valid = False
if "@" not in email or "." not in email:
    valid = False
elif email[0] == "@" or email[-1] == "@":
    valid = False
elif email[-4:] != ".edu":
    valid = False
if len(password) < 8:
    valid = False
elif not ('A' <= password[0] <= 'Z'):
    valid = False
elif not any(char.isdigit() for char in password):
    valid = False
if len(referral) != 6:
    valid = False
elif referral[0:3] != "REF":
    valid = False
elif not (referral[3].isdigit() and referral[4].isdigit()):
    valid = False
elif referral[5] != "@":
    valid = False
if valid:
    print("Approved !!")
else:
    print("Rejected!!") 
