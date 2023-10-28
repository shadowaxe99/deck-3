```python
import speech_recognition as sr

def listen_for_voice_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except:
            return None

def activate_testimonials():
    command = listen_for_voice_command()
    if command and "tell me more" in command.lower():
        return True
    return False
```