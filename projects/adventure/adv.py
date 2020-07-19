from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# NEED TO KNOW:
    # player.current_room.id --> gives us the position of the player is on
    # player.current_room.get_exits() --> returns a list of directions or edges traveling from the position we are on.
    # player.travel() --> moves us the next room
    # player.travel(get_room_in_direction) --> gives us in which direction we want to move in the room we are.
    
    
# PLAYER AND ROOM DESCRIPTION METHODOLOGY
# Do we explored the room?
    # No:
        # if this room is not explored does it has any doors?
            # If Yes:
                # 1. How many doors we seeing?
                # 2. Store the doors in dictionary
                # 3. move towards one door
                # 4. remove the door we stored
                # 5. add directions to our path
                # 6. update exploration
                # 7. check again
            # if No:
                # 1. Return (reverse) back to our previous room(were we came from)
                # 2. Add directions to our path
                # 3. Check for another door(not the same one)-take a look at our storage(dictionary)

    # Yes:
        # Are there any doors left that needed to be explored?
            # if yes (move line 45 and follow the steps)
            # if no:
                # 1. Return (reverse) back to our previous room
                # 2. Add directions to our path
                # 3. Check for another door(not the same one)- take a look at our storage(dictionary)

# MVP
# We hit the jackpot when we reach our FINISH LINE visiting all the rooms of our maze(500)
# Goal ---> to traverse the graph by using as much as less steps < 2000
# Project MVP 1995 < 2000 !!!!!

# A dictionary to store rooms and their doors
visited = dict()

# direction for reverse navigation
reverse_nav = {"n":"s","e":"w","s":"n","w":"e"}

# Initialize as Stack
stack = Stack()

# we add in the stack our player.current_room were player is on
stack.push(player.current_room)

# Fire in the hole!
# while looping the length of the rooms we visited less than the length of our 500 maze
while len(visited) < len(world.rooms):
    # if the room we are looking for doesn't exist in our dict
    if player.current_room.id not in visited:
        # add to dictionary, with values(directions)
        visited[player.current_room.id] = player.current_room.get_exits()
        # for every connected room that hasn't been visited, then visit !
        if len(visited[player.current_room.id]) is not 0:
            # visit the last room
            next_room = visited[player.current_room.id].pop()
            print("pop", next_room)
            # save the directions for the reverse_nav!!
            stack.push(next_room)
            # Then append the direction to the traversal path
            traversal_path.append(next_room)
            # travel towards to the next room 
            player.travel(next_room)
        # if you find a deadend or there any more rooms to explore
        else:
            # get the last directions from the previous room 
            # were you stored them in the stack
            directions = stack.pop()
            # get the opposites ones directions
            prev_room = reverse_nav[directions]
            # move to the previous room
            player.travel(prev_room)
            # and add it to the traversal_path
            traversal_path.append(prev_room)
        # if the room has already been visited repeat the movement!
    else:
        if len(visited[player.current_room.id]) is not 0:
            # visit the last room
            next_room = visited[player.current_room.id].pop()
            print("pop",next_room)
            # save the reverse_nav!
            stack.push(next_room)
            #add the direction to the path
            traversal_path.append(next_room)
            # move the the next room!
            player.travel(next_room)
        # If you find a deadend or there are any other rooms to be explored
        else:
        # get the last directions from the previous room 
            # were you stored them in the stack
            directions = stack.pop()
            # get the opposites ones
            prev_room = reverse_nav[directions]
            # move to the previous room
            player.travel(prev_room)
            # and add it to the traversal_path
            traversal_path.append(prev_room)
            
print("TP:",traversal_path)
print("VISITED",visited)




# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
breakpoint()
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")