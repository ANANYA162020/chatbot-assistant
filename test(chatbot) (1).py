import speech_recognition as sr
import playsound
from gtts import gTTS
import random
from time import ctime
import webbrowser
import yfinance as yf
import ssl
import certifi
import time
import os #  


class person:
    name = ''

    def setName(self, name) -> object:
        self.name = name


def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True


r = sr.Recognizer()  # initialise a recogniser


# listen for audio and convert it to text:
def record_audio(ask=False):
    with sr.Microphone() as source:  # microphone as source
        if ask:
            speak(ask)
        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError:  # error: recognizer does not understand
            speak('I did not get that')
        except sr.RequestError:
            speak('Sorry, the service is down')  # error: recognizer is not connected
        print(f">> {voice_data.lower()}")  # print what user said
        return voice_data.lower()


# get string and make a audio file to be played
def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')  # text to speech(voice)
    r = random.randint(1, 20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)  # save as mp3
    playsound.playsound(audio_file)  # play the audio file
    print(f"chatbot: {audio_string}")  # print what app said
    os.remove(audio_file)  # remove audio file


def respond(voice_data):
    # 1: greeting
    if there_exists(['hey', 'hi', 'hello']):
        greetings = [f"hey, how can I help you {person_obj.name}", f"hey, what's up? {person_obj.name}",
                     f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}",
                     f"hello {person_obj.name}"]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        speak(greet)

    # 2: name
    if there_exists(["what is your name", "what's your name", "tell me your name"]):
        if person_obj.name:
            speak("my name is Alexis")
        else:
            speak("my name is Alexis. what's your name?")

    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        speak(f"okay, i will remember that {person_name}")
        person_obj.setName(person_name)  # remember name in person object

    # 3: greeting
    if there_exists(["what is cancer"]):
        speak(f"Cancer is the uncontrolled growth of abnormal cells in the body. Cancer develops when the body’s normal control mechanism stops working. Old cells do not die and instead grow out of control, forming new, abnormal cells. These extra cells may form a mass of tissue, called a tumor. Some cancers, such as leukemia, do not form tumors {person_obj.name}")

    if there_exists(["what are the most common symptoms of covid-19"]):
        speak(f"Fever, Dry cough, Fatigue {person_obj.name}")

    if there_exists(["what are the severe symptoms of covid-19"]):
        speak(f"shortness of breath, loss of appetite, confusion {person_obj.name}")

    if there_exists(["are there long term effects of covid-19"]):
        speak(f"Some people who have had COVID-19, whether they have needed hospitalization or not, continue to experience symptoms {person_obj.name}")

    if there_exists(["how can we protect ourselves if we do not know who is infected"]):
        speak(f"Stay safe by taking some simple precautions, such as physical distancing, wearing a mask, especially when distancing cannot be maintained {person_obj.name}")

    if there_exists(["what tests should i get to see if i have covid-19"]):
        speak(f"In most situations, a molecular test is used to detect SARS-CoV-2 and confirm infection. Polymerase chain reaction (PCR) is the most commonly used molecular test {person_obj.name}")

    if there_exists(["if i want to find out if i had covid-19 in the past what tests should i take"]):
        speak(f"Antibody tests can tell us whether someone has had an infection in the past, even if they have not had symptoms {person_obj.name}")

    if there_exists(["what should i do if i have been exposed to someone who has covid-19"]):
        speak(f"If testing is not available, stay home and away from others for 14 days {person_obj.name}")

    if there_exists(["what are the treatments available for covid-19"]):
        speak(f"now a days there are vaccines that are available {person_obj.name}")

    if there_exists(["Can humans become infected with a novel coronavirus of animal source?"]):
        speak(f"Several known coronaviruses are circulating in animals that have not yet infected humans. As surveillance improves around the world, more coronaviruses are likely to be identified {person_obj.name}")

    if there_exists(["is it possible to have flu and covid 19 at the same time"]):
        speak(f"Yes. It is possible to test positive for flu (as well as other respiratory infections) and COVID-19 at the same time {person_obj.name}")

    if there_exists(["whp is at increased risk for developing severe illness from corona virus"]):
        speak(f"earlier it was more dangerous for older people but now it is affecting more to the people under twenty five {person_obj.name}")

    if there_exists(["are people with disabilities at a higher risk"]):
        speak(f"Adults with disabilities are more likely to have an underlying medical condition that may put them at increased risk of severe illness from COVID-19 including, but not limited to, heart disease, stroke, diabetes, chronic kidney disease, cancer, high blood pressure, and obesity {person_obj.name}")

    if there_exists(["what is the difference between covid-19 and seasonal allergies"]):
        speak(f"COVID-19 is a contagious respiratory illness caused by infection with a new coronavirus (called SARS-CoV-2, the virus that causes COVID-19) {person_obj.name}")

    if there_exists(["what is contact tracing"]):
        speak(f"Contact tracing has been used for decades by state and local health departments to slow or stop the spread of infectious diseases {person_obj.name}")




    # 4: time

    # 5: search google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on google')

    # 6: search youtube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on youtube')

    if there_exists(["find location"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://google.nl/maps/place/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'here is what i found for {search_term} on maps')

    # 7: get stock price
    if there_exists(["price of"]):
        search_term = voice_data.lower().split(" of ")[
            -1].strip()  # strip removes whitespace after/before a term in string
        stocks = {
            "apple": "AAPL",
            "microsoft": "MSFT",
            "facebook": "FB",
            "tesla": "TSLA",
            "bitcoin": "BTC-USD"
        }
        try:
            stock = stocks[search_term]
            stock = yf.Ticker(stock)
            price = stock.info["regularMarketPrice"]

            speak(f'price of {search_term} is {price} {stock.info["currency"]} {person_obj.name}')
        except:
            speak('oops, something went wrong')
    if there_exists(["exit", "quit", "goodbye"]):
        speak("going offline")
        exit()

time.sleep(1)

person_obj = person()
while (1):
    voice_data = record_audio()  # get the voice input
    respond(voice_data)  # respond

r = sr.Recognizer()





