calendar = {"월": [], "화": [], "수": [], "목": [], "금": []}
cnt = 0
while cnt < 8:
    cnt += 1
    input_name = input()
    if input_name[0:3] == "강유림":
        name = input_name[0:3]
    else:
        name = input_name[5:9]

    name = name.strip(" ")

    input_str = input()
    result = [i for i in input_str if i in "월화수목금"]

    for val in result:
        calendar[val].append(name)


for day, names in calendar.items():
    print(f'{day} : {", ".join(names)}')
