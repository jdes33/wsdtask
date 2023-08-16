# Author: Jason De Souza
# Date: 16/08/23

################################################################
# Function for bonus task: different flow rates (bonus task 3) [changed param, added exception, changed line 118 and 139]
################################################################

import heapq
def compute_fill_time_different_flows(queue, flow_rates, walk_time=3):
    """Computes the time needed for queue of water bottles to be filled by taps

    Args:
        queue (int): The volumes in ml of each bottle in the queue, index 0 represents first bottle in queue
        flow_rates (float): The flow rate corresponding to each tap in ml/s
        walk_time (float): Time taken for any person in queue to walk to tap in seconds (default is 3)

    Returns:
        float:  Amount of time in seconds needed for all bottles to be filled
    """
    num_taps = len(flow_rates)

    formula = lambda queue_index, tap_index : queue[queue_index] / flow_rates[tap_index] + walk_time

    # assign first bottles to empty taps accounting for flow rate and walk time (intialise)
    taps = []
    for i in range(num_taps): # O(t)
        if i < min(num_taps, len(queue)):
            taps.append((formula(i, i), i))
        else:
            taps.append((0, i))

    # validation
    if any(map(lambda x: x < 0, queue)):
        raise Exception("Cannot have negative bottle volumes")
    if num_taps < 1:
        raise Exception("Must have at least one tap")
    if any(map(lambda x: x < 0, flow_rates)):
        raise Exception("Cannot have negative tap flow rates")
    if walk_time < 0:
        raise Exception("Cannot have negative time to walk to tap")

    heapq.heapify(taps) #O(t)

    q_idx = num_taps
    current_time = 0
    smallest_accumulator =  0
    while q_idx < len(queue): # O(q)

        smallest_value = taps[0][0] # first elem in heapq will always be smallest
        smallest_accumulator += smallest_value

        while taps[0][0] == smallest_value: # this loop can be thought of as part of the O(q) since it advances q ptr
            _ , tap_index =  heapq.heappop(taps) # O(log(t))
            heapq.heappush(taps, (smallest_accumulator + formula(q_idx, tap_index), tap_index)) # O(log(t))
            q_idx += 1 # move to next bottle

        current_time += smallest_value - smallest_accumulator # when reading time subtract 

    # wait for last bottle
    if taps:
        current_time += max(taps)[0] # O(t)

    # overall time complexity is O(t + t + q * 2 * logt + t) = O(qlogt)
    
    return current_time


#################################################
# Additional tests cases (Ignore)
#################################################

q1 = [200, 300, 150, 200]
q2 = [200, 300, 150, 200, 200, 300, 150, 200]
q3 = [200, 200, 200, 100, 100, 100]
q4 = [200, 200, 200, 100, 150, 100]

basic_flow_rate = 100

print("Running tests on varying flow rates function")

walk_time = 3
flow_rate = 100
assert (compute_fill_time_different_flows(
    q1, [100] * 2) == 500 / basic_flow_rate + 2 * walk_time)
assert (compute_fill_time_different_flows(
    q1, [50, 150]) == 200 / 50 + 200 / 50 + 2 * walk_time)  # different rates
# t1 takes 1s (+3 for walk), t2 takes 2 seconds (+3 for walk), so t1 gets big bottle => result 4s+ 13s = 17
assert (compute_fill_time_different_flows(
    queue=[100, 10, 1000], flow_rates=[100, 5]) == 17)
# t1 takes 1s (+3 for walk), t2 takes half a second (+3 for walk), so t2 gets big bottle => 3.5s + 53s = 56.5s
assert (compute_fill_time_different_flows(
    queue=[100, 10, 1000], flow_rates=[100, 20]) == 56.5)
# t1 takes 13s, t2 takes 103s, so t1 gets 8k and takes 83s which is 96s total so far so it then gets 10k which takes 103s totalling 199s
assert (compute_fill_time_different_flows(
    queue=[1000, 1000, 8000, 10000], flow_rates=[100, 10]) == 199)
# t1 takes 13s, t2 takes 53s, so t1 gets 8k and takes 83s which is 96 total so far so t2 gets 10k this time which takes 503 seconds totalling 556s
assert (compute_fill_time_different_flows(
    queue=[1000, 1000, 8000, 10000], flow_rates=[100, 20]) == 556)

#assert(compute_fill_time_with_walk([], 0) == 0) # no taps raises error as expected
assert(compute_fill_time_different_flows(queue=[], flow_rates=[10, 20, 50]) == 0)# no people in queue
assert(compute_fill_time_different_flows(queue=[100, 60], flow_rates=[10, 20, 50]) == 13)# len(queue) < num_taps