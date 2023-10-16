import speech_recognition as sr
import webbrowser
import pyttsx3
import openai
from config import apikey
import datetime
import os

# Set up the Text-to-Speech engine
engine = pyttsx3.init()

# Define the chat history
chatStr = ""

# OpenAI API key
openai.api_key = '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'  # Replace with your OpenAI API key


def chat(query):
    global chatStr
    print(chatStr)
    chatStr += f"User: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def ai(prompt):
    text = f"OpenAI response for Prompt: {prompt}\n*************************\n\n"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text += response["choices"][0]["text"]

    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # Remove illegal characters from the filename (for Windows)
    filename = ''.join(c for c in prompt if c.isalnum() or c in (' ', '.', '-')).strip()
    with open(f"Openai/{filename}.txt", "w") as f:
        f.write(text)
def say(text):
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"


if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    say("Jarvis A.I")
    while True:
        print("Listening...")
        query = takeCommand()
        # say(query)

        # Define websites to open
        sites = [
            ["youtube", "https://www.youtube.com"],
            ["wikipedia", "https://www.wikipedia.com"],
            ["google", "https://www.google.com"],
        ]

        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        if "open music" in query:
            musicPath = "C:/Users/Rakshitha/Downloads/rainy_days.mp3"
            os.system(f"start {musicPath}")

        if " the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} hours {min} minutes")

        if "open notepad".lower() in query.lower():
            say(f"Opening notepad")
            os.system(f"C:/Windows/System32/notepad.exe")

        if "open canva" in query:
            say(f"Opening canva")
            os.system(f"C:/Users/Rakshitha/OneDrive/Desktop/Canva.lnk")

        if "Using artificial intelligence" in query:
            ai(prompt=query)

        if "Jarvis Quit" in query:
            say("Goodbye, Sir.")
            exit()

        if "reset chat" in query:
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)
