import btctxt

def count_sentences(text):
    count = 0
    
    terminals = ".;?!"
    for char in text:
        if char in terminals:
            count = count + 1
            
    return count

def count_characters(text):
    count = 0
    
    for char in text:
        if char != " ":
            count = count + 1
        else:
            count = count
        
    return count
        

def count_syllables(words):
    count = 0
    
    for word in words:
        count_in_word = count_syllables_in_word(word)
        count = count + count_in_word
        
    return count

def count_syllables_in_word(word):
    count = 0
    
    endings = ".,;!?:"
    last_char = word[-1]
    
    if last_char in endings:
        processed_word = word[0:-1]
    else:
        processed_word = word
        
    if len(processed_word) <= 3:
        return 1
    
    if processed_word [-1] in "eE":
        processed_word = processed_word[0:-1]
    
    vowels = "aeiouAEIOU"
    previous_char_is_vowel = False
    for char in processed_word:
            
        # My Version(works) = if char in vowels and previous_char_is_vowel == False:
                                 #previous_char_is_vowel = True
                                 #count = count + 1
                             #else:
                                 #previous_char_is_vowel = False
        if char in vowels:
            
            if not previous_char_is_vowel:
                count = count + 1
            previous_char_is_vowel = True
        else:
            previous_char_is_vowel = False
            
    if processed_word[-1] in "yY": # TRY TO REMEMBER THE in FUNCTION can be used this way!!!
        count = count + 1
        
    
    return count

def output_results(score):
    if score >= 90.0:
        print("Reading level of 5th Grade")
    elif score >= 80.0:
        print("Reading level of 6th Grade")
    elif score >= 70.0:
        print("Reading level of 7th Grade")
    elif score >= 60.0:
        print ("Reading level of 8th-9th Grade")
    elif score >= 50.0:
        print("Reading level of 10th-12th Grade")
    elif score >= 30.0:
        print("Reading level of College Student")
    else:
        print("Reading level of College Graduate")


def compute_readability(text):
    total_words = 0
    total_sentences = 0
    total_syllables = 0
    score = 0
    
    
    words = text.split()
    total_words = len(words)
    total_sentences = count_sentences(text)
    total_syllables = count_syllables(words)
    total_characters = count_characters(text)
  
    score = (206.835 - 1.015 * (total_words / total_sentences)
             - 84.6 * (total_syllables / total_words)) #Remember we can wrap a formular in parentheses so we can use miltiple lines
 
    print(total_characters, "characters") 
    print(total_words, "words")
    print(total_sentences, "sentences")
    print(total_syllables, "syllables")
    print(score, "reading ease score")
    output_results(score)

compute_readability(btctxt.text)
