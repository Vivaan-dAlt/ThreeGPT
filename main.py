import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

# Initialize the speech recognition engine
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the voice for the assistant
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Define a function to speak the assistant's response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said: " + text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            return ""
        except sr.RequestError as e:
            print("Sorry, I couldn't request results from Google Speech Recognition service; {0}".format(e))
            return ""

# Define a function to handle user commands
def handle_command(command):
    if 'what is' in command:
        query = command.replace('what is', '')
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak('The time is ' + time)
    else:
        speak("Sorry, I didn't understand that command.")

# Start the assistant
speak("Hello, I'm your AI assistant. How can I help you?")
while True:
    command = recognize_speech().lower()
    if 'exit' in command:
        speak("Goodbye!")
        break
    handle_command(command)
