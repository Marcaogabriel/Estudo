import pytesseract
import cv2

#Passo 1 ler a imagem
imagem = cv2.imread("mvquinze.jpg")

caminho = r"C:\Program Files\Tesseract-OCR"
#Passo 2 pedir pro tesseract extrair o texto da imagem

pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
texto = pytesseract.image_to_string(imagem)
print(texto)