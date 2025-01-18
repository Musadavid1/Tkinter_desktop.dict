import tkinter as tk

'Dictionary'
lang_dict = {
    "Bonjour": "Hello",
    "Au revoir": "Goodbye",
    "Merci": "Thank you",
    "Eau": "Water",
    "Pain": "Bread",
    "Maison": "House",
    "Voiture": "Car",
    "Bike": "Bicycle",
    "Amour": "Love",
    "Fleur": "Flower",
    "Soleil": "Sun",
    "Lune": "Moon",
    "Étoile": "Star",
    "Oiseau": "Bird",
    "Poisson": "Fish",
    "Livre": "Book",
    "École": "School",
    "Jardin": "Garden"
}


def translate():
    word = entry.get()
    translation = lang_dict.get(word, "Not found")
    result.delete(1.0, tk.END)
    result.insert(tk.END, translation)


root = tk.Tk()
root.title("French-English Dictionary")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Translate", command=translate)
button.pack()

result = tk.Text(root, height=5)
result.pack()

root.mainloop()

