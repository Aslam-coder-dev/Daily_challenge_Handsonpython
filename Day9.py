import copy

def cricket_auth():
    answer = input("How many runs has Virat Kohli scored in Test cricket? ")
    correct_runs = 9000
    try:
        if abs(int(answer) - correct_runs) <= 200:
            print("Access Granted")
            return True
        else:
            print("Access Denied")
            return False
    except:
        print("Invalid Input")
        return False

def get_roll_logic():
    roll = int(input("Enter your roll number: "))
    if roll % 2 == 0:
        print("Even Roll Number - Add File Logic")
    else:
        print("Odd Roll Number - Remove File Logic")
    return roll

def gen_data():
    return [
        {"id": 1, "data": {"files": ["a.txt", "b.txt"], "usage": 500}},
        {"id": 2, "data": {"files": ["c.txt"], "usage": 300}}
    ]

def rep_data(original):
    assigned = original
    shallow = copy.copy(original)
    deep = copy.deepcopy(original)
    return assigned, shallow, deep

def mod_data(data, roll):
    for user in data:
        if roll % 2 == 0:
            user["data"]["files"].append("new_file.txt")
        else:
            if user["data"]["files"]:
                user["data"]["files"].pop(0)
        user["data"]["usage"] += 100

def integrity_check(original, shallow, deep):
    leakage_count = 0
    safe_count = 0
    overlap_files = set()

    for i in range(len(original)):
        org_files = set(original[i]["data"]["files"])
        shallow_files = set(shallow[i]["data"]["files"])
        deep_files = set(deep[i]["data"]["files"])

        if org_files == shallow_files:
            leakage_count += 1

        if org_files != deep_files:
            safe_count += 1

        overlap_files.update(org_files.intersection(shallow_files))

    return (leakage_count, safe_count, len(overlap_files))

def explain():
    print("Inner list got affected because shallow copy shares references of nested mutable objects.")
    print("So when the files list is modified, both original and shallow copy reflect the change.")
    print("Deep copy avoids this by creating completely independent nested objects.")

def main():
    access = cricket_auth()
    roll = get_roll_logic()

    original = gen_data()
    print("Before Modification:", original)

    assigned, shallow, deep = rep_data(original)

    if access:
        mod_data(shallow, roll)
        mod_data(deep, roll)
    else:
        print("Modification Blocked")

    print("After Modification:")
    print("Original:", original)
    print("Assigned:", assigned)
    print("Shallow:", shallow)
    print("Deep:", deep)

    report = integrity_check(original, shallow, deep)
    print("Integrity Report:", report)

    explain()

main()
