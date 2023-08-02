# Author: Jason De Souza
# Date: 2/08/23

##########################################################################
# Function for main/most basic task (with input validation, bonus task 1)
##########################################################################
def compute_fill_time_basic(queue, num_taps):
    """Computes the time needed for queue of water bottles to be filled by taps (flowing at 100ml/s)

    Args:
        queue (int): The volumes in ml of each bottle in the queue, index 0 represents first bottle in queue
        num_taps (int): Number of taps at festival

    Returns:
        float:  Amount of time in seconds needed for all bottles to be filled
    """
    
    flow_rate = 100
    # assign first bottles to empty taps (intialise)
    # list holding current state of taps (time remaining in seconds)
    taps = [0] * num_taps
    for i in range(min(num_taps, len(queue))):
        taps[i] = queue[i] / flow_rate

    # validation
    if any(map(lambda x: x < 0, queue)):
        raise Exception("Cannot have negative bottle volumes")
    if num_taps < 1:
        raise Exception("Must have at least one tap")

    q_idx = num_taps
    current_time = 0
    while q_idx < len(queue):
        smallest = min(taps)
        # finish bottle at tap with least remaining and add new bottles where zero
        for idx in range(len(taps)):
            taps[idx] -= smallest
            if taps[idx] == 0:
                # add next bottle
                taps[idx] = queue[q_idx] / flow_rate
                q_idx += 1

        current_time += smallest

    # wait for last bottle
    return current_time + max(taps)

##############################################################
# Function for bonus task: time to walk to tap (bonus task 2) [added param, exception and changed line 70 and 89]
##############################################################


def compute_fill_time_with_walk(queue, num_taps, walk_time=3):
    """Computes the time needed for queue of water bottles to be filled by taps (flowing at 100ml/s).

    Args:
        queue (int): The volumes in ml of each bottle in the queue, index 0 represents first bottle in queue
        num_taps (int): Number of taps at festival
        walk_time (float): Time taken for any person in queue to walk to tap in seconds (default is 3)

    Returns:
        float:  Amount of time in seconds needed for all bottles to be filled
    """

    flow_rate = 100
    # assign first bottles to empty taps and add walk time (intialise)
    # list holding current state of taps (time remaining in seconds)
    taps = [0] * num_taps
    for i in range(min(num_taps, len(queue))):
        taps[i] = queue[i] / flow_rate + walk_time

    # validation
    if any(map(lambda x: x < 0, queue)):
        raise Exception("Cannot have negative bottle volumes")
    if num_taps < 1:
        raise Exception("Must have at least one tap")
    if walk_time < 0:
        raise Exception("Cannot have negative time to walk to tap")

    q_idx = num_taps
    current_time = 0
    while q_idx < len(queue):
        smallest = min(taps)
        # subtract from all and add new bottle where zero
        for idx in range(len(taps)):
            taps[idx] -= smallest
            if taps[idx] == 0:
                # add next bottle
                taps[idx] = queue[q_idx] / flow_rate + walk_time
                q_idx += 1

        current_time += smallest

    # wait for last bottle
    return current_time + max(taps)

################################################################
# Function for bonus task: different flow rates (bonus task 3) [changed param, added exception, changed line 119 and 139]
################################################################


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
    # assign first bottles to empty taps accounting for flow rate and walk time (intialise)
    taps = [0] * num_taps
    for i in range(min(num_taps, len(queue))):
        taps[i] = queue[i] / flow_rates[i] + walk_time

    # validation
    if any(map(lambda x: x < 0, queue)):
        raise Exception("Cannot have negative bottle volumes")
    if num_taps < 1:
        raise Exception("Must have at least one tap")
    if any(map(lambda x: x < 0, flow_rates)):
        raise Exception("Cannot have negative tap flow rates")
    if walk_time < 0:
        raise Exception("Cannot have negative time to walk to tap")

    q_idx = num_taps
    current_time = 0
    while q_idx < len(queue):
        smallest = min(taps)
        # subtract from all and add new bottle where zero
        for idx in range(len(taps)):
            taps[idx] -= smallest
            if taps[idx] == 0:
                # add next bottle
                taps[idx] = queue[q_idx] / flow_rates[idx] + walk_time
                q_idx += 1

        current_time += smallest

    # wait for last bottle
    return current_time + max(taps)

############################################################
# Bonus task 4 (two examples shown, can ignore explanation)
############################################################

