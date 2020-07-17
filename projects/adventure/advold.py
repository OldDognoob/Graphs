from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)

    def end(self):
        return self.stack[-1]

class Graph:

    # init a graph
    def __init__(self):
        self.verticies = {}

    def add_vertex(self, vertex):
        '''
        Add a vertex to the graph
        the vertex passed to us is going to be a room id number
        '''
        
        if vertex not in self.verticies:
            self.verticies[vertex] = {'n': '?', 's': '?', 'e': '?', 'w': '?'}

    def add_edge(self, vertex, key, value):
        '''
        Add an edge to the vertex
        Vertex should be a room id
        key should be a string of n,s,e,w
        value is going to be a room id 
        '''
        self.verticies[vertex][key] = value

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
# traversal_path = []



# The main purpose is:
# To explore the connecting rooms by walking from room to room
# and keep in track our directions using the fastest sufficient search.

# What we need to bare in mind:
# these '?' are unexplored rooms
# we are recording the direction we took to get into the room so the "traversal_path" will be 
# later populated with 500 rooms of the maze
# we adding reverse directions se we can move backwards if we need to
directions = {'n':'s', 's':'n','w':'e','e':'w'}
# player.current_room.id => This will give us the current room id
# player.current_room.get_exits() => it points out a return list of possible moves
# player.travel(direction) => This will allow us to traverse to rooms
# Graph Class lines to follow:
# vertex will be the current room ID
# edges will be the rooms that the room ID connects
# the keys will be a room id
# the values will be a dictionary, where n,s,w,e values will be the room id for making our move

def build_path(graph, starting_room = 0):
    """
    Using Depth-First Traversal to traverse the maze.
    """

    # Create an empty stack that contains our current path
    s = Stack()
    # Create an array to hold the moves of our path
    moves = []
    # Set a visited list
    visited = set()
    # start our traversal with the 0 index room
    s.push([starting_room])
    # While length of the rooms we visited is less than the 500 rooms of maze
    while len(visited) < len(graph):
        # get the id of the current room in the stack
        path = s.pop()
        room_id = path[-1]
        # mark as visited
        visited.add(room_id)
        # get information on the current room 
        current_room = graph[room_id]
        # add the moves we are doing in the current room in our room dictionary
        rooms_dict = current_room[1]
        # set an array of unexplored rooms that I have not visited
        unexplored= []
        # store undiscovered rooms in relationship to the current room
        for direction, room_id in rooms_dict.items():
            # if it not visited
            if room_id not in visited:
                # add the number of our room in the unexplored list
                unexplored.append(room_id)
        # assign the next room
        # if we reached a dead end, reverse back
        if len(unexplored) > 0:
            # if our next room is unexplored push the next room onto the stack
            next_room = unexplored[0]
            s.push(next_room)
        else:
            # otherwise remove the next room and exit the traversal path
            s.pop()
            next_room = s.end()

        # explore the rooms around our current room. 
        # if the next move matches the room_id, add that to moves
        # adjacent id in rooms dict is the same with the next room add the direction to the 
        # traversal path and move to the next room
        for direction, adjacent_id in rooms_dict.items():
            if adjacent_id == next_room:
                moves.append(direction)

    return moves


traversal_path = build_path(room_graph)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
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