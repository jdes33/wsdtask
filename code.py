
def compute_fill_time(queue, flow_rates, walk_time=3):
    """Computes the time needed for queue of water bottles to be filled by taps

    Args:
        queue (float): The volumes in ml of each bottle in the queue, index 0 represents first bottle in queue
        flow_rates (float): The flow rate corresponding to each tap in ml/s
        walk_time (float): Time taken for any person in queue to walk to tap in seconds (default is 3)

    Returns:
        list: a list of strings representing the header columns
    """

    num_taps = len(flow_rates)
    print("initial q:", queue)

    # assign first people to empty taps (intialise)
    taps = [0] * num_taps
    for i in range(num_taps):
        # apply flow rate to compute time the person will be at this tap, and also add walk time
        taps[i] = queue[i] / flow_rates[i] + walk_time 

    ## validation
    if any(map(lambda x : x < 0, queue)):
        raise Exception("Cannot have negative bottle volumes")
    if num_taps < 1:
        raise Exception("Must have at least one tap")
    if any(map(lambda x : x < 0, flow_rates)):
        raise Exception("Cannot have negative tap flow rates")
    if walk_time < 0:
        raise Exception("Cannot have negative time to walk to tap")


    q_idx = num_taps
    current_time = 0
    while q_idx < len(queue): # O(q)
        x = min(taps) # O(t) [could switch to O(logt) with heap]
        print("x: =", x)
        # subtract from all and add new bottle where zero
        for idx in range(len(taps)): # O(t)
            taps[idx] -= x
            if taps[idx] == 0:
                # add next bottle
                taps[idx] = queue[q_idx] / flow_rates[idx] + walk_time

                q_idx += 1

        current_time += x
        print("time:", current_time)

    # wait for last bottle
    current_time += max(taps) # O(t)

    print("final state", taps, "\ttime: ", current_time)

    # time complexity
    # O(q) * [2 * O(t)] + O(t)
    # O(q)O(t) + O(t)
    # O(qt) where q is length of queue and t is number of taps
            
    return current_time

q1 = [200, 300, 150, 200]
q2 = [200, 300, 150, 200, 200, 300, 150, 200]
q3 = [200, 200, 200, 100, 100, 100]
q4 = [200, 200, 200, 100, 150, 100]


#bad_version(q1, 2)
#really_bad(q1,2)
walk_time = 3
flow_rate = 100
print("TEST1: ")
assert(compute_fill_time(q1, [100] * 2) == 500/flow_rate + 2 * walk_time)
print("TEST2: ")
assert(compute_fill_time(q2, [100] * 3) == 600/flow_rate + 3 * walk_time)
print("TEST3: ")
assert(compute_fill_time(q3, [100] * 3) == 300/flow_rate + 2 * walk_time)
print("TEST4: ")
assert(compute_fill_time(q4, [100] * 3) == 350/flow_rate + 2 * walk_time)
print("TEST5: vary rate")
assert(compute_fill_time(q1, [50, 150]) == 200/50 + 200/50 + 2 * walk_time)


print("\npart 4 before:")
compute_fill_time([100,10,1000], [100,5]) #t1 takes 1s (+3 for walk), t2 takes 2 seconds (+3 for walk), so t1 gets big task => result 4s+ 13s = 17
print("\npart 4 after:")
compute_fill_time([100,10,1000], [100,20]) # t1 takes 1s (+3 for walk), t2 takes half a second (+3 for walk), so t2 gets big task => 3.5s + 53s = 56.5s

# THIS EXAMPLE USES 1000ML FOR FIRST TWO TASKS, SO EVEN IF SWITCHED AROUND WOULDNT CHANGE OUTCOME
# the 3s in the calculations are for walking times. (You can scale down all the numbers if you scale down walking time too)
print("\npart 4 better example before:")
compute_fill_time([1000, 1000, 8000, 10000], [100,10]) # t1 takes 13s, t2 takes 103s, so t1 gets 8k and takes 83s which is 96s total so far so it then gets 10k which takes 103s totalling 199s

print("\npart 4 better example after:")
compute_fill_time([1000, 1000, 8000, 10000], [100,20]) # t1 takes 13s, t2 takes 53s, so t1 gets 8k and takes 83s which is 96 total so far so t2 gets 10k this time which takes 503 seconds totalling 556s 