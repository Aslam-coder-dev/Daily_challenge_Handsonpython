import random
import math
import numpy as np
import pandas as pd
import copy

def jer_auth():
    ans = int(input("Enter Virat Kohli Test Runs: "))
    if ans != 9230:
        print("Authentication Failed")
        exit()
    print("Welcome Player")

def build(n):
    data=[]
    for i in range(n):
        data.append({
            "zone": i+1,
            "metrics":{
                "traffic": random.randint(70,200),
                "pollution": random.randint(50,150),
                "energy": random.randint(60,180)
            },
            "history":[random.randint(20,100) for _ in range(6)]
        })
    return data

def personalize(data, roll):
    if roll%2==0:
        return list(reversed(data))
    return data[3:]+data[:3]

def custom_risk(d):
    m=d["metrics"]
    return math.log(m["traffic"]+m["pollution"]+m["energy"])

def update(data):
    for d in data:
        d["metrics"]["energy"] += 12
        d["history"].append(random.randint(30,90))
        d["risk"]=custom_risk(d)

def convert(data):
    rows=[]
    for d in data:
        rows.append([
            d["zone"],
            d["metrics"]["traffic"],
            d["metrics"]["pollution"],
            d["metrics"]["energy"],
            d.get("risk",0)
        ])
    return pd.DataFrame(rows,columns=["zone","traffic","pollution","energy","risk"])

def manual_corr(a,b):
    am=np.mean(a)
    bm=np.mean(b)
    return sum((a-am)*(b-bm))/math.sqrt(sum((a-am)**2)*sum((b-bm)**2))

def clusters(df):
    risky=df[df["risk"]>df["risk"].mean()]["zone"].tolist()
    result=[]
    temp=[]
    for z in risky:
        if not temp or z==temp[-1]+1:
            temp.append(z)
        else:
            result.append(temp)
            temp=[z]
    if temp:
        result.append(temp)
    return result

jer_auth()

roll=703

original=personalize(build(15),roll)
assign=original
shallow=copy.copy(original)
deep=copy.deepcopy(original)

print("Before:",original[0])

update(shallow)

print("After shallow:",original[0])

update(deep)

df=convert(original)

mean=df.mean()
std=df.std()

anomaly=df[
    (df["traffic"]>mean["traffic"]+std["traffic"])|
    (df["pollution"]>mean["pollution"]+std["pollution"])|
    (df["energy"]>mean["energy"]+std["energy"])
]

stability=1/df["risk"].var()

max_risk=df["risk"].max()
min_risk=df["risk"].min()

final="Critical Failure" if len(anomaly)>5 else "Moderate Risk"

print(df)
print("Anomaly Zones:",list(anomaly["zone"]))
print("Correlation:",manual_corr(df["traffic"],df["pollution"]))
print("Clusters:",clusters(df))
print("Tuple:",(max_risk,min_risk,stability))
print("Decision:",final)
