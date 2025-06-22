from PIL import Image, ImageTk
import os
import tkinter as tk
from tkinter import filedialog, ttk, messagebox


def get_user_inputs():
    selected_file = {"path": None}
    selected_F = {"value": None}
    selected_d = {"value": None}
    preview_img = {"tk_image": None}
    F_values = []

    def choose_file():
        path = filedialog.askopenfilename(filetypes=[("Bitmap Images", "*.bmp")])
        if path:
            selected_file["path"] = path
            file_label.config(text=f"📁 Immagine: {os.path.basename(path)}")
            img = Image.open(path).convert("L")
            preview_img["image_array"] = img
            img.thumbnail((200, 200))
            tk_img = ImageTk.PhotoImage(img)
            preview_img["tk_image"] = tk_img
            preview_label.config(image=tk_img)
            preview_label.image = tk_img

            # Genera i valori di F validi dinamicamente
            width, height = img.size
            max_f = min(width, height)
            F_values.clear()
            F_values.extend(range(1, max_f + 1))
            F_combobox["values"] = F_values
            F_combobox.set(F_values[0])
            update_d_options()

    def update_d_options(event=None):
        try:
            F = int(F_combobox.get())
            selected_F["value"] = F
            d_values = list(range(0, 2 * F - 1))
            d_combobox["values"] = d_values
            d_combobox.set(d_values[0])
            selected_d["value"] = d_values[0]
        except:
            pass

    def on_submit():
        try:
            selected_d["value"] = int(d_combobox.get())
            root.quit()
            root.destroy()
        except:
            messagebox.showerror("Errore", "Valori F e d non validi")

    root = tk.Tk()
    root.title("📷 Compressione DCT2")
    root.geometry("600x720")
    w = 600
    h = 720
    root.configure(bg="#f9fafb")

    # Posizione apertura finestra interattiva
    # get screen width and height
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 3) - (h / 3)

    # set the dimensions of the screen
    # and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    # Titolo
    tk.Label(
        root,
        text="Compressione DCT2",
        bg="#f9fafb",
        font=("Segoe UI", 20, "bold"), fg="#1e3a8a").pack(pady=(15, 5))

    # Selezione immagine
    tk.Label(
        root, text="Selezionare immagine .bmp (grayscale):",
        bg="#f9fafb", font=("Segoe UI", 17), fg="#111827").pack(pady=(10, 0))

    tk.Button(
        root, text="📂 Sfoglia", command=choose_file,
        bg="#e0f2fe", font=("Segoe UI", 15), width=15).pack(pady=(5, 10))  # <-- Dimensione bottone

    file_label = tk.Label(
        root, text="Nessun file selezionato", bg="#f9fafb",
        font=("Segoe UI", 12, "italic"), fg="#6b7280")
    file_label.pack()

    preview_label = tk.Label(root, bg="#f9fafb")
    preview_label.pack(pady=10)

    # Selezione F
    tk.Label(
        root, text="Ampiezza blocchi F:",
        bg="#f9fafb", font=("Segoe UI", 15), fg="#111827").pack(pady=(5, 5))

    F_combobox = ttk.Combobox(
        root, state="readonly", width=10, font=("Segoe UI", 15))  # <-- Larghezza menu F
    F_combobox.pack()
    F_combobox.bind("<<ComboboxSelected>>", update_d_options)

    # Selezione d
    tk.Label(
        root, text="Soglia frequenze d:",
        bg="#f9fafb", font=("Segoe UI", 15), fg="#111827").pack(pady=(20, 5))

    d_combobox = ttk.Combobox(
        root, state="readonly", width=10, font=("Segoe UI", 15))  # <-- Larghezza menu d
    d_combobox.pack()

    # Pulsante conferma
    tk.Button(
        root, text="✅ AVVIA COMPRESSIONE", command=on_submit,
        bg="#d1fae5", font=("Segoe UI", 15), width=25).pack(pady=(40, 10))  # <-- Dimensione bottone conferma

    root.mainloop()

    return selected_file["path"], selected_F["value"], selected_d["value"]
