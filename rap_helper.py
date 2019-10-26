# Program to help aspiring rappers/poets develop their vocabulory
    
# PART 1: Basic rhyming words predictor                     (DONE)
# PART 2: Rhyming scheme basis - rhyming word predictor     (DONE)
# PART 3: Syllable basis recommender                        (NOPE)
# PART 4: GUI Input and Output system                       (NOPE)
# PART 5: Audio Input System                                (NOPE)
# PART 6: Theme based rhyming words                         (NOPE)
# PART 7: Export as a website or an app                     (NOPE)
    
import pronouncing
import random
import syllables as syl
#if unavailable, install first use: pip install <library name>

def rhyming_word_generator(rhyming_scheme):
    for alphabet in rhyming_scheme:
        #print("current alphabet of scheme: {}".format(alphabet))
        flag = 0
        if(bool(rhyme_pattern) == True):
            for key in rhyme_pattern.keys():
                #print("key check: {}".format(key))
                if key == alphabet:
                    flag = 1
                    words=rhyme_pattern[alphabet]
                    print("To match with line type '{}' with {} syllables in total: {}"\
                            .format(key, sentence_syllables[alphabet], words))
    
        if flag == 0:
            words = []
            sentence = input("Enter your line: ")
            #print("sentence: {}".format(sentence))
            sentence_words = sentence.split(" ")
            #print("sentence words: {}".format(sentence_words))
            sentence_syllables[alphabet] = syl.estimate(sentence)
            print(sentence_syllables[alphabet])
            last_word = sentence_words.pop()
            #print("last words: {}".format(last_word))
            l = pronouncing.rhymes(last_word)
            #print(l)
            for i in range(4):
                words.append(random.choice(l))
            rhyme_pattern[alphabet] = words

rhyme_pattern = {} #alphabet: word
sentence_syllables = {} #alphabet: syllable-count
pattern = []
exit = False

while(exit == False):
    
    rhyming_scheme = input("Enter rhyming scheme of a stanza (space separated): ")
    if rhyming_scheme == "exit":
        exit = True
        continue
    rhyming_pattern = rhyming_scheme.split(" ")
    # This information is useful to recommend in the future
    # if pre-recorded type re-appears, recommend those rhyming words
    #instead of the predecessor words rhyming options
    """
    for num,i in enumerate(rhyming_pattern):
        #if(flag == 1):
        
        sentence = input("Enter your sentence: ")
        
        print(sentence)
    
        sentence_words = sentence.split(" ")
        print(sentence_words)
    
        last_word = sentence_words.pop()
        print(last_word)
    """
    rhyming_word_generator(rhyming_pattern)
        #if rhyming_pattern[num+1] in rhyming_pattern[0:num]:
        #    flag = 1
        #print("Termination options for {} : {}".format(last_word,answer))
    
    
