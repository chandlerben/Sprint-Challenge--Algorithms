import math
_f_ = 0
# (whatever the highest story is that the egg will not break being dropped from. Whole numbers only!)
_n_ = 197
# (total stories of building starting with ground floor=1 (American standard) Whole numbers only!)


def throwing_egg(x):

    if x > _f_:
        return False
    if x <= _f_:
        return True


def making_an_omelette(top_floor, base_floor=0):
    if top_floor < 0:
        print("What, are you underground?")
        return
    if top_floor < base_floor:
        print(
            "Are you in 'The Upside-Down'? I'll string some Christmas lights to communicate.")
        return
    if throwing_egg(top_floor):
        print("This egg will survive anything. The highest floor that can be thrown from is %s" % top_floor)
        return top_floor
    floor_being_tested = top_floor - math.ceil((top_floor - base_floor)/2)
    if floor_being_tested == base_floor:
        found_f_ = floor_being_tested
        if floor_being_tested == 0:
            print(
                "This egg can survive nothing. It survives no drops and must remain at level 0.")
            return floor_being_tested
        print("The highest floor that can be thrown from is %s" % found_f_)
        return floor_being_tested
    if throwing_egg(floor_being_tested):
        making_an_omelette(top_floor, floor_being_tested)
    else:
        making_an_omelette(floor_being_tested, base_floor)


making_an_omelette(_n_)
