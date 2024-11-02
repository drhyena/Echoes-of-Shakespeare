import speech_recognition as sr
import google.generativeai as genai
import pyttsx3

# Configure the generative AI model
genai.configure(api_key="AlzaSyD4owEV2nQGHM8oN-Ir-YBxBeR-CM-70Ss")
model = genai.GenerativeModel("gemini-1.5-flash")

def call_it(query):
    response = model.generate_content(query)
    print(f"Shakespearean: {response.text}")
    engine = pyttsx3.init()
    engine.say(response.text)
    engine.runAndWait()

# Initialize recognizer class
r = sr.Recognizer()
continue_recording = True

while continue_recording:
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")

        try:
            # Recognize speech
            text = r.recognize_google(audio_text)
            print("Modern English: " + text)
            query = "Convert this into Shakespearean English: " + text
            call_it(query)
        except sr.UnknownValueError:
            print("Sorry, I did not get that.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

    # Prompt user to continue or stop
    na = input("Continue? (y/n): ")
    continue_recording = (na.lower() == "y")

print("Runtime over")
