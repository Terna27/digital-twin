Exercise 1 — Your turn


    A fair six-sided die is rolled.

    You are told that the number rolled is greater than 2.

    What is the probability that the number is even?

    Your tasks are to write a Python program that:
    1. Creates a list of numbers from 1 to 6.
    2. Finds all numbers greater than 2.
    3. From those numbers, identifies the even numbers.
    4. Calculates and prints the conditional probability as a decimal and percentage.



Exercise 2: Conditional Probability with Cards

        Let's increase the difficulty slightly.

       The cards are numbered 1 to 6, with three red cards and three blue cards.

A card is selected randomly. You are told that the selected card has an even number.

What is the probability that the selected card is blue?
Your Python task
Represent the cards as a list of dictionaries:

    cards = [    {"number": 1, "color": "red"},    {"number": 2, "color": "red"},    {"number": 3, "color": "red"},    {"number": 4, "color": "blue"},    {"number": 5, "color": "blue"},    {"number": 6, "color": "blue"}]



Create a function called card_probability() that identifies the given outcomes (even-numbered cards), identifies the favourable outcomes (blue cards among those), and returns both lists.

Then write a run() function that calculates and prints the conditional probability and percentage.

Hint: To access a card's number, use card["number"]. To check its color, use card["color"] == "blue".





# EXERCISE 3 --Conditional Probability with Students

    # A classroom has eight students. Each student has a gender 
    # and a result indicating whether they passed or failed an exam.
    
    students = [
        {"name": "Mary", "gender": "female", "passed": True},
        {"name": "John", "gender": "male", "passed": True},
        {"name": "Alice", "gender": "female", "passed": False},
        {"name": "Peter", "gender": "male", "passed": False},
        {"name": "Grace", "gender": "female", "passed": True},
        {"name": "David", "gender": "male", "passed": True},
        {"name": "Sarah", "gender": "female", "passed": True},
        {"name": "James", "gender": "male", "passed": False}
    ]
    
    Question: What is the probability that a randomly selected student is female, given that the student passed the exam?

        Your task is to create a function named student_probability() that identifies all students who passed, identifies the female students among those who passed, 
        returns both lists, and calculates the conditional probability inside a separate run() function.

        Use the same structure you developed in Exercise 2.

        Before writing your code, answer this question:

        Which students belong to Event B (passed the exam), and which belong to the intersection of Event A (female) and Event B (passed)?