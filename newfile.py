records = list()
rnames = list()
for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name,score])
n=len(records)
records=sorted(records, key = lambda x: x[1])
for i in range(n):
    if records[i][1]!= records[0][1]:
        second = records[i][1]
        break
rnames = [x[0] for x in records if x[1]==second]
rnames.reverse()
for j in rnames:
    print(j)
