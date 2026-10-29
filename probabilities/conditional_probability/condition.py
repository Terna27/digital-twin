


# # P(A|B) =  P(A INTERSECT B)/ P(B)
# numbers = [1,2,3,4,5,6]

# def find_b():
    
#     even_numb = []
#     favourable_num = []
    

#     for nb in numbers:
#         if nb % 2 == 0:
#             even_numb.append(nb)
#     for num in even_numb:
        
#         if num > 3:
#             favourable_num.append(num)
    
#     probability = len(favourable_num)/len(even_numb)
#     return probability

# fv = find_b()
# print(round(fv,2))
# print(round((fv * 100),1),"%")

# # Exercise ONE

# def conditional_probability():
#     given_outcomes = []
#     favourable_outcomes = []
    
#     for n in numbers:
#         if n > 2 :
#             given_outcomes.append(n)
#     for nb in given_outcomes:
#         if nb % 2 == 0:
#             favourable_outcomes.append(nb)
            
#     return favourable_outcomes, given_outcomes


# def run():
    
#     fvcm, given = conditional_probability()
#     probability = len(fvcm)/len(given)
    
#     print(round(probability, 2))
#     print(round(probability * 100,2), "%")
            
            
            
# EXERCISE TWO

# cards = [
#     {"number": 1, "color": "red"},
#     {"number": 2, "color": "red"},
#     {"number": 3, "color": "red"},
#     {"number": 4, "color": "blue"},
#     {"number": 5, "color": "blue"},
#     {"number": 6, "color": "blue"}
# ]

# def card_probability():
    
#     both_fav = []
#     all_even = []
    
    
#     for colors in cards:
#         if colors["number"] % 2 == 0 and colors["color"] == "blue":
#             both_fav.append(colors)
            
#     for even in cards:
#         if even["number"] % 2 == 0:  
#             all_even.append(even)
    
#     return both_fav, all_even


# def run():
    
#     both_fav , all_even = card_probability()
#     # fvcm, given = conditional_probability()

#     print(both_fav)
#     print(all_even)

#     probability = len(both_fav)/len(all_even)

#     print(round(probability, 2))
#     print(round(probability  * 100, 2), "%")
    
    
   
    
#     # probability = len(fvcm)/len(given)
    
#     # print(round(probability, 2))
#     # print(round(probability * 100,2), "%")
            


# # EXERCISE 3 Conditional Probability with Students


# students = [
#     {"name": "Mary", "gender": "female", "passed": True},
#     {"name": "John", "gender": "male", "passed": True},
#     {"name": "Alice", "gender": "female", "passed": False},
#     {"name": "Peter", "gender": "male", "passed": False},
#     {"name": "Grace", "gender": "female", "passed": True},
#     {"name": "David", "gender": "male", "passed": True},
#     {"name": "Sarah", "gender": "female", "passed": True},
#     {"name": "James", "gender": "male", "passed": False}
# ]

# def student_probability():
#     passed = []
#     female_passed = []
    
#     for student in students:
#         if student["passed"] == True:
#             passed.append(student)
            
            
#     for std in students:
#         if std["gender"] == "female" and std["passed"] == True:
#             female_passed.append(std["name"])
#     return passed, female_passed


# def run():
                
#     passed, female_passed = student_probability()
#     probability = len(female_passed)/len(passed)
#     print(passed)
#     print(female_passed)
#     print(probability)
#     print(round(probability * 100, 2), "%")
    
    
    
# Exercise 4 — Conditional Probability with Products


# products = [
#     {"name": "Laptop", "category": "electronics", "in_stock": True},
#     {"name": "Phone", "category": "electronics", "in_stock": True},
#     {"name": "Headphones", "category": "electronics", "in_stock": False},
#     {"name": "Shirt", "category": "clothing", "in_stock": True},
#     {"name": "Jeans", "category": "clothing", "in_stock": False},
#     {"name": "Tablet", "category": "electronics", "in_stock": True},
#     {"name": "Jacket", "category": "clothing", "in_stock": True},
#     {"name": "Shoes", "category": "clothing", "in_stock": False}
# ]


# def product_probability():
    
#     all_in_stock = []
#     electronics_in_stock = []
    
#     for product in products:
#         if product["category"] == "electronics" and product["in_stock"] == True:
#             electronics_in_stock.append(product["name"])
#     for stocks in products:
#         if stocks["in_stock"] == True:
#             all_in_stock.append(stocks)
            
#     return all_in_stock, electronics_in_stock
                
                
# def run():
#     all_stocks, elct_stock = product_probability()
     
    
#     probability = len(elct_stock)/len(all_stocks)
    
#     print(round(probability, 2))
#     print(round(probability * 100, 2),"%")


# def independent_events():
    
#     numbers = [1, 2, 3, 4, 5, 6]
    
    
#     even_numbers = []
#     greater_than_four = []
    
#     for nb in numbers:
#         if nb % 2 == 0:
#             even_numbers.append(nb)
#     probability = len(even_numbers)/len(numbers)
              
#     for num in numbers:
#         if num > 4:
#             greater_than_four.append(num)
#     probable = len(greater_than_four)/len(numbers)
    
#     return probability, probable
    

# def run():
    
#     probability, probable = independent_events()
    
#     event = probability * probable
    
#     print(round(event, 2))
#     print(round(event * 100, 2), "%")



# def dependent_events():
#     red_balls = 3
#     blue_balls = 2
#     counts = 0
#     rd_balls = 0
    
#     total_balls = red_balls + blue_balls
   
#     probability = red_balls/total_balls
    
#     counts = total_balls - 1
#     rd_balls = red_balls - 1
    
#     probab = rd_balls/counts
    
   
#     return probability, probab
    
    
# def run():
    
#     prob , pro = dependent_events()
    
#     probability = prob * pro

    
#     print(round(probability, 2) * 100, "%")



# EXAMPLE Drawing Cards Without Replacement



cards = [
    {"number": 1, "color": "red"},
    {"number": 2, "color": "red"},
    {"number": 3, "color": "red"},
    {"number": 4, "color": "blue"},
    {"number": 5, "color": "blue"},
    {"number": 6, "color": "blue"}
]

def dependent_cards():
    count = []
    
    fav_blue = []
    
    for card in cards:
        count.append(card)
        if card["color"] == "blue":
            
            fav_blue.append(card)
            
    probability = len(fav_blue)/len(count)     
    
    count = len(count) - 1
    fav_blue = len(fav_blue) - 1
    
    new_probability = fav_blue/count
    
    
   
    
    
    return probability, new_probability

def run():
    x, y = dependent_cards()
    
    output = x * y
    
    print(x)
    print(y)
    print(output * 100, "%")