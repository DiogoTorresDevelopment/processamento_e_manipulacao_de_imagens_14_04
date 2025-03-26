
# Processamento de Imagens de Exames Médicos

Este projeto consiste em um pipeline de processamento de imagens desenvolvido em Python com a biblioteca OpenCV. Ele foi criado para aprimorar imagens digitalizadas de exames médicos, facilitando a análise visual e digital dos exames.

## Objetivo

Aplicar uma série de transformações automáticas na imagem `imagem_exame.jpg` para:

- Melhorar a visualização dos detalhes.
- Ajustar cores, brilho e contraste.
- Executar transformações geométricas.
- Aplicar binarização para destacar informações importantes.

## Estrutura do Pipeline

O pipeline realiza as seguintes operações, **nesta ordem**:

### 1. Leitura e Exibição Inicial
- Leitura da imagem original e exibição em tela.

### 2. Pré-processamento
- Conversão para escala de cinza.
- Equalização de histograma para realce de detalhes.

### 3. Modificação de Cores
- Conversão para HSV.
- Aumento da saturação em 30%.

### 4. Ajuste de Brilho e Contraste
- Brilho aumentado em 50 unidades.
- Contraste ajustado com multiplicador (1.2).

### 5. Redimensionamento e Interpolação
- Redução para 50% (interpolação bicúbica).
- Aumento para 200% (interpolação linear).

### 6. Transformações Geométricas
- Rotação de 45° mantendo o tamanho original.
- Espelhamento horizontal.
- Recorte de 300x300px centralizado.

### 7. Binarização (Otsu)
- Aplicada na imagem em escala de cinza.

### 8. Salvamento
- Todas as imagens intermediárias são salvas na pasta `resultados/`.

## Execução

### Requisitos

- Python 3.x
- OpenCV

Instale o OpenCV com:

```bash
pip install opencv-python
```

### Como rodar

Certifique-se de que o arquivo `imagem_exame.jpg` está no mesmo diretório do script.

Execute:

```bash
python nome_do_arquivo.py
```

As imagens serão salvas automaticamente em `resultados/`.

## Estrutura do Projeto

```
📁 resultados/
    ├── 01_cinza.jpg
    ├── 02_equalizada.jpg
    ├── ...
📄 processamento.py
📄 imagem_exame.jpg
📄 README.md
```

## Autor

Desenvolvido por [Seu Nome] para a atividade de processamento de imagens médicas.

## Licença

Este projeto é livre para fins educacionais.

## Explicação das Funções

### `leitura_e_exibicao(caminho_img)`
- **O que faz**: Lê a imagem original do exame e exibe uma visualização inicial.
- **Impacto**: Nenhuma modificação. Apenas carrega a imagem para uso posterior.

### `pre_processamento(imagem)`
- **O que faz**: Converte a imagem para escala de cinza e aplica equalização de histograma.
- **Impacto**: Melhora o contraste e evidencia detalhes da imagem, especialmente útil em áreas com pouca variação de tons.

### `modificar_cores(imagem)`
- **O que faz**: Converte a imagem para o espaço de cores HSV e aumenta a saturação em 30%.
- **Impacto**: Torna as cores mais vívidas, facilitando a visualização de áreas coloridas importantes (como manchas, marcações ou legendas).

### `ajuste_brilho_contraste(imagem, brilho=50, contraste=1.2)`
- **O que faz**: Aplica uma transformação linear para aumentar o brilho e o contraste.
- **Impacto**: Realça a imagem como um todo, tornando-a mais clara e com contornos mais nítidos.

### `redimensionamento(imagem)`
- **O que faz**: Reduz a imagem pela metade com interpolação bicúbica e depois aumenta para o dobro usando interpolação linear.
- **Impacto**: Permite visualizar como a qualidade é afetada por diferentes métodos de redimensionamento.

### `transformacoes_geometricas(imagem)`
- **O que faz**: Executa três transformações:
  - Rotação de 45° mantendo o tamanho original.
  - Espelhamento horizontal (inversão da imagem).
  - Recorte central de 300x300 pixels.
- **Impacto**:
  - A rotação pode simular ajustes de orientação.
  - O espelhamento é útil para normalização de dados.
  - O recorte central foca em áreas de interesse específicas.

### `binarizacao(imagem_cinza)`
- **O que faz**: Aplica a binarização de Otsu sobre a imagem em escala de cinza.
- **Impacto**: Converte a imagem em preto e branco com base em limiar automático, útil para segmentação de texto ou marcações.

### `salvar_imagem(nome, imagem)`
- **O que faz**: Salva a imagem processada na pasta `resultados/` com o nome especificado.
- **Impacto**: Armazena os resultados intermediários e finais para análise e documentação.
