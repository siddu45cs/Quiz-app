import tkinter as tk
from tkinter import ttk
import random
import datetime

# ------------------ QUIZ DATA ------------------
questions = [
    {"question": "What does CPU stand for?", "options": ["Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Central Processor Unit"], "answer": "Central Processing Unit"},
    {"question": "What does HTML stand for?", "options": ["Hyper Trainer Marking Language", "Hyper Text Markup Language", "Hyper Text Marketing Language", "Hyper Tool Multi Language"], "answer": "Hyper Text Markup Language"},
    {"question": "Which language is used for AI?", "options": ["Python", "HTML", "C", "SQL"], "answer": "Python"},
    {"question": "Which is not an operating system?", "options": ["Windows", "Linux", "Oracle", "Mac"], "answer": "Oracle"},
    {"question": "What does RAM stand for?", "options": ["Read Access Memory", "Random Access Memory", "Run Access Memory", "Random Active Memory"], "answer": "Random Access Memory"},
    {"question": "Which one is not a programming language?", "options": ["Python", "Java", "C++", "HTML"], "answer": "HTML"},
    {"question": "Which company developed the Python language?", "options": ["Microsoft", "Google", "ABC", "Apple"], "answer": "ABC"},
    {"question": "What does GUI stand for?", "options": ["Graphical User Interface", "Graphical Unified Input", "General User Interaction", "Graphical Universal Interface"], "answer": "Graphical User Interface"},
    {"question": "Which one is used for web development?", "options": ["Flask", "NumPy", "Pandas", "Matplotlib"], "answer": "Flask"},
    {"question": "What is the binary value of decimal 5?", "options": ["101", "110", "111", "100"], "answer": "101"},
    {"question": "Who is the founder of Microsoft?", "options": ["Steve Jobs", "Bill Gates", "Mark Zuckerberg", "Elon Musk"], "answer": "Bill Gates"},
    {"question": "Which protocol is used for web?", "options": ["HTTP", "FTP", "SMTP", "TCP"], "answer": "HTTP"},
    {"question": "Which tag is used to add a link in HTML?", "options": ["<a>", "<link>", "<href>", "<src>"], "answer": "<a>"},
    {"question": "What is the default port for HTTP?", "options": ["21", "25", "80", "8080"], "answer": "80"},
    {"question": "Which device is used for network connectivity?", "options": ["Router", "Monitor", "Keyboard", "Scanner"], "answer": "Router"},
    {"question": "What does SQL stand for?", "options": ["Structured Query Language", "System Query Language", "Simple Query Logic", "Sequential Query Language"], "answer": "Structured Query Language"},
    {"question": "Which of the following is not a database?", "options": ["MySQL", "MongoDB", "Oracle", "Visual Studio"], "answer": "Visual Studio"},
    {"question": "Which key is used to stop a running program in Python IDE?", "options": ["Shift + F5", "Ctrl + C", "Alt + F4", "Ctrl + Z"], "answer": "Ctrl + C"},
    {"question": "What is used to define a block of code in Python?", "options": ["Brackets", "Indentation", "Parentheses", "Quotation"], "answer": "Indentation"},
    {"question": "Which of the following is immutable?", "options": ["List", "Set", "Dictionary", "Tuple"], "answer": "Tuple"},
    {"question": "What does IP stand for?", "options": ["Internet Provider", "Internet Protocol", "Internal Program", "Interface Program"], "answer": "Internet Protocol"},
    {"question": "What is the extension of Python files?", "options": [".java", ".py", ".html", ".exe"], "answer": ".py"},
    {"question": "Which data structure uses FIFO?", "options": ["Stack", "Queue", "Tree", "Graph"], "answer": "Queue"},
    {"question": "What is the brain of a computer?", "options": ["CPU", "GPU", "RAM", "ROM"], "answer": "CPU"},
    {"question": "What does BIOS stand for?", "options": ["Basic Input Output System", "Binary Input Output System", "Basic Integrated Operating System", "Base Input Output Setup"], "answer": "Basic Input Output System"},
]

# ------------------ MAIN APP ------------------
root = tk.Tk()
root.title("CS Quiz App")
root.geometry("700x500")
root.config(bg="#1E1E1E")

username = ""
score = 0
time_left = 60
current_q = 0
selected_option = tk.StringVar(value="")

# Shuffle questions
random.shuffle(questions)

