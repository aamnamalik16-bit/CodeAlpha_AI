import tkinter as tk
from tkinter import ttk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Expanded FAQ data (many questions)
questions = [
    # Greetings
    "hello","hi","how are you","who are you","what can you do",

    # AI
    "what is ai","define ai","explain artificial intelligence",
    "applications of ai","advantages of ai","disadvantages of ai",

    # Machine Learning
    "what is machine learning","define machine learning",
    "types of machine learning","supervised learning",
    "unsupervised learning","reinforcement learning",
    "what is overfitting","what is underfitting",

    # Deep Learning
    "what is deep learning","define deep learning",
    "difference between ai and deep learning",
    "what is neural network","types of neural networks",
    "what is cnn","what is rnn",

    # Data Science
    "what is data science","define data science",
    "role of data scientist","tools used in data science",

    # NLP
    "what is nlp","define nlp",
    "applications of nlp","examples of nlp",

    # Robotics
    "what is robotics","define robotics",
    "applications of robotics","types of robots",
    "robotics in ai","future of robotics",

    # Technology
    "what is technology","importance of technology",
    "latest technologies","what is cloud computing",
    "what is iot","what is blockchain",
    "what is cybersecurity","what is automation",
    "what is computer vision",

    # Programming
    "what is python","why python is used in ai",
    "what is programming","what is algorithm",
    "what is dataset"
]

answers = [
    # Greetings
    "Hello! How can I help you today about AI?",
    "Hi there! What would you like to know about AI?",
    "I am working perfectly! How can I assist you?",
    "I am an AI-Knowledge Assistant chatbot.",
    "I can answer questions related to AI, Machine Learning, Robotics, and Technology.",

    # AI
    "AI stands for Artificial Intelligence. It enables machines to think and make decisions.",
    "AI is the simulation of human intelligence in machines.",
    "Artificial Intelligence allows machines to learn, reason, and solve problems.",
    "AI is used in healthcare, self-driving cars, chatbots, and more.",
    "AI improves efficiency, automation, and decision-making.",
    "AI may cause job loss and requires high cost and data.",

    # Machine Learning
    "Machine Learning is a subset of AI that allows systems to learn from data.",
    "Machine Learning enables computers to improve automatically without programming.",
    "Types include supervised, unsupervised, and reinforcement learning.",
    "Supervised learning uses labeled data.",
    "Unsupervised learning finds hidden patterns in data.",
    "Reinforcement learning learns through rewards and punishments.",
    "Overfitting happens when a model memorizes training data.",
    "Underfitting happens when a model fails to learn patterns.",

    # Deep Learning
    "Deep Learning is a subset of machine learning using neural networks.",
    "Deep Learning uses multiple layers to learn complex patterns.",
    "AI is broader, while deep learning is a specialized part of AI.",
    "A neural network is inspired by the human brain structure.",
    "Types include CNN, RNN, and ANN.",
    "CNN is used for image processing.",
    "RNN is used for sequence data like text and speech.",

    # Data Science
    "Data Science involves analyzing data to extract useful insights.",
    "Data Science combines statistics, programming, and domain knowledge.",
    "A data scientist analyzes data and builds models.",
    "Tools include Python, R, SQL, and machine learning libraries.",

    # NLP
    "NLP stands for Natural Language Processing.",
    "NLP helps machines understand human language.",
    "Applications include chatbots, translation, and speech recognition.",
    "Examples include Siri, Google Translate, and chatbots.",

    # Robotics
    "Robotics involves designing and building robots.",
    "Robotics combines engineering, AI, and programming.",
    "Used in manufacturing, healthcare, and automation.",
    "Types include industrial, service, and humanoid robots.",
    "Robotics uses AI to make intelligent robots.",
    "The future includes smart and autonomous robots.",

    # Technology
    "Technology is the application of scientific knowledge.",
    "Technology improves productivity and quality of life.",
    "Examples include AI, IoT, blockchain, and cloud computing.",
    "Cloud computing provides services over the internet.",
    "IoT connects devices through the internet.",
    "Blockchain is a secure decentralized system.",
    "Cybersecurity protects systems from threats.",
    "Automation uses machines to perform tasks automatically.",
    "Computer Vision helps machines understand images.",

    # Programming
    "Python is a popular programming language used in AI.",
    "Python is simple and has powerful AI libraries.",
    "Programming is writing instructions for computers.",
    "An algorithm is a step-by-step solution to a problem.",
    "A dataset is a collection of data used for analysis."
]

