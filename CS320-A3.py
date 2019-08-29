import sys

# we can solve problem 1 by starting with the time interval that
# has minimum f(i) time.
# perhaps can hold the information in an Nx2 matrix where N is the number
# of interval pairs.
# could implement matrix using an array of arrays

def create_matrix_array(n):
    """
    create a list that contains a 'matrix' which is just a list of list e.g.
    below has two 'matrices' a 2x2 and 2x3.
    [ <- refer by variable
        [ <- refer by index - var[i]
            [1,2], <- refer by second index - var[i][j]
            [3,4] 
        ]
        ,
        [   [2,3,4],
            [3,5,6],
        ]
    ]
    one list contains start times, one list corresponding end times
    """
    matrix_array = [[] for x in range(n)] # creates n separate lists
    for i in range(n):
        inp = sys.stdin.readline()[:-1]
        inp = inp.replace(" ", "")
        A = list(inp[::2]) 
        B = list(inp[1::2])
        for j in range(len(A)):
            A[j] = int(A[j])
        for j in range(len(B)):
            B[j] = int(B[j])
        matrix_array[i].append(A) # can turn A's B's into tuples by:
        matrix_array[i].append(B) # tuple(A) tuple(B)
    return matrix_array

def solve_1(x):
    ''' n = int(sys.stdin.readline()[:-1])
    matrix_array = create_matrix_array(n) # this is like R in the book '''
    matrix_array = x # test case
    for i in range(len(matrix_array)):
        A = []
        while len(matrix_array[i][0]) != 0:
            counter = 0
            '''initial add of the first timeslot to the A matrix'''
            min_finish_time = min(matrix_array[i][1]) # get the minimum finish time (value)
            min_finish_index = matrix_array[i][1].index(min_finish_time) # get the index of minimum finish time (index)
            interval_start = matrix_array[i][0].pop(min_finish_index) # get the start of interval (value)
            interval_end = matrix_array[i][1].pop(min_finish_index) # get the end of interval (value) essentially the same as min_finish_time (?)
            A.append([interval_start, interval_end]) # append the interval (list) to A
            stop = False
            while stop == False:
                if len(matrix_array[i][0]) != 0:
                    next_interval_start = matrix_array[i][0][0] # (value)
                    next_interval_end = matrix_array[i][1][0] # (value)
                    if next_interval_start == next_interval_end:
                        '''if a timeslot is instantenous then it's a freebie add to A'''
                        A.append([matrix_array[i][0].pop(0),matrix_array[i][1].pop(0)])
                    elif next_interval_start <= interval_end and next_interval_end >= interval_end:
                        del(matrix_array[i][0][0])
                        del(matrix_array[i][1][0])
                    else:
                        interval_start = A[counter][0]
                        interval_end = A[counter][1]
                        A.append([matrix_array[i][0].pop(0), matrix_array[i][1].pop(0)])
                        counter += 1
                else:
                    stop = True
        print(len(A))

x = [
    [[1,0,3],[3,2,4]],
    [[0,1,1,4],[3,2,3,4]],
    [[0,3,5,3,2],[2,4,6,6,4]],
    [[1,1,1,1,1],[1,2,3,4,5]]
    ]

print(solve_1(x))