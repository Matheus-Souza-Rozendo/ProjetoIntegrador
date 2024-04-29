import numpy as np
import cv2



def redimensionar_quadro(frame):
    # Defina o tamanho máximo da janela
    max_width = 800
    max_height = 600

    # Obter as dimensões do quadro
    height, width = frame.shape[:2]
    
    # Verificar se precisamos redimensionar para o tamanho máximo
    if width > max_width or height > max_height:
        # Calcular a proporção de redimensionamento para manter a proporção da imagem
        scale = min(max_width / width, max_height / height)
        
        # Redimensionar o quadro
        new_width = int(width * scale)
        new_height = int(height * scale)
        frame = cv2.resize(frame, (new_width, new_height))

    return frame


def pre_processamento(image):
    # Redimensionar para uma largura máxima de 800 pixels, mantendo a proporção
    

    resized_image = redimensionar_quadro(image)

    # Converter para escala de cinza
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    # Equalizar o histograma
    equalized_image = cv2.equalizeHist(gray_image)

    # Aplicar um desfoque gaussiano
    blurred_image = cv2.GaussianBlur(equalized_image, (5, 5), 0)

    return blurred_image