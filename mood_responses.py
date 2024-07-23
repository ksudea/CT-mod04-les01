moods = {"happy", "sad", "energetic", "calm", "angry", "bored", "depressed", "irritated", "jubilant"}
def mood_response(mood):
    #mood = mood.lower()
    if mood == "happy" or mood == "calm" or mood == "energetic" or mood == "jubilant":
            return(f"Awesome! Glad you're {mood}.")
    elif mood == "sad" or mood == "angry" or mood == "depressed" or mood == "irritated":
            return(f"Oh no! I'm sorry you're {mood}. I think you should do something that'll help you feel better.")
    else:
        return(f"It's interesting that you're {mood}. I'm not very familiar with that mood!")