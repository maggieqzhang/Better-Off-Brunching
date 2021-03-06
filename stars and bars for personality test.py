# program stars and bars to be able to classify the diff types of thank you screens
from itertools import combinations

def logic_jumps_typeform(stars, bars):

    results = []
    
    def recurse(stars_left, bars_left, c = []):
        if stars_left == 0:
            results.append(c + [0]*(bars_left+1))
            return 
        if bars_left == 0:
            results.append(c + [stars_left])
            return
        for i in range(stars_left + 1):
            current = [i]
            r = recurse(stars_left - i, bars_left - 1, c + current)
        
    recurse(stars, bars)
    return results

tester = logic_jumps_typeform(8,4)
print(tester)

