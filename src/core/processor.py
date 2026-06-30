import time


class Processor:

    def processar(self, imagens, callback):

        total = len(imagens)

        for indice, imagem in enumerate(imagens, start=1):

            # simula o processamento
            time.sleep(0.1)

            progresso = indice / total

            callback(
                progresso,
                indice,
                total,
                imagem.name
            )