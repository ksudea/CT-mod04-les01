# Question 1

import mood_responses
try:
    mood = input("How are you feeling today? ")
    print(mood_responses.mood_response(mood))
except Exception as e:
     print(f"Couldn't understand your mood! Double check your input. {e}")

# Question 2
from text_utils import capitalize_string, reverse_string
try:
    cap_string = capitalize_string(input("Input a string to capitalize: "))
    rev_string = reverse_string(input("Input a string to reverse: "))
    print(f"Your capitalized string: {cap_string}")
    print(f"Your reversed string: {rev_string}")
except Exception as e:
    print(f"Couldn't use text utils on your string! Double check your input. {e}")
