import speech_recognition as sr
import pyttsx3
import random
import time
import pywhatkit
import requests

# Initialize speech recognition engine
recognizer = sr.Recognizer()

# Initialize text-to-speech engine
engine = pyttsx3.init()
    
def search(query):
    try:
        pywhatkit.search(query)
        print("Searching for:", query)
    except Exception as e:
        print("An error occurred:", str(e))

def play_song(song_name):
    pywhatkit.playonyt(song_name)
# Function to get user input through microphone
def get_audio():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print("You:", text)
            return text.lower()
        except sr.UnknownValueError:
            return "I'm sorry, I couldn't understand that."
        except sr.RequestError:
            return "Sorry, I'm having trouble accessing speech recognition services."

# Function to tell a random joke
def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you get when you cross a snowman with a vampire? Frostbite!",
        "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "How does a penguin build its house? Igloos it together!",
    ]
    joke = random.choice(jokes)
    speak(joke)

# Function to execute time commands
def execute_time_command(command):
    if "time" in command:
        current_time = time.strftime("%I:%M %p")
        speak("The current time is " + current_time)
    elif "date" in command:
        current_date = time.strftime("%A, %B %d, %Y")
        speak("Today's date is " + current_date)
    else:
        speak("I'm sorry, I couldn't recognize the time command.")


# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main loop
while True:
    command = get_audio()
    if "thank" in command:
        speak("your welcome!I am very happy to help you.")
        break
    if "bye" in command:
        speak("Goodbye! Have a great day.")
        break
    if "play a song" in command:
            speak("Sure, please say the name of the song.")
            song_name = get_audio()
            speak("Playing song on YouTube.")
            play_song(song_name)
    if "hello" in command:
        speak("Hi ! I am Slime, your personal A.I assistant.")
    elif "joke" in command:
        tell_joke()
    if "search" in command:
        query = command.replace("search", "").strip()
        search(query)
   
    elif "time" in command or "date" in command:
            execute_time_command(command)
    else:
        speak("Sorry, I didn't understand that command.")

