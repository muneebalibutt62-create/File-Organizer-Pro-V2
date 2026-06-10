import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# ================= APP =================
root = tk.Tk()
root.title("File Organizer Pro")
root.geometry("450x300")
root.config(bg="#1e1e1e")

selected_folder = ""

# ================= SELECT FOLDER =================
def select_folder():
    global selected_folder
    selected_folder = filedialog.askdirectory()

    if selected_folder:
        folder_label.config(text=selected_folder)

# ================= ORGANIZE FILES =================
def organize_files():
    if not selected_folder:
        messagebox.showerror("Error", "Select a folder first")
        return

    # file type mapping
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Videos": [".mp4", ".mkv", ".mov"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
        "Audio": [".mp3", ".wav"]
    }

    files = os.listdir(selected_folder)

    moved = 0

    for file in files:
        file_path = os.path.join(selected_folder, file)

        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower()

            moved_flag = False

            for folder_name, extensions in file_types.items():
                if ext in extensions:
                    target_folder = os.path.join(selected_folder, folder_name)

                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)

                    shutil.move(file_path, os.path.join(target_folder, file))
                    moved += 1
                    moved_flag = True
                    break

            if not moved_flag:
                other_folder = os.path.join(selected_folder, "Others")

                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)

                shutil.move(file_path, os.path.join(other_folder, file))
                moved += 1

    messagebox.showinfo("Done", f"Organized {moved} files successfully!")

# ================= UI =================
title = tk.Label(root, text="File Organizer Pro", font=("Arial", 16), fg="white", bg="#1e1e1e")
title.pack(pady=10)

folder_label = tk.Label(root, text="No folder selected", fg="gray", bg="#1e1e1e")
folder_label.pack(pady=5)

tk.Button(root, text="Select Folder", command=select_folder, bg="#3a3a3a", fg="white").pack(pady=5)

tk.Button(root, text="Organize Files", command=organize_files, bg="green", fg="white").pack(pady=10)

root.mainloop()