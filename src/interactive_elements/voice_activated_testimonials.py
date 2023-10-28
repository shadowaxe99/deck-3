```python
import speech_recognition as sr

class VoiceActivatedTestimonials:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.testimonials = ["Testimonial 1", "Testimonial 2", "Testimonial 3"]

    def listen_for_activation(self):
        with self.microphone as source:
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio)
                return self.process_command(text)
            except sr.UnknownValueError:
                return "Sorry, I did not understand that."
            except sr.RequestError as e:
                return f"Could not request results; {e}"

    def process_command(self, command):
        if "tell me more" in command.lower():
            return self.activate_testimonials()
        else:
            return "Sorry, I did not understand that."

    def activate_testimonials(self):
        return self.testimonials
```