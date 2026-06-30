import customtkinter as ctk


class Dashboard(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure((0, 1, 2), weight=1)

        # Título
        titulo = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Arial", 24, "bold")
        )
        titulo.grid(
            row=0,
            column=0,
            columnspan=3,
            pady=(20, 30)
        )

        # Card Fotos
        self.card_fotos = self.criar_card(
            "Fotos Encontradas",
            "0"
        )
        self.card_fotos.grid(row=1, column=0, padx=15, sticky="ew")

        # Card Processadas
        self.card_processadas = self.criar_card(
            "Processadas",
            "0"
        )
        self.card_processadas.grid(row=1, column=1, padx=15, sticky="ew")

        # Card Pendentes
        self.card_pendentes = self.criar_card(
            "Pendentes",
            "0"
        )
        self.card_pendentes.grid(row=1, column=2, padx=15, sticky="ew")

        # Barra de progresso
        self.progresso = ctk.CTkProgressBar(self)
        self.progresso.set(0)

        self.progresso.grid(
            row=2,
            column=0,
            columnspan=3,
            padx=20,
            pady=40,
            sticky="ew"
        )

        # Status
        self.status = ctk.CTkLabel(
            self,
            text="Aguardando processamento...",
            font=("Arial", 15)
        )

        self.status.grid(
            row=3,
            column=0,
            columnspan=3,
            pady=10
        )

    def criar_card(self, titulo, valor):

        frame = ctk.CTkFrame(self)

        titulo_label = ctk.CTkLabel(
            frame,
            text=titulo,
            font=("Arial", 16)
        )

        titulo_label.pack(pady=(20, 5))

        valor_label = ctk.CTkLabel(
            frame,
            text=valor,
            font=("Arial", 34, "bold")
        )

        valor_label.pack(pady=(5, 20))

        frame.valor = valor_label

        return frame

    def atualizar_estatisticas(self, total, processadas=0):
        pendentes = total - processadas

        self.card_fotos.valor.configure(text=str(total))
        self.card_processadas.valor.configure(text=str(processadas))
        self.card_pendentes.valor.configure(text=str(pendentes))