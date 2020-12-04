passwords = []
mm = []
c = 0
pCorrect = 0

while True:
    inp = input()
    if inp == "":
        break
    passwords.append(inp)

for x in passwords:
    mm = x.split(" ")[0].split("-")
    c = x.find(":")
    
    if ((x.count(x[c-1])-1) >= int(mm[0])) & ((x.count(x[c-1])-1) <= int(mm[1])):
        pCorrect += 1

print(pCorrect)
