import re
import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio


engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

def speak(audio):

    engine.say(audio)
    engine.runAndWait()


def takeCommand():

    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)     

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query        

# import long_responses as long

ls = 'I am not fully trained yet. Sorry'
def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)
   
    if 'fever' in message:
            
            print('whats your age')
            speak('whats your age')
            ip = int(takeCommand().lower())
            print("You: ",ip)

            if ip <=5:
                return 'Kindley take the prescribe medicen one in morning after breakfast and night after dinner : Medicien is  PARACETAMOL 120MG/5ML'
            elif ip>5 and ip<=9:
                return 'Kindley take the prescribe medicen one in morning after breakfast and night after dinner : Medicien is  PARACETAMOL/ACETAMINOPHEN 250MG/5ML'
            elif ip>9 and ip<=15:
                return 'Kindley take the prescribe medicen one in morning after breakfast and night after dinner : Medicien is  PARACETAMOL 500MG'
            elif ip >=16:
                return 'Kindley take the prescribe medicen one in morning after breakfast and night after dinner : Medicien is  PARACETAMOL 600MG'
    
    if 'cough' in message:
            a = print('Bot :whats your age')
            speak('whats your age')
            ip = int(input("You (age in numbers):"))
            speak(ip)
            if ip<9:
                return 'data not present'
            
            if ip>9 and ip<12:
                return 'Kindley take the prescribe medicen from chemist : Medicien is AMBROXOL-15MG + GUAIPHENESIN-50MG + LEVOSALBUTAMOL-0.5MG'
            elif ip>12 :
                ip = input("Bot : 1. Dry cough \n      2. Flum cough: ")
                if 1 == int(ip):
                    return 'Kindley take the prescribe medicen from chemist : Medicien is TERBUTALINE SULPHATE-1.25MG/5ML + BROMHEXINE HYDROCHLORIDE-2MG/5ML + GUAIPHENESIN-50MG/5ML + MENTHOL-0.5MG/5ML '
                if 2 == int(ip):
                    return 'Kindley take the prescribe medicen from chemist : Medicien is AMBROXOL-30MG + GUAIPHENESIN-50MG + LEVOSALBUTAMOL-1MG '
    
    if 'stomach' and 'pain'  in message:
            a = print('whats your age')
            speak('whats your age')
            ip = int(input("You (age in numbers):"))
            speak(ip)
            if ip <=10:
                return 'Kindley take the prescribe medicen from chemist : Medicien is DICYCLOMINE-10MG + SIMETHICONE-40MG'
            if ip >10:
                return 'Kindley take the prescribe medicen from chemist : Medicien is DICYCLOMINE-10MG + MEFENAMIC ACID-250MG'
            
    
    if 'head' and 'ache' in message:
            a = print('whats your age')
            speak('whats your age')

            ip = int(input("You (age in numbers):"))
            speak(ip)
            if ip > 2 and ip <=10:
                return 'Kindley take the prescribe medicen from chemist : Medicien is Aceclofenac(50.0 Mg) + Paracetamol / Acetaminophen(125.0 Mg'
            if ip >10:
                return 'Kindley take the prescribe medicen from chemist : Medicien is CAFFEINE-50MG + PARACETAMOL-300MG + PROPYPHENAZONE-150MG'
                
    if 'cold'  in message:
            a = print('whats your age')
            speak('whats your age')

            ip = int(input("You (age in numbers):"))
            if ip > 3 and ip <=16:
                return 'Kindley take the prescribe medicen from chemist : Medicien is CHLORPHENIRAMINE-1MG + PARACETAMOL-125MG + PHENYLEPHRINE-5MG + SODIUM CITRATE-60MG'
            if ip >16:
                return 'Kindley take the prescribe medicen from chemist : Medicien is CHLORPHENIRAMINE-8MG + PHENYLEPHRINE-20MG'
            
    else:
    # Responses -------------------------------------------------------------------------------------------------------
        response('Hello! How may i help you ?', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
        response('See you!', ['bye', 'goodbye'], single_response=True)
        response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
        response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
        response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    
        best_match = max(highest_prob_list, key=highest_prob_list.get)
        return ls if highest_prob_list[best_match] < 1 else best_match

# Testing the response system

print('Bot : Welcome, please tell ur medical problem')
query = 'Welcome, please tell ur medical problem'
speak(query)

while True:   
    query = takeCommand().lower()
    print("You: ",query)
    
    split_message = re.split(r'\s+|[,;?!.-]\s*', query)
    res = check_all_messages(split_message)    
    print('Bot: ' + res)
    speak(res)
