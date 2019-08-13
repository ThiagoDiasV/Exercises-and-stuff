import speech_recognition as sr
import webbrowser

r = sr.Recognizer()

mic = sr.Microphone()

url = 'https : // www .google . com . br / search?q=' # Separado com espaços para o site não transformar a URL

with mic as source:
    r.adjust_for_ambient_noise(source)
    print('Diga uma palavra pra procurar no google ')
    audio = r.listen(source)
    text = r.recognize_google(audio, language='pt-BR')
    print(f'Você disse {text}')
    webbrowser.open_new(f'{url}{text}')
