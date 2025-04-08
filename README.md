## Checkpoint 02 - Visão Computacional
### Solução
- Reconhecimento e leitura de textos para deficientes visuais.

### Contexto - Deficiência visual
- De acordo com a Organização Mundial da Saúde (OMS), cerca de 39 milhões de pessoas no mundo são cegas. No Brasil, de acordo com o IBGE, mais de 6,5 milhões de brasileiros têm alguma deficiência visual. Deste total, 506 mil são   cegos e 6 milhões têm baixa visão.
- Sendo assim, visando as dificuldades que as pessoas com deficiência visual enfrentam todos os dias, pensamos em uma solução   para tornar o dia a dia delas mais prático, realizando uma solução que leia informações de textos em voz alta apartir de      imagens.

### Pesquisa
- Para realizar essa solução utilizamos a biblioteca Tesseract para a extração do texto das imagens.
  O Tesseract OCR foi criado pela HP (Hewlett-Packard) entre 1985 e 1995, como um projeto de pesquisa interno e em 2005, o código foi liberado como open-source. Desde 2006,    passou a ser mantido e desenvolvido principalmente pelo Google, que o transformou em um dos melhores mecanismos de OCR gratuitos do mundo.
  Tesseract é uma ferramenta de OCR (Reconhecimento Óptico de Caracteres), usada para extrair texto de imagens ou PDFs escaneados. Ele transforma imagens em texto digital.

- Para a leitura em voz alta utilizamos a biblioteca Pyttsx3. 
  É uma biblioteca Python para síntese de fala (text-to-speech, TTS). O pyttsx3 permite que um programa Python converta texto em voz, de forma offline, sem depender de 
  conexão com a internet ou serviços externos.


  #### *Repositórios e links utilizados:* ####
  https://github.com/tesseract-ocr/tesseract
  
  https://gist.github.com/idcesares/7a0071080b73abb706436ec75c248073
  
  https://pypi.org/project/pyttsx3/
  
## Instalação:
- Baixe o tesseract (tesseract-ocr-w64-setup-5.5.0.20241111);
- Certifique-se de que foi instalado no caminho "C:\Program Files\Tesseract-OCR";
- Adicione o arquivo "por.traineddata" a pasta "C:\Program Files\Tesseract-OCR\tessdata".

### Instalação das bibliotecas:
- Abrir o Anaconda Navigator
- Executar o CMD.exe Prompt
- Copiar e colar os comandos do arquivo txt: "Imports CP2.txt".
  
### Executar o código:
- Abra o VS Code dentro do Anaconda
- Abra os arquivos .py (LeitorTextoWebcam.py e LeitorTextoImagem.py) 
- E por fim, execute o código.  

## Integrantes:
- Arthur Miranda Santos - 93023
- Ellen Tinin de Brito - 93462
- Renan Bandeira Leite - 96168
- Thomas D'àvila Meyer Pflug - 92915
- Vitor Tanabe - 93226
