from flask import Flask, render_template, request, redirect, url_for
import random
import json

app = Flask(__name__)

with open("words.json") as f:
    words = json.load(f)

word = random.choice(words)
hidden_word = ["_"] * len(word)
num_guesses = 0
vite = 7
guessed_letters = []
hangman_advance = 0

@app.route("/", methods=["GET", "POST"])
def index():
    global num_guesses, vite, hangman_advance
    if request.method == "POST":
        letter = request.form["letter"]
        num_guesses += 1
        if len(letter) > 1:
            if letter == word:
                return redirect(url_for("win"))
            else:
                return render_template("hangman.html", hidden_word=hidden_word, num_guesses=num_guesses, vite = vite, guessed_letters = guessed_letters, errore = "Inserisci una lettera alla volta, a meno che tu non sappia la parola")
        for i in range(len(word)):
            if word[i] == letter:
                hidden_word[i] = letter
        if letter in word:
            if "_" not in hidden_word:
                return redirect(url_for("win"))
            elif letter in guessed_letters:
                return render_template("hangman.html", hidden_word=hidden_word, num_guesses=num_guesses, vite = vite, guessed_letters = guessed_letters, errore = "Lettera già utilizzata")
            else:
                guessed_letters.append(letter)
                return render_template("hangman.html", hidden_word=hidden_word, num_guesses=num_guesses, vite = vite, guessed_letters = guessed_letters, errore = "Lettera corretta")
        elif letter not in word:
            if letter in guessed_letters:
                return render_template("hangman.html", hidden_word=hidden_word, num_guesses=num_guesses, vite = vite, guessed_letters = guessed_letters, errore = "Lettera già utilizzata")
            else:
                guessed_letters.append(letter)
                hangman_advance += 1
                vite -= 1
                if vite <= 0:
                    return redirect(url_for("lose"))
                return render_template("hangman.html", hidden_word=hidden_word, num_guesses=num_guesses, vite = vite, guessed_letters = guessed_letters, errore= "Lettera sbagliata")
        
        return render_template("hangman.html", hidden_word=hidden_word, num_guesses=num_guesses, vite = vite, guessed_letters = guessed_letters)
    
    return render_template("hangman.html", hidden_word=hidden_word, num_guesses=num_guesses, vite = vite, guessed_letters = guessed_letters)

@app.route("/play_again")
def play_again():
    global word, guessed_letters, num_guesses, hidden_word, hangman_advance, vite
    word = random.choice(words)
    hidden_word = ["_"] * len(word)
    num_guesses = 0
    guessed_letters = []
    hangman_advance = 0
    vite = 7
    return redirect(url_for("index"))

@app.route("/win")
def win():
    return render_template("win.html", word=word)

@app.route("/lose")
def lose():
    return render_template("lose.html", word=word)


if __name__ == "__main__":
    app.run(debug=True, port=5070)