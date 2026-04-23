import random
import math
import numpy as np
import pandas as pd
def gen_data(n=18):
    data = []

    traffic_lst = list(range(0, 101))
    aqi_lst = list(range(0, 301))
    energy_lst = list(range(0, 501))

    data.append({"zone": 1, "traffic": 0, "air_quality": 50, "energy": 100})
    data.append({"zone": 2, "traffic": 90, "air_quality": 280, "energy": 450})
    data.append({"zone": 3, "traffic": 75, "air_quality": 150, "energy": 480})

    for i in range(4, n+1):
        record = {
            "zone": i,
            "traffic": random.choice(traffic_lst),
            "air_quality": random.choice(aqi_lst),
            "energy": random.choice(energy_lst)
        }
        data.append(record)

    return data

def classify_zone(record):
    if record["air_quality"] > 200 or record["traffic"] > 80:
        return "High Risk"
    elif record["energy"] > 400:
        return "Energy Critical"
    elif record["traffic"] < 30 and record["air_quality"] < 100:
        return "Safe Zone"
    else:
        return "Moderate"

def calculate_risk(record):
    return round(
        record["traffic"] * 0.4 +
        record["air_quality"] * 0.4 +
        record["energy"] * 0.2, 2
    )

def custom_sort(data, key):
    for i in range(1, len(data)):
        current = data[i]
        j = i - 1

        while j >= 0 and data[j][key] < current[key]:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = current

    return data


def det_pat(df):
    threshold = df["risk_score"].mean()

    multi_risk = df[(df["risk_score"] > threshold) & (df["air_quality"].diff() > 0)]

    stability = np.var(df["traffic"]) < 500

    clus = []
    curr_clus = []

    for i in range(len(df)):
        if df.loc[i, "risk_score"] > threshold:
            curr_clus.append(df.loc[i, "zone"])
        else:
            if len(curr_clus) >= 2:
                clus.append(curr_clus)
            curr_clus = []

    return multi_risk, stability, clus


def main():
    roll_number = 703

    jersey = int(input("Enter your favourite jersey number: "))

    data = gen_data()

    if jersey == 18:
        print("\nChampion Mode Activated (Jersey 18)")
        for d in data:
            d["traffic"] = min(100, d["traffic"] + 10)
            d["air_quality"] = min(300, d["air_quality"] + 20)
        city_tag = "Champion City"
    else:
        city_tag = "Normal City"

    print("\nCity Mode:", city_tag)

    if roll_number % 3 == 0:
        random.shuffle(data)
    else:
        data = custom_sort(data, "traffic")

    for d in data:
        d["category"] = classify_zone(d)
        d["risk_score"] = calculate_risk(d)
        d["sqrt_risk"] = math.sqrt(d["risk_score"])

    df = pd.DataFrame(data)

    matrix = df[["traffic", "air_quality", "energy"]].values
    mean_values = np.mean(matrix, axis=0)

    sorted_data = custom_sort(data.copy(), "risk_score")
    top3 = sorted_data[:3]

    mul_risk, stability, clusters = det_pat(df)

    max_risk = df["risk_score"].max()
    avg_risk = df["risk_score"].mean()
    min_risk = df["risk_score"].min()
    risk_tuple = (max_risk, avg_risk, min_risk)

    if avg_risk < 100:
        decision = "City Stable"
    elif avg_risk < 180:
        decision = "Moderate Risk"
    elif avg_risk < 250:
        decision = "High Alert"
    else:
        decision = "Critical Emergency"

    print("\n=== DataFrame ===")
    print(df)

    print("\n=== Mean Values (Traffic, AQI, Energy) ===")
    print(mean_values)

    print("\n=== Top 3 Risk Zones ===")
    for z in top3:
        print(z)

    print("\n=== Risk Tuple ===")
    print(risk_tuple)

    print("\n=== Multi-factor Risk Zones ===")
    print(mul_risk[["zone", "risk_score"]])

    print("\n=== Stability ===")
    print("Stable Traffic" if stability else "Unstable Traffic")

    print("\n=== Critical Clusters ===")
    print(clusters)

    print("\n=== FINAL DECISION ===")
    print(decision)


main()
