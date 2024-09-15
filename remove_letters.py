
# todo Remove The Word!
# * Create a function that takes a list and string. The function should remove the letters in the string from the list, and return the list.

# ?  Examples
# ?remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string") ➞ ["w"]

# ?remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon") ➞ ["b", "g", "w"]

# ?remove_letters(["d", "b", "t", "e", "a", "i"], "edabit") ➞ []
# !Notes
# *If number of times a letter appears in the list is greater than the number of times the letter appears in the string, 
# *the extra letters should be left behind (see example #2).
# *If all the letters in the list are used in the string, the function should return an empty list (see example #3).



def remove_letters(letters, word):
   lst =[]
   for x in letters:
      if x not in word:
         lst.append(x)
   return lst
    
   
print(remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string"))
print(remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon"))
print(remove_letters(["d", "b", "t", "e", "a", "i"], "edabit"))



# ! ////////////////////////////////////////////////////////////////////////////////

def remove_letters(lst, word):
    # Convert the list to a copy to avoid modifying the original input
    for char in word:
        if char in lst:
            lst.remove(char)  # Remove only one occurrence of the character
    return lst

# Test cases
print(remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string"))  # ➞ ["w"]
print(remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon"))  # ➞ ["b", "g", "w"]
print(remove_letters(["d", "b", "t", "e", "a", "i"], "edabit"))  # ➞ []
