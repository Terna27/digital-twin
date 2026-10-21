# Probability with letters


letters = ["A", "B", "E", "F", "I", "K"]
vowels = ["A", "E", "I", "O", "U"]

def vowel_probability():
    favourable_outcome = 0
    for c in letters:
        is_vowel = False
        
        for v in vowels:
            if v == c:
                is_vowel = True
            
        if is_vowel:
            favourable_outcome += 1
            # lst = " ".join(favourable_outcome)
    return favourable_outcome
        
vow = vowel_probability()

print(vow)

total_outcome = 6
Probability = vow/total_outcome

print(Probability)
print(Probability * 100, "%")