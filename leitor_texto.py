import cv2
import pytesseract
import numpy as np
import pyttsx3  # Biblioteca para conversão de texto em fala

# Configurar o caminho do Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Inicializa o motor de voz
engine = pyttsx3.init()

def reconhecer_texto(imagem):
    """Melhora a qualidade da imagem e realiza OCR."""
    
    # Converter para escala de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Aplicar filtro para reduzir ruído antes da binarização
    imagem_suave = cv2.GaussianBlur(imagem_cinza, (5, 5), 0)

    # Aplicar binarização Otsu para segmentar melhor o texto
    _, imagem_binaria = cv2.threshold(imagem_suave, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # ** Inverter cores para deixar texto preto em fundo branco **
    imagem_invertida = cv2.bitwise_not(imagem_binaria)

    # ** Remover pequenos ruídos e buracos nas letras **
    kernel = np.ones((3, 3), np.uint8)
    imagem_sem_ruido = cv2.morphologyEx(imagem_invertida, cv2.MORPH_CLOSE, kernel, iterations=2)

    # Aplicar dilatação para engrossar letras e melhorar OCR
    imagem_melhorada = cv2.dilate(imagem_sem_ruido, kernel, iterations=1)

    # Salvar a imagem processada para depuração
    cv2.imwrite("imagem_processada_final.png", imagem_melhorada)

    # Exibir a imagem processada para verificação
    cv2.imshow("Imagem Processada", imagem_melhorada)
    cv2.waitKey(500)  # Mostra a imagem por meio segundo antes de continuar

    # Executa OCR com melhor configuração para reconhecer palavras
    texto = pytesseract.image_to_string(imagem_melhorada, lang="por", config="--psm 6")

    return texto.strip()

def falar_texto(texto):
    """Transforma o texto em fala."""
    if texto:
        print("Texto reconhecido:", texto)
        engine.say(texto)  # Converte o texto em fala
        engine.runAndWait()  # Executa a fala
    else:
        print("Nenhum texto detectado.")

# Captura de imagem pela webcam
cap = cv2.VideoCapture(0)

# Aumentar a resolução da webcam
cap.set(3, 1280)  # Largura
cap.set(4, 720)   # Altura

while True:
    ret, frame = cap.read()
    cv2.imshow("Pressione 's' para capturar", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("captura.png", frame)  # Salvar a imagem capturada
        texto_detectado = reconhecer_texto(frame)  # Aplicar OCR
        falar_texto(texto_detectado)  # Lê o texto em voz alta
        break

cap.release()
cv2.destroyAllWindows()