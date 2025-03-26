import cv2
import numpy as np
import os

# Função para salvar uma imagem na pasta 'resultados'
def salvar_imagem(nome, imagem):
    caminho = os.path.join('resultados', nome)  # Cria o caminho do arquivo
    cv2.imwrite(caminho, imagem)  # Salva a imagem

# Função para ler e exibir a imagem original
def leitura_e_exibicao(caminho_img):
    imagem = cv2.imread(caminho_img)  # Lê a imagem
    cv2.imshow('Imagem Original', imagem)  # Mostra a imagem em uma janela
    cv2.waitKey(0)  # Aguarda tecla para fechar
    cv2.destroyAllWindows()  # Fecha a janela
    return imagem  # Retorna a imagem lida

# Função de pré-processamento: conversão para cinza e equalização
def pre_processamento(imagem):
    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)  # Converte para escala de cinza
    equalizada = cv2.equalizeHist(cinza)  # Aplica equalização de histograma
    salvar_imagem('01_cinza.jpg', cinza)  # Salva imagem em cinza
    salvar_imagem('02_equalizada.jpg', equalizada)  # Salva imagem equalizada
    return equalizada  # Retorna imagem equalizada

# Função para modificar cores aumentando a saturação
def modificar_cores(imagem):
    hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)  # Converte para HSV
    h, s, v = cv2.split(hsv)  # Separa canais
    s = np.clip(s * 1.3, 0, 255).astype(np.uint8)  # Aumenta saturação e limita entre 0-255
    hsv_modificada = cv2.merge([h, s, v])  # Junta os canais novamente
    imagem_modificada = cv2.cvtColor(hsv_modificada, cv2.COLOR_HSV2BGR)  # Converte de volta para BGR
    salvar_imagem('03_hsv_saturacao.jpg', imagem_modificada)  # Salva imagem
    return imagem_modificada  # Retorna imagem modificada

# Função para ajustar brilho e contraste
def ajuste_brilho_contraste(imagem, brilho=50, contraste=1.2):
    ajustada = cv2.convertScaleAbs(imagem, alpha=contraste, beta=brilho)  # Aplica brilho e contraste
    salvar_imagem('04_brilho_contraste.jpg', ajustada)  # Salva imagem
    return ajustada  # Retorna imagem ajustada

# Função de redimensionamento com diferentes interpolações
def redimensionamento(imagem):
    metade = cv2.resize(imagem, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)  # Reduz 50% com bicúbica
    dobro = cv2.resize(imagem, (0, 0), fx=2.0, fy=2.0, interpolation=cv2.INTER_LINEAR)  # Aumenta 200% com linear
    salvar_imagem('05_redimensionada_50.jpg', metade)  # Salva imagem reduzida
    salvar_imagem('06_redimensionada_200.jpg', dobro)  # Salva imagem aumentada
    return metade, dobro  # Retorna ambas

# Função para transformações geométricas
def transformacoes_geometricas(imagem):
    h, w = imagem.shape[:2]  # Obtém altura e largura
    M_rot = cv2.getRotationMatrix2D((w // 2, h // 2), 45, 1.0)  # Matriz de rotação de 45 graus
    rotacionada = cv2.warpAffine(imagem, M_rot, (w, h))  # Aplica rotação
    espelhada = cv2.flip(imagem, 1)  # Espelha horizontalmente
    y1 = h // 2 - 150
    x1 = w // 2 - 150
    recorte = imagem[y1:y1 + 300, x1:x1 + 300]  # Recorte central 300x300px
    salvar_imagem('07_rotacionada.jpg', rotacionada)  # Salva imagem rotacionada
    salvar_imagem('08_espelhada.jpg', espelhada)  # Salva imagem espelhada
    salvar_imagem('09_recorte_central.jpg', recorte)  # Salva recorte
    return rotacionada, espelhada, recorte  # Retorna todas

# Função para binarização usando Otsu
def binarizacao(imagem_cinza):
    _, binarizada = cv2.threshold(imagem_cinza, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # Binarização Otsu
    salvar_imagem('10_binarizada.jpg', binarizada)  # Salva imagem binarizada
    return binarizada  # Retorna imagem binária

# Pipeline principal que chama todas as etapas acima
def pipeline(caminho_img):
    if not os.path.exists('resultados'):
        os.makedirs('resultados')  # Cria pasta 'resultados' se não existir

    original = leitura_e_exibicao(caminho_img)  # Etapa 1
    equalizada = pre_processamento(original)  # Etapa 2
    imagem_hsv = modificar_cores(original)  # Etapa 3
    ajustada = ajuste_brilho_contraste(imagem_hsv)  # Etapa 4
    redimensionamento(ajustada)  # Etapa 5
    transformacoes_geometricas(ajustada)  # Etapa 6
    binarizacao(equalizada)  # Etapa 7

# Ponto de entrada do script
if __name__ == "__main__":
    pipeline("imagem_exame.jpg")