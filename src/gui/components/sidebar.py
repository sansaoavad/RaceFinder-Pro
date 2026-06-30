import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, width=220, corner_radius=0)

        self.grid(row=0, column=0, rowspan=2, sticky="ns")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(10, weight=1)

        titulo = ctk.CTkLabel(
            self,
            text="🏍 RaceFinder PRO",
            font=("Arial", 22, "bold")
        )

        titulo.grid(row=0, column=0, pady=(20, 30), padx=15)

        self.bt_evento = ctk.CTkButton(
            self,
            text="📂 Evento"
        )

        self.bt_evento.grid(
            row=1,
            column=0,
            padx=15,
            pady=8,
            sticky="ew"
        )

        self.bt_processar = ctk.CTkButton(
            self,
            text="▶ Processar"
        )

        self.bt_processar.grid(
            row=2,
            column=0,
            padx=15,
            pady=8,
            sticky="ew"
        )

        self.bt_buscar = ctk.CTkButton(
            self,
            text="🔍 Buscar"
        )

        self.bt_buscar.grid(
            row=3,
            column=0,
            padx=15,
            pady=8,
            sticky="ew"
        )

        self.bt_exportar = ctk.CTkButton(
            self,
            text="📤 Exportar"
        )

        self.bt_exportar.grid(
            row=4,
            column=0,
            padx=15,
            pady=8,
            sticky="ew"
        )

        self.bt_config = ctk.CTkButton(
            self,
            text="⚙ Configurações"
        )

        self.bt_config.grid(
            row=5,
            column=0,
            padx=15,
            pady=8,
            sticky="ew"
        )