from src.core.scanner import Scanner
from src.core.processor import Processor
from src.database.database import Database


class Controller:

    def __init__(self):
        self.scanner = Scanner()
        self.processor = Processor()
        self.database = Database()

        self.evento = None
        self.imagens = []

    def abrir_evento(self, pasta):
        self.evento = pasta

        self.database.criar_banco(pasta)

        self.imagens = self.scanner.listar_imagens(pasta)

        for imagem in self.imagens:
            self.database.inserir_foto(imagem)

        return self.imagens

    def total_imagens(self):
        return len(self.imagens)

    def total_fotos_banco(self):
        return self.database.total_fotos()

    def processar(self, callback):
        self.processor.processar(
            self.imagens,
            callback
        )