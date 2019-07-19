Add your answers to the Algorithms exercises here.

1)  O(n)
    It is dependent on the size of n only once, since it is adding the value of n^2 an n amount of times until it is equal to the value of n^3.  This means it will run through the formula n times, adding the value of n^2 to a variable each time, until it is n^3.

2)  O(n^3)
    There are 4 for-loops, but only the first runs through the entire range of n.  The second runs through the range of n-1 on the first time around, but on the second it runs through the range of n-2, and at the end it isn't going to run at all. So for the first and second loops, If we were to chart this for n = 11, it would look something like this:

    10 
    9  10
    8  9  10 
    7  8  9  10 
    6  7  8  9  10 
    5  6  7  8  9  10 
    4  5  6  7  8  9  10 
    3  4  5  6  7  8  9  10 
    2  3  4  5  6  7  8  9  10 
    1  2  3  4  5  6  7  8  9  10  11  

    With the x axis being i for the first for loop, and y being j for the second.  Total, the first and the second loops are going to run for .5(n^2) times.  Once you add in the third for loop, You get a similar triangle in the z-axis, meaning we are in the range of n^3, with a coefficient in front.  However, in Big O the coefficient is ignored, since we care only about the largest aspect of the time constraint, meaning the first 3 loops are O(n^3).  The fourth loop is going to run 10 times no matter what, making it an O(1) loop, and so it does not matter since it pales in comparison to the immensity of the O(n^3)



3)  O(n)
    The formula repeats recursively with the 2 + bunnyEars(bunnies-1), eventually ending when bunnies equals 0.  2 doesn't affect the time at all and is O(1) with respect to time.  bunnyEars(bunnies-1) will run through the process a bunnies number of times, since it subtracts 1 each time until 0.  This means that it is O(n) with respect to time.  The entire process, then, is O(1) + O(n).  Since in Big O we are concerned only with the largest factors, and since O(1) wouldn't matter if we were dealing with an enormous piece of data (think 1*10^1000000000000000000 bunnies), the process' time constraint is O(n).

4) 

import math
_f_ = 93
# (whatever the highest floor is that the egg will not break on)
_n_ = 193
# (total stories of building starting with ground floor=1 (American standard))


def throwing_egg(x):

    if x > _f_:
        return False
    if x <= _f_:
        return True


def making_an_omelette(top_floor, base_floor=0):
    if throwing_egg(top_floor):
        print("This egg will survive anything. The highest floor that can be thrown from is %s" % top_floor)
        return top_floor
    floor_being_tested = top_floor - math.ceil((top_floor - base_floor)/2)
    if floor_being_tested == base_floor:
        found_f_ = floor_being_tested
        if floor_being_tested == 0:
            print("This egg can survive nothing.  It survives no drops at all and must remain at level 0.")
            return floor_being_tested
        print("The highest floor that can be thrown from is %s" % found_f_)
        return floor_being_tested
    if throwing_egg(floor_being_tested):
        making_an_omelette(top_floor, floor_being_tested)
    else:
        making_an_omelette(floor_being_tested, base_floor)


making_an_omelette(_n_)


    