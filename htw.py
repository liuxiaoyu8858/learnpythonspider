from random import choice
def setup_caves(caves_number):
        """create caves empty list"""	
	caves=[]
	for i in caves_number:
    		caves.append([])
		return caves

def visit_cave(cave_number):
	"""visit a cave """""
	visited_caves.append(cave_number)
	unvisited_caves.remove(cave_number)

def print_caves():
	"""print the net of caves"""
	for i in caves_number:
    		print i,":",caves[i]
		print "--------------------------------"

def choose_cave(caves_list):
	"""select a caves which has less than 3 tunel from the number"""
	cave=choice(caves_list)
	while len(caves[cave])>=3:
    		cave=choice(caves_list)
	return cave

def create_tunel(cave_from,cave_to):
	"""make tunel between two cave"""
	caves[cave_from].append(cave_to)
	caves[cave_to].append(cave_from)


def link_caves():
	"""link the caves"""
	while unvisited_caves !=[]:
    		this_cave=choose_cave(visited_caves)
    		next_cave=choose_cave(unvisited_caves)
    		create_tunel(this_cave,next_cave)
    		visit_cave(next_cave)
        

def finish_caves():
	"""at least 3 tunel"""
	for cave in caves_number:
	    while len(caves[cave])<3:
	        j=choose_cave(caves_number)
     		caves[cave].append(j)
	        create_tunel(cave,j)
        
def print_location(location):
	"""location"""
	print "you are in the cave",location
	print "you can see caves",caves[location]
	if v_loc in caves[location]:
	    print "its near here"

def get_next_loc():
	""" get a new loction"""
	print "from here you can see the caves as follow:",caves[u_loc]
	cave=raw_input("please choose a cave")
	if not cave.isdigit()or int(cave) not in caves[u_loc]:
    		return None
	else:
    		return cave


caves_number=range(0,20)
unvisited_caves=range(0,20)
visited_caves=[]
caves=setup_caves(caves_number)

visit_cave(0)
print_caves()
link_caves()
print_caves()
finish_caves()

v_loc=choice(caves_number)
u_loc=choice(caves_number)
while u_loc==v_loc:
    u_loc=choice(caves_number)
while True:
    print_location(u_loc)
    new_location=get_next_loc()
    if new_location is not None:
        u_loc=new_location
    if u_loc==v_loc:
        print "you got the v"
        break