# Window
root = tk.Tk()
root.title("🤖 AI-Knowledge Assistant")
root.geometry("900x550")
root.configure(bg="#09122a")

# Title
tk.Label(root, text="🤖 AI-Knowledge Assistant",
         font=("Segoe UI", 20, "bold"),
         bg="#0f172a", fg="white").pack(pady=10)

welcome = tk.Label(root,
                   text="I am an AI Assistant! Ask me anything about AI, ML, or Technology.",
                   font=("Segoe UI", 13),
                   bg="#0A142E",
                   fg="#d8e1e7",
                   wraplength=600,
                   justify="center")
welcome.pack(pady=5)

# Main frame 
main_frame = tk.Frame(root, bg="#081023")
main_frame.pack(fill="both", expand=True)

# Chat container FULL WIDTH
chat_container = tk.Frame(main_frame, bg="#0f172a")
chat_container.pack(fill="both", expand=True)

canvas = tk.Canvas(chat_container, bg="#0f172a", highlightthickness=0)

# Create styled scrollbar
style = ttk.Style()
style.theme_use("default")

style.configure("Custom.Vertical.TScrollbar",
                background="#363937",
                troughcolor="#18191a")

scrollbar = ttk.Scrollbar(chat_container,
                          orient="vertical",
                          command=canvas.yview,
                          style="Custom.Vertical.TScrollbar")

chat_frame = tk.Frame(canvas, bg="#0f172a")

chat_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.create_window((0, 0), window=chat_frame, anchor="nw", width=880)
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Chat bubbles
def add_message(text, sender="user"):
    row = tk.Frame(chat_frame, bg="#0f172a")
    row.pack(fill="x", pady=5)

    if sender == "user":
        bubble = tk.Label(row, text=text,
                          bg="#12873D", fg="white",
                          font=("Segoe UI", 14),
                          wraplength=400,
                          padx=10, pady=6)
        bubble.pack(side="right", padx=40)
    else:
        bubble = tk.Label(row, text=text,
                  bg="#274B80", fg="white",
                  font=("Segoe UI", 14),
                  wraplength=400,
                  justify="left",     
                  anchor="w",          
                  padx=10, pady=6)
        bubble.pack(side="left", padx=40)

    canvas.update_idletasks()
    canvas.yview_moveto(1.0)

# Chat logic
def send_message(event=None):
    msg = user_input.get("1.0", tk.END).strip().lower()
    if not msg:
        return

    add_message(msg, "user")

    all_texts = questions + [msg]
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(all_texts)

    similarity = cosine_similarity(vectors[-1], vectors[:-1])
    best_index = similarity.argmax()

    if similarity[0][best_index] > 0.3:
        reply = answers[best_index]
    else:
        reply = "Sorry, I don't understand. Please ask about AI, Machine Learning, or Technology."

    add_message(reply, "bot")
    user_input.delete("1.0", tk.END)

# INPUT (MODERN CENTERED STYLE)
input_frame = tk.Frame(main_frame, bg="#0f172a")
input_frame.pack(pady=20)

# Outer container (gives rounded card feel)
input_container = tk.Frame(input_frame,
                           bg="#1e293b",
                           bd=2,
                           relief="ridge")
input_container.pack(padx=10)

# Text input (clean & modern)
user_input = tk.Text(input_container,
                     height=1.5,
                     width=45,
                     bg="#243146",
                     fg="white",
                     insertbackground="white",
                     font=("Segoe UI", 14),
                     bd=0)
user_input.pack(side="left", padx=10, pady=8)

# Send button (modern style)
send_button = tk.Button(input_container,
                        text="➤",
                        bg="#1aaf51",
                        fg="Black",
                        font=("Segoe UI", 13, "bold"),
                        bd=0,
                        padx=12,
                        pady=6,
                        activebackground="#056729",
                        cursor="hand2",
                        command=send_message)
send_button.pack(side="right", padx=10)

# Enter key
def handle_enter(event):
    if not event.state & 0x1:
        send_message()
        return "break"

user_input.bind("<Return>", handle_enter)

root.mainloop()