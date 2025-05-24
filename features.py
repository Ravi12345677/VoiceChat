import os
import re
from playsound import playsound
import eel
import sqlite3
import webbrowser
from Engine.command import speak
from Engine.config import ASSISTANT_NAME
import pywhatkit as kit

conn = sqlite3.connect("rk.db")
cursor = conn.cursor()

@eel.expose

def playAssistantSound(): 
    music_dir = "WWW\\folder\\Assets\\Audio\\audio.mp3"
    playsound(music_dir)


def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    app_name = query.strip()

    # if app_name != "":

    #     try:
    #         cursor.execute(
    #             'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
    #         results = cursor.fetchall()

    #         if len(results) != 0:
    #             speak("Opening "+query)
    #             os.startfile(results[0][0])

    #         elif len(results) == 0: 
    #             cursor.execute(
    #             'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
    #             results = cursor.fetchall()
                
    #             if len(results) != 0:
    #                 speak("Opening "+query)
    #                 webbrowser.open(results[0][0])

    #             else:
    #                 speak("Opening "+query)
    #                 try:
    #                     os.system('start '+query)
    #                 except:
    #                     speak("not found")
    #     except:
    #         speak("some thing went wrong")

    if query!="":
        speak("Opening "+query)
        os.system('start '+query)
    else:
         speak("not found")

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)

def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None