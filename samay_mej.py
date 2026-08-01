import random
days = ["Mon", "Tue", "Wed", "Thu", "Fri","Sat"]
periods = 9
break_slot = 5
subjects = ["Math", "Physics", "Chemistry", "English", "CS"]
extras = ["Games", "VE", "Lib"]
freq = {
    "Math": 6,
    "Physics": 6,
    "Chemistry": 6,
    "English": 6,
    "CS": 6
}
for e in extras:
    subjects.append(e)
    freq[e] = 1
double_sub = ["CS"]
total_slots = len(days) * (periods - 1)
current_total = sum(freq.values())
while current_total < total_slots:
    for s in subjects:
        if s not in extras:
            freq[s] += 1
            current_total += 1
            if current_total == total_slots:
                break
timetable = [["" for _ in range(periods)] for _ in range(len(days))]
remaining = []
for s in subjects:
    remaining.append([s, freq[s]])
positions = []
for i in range(len(days)):
    for j in range(periods):
        if j == break_slot - 1:
            timetable[i][j] = "BREAK"
        else:
            positions.append((i, j))
index = 0
stack = []
while index < len(positions):
    i, j = positions[index]
    if timetable[i][j] != "":
        prev = timetable[i][j]
        for x in remaining:
            if x[0] == prev:
                x[1] += 1
        timetable[i][j] = ""
    random.shuffle(remaining)
    remaining.sort(key=lambda x: -x[1]) 
    placed = False
    for k in range(len(remaining)):
        sub, count = remaining[k]
        if count <= 0:
            continue
        if j > 0 and timetable[i][j-1] == sub:
            continue
        if sub in double_sub and j < periods - 1:
            if timetable[i][j+1] == "" and (j+1) != break_slot - 1:
                timetable[i][j] = sub
                timetable[i][j+1] = sub
                remaining[k][1] -= 2
                stack.append((i, j, sub, 2))
                index += 2
                placed = True
                break
        timetable[i][j] = sub
        remaining[k][1] -= 1
        stack.append((i, j, sub, 1))
        index += 1
        placed = True
        break
    if not placed:
        if not stack:
            print("No valid timetable possible")
            break
        li, lj, lsub, lcount = stack.pop()
        timetable[li][lj] = ""
        if lcount == 2:
            timetable[li][lj+1] = ""
        for x in remaining:
            if x[0] == lsub:
                x[1] += lcount
        index = max(0, index - lcount)
col_width = 12
print("\nFINAL TIMETABLE\n")
print("Day".ljust(col_width), end="")
for p in range(1, periods+1):
    print(f"P{p}".center(col_width), end="")
print()
print("-" * col_width * (periods + 1))
for i in range(len(days)):
    print(days[i].ljust(col_width), end="")
    for j in range(periods):
        print(timetable[i][j].center(col_width), end="")
    print()