# Yes, increasing the flow rate of at least one tap could lead to a longer overall time based on my function.
# The most basic example is when there are two taps, one fast and one slower. As for the bottles there are three, the last one having a large volume.
# Initially the first two bottles will be assigned to each of the taps and the faster tap will finish first (assuming equal len) and get the third bottle with big volume.
# To make the whole process take longer we can increase the speed of the slower tap so that it finishes it's first bottle before tap 1 finishes it's first.
# But we have a constraint that we can't increase tap 2's speed to match or exceed tap 1's speed or the whole process may finish just as fast
# (we want it to fill the big bottle slower than when tap 1 had it). Thus as well as increasing rate of slower tap, we decrease the volume of it's the first bottle it's assigned.
# note: the 3s in the calculations are for default walking times


print("\nExample 1 before:")
# t1 takes 1s (+3 for walk), t2 takes 2 seconds (+3 for walk), so t1 gets big bottle => result 4s+ 13s = 17
print(compute_fill_time_different_flows(
    queue=[100, 10, 1000], flow_rates=[100, 5]))
print("\nExample 1 after:")
# t1 takes 1s (+3 for walk), t2 takes half a second (+3 for walk), so t2 gets big bottle => 3.5s + 53s = 56.5s
print(compute_fill_time_different_flows(
    queue=[100, 10, 1000], flow_rates=[100, 20]))

# When more than 1 tap is free my function assumes an implicit ordering of the taps to assign the next person in the queue to a free tap.
# In the example above bottle 1 always goes to tap 1 and bottle 2 always goes to tap 2 at the start.
# (There wasn't a requirement compute min/max time to fill all bottles, if so then one possibility is a recursive function that recurses whenever more than one tap is simultaneously free to go over all the different assignments, bubbling up the min/max and the base case to be when it finishes queue).
# So one could argue that the above example only works due to this overlook/assumption.
# Thus without having to implement the recursive solution I present another example where switchning the order of the bottles when more than 1 tap is free wouldn't result in lower time.
# I do this by simply making the first two bottles have same volume, so even if they were switched it wouldn't matter.
# note: the 3s in the calculations are for default walking times
print("\nExample 2 before:")
# t1 takes 13s, t2 takes 103s, so t1 gets 8k and takes 83s which is 96s total so far so it then gets 10k which takes 103s totalling 199s
print(compute_fill_time_different_flows(
    queue=[1000, 1000, 8000, 10000], flow_rates=[100, 10]))
print("\nExample 2 after:")
# t1 takes 13s, t2 takes 53s, so t1 gets 8k and takes 83s which is 96 total so far so t2 gets 10k this time which takes 503 seconds totalling 556s
print(compute_fill_time_different_flows(
    queue=[1000, 1000, 8000, 10000], flow_rates=[100, 20]))

#################################################
# Additional tests cases (Ignore)
#################################################

q1 = [200, 300, 150, 200]
q2 = [200, 300, 150, 200, 200, 300, 150, 200]
q3 = [200, 200, 200, 100, 100, 100]
q4 = [200, 200, 200, 100, 150, 100]

basic_flow_rate = 100

print("Running tests on basic function")
assert (compute_fill_time_basic(q1, 2) == 500 / basic_flow_rate)
assert (compute_fill_time_basic(q2, 3) == 600 / basic_flow_rate)
assert (compute_fill_time_basic(q3, 3) == 300 / basic_flow_rate)
assert (compute_fill_time_basic(q4, 3) == 350 / basic_flow_rate)
# assert(compute_fill_time_basic([], 0) == 0) # no taps raises error as expected
assert(compute_fill_time_basic([], 4) == 0) # empty queue
assert(compute_fill_time_basic([40], 4) == 0.4) # num people < num taps

print("Running tests on walk time function")
walk_time = 3
assert (compute_fill_time_with_walk(q1, 2, walk_time)
        == 500 / basic_flow_rate + 2 * walk_time)
assert (compute_fill_time_with_walk(q2, 3, walk_time)
        == 600 / basic_flow_rate + 3 * walk_time)
assert (compute_fill_time_with_walk(q3, 3, walk_time)
        == 300 / basic_flow_rate + 2 * walk_time)
assert (compute_fill_time_with_walk(q4, 3, walk_time)
        == 350 / basic_flow_rate + 2 * walk_time)
#assert(compute_fill_time_with_walk([], 0) == 0) # no taps raises error as expected
assert(compute_fill_time_with_walk([], 4, walk_time=5) == 0) # empty queue
assert(compute_fill_time_with_walk([40], 4, walk_time=5) == 0.4 + 5) # num people < num taps

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