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
    affected_c = 0

    name = "Aslam Shaik"
    L = len(name.replace(" ", ""))
    PLI = L % 3

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

    if PLI == 0:
        for i in overload:
            invalid_entries.append(i)
            affected_c += 1
        overload = []

    elif PLI == 1:
        affected_c = len(very_light)
        very_light = []

    elif PLI == 2:
        affected_c = len(very_light) + len(overload)
        very_light = []
        overload = []

    print("\n--- Smart Transport Report ---")
    print("Name Length (L):", L)
    print("PLI Value:", PLI)
    print("Total Valid Packages:", valid_c)
    print("Packages affected by PLI:", affected_c)

    print("\n--- Final Loading Plan ---")
    print("Very Light Packages:", very_light)
    print("Normal Load Packages:", normal_load)
    print("Heavy Load Packages:", heavy_load)
    print("Overload Packages:", overload)
    print("Invalid Entries:", invalid_entries)

    print("\nAll trucks are ready for dispatch")

else:
    print("Access Denied ?? Unauthorized user")
