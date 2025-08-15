import tkinter as tk
from tkinter import ttk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

# -----------------------------
# Sample dataset
# -----------------------------
data = {
    'message': [
        'Free entry in a weekly competition to win FA Cup final tickets',
        'Hello, I would like to meet up sometime this week',
        'Congratulations! You have won a $1000 gift card',
        'Hey, are you free for a quick chat?',
        'Urgent! Your account has been compromised. Click here to secure it',
        'Hey, what’s up? Let’s grab lunch soon!'
    ],
    'label': [1, 0, 1, 0, 1, 0]  # 1 = spam, 0 = not spam
}

# Create DataFrame
df = pd.DataFrame(data)
X = df['message']
y = df['label']

# Vectorize the messages
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train the Naive Bayes model
model = MultinomialNB()
model.fit(X_vectorized, y)

# -----------------------------
# Functions
# -----------------------------
def predict_spam():
    input_message = text_entry.get("1.0", tk.END).strip()
    if input_message:
        input_vector = vectorizer.transform([input_message])
        prediction = model.predict(input_vector)
        if prediction[0] == 1:
            result_label.config(text="🚨 This message is SPAM!", foreground="red")
        else:
            result_label.config(text="✅ This message is NOT SPAM", foreground="green")
    else:
        result_label.config(text="⚠ Please enter a message.", foreground="orange")

def reset_fields():
    text_entry.delete("1.0", tk.END)
    result_label.config(text="", foreground="black")

# -----------------------------
# GUI Setup
# -----------------------------
root = tk.Tk()
root.title("📧 Spam Email Detection")
root.geometry("650x400")
root.configure(bg="#f4f4f4")

style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=6)
style.configure("TLabel", font=("Arial", 12))

# Title
title_label = tk.Label(root, text="Spam Email Detection (Naive Bayes)", font=("Arial", 16, "bold"), bg="#f4f4f4")
title_label.pack(pady=10)

# Instruction
instr_label = tk.Label(root, text="Enter your email/message below:", font=("Arial", 12), bg="#f4f4f4")
instr_label.pack()

# Text entry box
text_entry = tk.Text(root, height=6, width=70, font=("Arial", 12), wrap="word")
text_entry.pack(pady=10)

# Buttons frame
button_frame = tk.Frame(root, bg="#f4f4f4")
button_frame.pack(pady=5)

predict_button = ttk.Button(button_frame, text="Check Spam", command=predict_spam)
predict_button.grid(row=0, column=0, padx=10)

reset_button = ttk.Button(button_frame, text="Reset", command=reset_fields)
reset_button.grid(row=0, column=1, padx=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#f4f4f4")
result_label.pack(pady=15)

# Run the application
root.mainloop()
