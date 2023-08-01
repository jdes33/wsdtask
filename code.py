print("WSD")
import heapq
def most_basic_possible(queue, flow_rates): # switch to individual tap

    num_taps = len(flow_rates)
    walk_time = 3 # time to walk to tap
    print("initial q:", queue)

    # assign first people to empty taps (intialise)
    taps = [0] * num_taps
    for i in range(num_taps):
        # apply flow rate to compute time the person will be at this tap, and also add walk time
        taps[i] = queue[i] / flow_rates[i] + walk_time 

    ## validation
    if any(map(lambda x : x < 0, queue)):
        print(" ERROR MESSAGE INVALID BOTTLE VOLUMES")
    if num_taps < 1:
        print(" ERROR NO TAPS AVAILABLE")
    if any(map(lambda x : x < 0, flow_rates)):
        print(" ERROR MESSAGE INVALID FLOW RATE/S")

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
assert(most_basic_possible(q1, [100] * 2) == 500/flow_rate + 2 * walk_time)
print("TEST2: ")
assert(most_basic_possible(q2, [100] * 3) == 600/flow_rate + 3 * walk_time)
print("TEST3: ")
assert(most_basic_possible(q3, [100] * 3) == 300/flow_rate + 2 * walk_time)
print("TEST4: ")
assert(most_basic_possible(q4, [100] * 3) == 350/flow_rate + 2 * walk_time)