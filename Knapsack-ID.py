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
resultlst = None # global variable for found goal state

# function for checking if current state is the goal
def check(lst):
    global target_value
    global target_weight
    global resultlst
    total_value = total_weight = 0
    for item in lst:
        total_value += item.value
        total_weight += item.weight
    if total_value >= target_value and total_weight <= target_weight: # Is this the goal state?
        resultlst=lst
        return True # the goal state
    if total_weight > target_weight: # Is this state exceed the weight limit?
        return True # exceed weight limit
    else:
        return False #need to continue searching

# depth first search
def DFS(selected_list, available_list, target_depth):
    if resultlst: 
        return # stop searching if goal state is found
    if len(selected_list) > target_depth:
        return # stop searching if depth goes beyond
    if check(selected_list):
        return # stop searching if current state is the goal
    else:
        for i in range(len(available_list)): # keep searching for next depth level
            next_list = selected_list.copy()
            next_avail_list = available_list[i+1:]
            next_list.append(available_list[i])
            DFS(next_list, next_avail_list, target_depth)


with open('test.txt') as f: # read input from 'test.txt'
    content = f.readline()
    target_value, target_weight = map(float, content.split(' '))
    lines = f.readlines()
    lst = []
    for line in lines: # insert each object into a list
        lst.append(Item(*line.split(None)))
for i in range(len(lst)): # driver for Iterative Deepening
    if resultlst: # stop searching if goal state is found
        break
    listC = lst.copy()
    st = []
    DFS(st, listC, i)
if resultlst: 
    print(resultlst) # output if the goal state is found
else:
    print('No solution')
