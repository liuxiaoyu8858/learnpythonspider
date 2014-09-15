from random import choice
cave_number =range(0,20)
user_loc = choice(cave_number)
v_loc =choice (cave_number)
while user_loc == v_loc:
    user_loc =choice (cave_number)


print "it has ",len(cave_number),"caves"



while True:
    print "now you are at ",user_loc
    if v_loc== user_loc+1 or v_loc==user_loc -1:
        print "it's near you"
    loc=raw_input("please input a loc to find the cave>")
    if not loc.isdigit() or  int(loc) not in cave_number:
        print loc,"is not a cave"
    else:
        user_loc = int (loc)
        if user_loc ==v_loc:
            print"you find it"
            break
raw_input("any key continue")
