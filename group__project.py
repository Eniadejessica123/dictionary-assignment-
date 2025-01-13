import tkinter as tk

# Function to display dictionaries


def display_dictionary(language):
    dictionaries = {
        # Eniade Jessica Ayodamola
        'EDO.dic': {'lare': 'come',
                    'eki': 'market',
                    'uwese': 'thank you',
                    'itohan': 'mercy',
                    'odion': "senior",
                    'osa': 'God',
                    'oowa': 'house',
                    'igho': 'money',
                    'obohian': 'welcome',
                    'lahor': 'please',
                    'agbon': 'world',
                    'eghuae': 'palace',
                    'iye': 'mother',
                    'igue': 'village',
                    'ivwe': 'bead',
                    'iyeke': 'back',
                    'oba': 'king',
                    'olotun': 'leader',
                    'ota': 'evening',
                    'owie': 'morning'},
        # Temitope Ayomide Elizabeth
        'Yoruba.dic': {'sare': 'run',
                       'ibawo': 'when',
                       'aaro': 'morning',
                       'irole': 'evening',
                       'bata': 'shoe',
                       'ina': 'light',
                       'agbara': 'power',
                       'fila': 'cap',
                       'irun': 'hair',
                       'iwasu': 'preach',
                       'irinajo': 'journey',
                       'aso': 'cloth',
                       'ounje': 'food',
                       'iwaju': 'front',
                       'kiniun': 'lion',
                       'dobale': 'postrate',
                       'ewa': 'beauty',
                       'kini': 'what',
                       'ife': 'love',
                       'ago': 'watch'},
        # Ezeanah Joseph Chiemerie
        'Igbo.dic': {"Bia": "Come",
                     "Nri": "Food",
                     "Mmiri": "Water",
                     "Efere": "Plate",
                     "Iko": "Cup",
                     "Nkita": "Dog",
                     "Oke": "Rat",
                     "Osikapa": "Rice",
                     "Gbaa oso": "Run",
                     "Ututu": "Morning",
                     "Daalu": "Thank You",
                     "Enyi": "Friend",
                     "Biko": "Please",
                     "Ezinulo": "Family",
                     "Akwukwo": "Book",
                     "Akwa": "Bed",
                     "Uka": "Church",
                     "Agwa": "Beans",
                     "Ahia": "Market",
                     "Ngaji": "Spoon", },
        # Ganiyu Glory Toluwani
        'Spanish.dic': {"hola": "hello",
                        "mundo": "world",
                        "gracias": "thank you",
                        "adios": "goodbye",
                        "por favour": "please",
                        "amigo": "friend",
                        "familia": "family",
                        "comida": "food",
                        "escula": "school",
                        "feliz": "happy",
                        "casa": "house",
                        "perro": "dog",
                        "agua": "water",
                        "amor": "love",
                        "libro": "book",
                        "gato": "cat",
                        "coche": "car",
                        "noche": "night",
                        "sol": "sun",
                        "luna": "moon", },
        # AKINROGBE EMMANUELLA
        'Hausa.dic': {"Gida": "house",
                      "ruwa": "water",
                      "mota": "car",
                      "kudi": "money",
                      "gashi": "hair",
                      "kifi": "fish",
                      "suna": "name", 
                      "gari": "town",
                      "jin": "hear",
                      "gani": "see",
                      "makaranta": "school",
                      "yara": "boy",
                      "kofa": "door",
                      "doki": "horse",
                      "wuta": "fire",
                      "hanci": "nose",
                      "dabba": "animal",
                      "jirgi": "airplane",
                      "baki": "mouth",
                      "hanya":"road", }
    }
    # Format dictionary output for readability
    selected_dict = dictionaries.get(language, 'Not available')
    formatted_text = f"{language} Dictionary:\n"
    for key, value in selected_dict.items():
        formatted_text += f"{key}: {value}\n"
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, formatted_text)
    result_text.config(state=tk.DISABLED)

# Create main window


root = tk.Tk()
root.title("Dictionaries App")
root.geometry("800x70")
root.configure(bg='#f0f0f0')

# Add a title label
title_label = tk.Label(root, text="Dictionaries App", font=("Helvetica", 18, "bold"), bg='#f0f0f0')
title_label.pack(pady=20)

# Create a text widget to display the dictionary output
result_text = tk.Text(root, font=("Helvetica", 12), bg='#f0f0f0', height=15, width=70, wrap=tk.WORD)
result_text.pack(pady=20)
result_text.config(state=tk.DISABLED)

# Button data with titles
buttons = [
    "EDO.dic",
    "Yoruba.dic",
    "Igbo.dic",
    "Spanish.dic",
    "Hausa.dic"
]

# Create buttons
for text in buttons:
    btn = tk.Button(root, text=text, command=lambda t=text: display_dictionary(t), height=1, width=20, bg='#4caf50', fg='white', font=("Helvetica", 12))
    btn.pack(pady=10)

# Run the application
root.mainloop()
