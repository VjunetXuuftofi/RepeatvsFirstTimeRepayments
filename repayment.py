# Reads through all of the Kiva API loan data snapshots and determines the repayment rate for repeat borrowers and first
# time borrowers (identified by tags). Thanks to build.kiva.org for providing the snapshots.

import json

repeatpaid = 0
repeatdefault = 0
firstpaid = 0
firstdefault = 0

for i in range(1, 1980): #To read every loan file
    try:
        data = open('kiva_ds_json/loans/' + str(i) +'.json')
        data = json.load(data)
    except:
        continue
    for loan in data["loans"]:
            repeat = False
            first = False
            for tags in loan["tags"]:
                for tag in tags:
                    if tags[tag] == "#RepeatBorrower":
                        repeat = True
                    if tags[tag] == "#FirstLoan":
                        first = True
            if repeat:
                if loan["status"] == "paid":
                        repeatpaid += 1
                if loan["status"] == "defaulted":
                        repeatdefault += 1
            if first:
                if loan["status"] == "paid":
                    firstpaid += 1
                if loan["status"] == "defaulted":
                    firstdefault += 1

print("Repayment Rate for #RepeatBorrower: " + str(round((1-repeatdefault/(repeatpaid+repeatdefault))*100, 2)) + "%")
print("Repayment Rate for #FirstLoan: " + str((round((1-firstdefault/(firstpaid+firstdefault)*100), 2))) + "%")