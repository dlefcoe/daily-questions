import pyttsx3

def voice(text):
    ''' text to speach '''
    engine = pyttsx3.init()

    engine.setProperty('rate', 200) # Speed setting (default: 200)
    engine.setProperty('volume', 1.0)

    voices = engine.getProperty('voices')
    print(voices)
    # 0 for maerican accent, 1 for english accent
    engine.setProperty('voice', voices[0].id)

    # Speak text
    engine.say(text)
    engine.runAndWait()

# Get text to be spoken from user
text = 'hello world'

voice (text)

