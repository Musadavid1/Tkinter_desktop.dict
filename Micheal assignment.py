import tkinter as tk

# Tiv words and their English translations
tiv_dict = [
    ("Msen", "Love"),
    ("Tiv", "Tiv people"),
    ("Yô", "House"),
    ("Aondo", "God"),
    ("Ortom", "Food"),
    ("Mbatsav", "Children"),
    ("Kyôhô", "Thank you"),
    ("Kwagh", "Thing"),
    ("Shima", "Heart"),
    ("Or", "Person"),
    ("Tor", "King"),
    ("Nyian", "Life"),
    ("Gbenda", "Mountain"),
    ("Ken", "Road"),
    ("Yange", "Peace"),
    ("Tar", "Land"),
    ("Vesen", "Health"),
    ("Gba", "Stone"),
    ("Ior", "People"),
    ("Do", "Go"),
]

# Create the main application window
root = tk.Tk()
root.title("Tiv Language Words")

# Create a frame to hold the labels
frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

# Add headings
tk.Label(frame, text="Tiv Word", font=("Arial", 14, "bold"), width=15, anchor="w").grid(row=0, column=0)
tk.Label(frame, text="English Translation", font=("Arial", 14, "bold"), width=20, anchor="w").grid(row=0, column=1)

# Display the Tiv words and translations
for i, (tiv, eng) in enumerate(tiv_dict, start=1):
    tk.Label(frame, text=tiv, font=("Arial", 12), anchor="w").grid(row=i, column=0, sticky="w")
    tk.Label(frame, text=eng, font=("Arial", 12), anchor="w").grid(row=i, column=1, sticky="w")

# Run the application
root.mainloop()
