# Probability for a coin

# probability = favourable_outcome/ total_outcome


favourable_outcome = 1
total_outcome = 2

probability = favourable_outcome/total_outcome

print("probability : ", probability)

print("Percentage : ", probability * 100, "%")



# Probability for a DICE
# PROBABILITY OF EVEN NUMBER IN A DICE

def even_probability():
    
    favour_outcom = 0
    
    for nb in range(1, 7):
        if nb % 2 == 0:
            favour_outcom += 1
    return favour_outcom

fvcm = even_probability()

print(fvcm)

total_outcom = 6

probabiliti = fvcm/total_outcom

print(probabiliti)
print(probabiliti * 100, "%")

