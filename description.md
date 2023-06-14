# typing-test
Text File questions



Problem 01: Sample Paragraphs



- Which functions from utils.py will you use for interacting with the sample_paragraphs.txt file?


close(), readable(), readline(), readlines(), lower(), split(), strip()


Problem 02: Words Per Minute



- Given a long string that contains a full paragraph (e.g. "This is my name. It is Bob. Also, I have a cat named Troy."), what function will you use to separate a string containing a full paragraph into its individual words?


split()


- What is the calculation you will use in order to measure Words Per Minute speed? (You can describe your formula.)

If set number of characters as ch_num, set use time(minutes) as time. Word Per Minute = (ch_num / 5) / time. And ch_num means the number of words.



- What is the calculation you will use in order to measure accuracy? (You can describe your formula.)

If set the number of type right words as type_right_num, set the number of right word in text as right_num, and set the number of type word as type_num. If type_num > right_num, like type_num = 5, right_num = 3, only use the three first words to calculation. If type_num < right_num, like type_num = 2, right_num = 3, just calculate type words accuracy(at this time, right_num = type_num). And if type_num = 0, accuracy percentage = 0. Accuracy percentage = type_right_num / right_num (thr result shold ad a percentage). 



Problem 03: Pig Latin



- How will you identify that a word starts with a consonant cluster? 

If the first letter is not a vowel( vowel just include 'a', 'e', 'i', 'o', 'u')



Problem 04: Autocorrect Skeleton



- How will you calculate the difference scores between the user input string and each valid word, and determine which difference is the smallest?

set a function named score_function(user_input, word_list).set three arguments named pre_diff, new_diff, correct_word. Use for(or while) loop, compare the different letter between user_input and the word in word_list. the number of difference number is pre_diff, and the numbers of the difference of next word as new_diff. If new_diff < pre_diff, set the value of pre_diff as the same as new_diff, and set correct_word as this word in the word_list.




Problem 05: Score Function 



- What will your base case be?

Returns 0 if the first letter or character of two words is the same length, or if they are exactly the same length.(for example: 'pill' and 'pillage' or 'pill' and 'pill', return 0)


- Identify two example inputs which fall into different recursive calls. In each of these cases, what recursive call should be made?


Two cases: 1. have the same first letter. 2. the length of two words are different.
If case 1, use len(word1) to do recursive.
If case 2, use len(shorter one) to do recurisive.



Problem 06: 



- What does each of the recursive calls in the skeleton represent? Are there additional cases which don't fit into the three already given?

The three recursions represent adding letters, deleting letters, and changing letters in word1. 
No


- If we called score_function("bot", "boot"), list a series of successive recursive calls we would go through to reach the base case. For example, if we called score_function("add", "aadd"), one step could be score_function("add", "aadd") -> score_function("add", "add").

from "bot" to "boot" just remove 'o'



- Based on your above list of recursive calls, classify each step as an add, remove, a swap, or something else.


bot to boot is remove


- Why would your function choose this sequence of recursive calls over another?

Becase this one return the minimum number.

Problem 07: Accuracy



- In your own words, why do we need to improve the accuracy of our existing score_function? In other words, what is the problem that we are trying to solve?


Have more than one word is right, and their return score are the same. We can't choose to use which one of them. 


- How can you adapt your score function from the previous problem to take into account key distances?
 (Hint: which recursive call will need to be modified?)


Should change the swap_function. from every turn  just add one to every turn add the distance.


Problem 08: Efficiency



- What data structure will you use to store all of the differences that score_function has already calculated?


maybe Tree


- What types of values will this data structure contain?

list, boolean(been compared or not), value(distance, score)



- Using the data structure you described, given a pair of words, how will you check whether score_function has already been called on that pair of words? If so, how will you access the already calculated difference?

check parent root are equal or not, if have these two words, output label(children root).
