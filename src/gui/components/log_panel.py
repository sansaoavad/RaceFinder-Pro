import customtkinter as ctk


class LogPanel(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        titulo = ctk.CTkLabel(
            self,
            text="Log do Sistema",
            font=("Arial", 18, "bold")
        )
        titulo.grid(
            row=0,
            column=0,
            sticky="w",
            padx=15,
            pady=(10, 5)
        )

        self.log = ctk.CTkTextbox(
            self,
            height=180
        )

        self.log.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=15,
            pady=(0, 15)
        )

    def escrever(self, texto):
        self.log.insert("end", texto + "\n")
        self.log.see("end")

    def limpar(self):
        self.log.delete("1.0", "end")