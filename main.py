import subprocess
import requests
import json
# import os

def text_to_speech(text):
    command = f'''
    Add-Type -AssemblyName System.Speech
    $speechSynthesizer = New-Object System.Speech.Synthesis.SpeechSynthesizer
    $speechSynthesizer.Speak("{text}")
    '''

    subprocess.run(["powershell", "-Command", command])

def weather_api_process(city):
    url = f'http://api.weatherapi.com/v1/current.json?key=d6c0d2026c90422e93e110353240801&q={city}&aqi=no'
    
    r = requests.get(url)
    weather_dict_response = json.loads(r.text)
    temperature = weather_dict_response["current"]["temp_c"]

    text_to_speech(f"The current weather in {city} is {temperature} degrees. ")

    return temperature

if __name__ == '__main__':
    welcomeMsg = '''Welcome to RoboSpeaker 1.1 by Vinay
    To quit using robot type 'q'.
    Enter the text. So that I can read it aloud for you darling!:
    '''
    print(welcomeMsg)
    text_to_speech(welcomeMsg)
    while(True):
        city = input("Enter the City Name. So that I can give its temperature aloud!: ")
        if city == 'q':
            break
        text_to_speech(city)
        print(weather_api_process(city))
