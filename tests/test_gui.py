from interface.gui import get_user_inputs

if __name__ == "__main__":
    path, F, d = get_user_inputs()
    if path:
        print("\n✅ Parametri selezionati correttamente!")
        print(f"📂 File: {path}")
        print(f"📐 Dimensione blocco F: {F}")
        print(f"🔪 Soglia diagonale d: {d}")
    else:
        print("\n⚠️ Test GUI fallito o annullato.")
