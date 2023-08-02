# wsdtask

*See the full_code.py file for solutions to all parts required in task specification (including bonus tasks).*

Optional:
The other file smallest_possible_time_recursive.py is another version that explores different options whenever there is more than one tap available for the next person in the queue to chose from.
For example:
Using queue = [100, 60, 200, 30, 20, 40, 60] and 2 taps with flow rates = [10, 20] will generate the following 6 possible plans.
Where the shortest one took 27 seconds. (Since a person next in queue could pick from multiple different taps if more than one is free, and since they have differnt flow rates the tap they chose could impact the overall time for everyone in the queue to fill their bottles).
########  
\%\%\%\PLAN:   
Add (initial bottle): 100ml to tap 0, that'll take 13.0s.  
Add (initial bottle): 60ml to tap 1, that'll take 6.0s.  
Finished 6.0s from taps=[1], [t=6.0s]
Add bottle 200ml to tap 1 that'll take 13.0s.
Finished 7.0s from taps=[0], [t=13.0s]
Add bottle 30ml to tap 0 that'll take 6.0s.
Finished 6.0s from taps=[0, 1], [t=19.0s]
Add bottle 20ml to tap 0, that'll take 5.0s
Add bottle 40ml to tap 1, that'll take 5.0s
Finished 5.0s from taps=[0, 1], [t=24.0s]
Add bottle 60ml to tap 0, that'll take 9.0s
Finished last bottle of 9.0s [t=33.0]
 TOTAL TIME:33.0
########
########
\%\%\%\PLAN: 
Add (initial bottle): 100ml to tap 0, that'll take 13.0s.
Add (initial bottle): 60ml to tap 1, that'll take 6.0s.
Finished 6.0s from taps=[1], [t=6.0s]
Add bottle 200ml to tap 1 that'll take 13.0s.
Finished 7.0s from taps=[0], [t=13.0s]
Add bottle 30ml to tap 0 that'll take 6.0s.
Finished 6.0s from taps=[0, 1], [t=19.0s]
Add bottle 20ml to tap 0, that'll take 5.0s
Add bottle 40ml to tap 1, that'll take 5.0s
Finished 5.0s from taps=[0, 1], [t=24.0s]
Add bottle 60ml to tap 1, that'll take 6.0s
Finished last bottle of 6.0s [t=30.0]
 TOTAL TIME:30.0
########
########
\%\%\%\PLAN: 
Add (initial bottle): 100ml to tap 0, that'll take 13.0s.
Add (initial bottle): 60ml to tap 1, that'll take 6.0s.
Finished 6.0s from taps=[1], [t=6.0s]
Add bottle 200ml to tap 1 that'll take 13.0s.
Finished 7.0s from taps=[0], [t=13.0s]
Add bottle 30ml to tap 0 that'll take 6.0s.
Finished 6.0s from taps=[0, 1], [t=19.0s]
Add bottle 20ml to tap 0, that'll take 5.0s
Add bottle 40ml to tap 1, that'll take 5.0s
Finished 5.0s from taps=[0, 1], [t=24.0s]
Add bottle 60ml to tap 1, that'll take 6.0s
Finished last bottle of 6.0s [t=30.0]
 TOTAL TIME:30.0
########
########
\%\%\%\PLAN: 
Add (initial bottle): 100ml to tap 0, that'll take 13.0s.
Add (initial bottle): 60ml to tap 1, that'll take 6.0s.
Finished 6.0s from taps=[1], [t=6.0s]
Add bottle 200ml to tap 1 that'll take 13.0s.
Finished 7.0s from taps=[0], [t=13.0s]
Add bottle 30ml to tap 0 that'll take 6.0s.
Finished 6.0s from taps=[0, 1], [t=19.0s]
Add bottle 20ml to tap 1, that'll take 4.0s
Add bottle 40ml to tap 0, that'll take 7.0s
Finished 4.0s from taps=[1], [t=23.0s]
Add bottle 60ml to tap 1 that'll take 6.0s.
Finished last bottle of 6.0s [t=29.0]
 TOTAL TIME:29.0
########
########
\%\%\%\PLAN: 
Add (initial bottle): 100ml to tap 0, that'll take 13.0s.
Add (initial bottle): 60ml to tap 1, that'll take 6.0s.
Finished 6.0s from taps=[1], [t=6.0s]
Add bottle 200ml to tap 1 that'll take 13.0s.
Finished 7.0s from taps=[0], [t=13.0s]
Add bottle 30ml to tap 0 that'll take 6.0s.
Finished 6.0s from taps=[0, 1], [t=19.0s]
Add bottle 20ml to tap 1, that'll take 4.0s
Add bottle 40ml to tap 0, that'll take 7.0s
Finished 3.0s from taps=[0], [t=22.0s]
Add bottle 60ml to tap 0 that'll take 9.0s.
Finished last bottle of 9.0s [t=31.0]
 TOTAL TIME:31.0
########
########
\%\%\%\PLAN: 
Add (initial bottle): 60ml to tap 0, that'll take 9.0s.
Add (initial bottle): 100ml to tap 1, that'll take 8.0s.
Finished 8.0s from taps=[1], [t=8.0s]
Add bottle 200ml to tap 1 that'll take 13.0s.
Finished 1.0s from taps=[0], [t=9.0s]
Add bottle 30ml to tap 0 that'll take 6.0s.
Finished 6.0s from taps=[0], [t=15.0s]
Add bottle 20ml to tap 0 that'll take 5.0s.
Finished 5.0s from taps=[0], [t=20.0s]
Add bottle 40ml to tap 0 that'll take 7.0s.
Finished 1.0s from taps=[1], [t=21.0s]
Add bottle 60ml to tap 1 that'll take 6.0s.
Finished last bottle of 6.0s [t=27.0]
 TOTAL TIME:27.0
########
########################## SHORTEST PLAN FOUND = 27.0 seconds
