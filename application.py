import tkinter as tk

# Define a dictionary to map English letters to Bengali phonemes
phoneme_map = {
    "a": "অ",
    "b": "ব",
    "c": "ক",
    "d": "দ",
    "e": "ই",
    "f": "ফ",
    "g": "গ",
    "h": "হ",
    "i": "ই",
    "j": "জ",
    "k": "ক",
    "l": "ল",
    "m": "ম",
    "n": "ন",
    "o": "ও",
    "p": "প",
    "q": "ক",
    "r": "র",
    "s": "স",
    "t": "ট",
    "u": "উ",
    "v": "ভ",
    "w": "ও",
    "x": "ক্স",
    "y": "ই",
    "z": "জ"
}

# Define a dictionary to map context-dependent phonemes
context_phoneme_map = {
    "sh": "শ"
}

# Define a function to convert English text to Bengali using the phoneme maps
def convert_to_bengali(english_text):
    # Apply the initial phoneme mapping from English to Bengali
    bengali_text = ""
    for i in range(len(english_text)):
        if i < len(english_text) - 1 and english_text[i:i+2].lower() in context_phoneme_map:
            phoneme = context_phoneme_map[english_text[i:i+2].lower()]
            bengali_text += phoneme
        else:
            phoneme = phoneme_map.get(english_text[i].lower(), english_text[i])
            bengali_text += phoneme

    return bengali_text

# Define a function to handle the "Convert" button click event
def on_convert_button_click():
    # Retrieve the text from the input field
    english_text = input_field.get()

    # Convert the English text to Bengali using the phoneme maps
    bengali_text = convert_to_bengali(english_text)

    # Insert the Bengali text into the output field
    output_field.delete("1.0", tk.END)
    output_field.insert("1.0", bengali_text)

# Create the Tkinter window
root = tk.Tk()
root.title("Bengali Typing Application")

# Create the input field and label
input_label = tk.Label(root, text="Enter text in English:")
input_label.pack()
input_field = tk.Entry(root)
input_field.pack()

# Create the output field and label
output_label = tk.Label(root, text="Bengali output:")
output_label.pack()
output_field = tk.Text(root)
output_field.pack()

# Create the convert button
convert_button = tk.Button(root, text="Convert", command=on_convert_button_click)
convert_button.pack()

# Start the Tkinter event loop
root.mainloop()
