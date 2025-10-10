import copy

def SHALLOW_COPY():
    l1 = [1, 2, [3, 4]]
    l2 = copy.copy(l1)
    
    l2[0] = 100
    l2[2][0] = 300
    
    print(l1)
    print(l2)

def DEEP_COPY():
    l1 = [1, 2, [3, 4]]
    l2 = copy.deepcopy(l1)
    
    l2[0] = 100
    l2[2][0] = 300
    
    print(l1)
    print(l2)

SHALLOW_COPY()
DEEP_COPY()