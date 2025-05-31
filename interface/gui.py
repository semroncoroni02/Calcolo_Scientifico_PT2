from PIL import Image, ImageTk
import os
import tkinter as tk
from tkinter import filedialog, ttk, messagebox

# Esempio di valori predefiniti per F
VALORI_F = [2, 4, 8, 16, 32, 64, 128, 256]


def avvia_gui():
    def scegli_immagine():
        filepath = filedialog.askopenfilename(
            title="Seleziona un'immagine BMP in toni di grigio",
            filetypes=[("Bitmap Images", "*.bmp")]
        )
        if filepath:
            path_var.set(filepath)
            carica_immagine(filepath)

    def carica_immagine(path):
        try:
            image = Image.open(path)
            image = image.convert("L")  # Scala di grigi
            image = image.resize((256, 256))  # Ridimensionamento per anteprima
            photo = ImageTk.PhotoImage(image)
            immagine_label.config(image=photo)
            immagine_label.image = photo
        except Exception as e:
            messagebox.showerror("Errore", f"Impossibile caricare l'immagine:\n{e}")

    def aggiorna_menu_d(*args):
        try:
            f = int(f_var.get())
            valori_d = list(range(0, 2 * f - 1))
            d_menu['menu'].delete(0, 'end')
            for val in valori_d:
                d_menu['menu'].add_command(label=val, command=tk._setit(d_var, val))
            d_var.set(valori_d[0])  # Seleziona il primo valore di default
        except:
            pass

    def avvia_elaborazione():
        path = path_var.get()
        f = int(f_var.get())
        d = int(d_var.get())
        if not os.path.exists(path):
            messagebox.showerror("Errore", "Devi prima selezionare un'immagine valida.")
            return
        print(f"📂 Immagine selezionata: {path}")
        print(f"🔳 Dimensione blocchi F: {f}")
        print(f"🔪 Soglia frequenze d: {d}")
        # Qui si richiama la funzione principale per l'elaborazione
        # es: processa_immagine(path, f, d)

    # Finestra principale
    root = tk.Tk()
    root.title("Compressione JPEG semplificata con DCT2")
    root.geometry("650x600")

    path_var = tk.StringVar()
    f_var = tk.StringVar()
    d_var = tk.StringVar()

    # Layout
    tk.Label(root, text="1️⃣ Seleziona un'immagine .bmp (grayscale):").pack()
    tk.Button(root, text="Scegli Immagine", command=scegli_immagine).pack()
    immagine_label = tk.Label(root)
    immagine_label.pack(pady=5)

    tk.Label(root, text="2️⃣ Scegli F (dimensione dei blocchi):").pack()
    f_menu = tk.OptionMenu(root, f_var, *VALORI_F)
    f_menu.pack()

    tk.Label(root, text="3️⃣ Scegli d (soglia delle frequenze):").pack()
    d_menu = tk.OptionMenu(root, d_var, "")  # sarà popolato dinamicamente
    d_menu.pack()

    f_var.trace_add("write", aggiorna_menu_d)

    tk.Button(root, text="Avvia Elaborazione", command=avvia_elaborazione).pack(pady=10)

    root.mainloop()


def get_user_inputs():
    selected_file = {"path": None}
    selected_F = {"value": None}
    selected_d = {"value": None}
    preview_img = {"tk_image": None}

    def update_d_options(event=None):
        F = int(F_combobox.get())
        selected_F["value"] = F
        d_values = list(range(0, 2 * F - 1))
        d_combobox["values"] = d_values
        d_combobox.current(0)
        selected_d["value"] = d_values[0]

    def choose_file():
        path = filedialog.askopenfilename(filetypes=[("Bitmap Images", "*.bmp")])
        if path:
            selected_file["path"] = path
            file_label.config(text=f"📁 Immagine: {path.split('/')[-1]}")
            # Carica e mostra anteprima
            img = Image.open(path).convert("L")
            img.thumbnail((200, 200))
            tk_img = ImageTk.PhotoImage(img)
            preview_img["tk_image"] = tk_img
            preview_label.config(image=tk_img)

    def on_submit():
        selected_d["value"] = int(d_combobox.get())
        root.quit()
        root.destroy()

    root = tk.Tk()
    root.title("📷 Seleziona immagine e parametri DCT2")
    root.geometry("550x750")
    root.configure(bg="#f0f0f0")

    tk.Label(root, text="SCEGLI IMMAGINE .bmp (grayscale):", bg="#f0f0f0", font=("Segoe UI", 15)).pack(pady=(15, 5))
    tk.Button(root, text="📂 Sfoglia", command=choose_file, bg="#dbeafe", font=("Segoe UI", 12)).pack()

    file_label = tk.Label(root, text="Nessun file selezionato", bg="#f0f0f0", font=("Segoe UI", 10, "italic"))
    file_label.pack(pady=(5, 10))

    preview_label = tk.Label(root, bg="#f0f0f0")
    preview_label.pack()

    tk.Label(root, text="SELEZIONA AMPIEZZA BLOCCHI (F):", bg="#f0f0f0", font=("Segoe UI", 15)).pack(pady=(10, 5))
    F_combobox = ttk.Combobox(root, values=[4, 8, 16, 32, 64], state="readonly", font=("Segoe UI", 10))
    F_combobox.pack()
    F_combobox.bind("<<ComboboxSelected>>", update_d_options)

    tk.Label(root, text="SELEZIONA SOGLIA FREQUENZE (d):", bg="#f0f0f0", font=("Segoe UI", 15)).pack(pady=(20, 5))
    d_combobox = ttk.Combobox(root, values=[], state="readonly", font=("Segoe UI", 10))
    d_combobox.pack()

    tk.Button(root, text="✅ Conferma", command=on_submit, bg="#bbf7d0", font=("Segoe UI", 12)).pack(pady=(70, 10))

    root.mainloop()

    return selected_file["path"], selected_F["value"], selected_d["value"]
