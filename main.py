import subprocess
# import os

def text_to_speech(text):
    command = f'''
    Add-Type -AssemblyName System.Speech
    $speechSynthesizer = New-Object System.Speech.Synthesis.SpeechSynthesizer
    $speechSynthesizer.Speak("{text}")
    '''

    subprocess.run(["powershell", "-Command", command])

if __name__ == '__main__':
    welcomeMsg = '''Welcome to RoboSpeaker 1.1 by Vinay
    To quit using robot type 'q'.
    Enter the text. So that I can read it aloud for you darling!:
    '''
    print(welcomeMsg)
    text_to_speech(welcomeMsg)
    while(True):
        user_input = input("Enter the text. So that I can read it aloud!: ")
        if user_input == 'q':
            break
        text_to_speech(user_input)
