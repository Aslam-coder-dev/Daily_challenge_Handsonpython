print("=== Smart Transport System Login ===")

username = input("Enter username: ")
password = input("Enter password: ")

if username == "Aslam" and password == "SR310":
    print("Access Granted!!\n")

    n = int(input("Enter no.of weights: "))
    weights = [0] * n

    for i in range(n):
        weights[i] = int(input(f"Enter weight {i+1}: "))

    print("Entered Weights:", weights)

else:
    print("Access Denied ?? Unauthorized user")
