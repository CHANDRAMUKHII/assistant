import speech_recognition as sr
import pyttsx3
import os

speech = sr.Recognizer()

intro_list = ['who are you', 'what can you do', 'introduce yourself']
greet_list=['hello','hai','hai sera','hello sera','hey sera','hey']

try:
    engine = pyttsx3.init()
except ImportError:
    print("Driver not found")
except RuntimeError:
    print("Driver fails to initialise")

voices = engine.getProperty('voices')

'''for voice in voices:
    print(voice.id)'''
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0')
engine.setProperty('rate', 180)

def talk(cmd):
    engine.say(cmd)
    engine.runAndWait()


def read_voice_cmd():
    voice_text = ''
    print('Listening..')
    with sr.Microphone() as source:
        audio = speech.listen(source)
    try:
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print('Network Error')
    return voice_text


if __name__ == '__main__':
    talk("   Assistance mode activated! Awaiting your command sir..")

    while True:

        voice_note = read_voice_cmd().lower()
        print('cmd : {}'.format(voice_note))
        if voice_note in greet_list:
            print("Hi sir, How can I help you?")
            talk("Hi sir, How can I help you?")
            continue
        elif voice_note in intro_list:
            print("I am tommy!! Your virtual assistant. Ask me anything you are curious about!")
            talk("I am tommy!! Your virtual assistant. Ask me anything you are curious about!")
            continue
        elif 'how are you' in voice_note:
            print("I was made to be perfect, Hope you're good too!")
            talk("I was made to be perfect, Hope you're good too!")
            continue
        elif 'your inspiration' in voice_note:
            print("JARVIS is my role model. To be frank, I'm still under development to be like him. ;-")
            talk("JARVIS is my role model. To be frank, I'm still under development to be like him.")
            continue
        elif 'open' in voice_note:
            talk('Done sir')
            os.system('explorer C:\\"{}"'.format(voice_note.replace('open ', '')))
            print('Done')
            continue
        elif 'launch' in voice_note:
            talk('Launching sir')
            os.system('explorer C:\\"{}"'.format(voice_note.replace('launch ', '')))
            print('Done')
            continue
        elif 'thank you' in voice_note:
            print('You are welcome,sir!')
            talk('You are welcome,sir!')
            exit()
        elif 'bye' in voice_note:
            print('Glad to assist you,sir :-) ')
            talk('Glad to assist you,sir!')
            exit()
        elif 'bye tommy' in voice_note:
            print('Glad to assist you,sir :-) ')
            talk('Glad to assist you,sir!')
            exit()
        elif 'see you tommy' in voice_note:
            print('see you too')
            talk('see you too,sir!')
            exit()
        
        elif '' in voice_note:
            talk('wrong or not any commands received,I gonna sleep')
            print('Slept;-)')
            exit()