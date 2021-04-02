# triangle numero uno
star = ""
for i in range(0, 19):
    if i < 10:
        star += "*"
    else:
        star = star[1:]
    print(star)

#triangle numero dos
star2 = ""
for i in range(1, 10):
    star2 += ("*")*i
    print(star2)
for i in range (10, 0, -1):
    star2 = star2[i-1:]
    print(star2)

#triangle numero tres
star3 = "*"*21
count = 0
while star3:
    star4 = ""
    star4 += (" "*count + star3 + " " *count)
    count += 1
    star3 = star3[2:]
    print(star4)



if __name__ == "__main__":
    pass