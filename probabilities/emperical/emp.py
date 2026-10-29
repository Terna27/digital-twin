historical_activities = [
    1, 0, 1, 4, 1,
    2, 1, 3, 1, 0,
    1, 4, 1, 1, 1,
    0, 1, 4, 1, 2,
    1, 1, 3, 1, 0,
    1, 1, 4, 1, 1
]

activity_names = {
    0: "Sleep",
    1: "Work",
    2: "Exercise",
    3: "Social",
    4: "Leisure"
}

def count_activities():
    
    count = {}
    
    for num in historical_activities:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    return count



def calculate_probabilities():
    
    next = count_activities()
    probabilities = {}
    total = len(historical_activities)
    
    for value, freq in next.items():
            prob = freq/total
            probabilities[value] = prob
            
    return probabilities
    
    

def run():
    
    probability = calculate_probabilities()
        
    sorted_result = sorted(probability.items(),
                           key=lambda item: item[1], 
                           reverse=True
                           )
    
    for name, percentage in sorted_result:
        activity_name = activity_names[name]
        prec = round(percentage * 100,2)
        
        print(activity_name, prec )
    
