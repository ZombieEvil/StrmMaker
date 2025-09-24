**# StrmMaker**



**\*\*StrmMaker\*\* est un outil Windows pour créer facilement des fichiers `.strm` à partir d'un fichier d'URLs YouTube.**



**## 📂 Contenu du repo**



**- `bin/StrmMaker.exe` : exécutable prêt à l'emploi.**

**- `src/StrmMaker\_GUI\_Pro.py` : code source Python.**

**- `urls\_sample.txt` : exemple de fichier d'URLs.**

**- `README.md` : instructions.**



**## ⚡ Utilisation**



**1. Télécharger `StrmMaker.exe` depuis \[Releases](lien\_vers\_release).**  

**2. Préparer un fichier `urls.txt` contenant les IDs ou liens YouTube (une URL par ligne).**  

**3. Lancer l'exécutable :**  

   **- Sélectionner le fichier `urls.txt`.**  

   **- Choisir le dossier de sortie.**  

   **- Entrer le nom de la série et le numéro de saison.**  

   **- Cliquer sur \*\*Créer les fichiers .strm\*\*.**  

**4. Tous les fichiers `.strm` seront créés dans le dossier choisi.**



**## 🛠 Pour les développeurs**



**- Python 3.x et Tkinter nécessaires pour lancer le script `.py`.**  

**- Pour créer l'exécutable :**  

**```bash**

**pyinstaller --onefile --windowed src/StrmMaker\_GUI\_Pro.py**



