import tkinter as tk
import random

# Definiera en lista med ord som spelet kan välja ifrån.
WORDS = ["python", "programmering", "utbildning", "hangman", "cykel", "skola", "matematik", "spel", "musik", "konst"]

# Definiera max antal gissningar.
MAXIMUM_NUMBER_OF_WRONG_LETTERS = 6

# Välj ett slumpmässigt ord som sperlaren ska gissa.
secret_word = random.choice(WORDS)
letters_guessed = []
number_of_wrong_guesses = 0

# Skapa huvudfönststret, "Main Window".
root = tk.Tk()
root.title("Hänga gubbe!")

# Funktion för att uppdatera visningen av ordet med rätt gissade bokstäver.
def display_word():
    displayed = "" # Skapa en tom sträng för att visa ordet.
    for letter in secret_word:
        if letter in letters_guessed:
            displayed += letter + " " # Om bokstaven är gissad, visa den.
        else:
            displayed += "_ " # Om bokstaven inte är gissad, visa istället ett underscore.
    return displayed

# Funktion som körs när spelaren klickar på "Gissa"-knappen och hanterar själva gissningen.
def guess():
    global number_of_wrong_guesses

    letter = players_guess.get().lower()
    players_guess.delete(0, tk.END)

    # Kontrollera att användaren bara matar in en bokstav.
    if len(letter) != 1 or not letter.isalpha():
        result_label.config(text="Gissa enbokstav!")
        return

    if letter in letters_guessed:
        result_label.config(text="Du har redan gissat på den bokstaven. Välj en annan :-)")
        return

    # Lägg till bokstaven i listan med gissade bokstäver.
    letters_guessed.append(letter) 

    if letter in secret_word:
        result_label.config(text="Rätt gissat!")
    else:
        number_of_wrong_guesses += 1
        result_label.config(text="Fel gissat!")

    word_label.config(text=display_word())
    wrong_guesses_label.config(text=f"Antal fel gissningar: {number_of_wrong_guesses} / {MAXIMUM_NUMBER_OF_WRONG_LETTERS}")

    # Kontrollera om spelaren vunnit.
    if all(b in letters_guessed for b in secret_word):
        result_label.config(text="Grattis! Du vann!")
        guess_button.config(state=tk.DISABLED)

    # Kontrollera om spelaren har förlorat.
    elif number_of_wrong_guesses >= MAXIMUM_NUMBER_OF_WRONG_LETTERS:
        result_label.config(text=f"GameOver! Ordet är: {secret_word}")
        guess_button.config(state=tk.DISABLED)

# Skapa användargränssnittet.
how_to_play_label = tk.Label(root, text="Gissa en bokstav:")
how_to_play_label.pack()

# Textbox för gissningen.
players_guess = tk.Entry(root)
players_guess.pack()

# Gissa-knappen.
guess_button = tk.Button(root, text="Gissa", command=guess)
guess_button.pack()

# Label för att visa ordet.
word_label = tk.Label(root, text=display_word(), font=("Courier", 24))
word_label.pack(pady=10)

# Label för att visa antalet fel gissningar.
wrong_guesses_label = tk.Label(root, text=f"Antal fel gissningar: {number_of_wrong_guesses} / {MAXIMUM_NUMBER_OF_WRONG_LETTERS}")
wrong_guesses_label.pack()

# Label för att visa resultatet av gissningen.
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Starta spelet.
root.mainloop()
