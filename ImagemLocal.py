import cv2         # Biblioteca para vídeo e imagens
import numpy as np # Biblioteca para cálculos matemáticos (vetores e ângulos)
import pytesseract # Biblioteca para leitura do texto de uma imagem
import pyttsx3     # Biblioteca para conversão de texto em fala

# Passar o caminho do Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Inicializa o motor de voz
engine = pyttsx3.init()

# Reconhece o texto da imagem demonstrada (Webcam ou foto)
def reconhecer_texto(imagem):
    
    # Converter para escala de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Aumentar contraste para melhorar a detecção
    imagem_contraste = cv2.convertScaleAbs(imagem_cinza, alpha=1.5, beta=0)

    # Aplicar filtro para reduzir ruído antes da binarização
    imagem_suave = cv2.GaussianBlur(imagem_contraste, (5, 5), 0)

    # Aplicar binarização Otsu para segmentar melhor o texto
    _, imagem_binaria = cv2.threshold(imagem_suave, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Remover ruídos
    kernel = np.ones((2, 2), np.uint8)
    imagem_sem_ruido = cv2.morphologyEx(imagem_binaria, cv2.MORPH_CLOSE, kernel, iterations=1)
    
    # Aplicar erosão para reduzir caracteres falsos
    imagem_final = cv2.erode(imagem_sem_ruido, kernel, iterations=1)

    # Exibir a imagem processada para verificação
    cv2.imshow("Imagem Processada", imagem_final)
    cv2.waitKey(1000)  # Mostra a imagem por um segundo antes de continuar


    # Executa OCR com melhor configuração para reconhecer palavras
    config_tesseract = "--oem 3 --psm 6"
    texto = pytesseract.image_to_string(imagem_final, lang="por", config=config_tesseract)

    return texto.strip()

# Transformar texto em fala
def falar_texto(texto):
    if texto:
        print("Texto reconhecido:", texto)
        engine.say(texto)  # Converte o texto em fala
        engine.runAndWait()  # Executa a fala
    else:
        print("Nenhum texto detectado.")


# Pegar a imagem
imagem = cv2.imread("informacoes.png")

if imagem is not None:
    texto_detectado = reconhecer_texto(imagem)
    falar_texto(texto_detectado)


# Finaliza a aplicação
cv2.destroyAllWindows()