# ------------------ FUNCTIONS ------------------
def start_quiz():
    global username, current_q, score, time_left
    username = name_entry.get()
    if not username:
        name_label.config(text="Enter your name before starting!", fg="red")
        return

    welcome_frame.pack_forget()
    quiz_frame.pack(fill="both", expand=True)
    score = 0
    current_q = 0
    time_left = 60
    load_question()
    update_timer()

def load_question():
    global current_q
    q = questions[current_q]
    question_label.config(text=f"Q{current_q+1}. {q['question']}")
    selected_option.set(None)

    opts = q['options'][:]
    random.shuffle(opts)
    for i, option in enumerate(opts):
        option_buttons[i].config(text=option, value=option)

def next_question():
    global current_q, score
    if selected_option.get() == questions[current_q]['answer']:
        score += 1
    current_q += 1
    if current_q < len(questions):
        load_question()
    else:
        show_result()

def update_timer():
    global time_left
    if time_left > 0:
        time_left -= 1
        timer_label.config(text=f"⏳ Time left: {time_left}s")

        # Progress bar color change
        if time_left <= 10:
            style.configure("green.Horizontal.TProgressbar", troughcolor="#444", background="red")
        elif time_left <= 30:
            style.configure("green.Horizontal.TProgressbar", troughcolor="#444", background="orange")

        progress['value'] = (time_left / 60) * 100
        root.after(1000, update_timer)
    else:
        show_result()

def show_result():
    quiz_frame.pack_forget()
    save_score()
    result_label.config(text=f"Quiz Over!\n{username}, your score is {score}/{len(questions)} 🎯")
    result_frame.pack(fill="both", expand=True)

def restart_quiz():
    result_frame.pack_forget()
    welcome_frame.pack(fill="both", expand=True)
    name_entry.delete(0, tk.END)

def save_score():
    with open("quiz_scores.txt", "a") as f:
        f.write(f"{username} - {score}/{len(questions)} - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

# ------------------ STYLING ------------------
style = ttk.Style()
style.theme_use("clam")
style.configure("green.Horizontal.TProgressbar", troughcolor="#333", background="green", thickness=20)

# ------------------ WELCOME FRAME ------------------
welcome_frame = tk.Frame(root, bg="#1E1E1E")
welcome_frame.pack(fill="both", expand=True)

title_label = tk.Label(welcome_frame, text="Welcome to the CS Quiz App 💻", font=("Arial", 24, "bold"), fg="white", bg="#1E1E1E")
title_label.pack(pady=50)

name_label = tk.Label(welcome_frame, text="Enter your name:", font=("Arial", 16), fg="white", bg="#1E1E1E")
name_label.pack(pady=10)

name_entry = tk.Entry(welcome_frame, font=("Arial", 16), width=25, justify="center")
name_entry.pack(pady=10)

start_button = tk.Button(welcome_frame, text="Start Quiz", command=start_quiz, font=("Arial", 16, "bold"), bg="#4CAF50", fg="white", width=15)
start_button.pack(pady=20)

# ------------------ QUIZ FRAME ------------------
quiz_frame = tk.Frame(root, bg="#1E1E1E")

question_label = tk.Label(quiz_frame, text="", font=("Arial", 18, "bold"), wraplength=600, fg="white", bg="#1E1E1E")
question_label.pack(pady=30)

option_buttons = []
for i in range(4):
    btn = tk.Radiobutton(quiz_frame, text="", variable=selected_option, value="", font=("Arial", 14),
                         fg="white", bg="#1E1E1E", selectcolor="#333", activebackground="#333", anchor="w", justify="left")
    btn.pack(fill="x", padx=100, pady=5)
    option_buttons.append(btn)

next_button = tk.Button(quiz_frame, text="Next ➡️", command=next_question, font=("Arial", 14, "bold"),
                        bg="#2196F3", fg="white", width=10)
next_button.pack(pady=20)

timer_label = tk.Label(quiz_frame, text="", font=("Arial", 14, "bold"), fg="yellow", bg="#1E1E1E")
timer_label.pack()

progress = ttk.Progressbar(quiz_frame, style="green.Horizontal.TProgressbar", length=400)
progress.pack(pady=10)

# ------------------ RESULT FRAME ------------------
result_frame = tk.Frame(root, bg="#1E1E1E")
result_label = tk.Label(result_frame, text="", font=("Arial", 20, "bold"), fg="white", bg="#1E1E1E")
result_label.pack(pady=80)

restart_button = tk.Button(result_frame, text="Restart Quiz 🔁", command=restart_quiz, font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", width=15)
restart_button.pack(pady=20)

root.mainloop()

