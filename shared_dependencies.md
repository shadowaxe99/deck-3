Shared Dependencies:

1. **Exported Variables**: 
   - `user_name`: The name of the user interacting with the pitch deck.
   - `current_time`: The current time when the user is interacting with the pitch deck.
   - `user_country`: The country of the user for accessibility information.

2. **Data Schemas**: 
   - `User`: Contains user's information like name, country, etc.
   - `Slide`: Contains information about each slide like title, bullet points, etc.
   - `InteractiveElement`: Contains information about the interactive elements on each slide.

3. **DOM Element IDs**: 
   - `slide-title`: The title of each slide.
   - `slide-content`: The content of each slide.
   - `interactive-element`: The interactive element on each slide.

4. **Message Names**: 
   - `welcomeMessage`: The personalized welcome message on slide 2.
   - `testimonialActivation`: The voice command to activate testimonials on slide 7.

5. **Function Names**: 
   - `displaySlide()`: Function to display each slide.
   - `displayInteractiveElement()`: Function to display the interactive element on each slide.
   - `activateTestimonials()`: Function to activate testimonials on voice command.
   - `scheduleMeeting()`: Function to schedule a meeting using the AI scheduling bot.
   - `eyeTracking()`: Function to enable eye-tracking for no-touch scrolling and interaction.