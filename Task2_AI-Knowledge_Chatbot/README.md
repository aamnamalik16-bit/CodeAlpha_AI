# AI Knowledge Assistant (Chatbot)

This project is developed as part of the CodeAlpha Artificial Intelligence Internship.

---

## Project Overview
AI Knowledge Assistant is a GUI-based chatbot built using Python and Tkinter.  
It answers user queries related to Artificial Intelligence, Machine Learning, Deep Learning, Robotics, and Technology using Natural Language Processing techniques.

The chatbot uses TF-IDF (Term Frequency–Inverse Document Frequency) and Cosine Similarity to match user questions with predefined FAQs and generate relevant responses.

---

## Features
- GUI-based chatbot interface using Tkinter
- Left-right aligned chat bubbles (user and bot)
- Dark theme professional UI
- Scrollable chat window
- Smart FAQ matching using NLP
- Covers multiple domains:
  - Artificial Intelligence
  - Machine Learning
  - Deep Learning
  - Robotics
  - Technology

---

## Technologies Used
- Python 3.10+
- Tkinter (GUI development)
- Scikit-learn
  - TfidfVectorizer
  - Cosine Similarity

---

## Requirements

Make sure you have the following installed:

Python 3.10 or above  
pip install scikit-learn

---

## How to Run

1. Clone or download the repository  
2. Open terminal in project folder  
3. Install dependencies:

pip install scikit-learn

4. Run the chatbot:

python chatbot.py

---

## How It Works

1. User enters a question in the chat interface  
2. Input is compared with predefined FAQ dataset  
3. TF-IDF converts text into numerical vectors  
4. Cosine similarity finds the closest matching question  
5. Best matched answer is displayed to the user  

---

## Learning Outcomes

- GUI development using Tkinter  
- Basic Natural Language Processing  
- Implementing TF-IDF and Cosine Similarity  
- Building interactive AI applications  

---

## Future Improvements

- Add voice input/output  
- Integrate real AI APIs (ChatGPT, Gemini)  
- Add database for dynamic learning  
- Improve NLP accuracy  

---

## Author

Developed by [Aamna Amin]  
CodeAlpha AI Internship - Task 2
