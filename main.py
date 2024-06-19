from time import time # Importing time for measuring the time spent for typing

print("Welcome to Typing app")
print("Press Enter to start typing")
print("Press Enter twice to finish typing")
input("--------------------------------------------")

start_time = time() # Start time of the typing
input_text = [] # For storing the overall input

while True:
    input_line = input() # Taking current input till the next line
    if not input_line:
        break; # Exiting loop if empty line is inserted(Enter pressed twice)
    input_text.append(input_line) # Appending the current line into list

end_time = time() # End time of the typing

## The following commented parts are for testing purposes
# print("You inserted the following text:")
# print("--------------------------------------------")
# for input_line in input_text:
#     print(input_line) # Printing each line in the list

total_time = (end_time-start_time)/60 # Finding the total time spent for typing and converting to minutes

print(f"You spent {total_time} minutes in total") # Printing total time spent in minutes

overall_words_count = 0 # Counter for words
for input_line in input_text: # Traversing over the whole input and taking each input line
    word_line = input_line.split() # Splitting and finding the words of each line
    overall_words_count += len(word_line) # Adding the total count for each line to overall words counter

print(f"In total, you entered {overall_words_count} words ")

wpm = round(overall_words_count/total_time, 2) # Finding the word per minute by dividing the overall number of words to total time spent and rounding it up to 2 floating numbers

print("Your WPM is: ", wpm) # Printing the WPM for user 