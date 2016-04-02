parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

test_string = """Straight outta PLACE, crazy NOUN named PERSON, 
from the gang called PLURALNOUN Wit Attitude"""

def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None
        
def play_game(ml_string, parts_of_speech):    
    replaced = []
    # your code here
    ml_list = ml_string.split()
    for word in ml_list:
        replacement = word_in_pos(word, parts_of_speech)
        if replacement != None:
            user_input = input("Type in a: " + replacement + ": ")
            word = word.replace(replacement, user_input)
            replaced.append(word)
        else:
                replaced.append(word)
    return " ".join(replaced)      
    
print (play_game(test_string, parts_of_speech))    
