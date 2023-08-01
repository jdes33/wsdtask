print("WSD")
import heapq
def most_basic_possible(queue, num_taps):
    print("initial q:", queue)
    taps = queue[0: num_taps]
    
    ## validation
    ## MAKE SURE ALL VALUES IN QUEUE AND NUM_TAPS ARE NON ZERO
    if any(map(lambda x : x < 0, queue)):
        print(" ERROR MESSAGE INVALID BOTTLE VOLUMES")
    if num_taps < 1:
        print(" ERROR NO TAPS AVAILABLE")

    #if 3 200's and they all go to zero then time is took is still same as if 1

    q_idx = num_taps
    current_time = 0
    while q_idx < len(queue): # O(q)
        x = min(taps) # O(t) [could switch to O(logt) with heap]
        
        # subtract from all and add new bottle where zero
        for idx in range(len(taps)): # O(t)
            taps[idx] -= x
            if taps[idx] == 0:
                taps[idx] = queue[q_idx]
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


        

def really_bad(queue, num_taps):
    print("queue", queue)
    # case where one bottle in queue
    if len(queue) == 1 and num_taps >= 0: return queue / 10

    # state of taps (how much each person at the taps has left to fill)
    taps = queue[0: num_taps]   # initialise taps remaining
    print("taps initially:", taps)

    sub = 0
    current_time = 0

    heapq.heapify(taps)

    q_idx = num_taps
    for i in range(num_taps, len(queue)):
        print(f"i is {i}")

        # BASED ON HOW U DO CURRENT TIME YOU NEEDA DO INNER LOOP OR SMTHN IN CASE ALL GO TO ZERO

        # finish smallest
        x = heapq.heappop(taps)
        to_add = 0
        for idx in range(len(taps)):
            taps[idx] -= x
            if taps[idx] == 0:
                to_add += 1
        current_time += x # update to show how long it took to finish smallest
        print("finish smallest: ", taps)

        heapq.heappush(taps, queue[i])
        print("add next: ", taps)

    print("total time: ", current_time)
    return

    print(current_time, taps)

    while q_index < len(queue):

        # finish smallest
        m = min(taps)
        # compute time
        current_time += m - sub
        # subtract m from all taps
        sub += m

        # add next to smallest
        print(f"adding next: {queue[q_index]}")
        taps[taps.index(m)] += queue[q_index]
        
        print(current_time, taps)
        print("last queue index", q_index)
        q_index += 1

    # FINISHING SMALLEST
    # finish smallest
    m = min(taps)
    # compute time
    current_time += m - sub
    # subtract m from all taps
    sub += m

    # wait for last person to finish filling bottle
    current_time += max(taps) - sub
    print(current_time, taps)
        
def bad_version(queue, num_taps):

    taps = [] # state of taps (how much each person at the taps has left to fill)
    q_index = 0

    # initialise taps remaining
    for _ in range(num_taps):
        taps.append(queue[q_index])
        q_index += 1
    sub = 0
    current_time = 0

    print(current_time, taps)

    while q_index < len(queue):

        # finish smallest
        m = min(taps)
        # compute time
        current_time += m - sub
        # subtract m from all taps
        sub += m

        # add next to smallest
        print(f"adding next: {queue[q_index]}")
        taps[taps.index(m)] += queue[q_index]
        
        print(current_time, taps)
        print("last queue index", q_index)
        q_index += 1

    # FINISHING SMALLEST
    # finish smallest
    m = min(taps)
    # compute time
    current_time += m - sub
    # subtract m from all taps
    sub += m

    # wait for last person to finish filling bottle
    current_time += max(taps) - sub
    print(current_time, taps)
        

    

q1 = [200, 300, 150, 200]
q2 = [200, 300, 150, 200, 200, 300, 150, 200]
q3 = [200, 200, 200, 100, 100, 100]
q = [200, 200, 200, 100, 150, 100]


#bad_version(q1, 2)
#really_bad(q1,2)
most_basic_possible(q1, 2)
assert(most_basic_possible(q1, 2) == 500)
assert(most_basic_possible(q2, 3) == 600)
assert(most_basic_possible(q3, 3) == 300)
assert(most_basic_possible(q4, 3) == 350)