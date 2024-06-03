# Group: Irvin Rafael, Joshua Villareal
# CPSC481-02
# June 14, 2023
#Project 1
from search import *

class MissCannibals(Problem):
    #DONE: constructor (already completed)
    def __init__(self, M=3, C=3, goal=(0, 0, False)):
        #false means boat is on right, true means boat is on left
        initial = (M, C, True)
        self.M = M
        self.C = C
        super().__init__(initial, goal)

    #DONE: method goal_test(state) (default in the Problem superclass is sufficient)
    def goal_test(self, state):
        return super().goal_test(state)

    #DONE: method result(state, action) that returns the new state reached from the given state and action
    def result(self, state, action):
        #Assume that the state and action is valid
        m = state[0]
        c = state[1]
        side = not state[2]

        #if boat is on left side
        if state[2]:
            #since boat is currently on left we
            #decrease amount on left
            if action == 'MM':
                m -= 2
            elif action == 'M':
                m -= 1
            elif action == 'CC':
                c -= 2
            elif action == 'C':
                c -= 1
            elif action == 'MC':
                m -= 1
                c -= 1
        #if boat is on right side
        else:
            #since boat is currently on right we
            #increase the amount on left
            if action == 'MM':
                m += 2
            elif action == 'M':
                m += 1
            elif action == 'CC':
                c += 2
            elif action == 'C':
                c += 1
            elif action == 'MC':
                m += 1
                c += 1
        return (m,c,side)

    #DONE: method actions(state) that returns a list of valid actions in the given state
    def actions(self, state):
        possible_act = ['M', 'C', 'MC', 'MM', 'CC']
        valid_act = []

        for act in possible_act:
            test_state = self.result(state, act)
            m = test_state[0]
            c = test_state[1]
            #if m/c is negative or bigger than possible ignore it
            if m < 0 or c < 0 or self.M < m or self.C < c:
                continue
            #if m is smaller than c at either side while m != 0 ignore
            if (m < c) and m > 0:
                continue
            if (self.M - m < self.C - c) and self.M - m > 0:
                continue
            #if act didnt get ignored then add it
            valid_act.append(act)
        return valid_act

if __name__ == '__main__':
    mc = MissCannibals(M=3, C=3)

    path = depth_first_graph_search(mc).solution()
    print(path)
    path = breadth_first_graph_search(mc).solution()
    print(path)

    #Tests for method actions()
    # print(mc.actions((3, 2, True))) # Test your code as you develop! This should return  ['CC', 'C', 'M']
    # print(mc.actions((1,1,False)))

    #tests for method result()
    # print(mc.result(state=(3,3,True),action="MM"))
    # print(mc.result(state=(2,2,False),action="MC"))
