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

    very_light = []
    normal_load = []
    heavy_load = []
    overload = []
    invalid_entries = []

    valid_c = 0

    for w in weights:
        if w < 0:
            invalid_entries.append(w)
        elif w <= 5:
            very_light.append(w)
            valid_c += 1
        elif w <= 25:
            normal_load.append(w)
            valid_c += 1
        elif w <= 60:
            heavy_load.append(w)
            valid_c += 1
        else:
            overload.append(w)
            valid_c += 1

    print("Very Light Packages:", very_light)
    print("Normal Load Packages:", normal_load)
    print("Heavy Load Packages:", heavy_load)
    print("Overload Packages:", overload)
    print("Invalid Entries:", invalid_entries)

else:
    print("Access Denied ?? Unauthorized user")
