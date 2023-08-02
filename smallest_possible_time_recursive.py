# Author: Jason De Souza
# Additional task, whereas previous functions assigned an arbritary ordering when more than one tap available for next person,
# this function recusively explores all possible options, prints out each plan and returns the time of shortest plan

from itertools import permutations
def compute_smallest_fill_time_different_flows(queue, flow_rates, walk_time=3, taps=[], q_idx=0, current_time=0, description=""):
    """Computes the shortest time needed for all water bottles to be filled by taps
        Also prints out every possible plan (when more than one tap is free it gives next person in queue a choice, thus generating more plans)

    Args:
        queue (int): The volumes in ml of each bottle in the queue, index 0 represents first bottle in queue
        flow_rates (float): The flow rate corresponding to each tap in ml/s
        walk_time (float): Time taken for any person in queue to walk to tap in seconds (default is 3)

    Returns:
        float:  Amount of time in seconds needed for all bottles to be filled
    """

    num_taps = len(flow_rates)

    # validation
    if any(map(lambda x: x < 0, queue)):
        raise Exception("Cannot have negative bottle volumes")
    if num_taps < 1:
        raise Exception("Must have at least one tap")
    if any(map(lambda x: x < 0, flow_rates)):
        raise Exception("Cannot have negative tap flow rates")
    if walk_time < 0:
        raise Exception("Cannot have negative time to walk to tap")

    if not taps and num_taps > 1:
        # return min of all possibilities
        smallestPerm = None
        # get num_taps from front of queue and work out all computations of adding to taps
        extract = queue[0:min(num_taps, len(queue))]
        for perm in permutations(extract):
            # compute taps
            taps = [0] * num_taps
            desc = ""
            for i in range(min(num_taps, len(queue))):
                taps[i] = perm[i] / flow_rates[i] + walk_time
                desc += f"\nAdd (initial bottle): {perm[i]} to tap {i}, that'll take {taps[i]}s."

            t = compute_smallest_fill_time_different_flows(queue, flow_rates, walk_time, taps, q_idx=min(num_taps, len(queue)), description=desc)
            if smallestPerm is None or t < smallestPerm:
                smallestPerm = t
        print(f"########################## SHORTEST PLAN FOUND = {smallestPerm} seconds")
        return smallestPerm # DONE!
    elif not taps and num_taps == 1:
        # no need to recurse as only one option
        # SHOULD SETUP STUFF HERE THO
        pass

    while q_idx < len(queue):
        smallest = min(taps)
        # subtract from all and add new bottle where zero
        extract = []
        free_idxs = []
        for idx in range(len(taps)):
            taps[idx] -= smallest
            if taps[idx] == 0:
                free_idxs.append(idx)

        current_time+=smallest  # only upate time here as we have finished an event/bottle filling task (1 or more bottles filled)
        description += f"\nFinished {smallest} from {free_idxs}, [t={current_time}]"

        if len(free_idxs) == 1:
            # add new bottle where index zero and increment to next in queue
            taps[free_idxs[0]] = queue[q_idx] / flow_rates[free_idxs[0]] + walk_time
            description += f"\nAdd bottle {queue[q_idx]} to tap {free_idxs[0]} that'll take {taps[free_idxs[0]]} s."
            q_idx += 1
        else:
            smallestPerm = None
            num_bottles_to_extract = min(len(free_idxs), len(queue) - q_idx) # could have more taps available than bottles remaining 
            tap_permutations = permutations([i for i in range(num_taps)]) # permutations of tap indexes
            if num_bottles_to_extract != len(free_idxs):
                # reduce permutations to only get number of needed and to remove redundant
                tap_permutations = set([perm[0:num_bottles_to_extract] for perm in tap_permutations])
                  
            saved_taps = taps[:]
            new_taps = taps[:]

            for tperm in tap_permutations:
                desc = description
                taps = saved_taps[:]
                # compute taps
                for i in range(num_bottles_to_extract):
                    taps[tperm[i]] = queue[q_idx + i] / flow_rates[tperm[i]] + walk_time
                    #print("add bottle: ", queue[q_idx + i], " to tap ", tperm[i], " that'll take ", taps[tperm[i]], "s")
                    desc += f"\nAdd bottle {queue[q_idx + i]} to tap {tperm[i]}, that'll take {taps[tperm[i]]}s"

                t = compute_smallest_fill_time_different_flows(queue, flow_rates, walk_time, taps, q_idx+num_bottles_to_extract, current_time=current_time, description=desc) # we can't acc go past end of queue i think so dw
                if smallestPerm is None or t < smallestPerm:
                    smallestPerm = t
                    new_taps = taps[:]

            taps = new_taps[:]
            q_idx+=num_bottles_to_extract

    # wait for last bottle
    current_time+=max(taps)
    description += f"\nFinished last bottle of {max(taps)} [t={current_time}]"
    print("########")
    print(f"\%\%\%\PLAN: {description}\n TOTAL TIME:{current_time}")
    print("########")
    return current_time



print("\n\n\n")
print("###################################")
print("##### RETURN VALUE= ", compute_smallest_fill_time_different_flows(queue=[100, 60, 200, 30, 20, 40, 60], flow_rates=[10, 20], walk_time=3), " SECONDS")