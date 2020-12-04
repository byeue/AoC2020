passwords = []
mm = []
c = 0
pw = ""
pCorrect = 0

while True:
    inp = input()
    if inp == "":
        break
    passwords.append(inp)

for x in passwords:
    mm = x.split(" ")[0].split("-")
    c = x.find(":")
    pw = x.split(" ")[2]

    if ((pw[int(mm[0])-1] == x[c-1]) and (pw[int(mm[1])-1] != x[c-1])) or ((pw[int(mm[0])-1] != x[c-1]) and (pw[int(mm[1])-1] == x[c-1])):
        pCorrect += 1

print(pCorrect)
