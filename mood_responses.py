def mood_response(mood):
    mood = mood.lower().strip()
    if mood in ['happy', 'excited']:
        return "That's greeeeaaattt!!"
    elif mood in ['sad', 'down']:
        return "I'm sorry to hear you are feeling that way, if you would like cheering up let me know."
    elif mood in ['angry', 'frustrated']:
        return "Its ok no need to Hulk out, just relax and think happy thoughts."
    elif mood in ['anxious', 'nervous']:
        return "Hey I know what your feeling right now, it will pass."
    else:
        return "Well I hope you are feeling a little better after using this app."