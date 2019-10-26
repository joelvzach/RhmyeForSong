# Program to help aspiring rappers/poets develop their vocabulory
    
# PART 1: Basic rhyming words predictor                     (DONE)
# PART 2: Rhyming scheme basis - rhyming word predictor     (NOPE)
# PART 3: Syllable basis recommender                        (NOPE)
# PART 4: GUI Input and Output system                       (NOPE)
# PART 5: Audio Input System                                (NOPE)
# PART 6: Theme based rhyming words                         (NOPE)
# PART 7: Export as a website or an app                     (NOPE)
    
import pronouncing #if unavailable, install first use: pip install pronouncing
import random

def rhyming_word_generator(end_word):
    words = []
    l = pronouncing.rhymes(end_word)
    for i in range(4):
        words.append(random.choice(l))
    return words

pattern = []
exit = False
while(exit == False):
    
    rhyming_scheme = input("Enter rhyming scheme of a stanza: ")
    rhyming_pattern = rhyming_scheme.split(" ")
    # This information is useful to recommend in the future
    # if pre-recorded type re-appears, recommend those rhyming words
    #instead of the predecessor words rhyming options
    
    for num,i in enumerate(rhyming_pattern):
        #if(flag == 1):
            
        sentence = input("Enter your sentence: ")
        
        #if(sentence == 'exit'):
        #    exit = True
        #    break
        
        print(sentence)
    
        sentence_words = sentence.split(" ")
        print(sentence_words)
    
        last_word = sentence_words.pop()
        print(last_word)
    
        answer = rhyming_word_generator(last_word)
        #if rhyming_pattern[num+1] in rhyming_pattern[0:num]:
        #    flag = 1
        print("Termination options for {} : {}".format(last_word,answer))
    
    
