# Fichier complet : StrmMaker_GUI_Pro.py
# Interface graphique améliorée pour créer des fichiers .strm à partir d'un fichier d'URLs

import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

youtube_prefix = "https://www.youtube.com/watch?v="

# === Fonctions ===
def browse_input():
    file_path = filedialog.askopenfilename(title="Sélectionner le fichier d'URLs", filetypes=[("Fichiers texte","*.txt")])
    if file_path:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, file_path)

def browse_output():
    folder_path = filedialog.askdirectory(title="Sélectionner le dossier de sortie")
    if folder_path:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, folder_path)

def generate_strm():
    input_file = input_entry.get().strip()
    output_folder = output_entry.get().strip()
    serie_name = serie_entry.get().strip()
    season_number = season_spin.get()

    if not input_file or not output_folder or not serie_name:
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
        return

    os.makedirs(output_folder, exist_ok=True)

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            raw_urls = [line.strip() for line in f if line.strip()]

        for idx, raw in enumerate(raw_urls, start=1):
            full_url = raw if raw.startswith(youtube_prefix) else youtube_prefix + raw
            filename = f"{serie_name} {season_number}x{idx:02}.strm"
            filepath = os.path.join(output_folder, filename)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(full_url)

        messagebox.showinfo("Succès", f"{len(raw_urls)} fichiers .strm créés dans '{output_folder}'")
    except Exception as e:
        messagebox.showerror("Erreur", str(e))

# === Fenêtre principale ===
root = tk.Tk()
root.title("StrmMaker")
root.geometry("600x250")
root.resizable(False, False)
root.configure(bg="#2c3e50")

# Styles
style = ttk.Style(root)
style.configure("TLabel", background="#2c3e50", foreground="#ecf0f1", font=("Arial", 11))
style.configure("TButton", font=("Arial", 11, "bold"), padding=6)
style.configure("TEntry", font=("Arial", 11))

# === Widgets ===
frame = tk.Frame(root, bg="#2c3e50", padx=20, pady=20)
frame.pack(expand=True, fill="both")

# Fichier d'URLs
tk.Label(frame, text="Fichier d'URLs :").grid(row=0, column=0, sticky="e", pady=5)
input_entry = ttk.Entry(frame, width=45)
input_entry.grid(row=0, column=1, padx=10)
ttk.Button(frame, text="Parcourir", command=browse_input).grid(row=0, column=2)

# Dossier de sortie
tk.Label(frame, text="Dossier de sortie :").grid(row=1, column=0, sticky="e", pady=5)
output_entry = ttk.Entry(frame, width=45)
output_entry.grid(row=1, column=1, padx=10)
ttk.Button(frame, text="Parcourir", command=browse_output).grid(row=1, column=2)

# Nom de la série
tk.Label(frame, text="Nom de la série :").grid(row=2, column=0, sticky="e", pady=5)
serie_entry = ttk.Entry(frame, width=45)
serie_entry.grid(row=2, column=1, columnspan=2, sticky="w")

# Numéro de saison
tk.Label(frame, text="Numéro de saison :").grid(row=3, column=0, sticky="e", pady=5)
season_spin = ttk.Spinbox(frame, from_=1, to=99, width=5, font=("Arial", 11))
season_spin.grid(row=3, column=1, sticky="w")

# Bouton principal
generate_btn = tk.Button(frame, text="Créer les fichiers .strm", command=generate_strm,
                         bg="#27ae60", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5)
generate_btn.grid(row=4, column=0, columnspan=3, pady=20)

root.mainloop()
