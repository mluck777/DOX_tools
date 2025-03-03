import tkinter as tk
from tkinter import ttk, messagebox
import ttkbootstrap as ttkb

# Création de la fenêtre principale
root = ttkb.Window(themename="darkly")
root.title("DEATH 1 - DOX Tools")
root.geometry("950x550")
root.configure(bg="#2C2F33")  # Fond gris foncé

# Style des boutons
style = ttk.Style()
style.configure("TButton", font=("Arial", 12, "bold"), padding=10, relief="flat")

# Titre principal
title = ttk.Label(root, text="🔥 DEATH 1 - DOX Tools 🔥", font=("Arial", 26, "bold"), foreground="#32CD32", background="#2C2F33")
title.pack(pady=10)

# Cadre principal
frame = ttk.Frame(root)
frame.pack(pady=10, padx=20, fill="both", expand=True)

# Cadre gauche (options normales)
left_frame = ttk.Frame(frame)
left_frame.pack(side="left", padx=20, pady=10, fill="both", expand=True)

# Cadre droit (mode avancé)
advanced_frame = ttk.Frame(frame)

# Variables pour les champs
nom_var = tk.StringVar()
prenom_var = tk.StringVar()
date_var = tk.StringVar()
ip_var = tk.StringVar()
loc_var = tk.StringVar()
email_var = tk.StringVar()
phone_var = tk.StringVar()
image_count_var = tk.IntVar(value=0)  # Nombre d'images déplacé ici
image_link_vars = []

# Champs standard
champs = [
    ("Nom :", nom_var),
    ("Prénom :", prenom_var),
    ("Date de naissance :", date_var),
    ("Adresse IP :", ip_var),
    ("Localisation :", loc_var),
    ("Email :", email_var),
    ("Téléphone :", phone_var),
]

for label, var in champs:
    ttk.Label(left_frame, text=label, background="#2C2F33", foreground="white").pack(anchor="w")
    ttk.Entry(left_frame, textvariable=var, width=30).pack()

# Champ "Nombre d'images" (dans la section normale)
ttk.Label(left_frame, text="Nombre d'images :", background="#2C2F33", foreground="white").pack(anchor="w")
ttk.Entry(left_frame, textvariable=image_count_var, width=5).pack()

# Checkbox pour activer le mode avancé
advanced_var = tk.BooleanVar()
advanced_check = ttk.Checkbutton(left_frame, text="Activer Mode Avancé", variable=advanced_var, command=lambda: toggle_mode())
advanced_check.pack(pady=5)

# Fonction pour afficher/masquer le mode avancé
def toggle_mode():
    if advanced_var.get():
        advanced_frame.pack(side="right", padx=20, pady=10, fill="both", expand=True)
    else:
        advanced_frame.pack_forget()

# Variables pour les comptes
pseudo_discord_var = tk.StringVar()
password_discord_var = tk.StringVar()
pseudo_instagram_var = tk.StringVar()
password_instagram_var = tk.StringVar()
pseudo_facebook_var = tk.StringVar()
password_facebook_var = tk.StringVar()
pseudo_github_var = tk.StringVar()
password_github_var = tk.StringVar()

# Champs du mode avancé
champs_avances = [
    ("Pseudo Discord :", pseudo_discord_var, "Mot de passe :", password_discord_var),
    ("Pseudo Instagram :", pseudo_instagram_var, "Mot de passe :", password_instagram_var),
    ("Pseudo Facebook :", pseudo_facebook_var, "Mot de passe :", password_facebook_var),
    ("Pseudo GitHub :", pseudo_github_var, "Mot de passe :", password_github_var),
]

for label_pseudo, var_pseudo, label_mdp, var_mdp in champs_avances:
    row_frame = ttk.Frame(advanced_frame)
    row_frame.pack(fill="x", pady=2)

    ttk.Label(row_frame, text=label_pseudo, background="#2C2F33", foreground="white").pack(side="left", padx=5)
    ttk.Entry(row_frame, textvariable=var_pseudo, width=20).pack(side="left", padx=5)
    
    ttk.Label(row_frame, text=label_mdp, background="#2C2F33", foreground="white").pack(side="left", padx=5)
    ttk.Entry(row_frame, textvariable=var_mdp, width=20).pack(side="left", padx=5)

# Cadre pour les images (en mode avancé)
image_frame = ttk.Frame(advanced_frame)
image_frame.pack(fill="x", pady=10)

# Fonction pour ajouter les champs des images
def ask_images():
    global image_link_vars
    image_frame.pack(fill="x", pady=10)

    # Supprimer les anciens champs
    for widget in image_frame.winfo_children():
        widget.destroy()

    # Créer de nouveaux champs
    image_link_vars = []
    for i in range(image_count_var.get()):
        var = tk.StringVar()
        image_link_vars.append(var)

        ttk.Label(image_frame, text=f"Lien Image {i+1} :", background="#2C2F33", foreground="white").pack(anchor="w")
        ttk.Entry(image_frame, textvariable=var, width=40).pack()

    toggle_mode()  # Assure que le mode avancé reste visible

# Bouton pour ajouter les images
ttk.Button(advanced_frame, text="Ajouter des Images", command=ask_images).pack(pady=5)

# Fonction pour enregistrer les données
def enregistrer():
    nom_fichier = f"{nom_var.get()}_{prenom_var.get()}.txt"

    try:
        with open(nom_fichier, "w", encoding="utf-8") as f:
            f.write(f"🔥 DEATH 1 🔥\n")
            f.write("=" * 40 + "\n")
            f.write(f"Nom : {nom_var.get()}\n")
            f.write(f"Prénom : {prenom_var.get()}\n")
            f.write(f"Date de naissance : {date_var.get()}\n")
            f.write(f"IP : {ip_var.get()}\n")
            f.write(f"Localisation : {loc_var.get()}\n")
            f.write(f"Email : {email_var.get()}\n")
            f.write(f"Téléphone : {phone_var.get()}\n")
            f.write(f"Nombre d'images : {image_count_var.get()}\n")

            if advanced_var.get():
                f.write("\n[Mode Avancé]\n")
                f.write(f"Discord : {pseudo_discord_var.get()} - {password_discord_var.get()}\n")
                f.write(f"Instagram : {pseudo_instagram_var.get()} - {password_instagram_var.get()}\n")
                f.write(f"Facebook : {pseudo_facebook_var.get()} - {password_facebook_var.get()}\n")
                f.write(f"GitHub : {pseudo_github_var.get()} - {password_github_var.get()}\n")

            if image_link_vars:
                f.write("\n[Liens d'images]\n")
                for link_var in image_link_vars:
                    if link_var.get().strip():
                        f.write(f"- {link_var.get()}\n")

        messagebox.showinfo("Succès", f"Fichier enregistré sous {nom_fichier}")

    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible d'enregistrer : {e}")

# Bouton d'enregistrement
ttk.Button(root, text="ENREGISTRER", command=enregistrer, style="TButton").pack(pady=20)

# Signature en bas
signature = ttk.Label(root, text="Created by m.luck777", font=("Arial", 10, "italic"), foreground="red", background="#2C2F33")
signature.pack(side="bottom", pady=5)

# Lancement de l'application
root.mainloop()
