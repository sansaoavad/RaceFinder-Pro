from pathlib import Path


class Scanner:

    EXTENSOES = (".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff", ".webp")

    def listar_imagens(self, pasta):

        pasta = Path(pasta)

        imagens = []

        for arquivo in pasta.rglob("*"):

            if arquivo.is_file():

                if arquivo.suffix.lower() in self.EXTENSOES:

                    imagens.append(arquivo)

        imagens.sort()

        return imagens
