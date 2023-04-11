from ast import ListComp
from json.encoder import INFINITY
from random import random

# defining object with name, weight, and value
class Item:
    def __init__(self, name, value, weight) -> None:
        self.name = name
        self.weight = float(weight)
        self.value = float(value)

    def __str__(self):
        return self.name

    def __repr__(self) -> str:
        return self.__str__()


target_weight = 0 # global variable for weight limit
target_value = 0 # global variable for goal value

# error function calculator
def error(lst):
    global target_value
    global target_weight
    weight = 0
    value = 0
    for item in lst:
        weight += item.weight
        value += item.value
    return max(0,weight-target_weight)+max(0,target_value-value)

# random state generator
def restart(lst):
    random_lst=[]
    for item in lst:
        prob = random()
        if prob < 0.5:
            random_lst.append(item)
    return random_lst

# function for searching the neighbor with lowest error
def search(lst,current_state):
    max_error = INFINITY
    next_state = []
    for item in lst:
        if item not in current_state:
            neighbor = current_state.copy()
            neighbor.append(item) # adding a new object
            if max_error>error(neighbor):
                max_error = error(neighbor)
                next_state = neighbor
            for itemN in current_state: 
                copy_neighbor = neighbor.copy()
                copy_neighbor.remove(itemN) # swapping the new object with an old object in the state
                if max_error>error(copy_neighbor):
                    max_error = error(copy_neighbor)
                    next_state = copy_neighbor
        else:
            neighbor = current_state.copy()
            neighbor.remove(item) # deleting an old object
            if max_error>error(neighbor):
                max_error = error(neighbor)
                next_state = neighbor
    return next_state


with open('test.txt') as f: # read input from 'test.txt'
    content = f.readline()
    target_value, target_weight = map(float, content.split(' '))
    lines = f.readlines()
    lst = []
    for line in lines: # insert each object into a list
        lst.append(Item(*line.split(None)))
    result_list = []
    for i in range(10): # restart 10 times
        current_state = next_state = restart(lst)
        while True:
            if error(current_state) == 0: # check if it is the goal currently
                result_list = current_state
                break # stop searching if the goal state is found
            next_state = search(lst,current_state) 
            if error(next_state)<=error(current_state): # check if the best neighbor is valid
                current_state = next_state 
            else:
                break # stop searching if all neighjbors' errors are larger than that of current state which is not equal to 0
    if result_list:
        print(result_list)
    else:
        print('No Solution')



