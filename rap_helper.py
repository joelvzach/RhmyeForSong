# Program to help aspiring rappers/poets develop their vocabulory
    
# PART 1: Basic rhyming words predictor                     (DONE)
# PART 2: Rhyming scheme basis - rhyming word predictor     (NOPE)
# PART 3: Syllable basis recommender                        (NOPE)
# PART 4: GUI Input and Output system                       (NOPE)
# PART 5: Audio Input System                                (NOPE)
# PART 6: Theme based rhyming words                         (NOPE)
# PART 7: Export as a website or an app                     (NOPE)
    
import pronouncing #if unavailable, install first use: pip install pronouncing
    
def rhyming_word_generator(end_word):
    l = pronouncing.rhymes(end_word)
    return l[0:4]
    
exit = True
while(exit == False):
    
    rhyming_scheme = input("Enter rhyming scheme of a stanza: ")
    rhyming_pattern = rhyming_scheme.split(" ")
    # This information is useful to recommend in the future
    # if pre-recorded type re-appears, recommend those rhyming words
    #instead of the predecessor words rhyming options
    
    for i in rhyming_pattern:
        sentence = input("Enter your sentence: ")
        if(sentence == 'exit'):
            exit = False
            continue
        #print(sentence)
    
        sentence_words = sentence.split(" ")
        #print(sentence_words)
    
        last_word = sentence_words.pop()
        #print(last_word)
    
        answer = rhyming_word_generator(i, last_word)
        print("Termination options for {} : {}".format(last_word,answer))
    
    
