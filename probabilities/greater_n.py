
# find the probability of an even number greater than 3
def greater_than_three():
    grtr = []
    count = 0
    for nb in range(1, 7):
        
        is_even = False
        if nb % 2 == 0 and nb > 3:
            is_even = True
            
        if is_even:
            count += 1
    #         grtr.append(nb)
    # print(grtr)
    return count

def run():
    
    greater_even = greater_than_three()
    
    probability = greater_even/6
    print(greater_even)
    print(probability * 100, "%")