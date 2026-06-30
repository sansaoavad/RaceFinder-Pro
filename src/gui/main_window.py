from tkinter import filedialog
import customtkinter as ctk

from src.controller.controller import Controller
from src.gui.components.sidebar import Sidebar
from src.gui.components.dashboard import Dashboard
from src.gui.components.log_panel import LogPanel


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("RaceFinder PRO")
        self.geometry("1400x800")

        self.controller = Controller()
        self.pasta_evento = None
        self.imagens = []

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(1, weight=2)

        self.sidebar = Sidebar(self)

        self.dashboard = Dashboard(self)
        self.dashboard.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=20,
            pady=20
        )

        self.log_panel = LogPanel(self)
        self.log_panel.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=20,
            pady=(0, 20)
        )

        self.inicializar()

    def inicializar(self):
        self.log_panel.escrever("RaceFinder PRO iniciado.")
        self.log_panel.escrever("Sistema pronto.")

        self.sidebar.bt_evento.configure(
            command=self.selecionar_evento
        )

        self.sidebar.bt_processar.configure(
            command=self.iniciar_processamento,
            state="disabled"
        )

    def selecionar_evento(self):
        pasta = filedialog.askdirectory(
            title="Selecione a pasta do evento"
        )

        if not pasta:
            return

        self.pasta_evento = pasta
        self.log_panel.escrever(f"Pasta: {pasta}")

        try:
            self.log_panel.escrever("Chamando Controller...")

            imagens = self.controller.abrir_evento(pasta)
            self.imagens = imagens

            self.log_panel.escrever("Controller retornou.")

            total = len(imagens)
            self.log_panel.escrever(f"Total: {total}")

            self.dashboard.atualizar_estatisticas(
                total=total,
                processadas=0
            )

            self.dashboard.progresso.set(0)
            self.dashboard.status.configure(
                text="Aguardando processamento..."
            )

            self.log_panel.escrever("Dashboard atualizado.")

            total_banco = self.controller.total_fotos_banco()

            self.log_panel.escrever(
                f"Fotos cadastradas no banco: {total_banco}"
            )

            if total > 0:
                self.sidebar.bt_processar.configure(state="normal")

        except Exception as e:
            self.log_panel.escrever(f"ERRO: {e}")

    def iniciar_processamento(self):
        if not self.imagens:
            self.log_panel.escrever("Nenhuma imagem para processar.")
            return

        self.sidebar.bt_processar.configure(state="disabled")

        self.log_panel.escrever("Iniciando processamento...")

        self.controller.processar(
            self.atualizar_progresso
        )

    def atualizar_progresso(
        self,
        progresso,
        indice,
        total,
        nome_imagem
    ):
        self.dashboard.progresso.set(progresso)

        self.dashboard.status.configure(
            text=f"Processando {indice}/{total}"
        )

        self.dashboard.atualizar_estatisticas(
            total=total,
            processadas=indice
        )

        self.log_panel.escrever(
            f"{indice}/{total} - {nome_imagem}"
        )

        if indice == total:
            self.dashboard.status.configure(
                text="Processamento concluído."
            )

            self.sidebar.bt_processar.configure(
                state="normal"
            )

            self.log_panel.escrever(
                "✔ Processamento finalizado."
            )