# # Probability for a coin

# # probability = favourable_outcome/ total_outcome


# favourable_outcome = 1
# total_outcome = 2

# probability = favourable_outcome/total_outcome

# print("probability : ", probability)

# print("Percentage : ", probability * 100, "%")



# # Probability for a DICE
# # PROBABILITY OF EVEN NUMBER IN A DICE

# def even_probability():
    
#     favour_outcom = 0
    
#     for nb in range(1, 7):
#         if nb % 2 == 0:
#             favour_outcom += 1
#     return favour_outcom

# fvcm = even_probability()

# print(fvcm)

# total_outcom = 6

# probabiliti = fvcm/total_outcom

# print(probabiliti)
# print(probabiliti * 100, "%")




# PROBABILITY OF A PRIME NUMBER IN A DICE
def is_primer():
    count = 0
    for num in range(2, 7):
        is_prime = True
        
        for nb in range(2, num):
            if num % nb == 0:
                is_prime = False
                break
        if is_prime:
                count += 1
                
    return count


total_prime = is_primer()
total_outcome = 6
print(total_prime)

probability_prime = total_prime/total_outcome

print(probability_prime)
print(probability_prime * 100, "%")