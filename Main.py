import streamlit as st
import random

class EmotionChatbot:
    def __init__(self):
        # Define emotion keywords
        self.emotion_keywords = {
        'happy': [
            'happy', 'joy', 'excited', 'great', 'awesome', 'wonderful', 'fun', 
            'amazing', 'delighted', 'smile', 'laugh', 'yay', 'cheerful', 'glad', 
            'love', 'good', 'cool', 'super', 'wow', 'sunny'],
        'sad': [
            'sad', 'upset', 'unhappy', 'depressed', 'down', 'miserable', 'lonely', 
            'bad', 'terrible', 'cry', 'tears', 'blue', 'bored', 'hurt', 'sorry', 
            'worried', 'missing', 'gloomy', 'blah'],
        'angry': [
            'angry', 'mad', 'furious', 'irritated', 'annoyed', 'frustrated', 'rage', 
            'upset', 'yell', 'mean', 'grumpy', 'bad', 'ugh', 'argh', 'shout', 'hate', 
            'fighting', 'no', 'red'],
        'fear': [
            'scared', 'afraid', 'worried', 'nervous', 'anxious', 'terrified', 'panic', 
            'dread', 'spooky', 'ghost', 'dark', 'alone', 'shaking', 'oh no', 'help', 
            'trouble', 'creepy', 'monster', 'boo', 'shy'],
        'surprise': [
            'wow', 'surprised', 'shocked', 'amazing', 'unexpected', 'unbelievable', 
            'oh', 'yay', 'what', 'really', 'cool', 'whoa', 'look', 'omg', 'guess', 
            'new', 'yay', 'gift', 'big', 'suddenly'],
        'neutral': [
            'okay', 'fine', 'alright', 'normal', 'meh', 'so-so', 'neutral', 
            'average', 'nothing', 'ok', 'alright', 'whatever', 'hmm', 'huh', 
            'thinking', 'calm', 'steady', 'same', 'usual', 'regular']
        }

        
        # Responses for different emotions
        self.emotion_responses = {
            'happy': [
                "It's wonderful that you're feeling happy!",
                "Great to hear you're in a good mood!",
                "Happiness is awesome! Keep smiling!"
            ],
            'sad': [
                "I'm sorry you're feeling sad. Would you like to talk about it?",
                "It's okay to feel down sometimes. Remember, things will get better.",
                "Sending you a virtual hug and support."
            ],
            'angry': [
                "I can sense you're feeling frustrated. Would you like to calm down?",
                "It's okay to feel angry. Let's take some deep breaths.",
                "Anger is a normal emotion. Let's talk about what's bothering you."
            ],
            'fear': [
                "It sounds like you're feeling worried. You're not alone.",
                "Fear is a natural emotion. Would you like to discuss what's making you anxious?",
                "Remember, many things we fear don't end up being as bad as we imagine."
            ],
            'surprise': [
                "Wow, that sounds like an unexpected moment!",
                "Surprises can be exciting! Tell me more.",
                "What a surprising turn of events!"
            ],
            'neutral': [
                "I'm listening. How are you feeling?",
                "Tell me more about what's on your mind.",
                "I'm here to chat and understand your emotions."
            ]
        }
    
    def detect_emotion(self, user_input):
        """
        Detect the emotion in the user's input
        """
        # Convert input to lowercase
        user_input = user_input.lower()
        
        # Check for emotion keywords
        for emotion, keywords in self.emotion_keywords.items():
            for keyword in keywords:
                if keyword in user_input:
                    return emotion
        
        # If no specific emotion is detected
        return 'neutral'
    
    def respond(self, user_input):
        """
        Generate a response based on detected emotion
        """
        # Detect the emotion
        emotion = self.detect_emotion(user_input)
        
        # Select a random response for the detected emotion
        response = random.choice(self.emotion_responses[emotion])
        
        return emotion, response

def main():
    # Set page title and icon
    st.set_page_config(page_title="Emotion Recognition Chatbot", page_icon="🤖")
    
    # Create chatbot instance
    chatbot = EmotionChatbot()
    
    # Title and description
    st.title("🤖 MoodMate: Your Emotion Companion!")
    st.write("Talk to me and I'll help you understand your emotions!")
    
    # Emotion display area
    emotion_placeholder = st.empty()
    emoji_placeholder = st.empty()
    response_placeholder = st.empty()
    image_placeholder = st.empty()
    
    # Chat input
    user_input = st.text_input("Your message:", key="user_input")
    
    # Add a button to trigger emotion detection
    if st.button("Submit"):
        # Process user input when button is clicked
        if user_input.strip():  # Check if user_input is not empty
            # Detect emotion and get response
            detected_emotion, bot_response = chatbot.respond(user_input)
            
            # Display emotion with colorful styling
            emotion_color_map = {
                'happy': '🟢 Happy',
                'sad': '🔵 Sad',
                'angry': '🔴 Angry',
                'fear': '🟠 Afraid',
                'surprise': '🟣 Surprised',
                'neutral': '⚪ Neutral'
            }

            emoji_images = {
                'happy': 'D:\Anbazhagan\Abishek\Emotion\Images\happy.png',      
                'sad': 'D:\Anbazhagan\Abishek\Emotion\Images\Sad.png',          
                'angry': 'D:\Anbazhagan\Abishek\Emotion\Images\\angry.png',      
                'fear': 'D:\Anbazhagan\Abishek\Emotion\Images\\fear.png',        
                'surprise': 'D:\Anbazhagan\Abishek\Emotion\Images\surprise.png',
                'neutral': 'D:\Anbazhagan\Abishek\Emotion\Images\\neutral.png'   
            }
            
            emotion_placeholder.markdown(f"**Emotion Detected:** {emotion_color_map[detected_emotion]}")
            emoji_placeholder.image(emoji_images[detected_emotion], width=400)
            response_placeholder.info(bot_response)
        else:
            response_placeholder.warning("Please enter a message before clicking Submit!")
        
       
    # Sidebar information
    st.sidebar.header("About the Chatbot")
    st.sidebar.info("""
    This AI chatbot uses simple Natural Language Processing (NLP)
    to detect emotions in text. It looks for specific keywords
    to understand how you're feeling.
    
    **How it works:**
    1. Type a message
    2. The bot detects your emotion
    3. Provides a supportive response
                    
    **Tools & Technologies used:**
                    
    This app uses Python constructs like classes to encapsulate chatbot logic, with the __init__ method initializing emotion keywords and responses stored 
    in dictionaries. The chatbot identifies emotions using loops to match keywords and generates responses using random.choice. Streamlit handles the UI 
    with functions like st.text_input, st.button, st.markdown, and st.image, combined with HTML/CSS for styling. Conditional statements (if-else) process 
    user inputs and control responses. Overall, it integrates Python’s OOP, data structures, and Streamlit's interactive elements for a seamless chatbot experience.

    **Author:**
                    
    Abishek Anbazhagan,
    Grade VI, Amrita Vidyalayam, Ettimadai.

    """)


if __name__ == "__main__":
    main()