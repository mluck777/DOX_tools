import tkinter as tk
from tkinter import ttk, messagebox
import ttkbootstrap as ttkb

# Main window
root = ttkb.Window(themename="darkly")
root.title("DEATH 1 - DOX Tools")
root.geometry("950x550")
root.configure(bg="#2C2F33")  # Dark gray background

# Button style
style = ttk.Style()
style.configure("TButton", font=("Arial", 12, "bold"), padding=10, relief="flat")

# Main title
title = ttk.Label(root, text="🔥 DEATH 1 - DOX Tools 🔥", font=("Arial", 26, "bold"), foreground="#32CD32", background="#2C2F33")
title.pack(pady=10)

# Main frame
frame = ttk.Frame(root)
frame.pack(pady=10, padx=20, fill="both", expand=True)

# Left frame (normal options)
left_frame = ttk.Frame(frame)
left_frame.pack(side="left", padx=20, pady=10, fill="both", expand=True)

# Right frame (advanced mode)
advanced_frame = ttk.Frame(frame)

# Variables for input fields
first_name_var = tk.StringVar()
last_name_var = tk.StringVar()
dob_var = tk.StringVar()
ip_var = tk.StringVar()
location_var = tk.StringVar()
email_var = tk.StringVar()
phone_var = tk.StringVar()
image_count_var = tk.IntVar(value=0)  # Number of images (moved here)
image_link_vars = []

# Standard fields
fields = [
    ("First Name:", first_name_var),
    ("Last Name:", last_name_var),
    ("Date of Birth:", dob_var),
    ("IP Address:", ip_var),
    ("Location:", location_var),
    ("Email:", email_var),
    ("Phone Number:", phone_var),
]

for label, var in fields:
    ttk.Label(left_frame, text=label, background="#2C2F33", foreground="white").pack(anchor="w")
    ttk.Entry(left_frame, textvariable=var, width=30).pack()

# Number of images field (in normal section)
ttk.Label(left_frame, text="Number of Images:", background="#2C2F33", foreground="white").pack(anchor="w")
ttk.Entry(left_frame, textvariable=image_count_var, width=5).pack()

# Checkbox for advanced mode
advanced_var = tk.BooleanVar()
advanced_check = ttk.Checkbutton(left_frame, text="Enable Advanced Mode", variable=advanced_var, command=lambda: toggle_mode())
advanced_check.pack(pady=5)

# Function to toggle advanced mode
def toggle_mode():
    if advanced_var.get():
        advanced_frame.pack(side="right", padx=20, pady=10, fill="both", expand=True)
    else:
        advanced_frame.pack_forget()

# Account variables
discord_user_var = tk.StringVar()
discord_pass_var = tk.StringVar()
instagram_user_var = tk.StringVar()
instagram_pass_var = tk.StringVar()
facebook_user_var = tk.StringVar()
facebook_pass_var = tk.StringVar()
github_user_var = tk.StringVar()
github_pass_var = tk.StringVar()

# Advanced mode fields
advanced_fields = [
    ("Discord Username:", discord_user_var, "Password:", discord_pass_var),
    ("Instagram Username:", instagram_user_var, "Password:", instagram_pass_var),
    ("Facebook Username:", facebook_user_var, "Password:", facebook_pass_var),
    ("GitHub Username:", github_user_var, "Password:", github_pass_var),
]

for user_label, user_var, pass_label, pass_var in advanced_fields:
    row_frame = ttk.Frame(advanced_frame)
    row_frame.pack(fill="x", pady=2)

    ttk.Label(row_frame, text=user_label, background="#2C2F33", foreground="white").pack(side="left", padx=5)
    ttk.Entry(row_frame, textvariable=user_var, width=20).pack(side="left", padx=5)
    
    ttk.Label(row_frame, text=pass_label, background="#2C2F33", foreground="white").pack(side="left", padx=5)
    ttk.Entry(row_frame, textvariable=pass_var, width=20).pack(side="left", padx=5)

# Image links frame (in advanced mode)
image_frame = ttk.Frame(advanced_frame)
image_frame.pack(fill="x", pady=10)

# Function to add image fields
def ask_images():
    global image_link_vars
    image_frame.pack(fill="x", pady=10)

    # Remove old fields
    for widget in image_frame.winfo_children():
        widget.destroy()

    # Create new fields
    image_link_vars = []
    for i in range(image_count_var.get()):
        var = tk.StringVar()
        image_link_vars.append(var)

        ttk.Label(image_frame, text=f"Image Link {i+1}:", background="#2C2F33", foreground="white").pack(anchor="w")
        ttk.Entry(image_frame, textvariable=var, width=40).pack()

    toggle_mode()  # Ensure advanced mode stays visible

# Button to add images
ttk.Button(advanced_frame, text="Add Images", command=ask_images).pack(pady=5)

# Function to save data
def save_data():
    filename = f"{first_name_var.get()}_{last_name_var.get()}.txt"

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"🔥 DEATH 1 🔥\n")
            f.write("=" * 40 + "\n")
            f.write(f"First Name: {first_name_var.get()}\n")
            f.write(f"Last Name: {last_name_var.get()}\n")
            f.write(f"Date of Birth: {dob_var.get()}\n")
            f.write(f"IP Address: {ip_var.get()}\n")
            f.write(f"Location: {location_var.get()}\n")
            f.write(f"Email: {email_var.get()}\n")
            f.write(f"Phone Number: {phone_var.get()}\n")
            f.write(f"Number of Images: {image_count_var.get()}\n")

            if advanced_var.get():
                f.write("\n[Advanced Mode]\n")
                f.write(f"Discord: {discord_user_var.get()} - {discord_pass_var.get()}\n")
                f.write(f"Instagram: {instagram_user_var.get()} - {instagram_pass_var.get()}\n")
                f.write(f"Facebook: {facebook_user_var.get()} - {facebook_pass_var.get()}\n")
                f.write(f"GitHub: {github_user_var.get()} - {github_pass_var.get()}\n")

            if image_link_vars:
                f.write("\n[Image Links]\n")
                for link_var in image_link_vars:
                    if link_var.get().strip():
                        f.write(f"- {link_var.get()}\n")

        messagebox.showinfo("Success", f"File saved as {filename}")

    except Exception as e:
        messagebox.showerror("Error", f"Could not save file: {e}")

# Save button
ttk.Button(root, text="SAVE", command=save_data, style="TButton").pack(pady=20)

# Signature at the bottom
signature = ttk.Label(root, text="Created by m.luck777", font=("Arial", 10, "italic"), foreground="red", background="#2C2F33")
signature.pack(side="bottom", pady=5)

# Run the application
root.mainloop()
