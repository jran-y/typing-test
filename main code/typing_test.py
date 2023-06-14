""" Typing Test implementation """

from utils import *
from ucb import main
import linecache

# BEGIN Q1-5
"*** YOUR CODE HERE ***"
def lines_from_file(path):
    file = open(path, mode='r')
    linelist = [strip(line) for line in readlines(file)]
    return linelist

def new_sample(path, i):
    file = open(path, mode='r')
    line = linecache.getline(path, i+1).strip('\n')
    return line

def analyze(sample_paragraph, type_string, start_time, end_time):
    word_pre_minute = 0
    accuracy_percentage = 0
    word_num = len(type_string) / 5
    time = (end_time - start_time) / 60
    word_pre_minute = word_num / time
    type = type_string.split()
    sample = sample_paragraph.split()
    right_num = 0
    if len(type) == 0:
        accuracy_percentage = 0.0
    elif len(type) >= len(sample):
        for i in range(len(sample)):
            if type[i] == sample[i]:
                right_num += 1
        accuracy_percentage = (right_num / len(sample)) * 100
    elif len(type) < len(sample):
        for i in range(len(type)):
            if type[i] == sample[i]:
                right_num += 1
        accuracy_percentage = (right_num / len(type)) * 100
    return [word_pre_minute, accuracy_percentage]

def pig_latin(word):
    Word = list(word)
    Vowel = ['a','e','i','o','u']
    if Word[0] in Vowel:
        Word +='way'
    else:
        for i in range(len(Word)):
            if Word[0] in Vowel:
                Word += 'ay'
                word = ''.join(Word)
                return word
            else:
                letter = Word[0

                ]
                Word.remove(letter)
                Word.append(letter)
        Word += 'ay'
    word = ''.join(Word)
    return word

def autocorrect(user_input, word_list, score_function):
    if user_input in word_list:
        return user_input
    else:
        diff = []
        num = 0
        for i in range(len(word_list)):
            diff += [score_function(user_input, word_list[i])]
            if i == 0:
                min = diff[0]
            elif diff[i] < min:
                min = diff[i]
                num = i
        return word_list[num]

def swap_score(word1, word2):
    num_changed = 0
    if not word1 or not word2:
        return 0
    if word1[0] == word2[0]:
        return swap_score(word1[1:], word2[1:])
    else:
        num_changed += 1
        return num_changed + swap_score(word1[1:], word2[1:])
    return num_changed

# END Q1-5

# Question 6
def score_function(word1, word2):
    #BEGIN Q6
    score = 0
    if not word1 or not word2:
        return len(word1) or len(word2)
    elif word1[0] == word2[0]:
        return score_function(word1[1:], word2[1:])
    else:
        add_char = score_function(word1, word2[1:])
        remove_char = score_function(word1[1:], word2)
        substitute_char = score_function(word1[1:], word2[1:])
        score += 1
        return score + min(add_char, remove_char, substitute_char)
    # END Q6



KEY_DISTANCES = get_key_distances()

# BEGIN Q7-8
"*** YOUR CODE HERE ***"
def score_function_accurate(word1, word2):
    if not word1 or not word2:
        return len(word1) or len(word2)
    elif word1[0] == word2[0]:
        return score_function_accurate(word1[1:], word2[1:])
    else:
        add_char = score_function_accurate(word1, word2[1:]) + 1
        remove_char = score_function_accurate(word1[1:], word2) + 1
        substitute_char = KEY_DISTANCES[word1[0], word2[0]] + score_function_accurate(word1[1:], word2[1:])
        return min(add_char, remove_char, substitute_char)

memory = {}
def score_function_final(word1, word2):
    if (word1, word2) in memory:
        return memory[word1, word2]
    elif (word2, word1) in memory:
        return memory[word2, word1]
    elif not word1 or not word2:
        return len(word1) or len(word2)
    elif word1[0] == word2[0]:
        return score_function_final(word1[1:], word2[1:])
    else:
        add_char = score_function_final(word1, word2[1:]) + 1
        remove_char = score_function_final(word1[1:], word2) + 1
        substitute_char = KEY_DISTANCES[word1[0], word2[0]] + score_function_final(word1[1:], word2[1:])
        score = min(add_char, remove_char, substitute_char)
        memory[word1, word2] = score
        return score
# END Q7-8
