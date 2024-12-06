import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import datetime
import google.generativeai as genai
from config import apikey

engine = pyttsx3.init()
genai.configure(api_key=apikey)
chatStr = ""

def say(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Nova"

def chat(query):
    """Handle chat interaction using Google Generative AI."""
    global chatStr
    chatStr += f"Sahil: {query}\nNova: "
    print(chatStr)

    model = genai.GenerativeModel("gemini-1.5-flash")
    chat = model.start_chat(history=[{"role": "user", "parts": "Hello"}])

    # Send the message using the correct argument
    response = chat.send_message(chatStr, stream=True)

    response_text = ""
    for chunk in response:
        print(chunk.text)
        print("_" * 80)
        say(chunk.text)
        chatStr += f"{chunk.text}\n"
        response_text += chunk.text
    return response_text

def ai(prompt):
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"
    model = genai.GenerativeModel("gemini-1.5-flash")
    chat = model.start_chat(
        history=[
            {"role": "user", "parts": "Hello"},
            {"role": "model", "parts": "Great to meet you. What would you like to know?"},
        ]
    )
    response = chat.send_message(prompt, stream=True)
    for chunk in response:
        print(chunk.text)
        print("_" * 80)
        text += chunk.text + "\n"
    if not os.path.exists("Genai"):
        os.mkdir("Genai")
    with open(f"Genai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as file:
        file.write(text)

if __name__ == '__main__':
    print('Welcome to Nova')
    say("Hello, I am Nova, your personal assistant.")
    while True:
        print("Listening...")
        query = takeCommand()
        if query is None:
            continue

        # Commands for opening websites
        sites = [["youtube", "https://www.youtube.com"],
                 ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"]]

        for site in sites:
            if f"open {site[0]}" in query.lower():
                say(f"Opening {site[0]}...")
                webbrowser.open(site[1])
                break

        application = [["brave", r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Brave.lnk"],
                       ["excel", r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk"],
                       ["microsoft edge", r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Edge.lnk"]]

        for app in application:
            if f"open {app[0]}" in query.lower():
                say(f"Opening {app[0]}...")
                os.startfile(app[1])
                break

        # Command for opening a specific movie
        if "open movie" in query.lower():
            musicPath = r"E:\Vit\INTERIM SEMESTER 2021-22\Data Structures and Algorithms\Video\July 2021\13rd July.mp4"
            say("Opening your movie...")
            os.startfile(musicPath)

        #Real Clock Time
        elif "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} hour {min} minutes")

        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        # Exit condition
        elif "nova quit" in query.lower() or "stop" in query.lower():
            say("Goodbye! Have a great day!")
            exit()
        # Resetting Chat
        elif "reset chat".lower() in query.lower():
            chatStr = ""
        else:
            print("Chatting...")
            chat(query)