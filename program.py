#Advent Of Code day 02
start_vert = 0
start_hori = 0

aim = 0
second_vert = 0
second_hort = 0

depth_num = []
splitted_num = []

with open('input.txt') as f:
    lines = f.read().splitlines()

    for i in lines:
    	depth_num.append(i)

    for i in depth_num:
    	splitted_num.append(i.split())

    for i in splitted_num:
    	if i[0] == "forward":
    		#first part
    		start_hori = start_hori + int(i[1])
    		#second part
    		second_hort = second_hort + int(i[1])
    		second_vert = second_vert + (aim * int(i[1]))

    	elif i[0] == "down":
    		#first part
    		start_vert = start_vert + int(i[1])
    		#second part
    		aim = (aim + int(i[1]))

    	elif i[0] == "up":
    		# first part
    		start_vert = start_vert - int(i[1])
    		# second part
    		aim = aim - int(i[1])
    		

print(start_hori * start_vert)
print (second_hort * second_vert)
