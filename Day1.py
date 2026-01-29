full_name = input("Enter Full Name: ")
email = input("Enter Email ID: ")
mobile = input("Enter Mobile Number: ")
age = int(input("Enter Age: "))

valid = True

if full_name[0] == " " or full_name[-1] == " ":
    print("Invalid : Full Name should not start or end with a space")
    valid = False
elif " " not in full_name:
    print("Invalid : Full Name must contain at least two words")
    valid = False

if valid:
    if "@" not in email or "." not in email:
        print("Invalid : Email must contain '@' and '.'")
        valid = False
    elif email[0] == "@":
        print("Invalid : Email must not start with '@'")
        valid = False
    elif (" " in email or "!" in email or "#" in email or "$" in email or
          "%" in email or "^" in email or "&" in email or "*" in email or
          "(" in email or ")" in email or "_" in email or "+" in email or
          "-" in email or "=" in email or "{" in email or "}" in email or
          "[" in email or "]" in email or "|" in email or "\\" in email or
          ":" in email or ";" in email or "\"" in email or "'" in email or
          "<" in email or ">" in email or "," in email or "?" in email or
          "/" in email or '0' in email or '1' in email or '2' in email or
          '3' in email or '4' in email or '5' in email or '6' in email or
          '7' in email or '8' in email or '9' in email):
        print("Invalid : Email contains invalid characters")
        valid = False

if valid:
    if mobile[9] and mobile[10:]:
        print("Invalid : Mobile number must be exactly 10 digits")
        valid = False
    elif mobile[0] == "0":
        print("Invalid : Mobile number must not start with 0")
        valid = False
    elif not ('0' <= mobile[0] <= '9' and
              '0' <= mobile[1] <= '9' and
              '0' <= mobile[2] <= '9' and
              '0' <= mobile[3] <= '9' and
              '0' <= mobile[4] <= '9' and
              '0' <= mobile[5] <= '9' and
              '0' <= mobile[6] <= '9' and
              '0' <= mobile[7] <= '9' and
              '0' <= mobile[8] <= '9' and
              '0' <= mobile[9] <= '9'):
        print("Invalid : Mobile number must contain only digits")
        valid = False

if valid:
    if age < 18 or age > 60:
        print("Invalid : Age must be between 18 and 60")
        valid = False


if valid:
    print("User Profile is VALID")
else:
    print("User Profile is INVALID")
