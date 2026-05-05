import customtkinter as ctk
from ferramentas.ransomware import RansomwareSim
from ferramentas.keylogger import KeyloggerSim
import threading

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Lab de Cibersegurança - Memell87")
        self.geometry("500x400")
        
        self.ransom = RansomwareSim("ambiente_teste")
        self.keylogger = KeyloggerSim("logs_capturados/keylog.txt")

        ctk.CTkLabel(self, text="Simulador de Malware Educacional", font=("Arial", 20)).pack(pady=20)

        self.btn_enc = ctk.CTkButton(self, text="Criptografar e Nota de Resgate", fg_color="red", command=self.ransom.criptografar_pasta).pack(pady=10)
        self.btn_dec = ctk.CTkButton(self, text="Descriptografar", fg_color="green", command=self.ransom.descriptografar_pasta).pack(pady=10)
        
        self.btn_key = ctk.CTkButton(self, text="Iniciar Keylogger", command=self.toggle_key)
        self.btn_key.pack(pady=20)

    def toggle_key(self):
        if not self.keylogger.running:
            threading.Thread(target=self.keylogger.start, daemon=True).start()
            self.btn_key.configure(text="Parar Keylogger", fg_color="orange")
        else:
            self.keylogger.stop()
            self.btn_key.configure(text="Iniciar Keylogger", fg_color=["#3B8ED0", "#1F6AA5"])

if __name__ == "__main__":
    App().mainloop()