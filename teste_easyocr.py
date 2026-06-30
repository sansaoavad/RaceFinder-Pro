import easyocr

reader = easyocr.Reader(["en"], gpu=False)

resultado = reader.readtext("teste.jpg")

for r in resultado:
    print(r)
