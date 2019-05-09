# pyWidroweb
Algoritimo para baixar dados das estações do site  [Hidroweb] (http://www.snirh.gov.br/hidroweb/publico/apresentacao.jsf). 
Usando como base os projetos do
1. [JeanFavaretto] (https://gist.github.com/JeanFavaretto/58110021276b27d65e89)
2. [duartejr] (https://github.com/duartejr/pyHidroWeb)

# Bibliotecas necessarias:
- pyvirtualdisplay
- selenium
- geckodriver
- tkinter



# Como usar:
Primeiro se cria um arquivo de entrada, sendo cada linha do arquivo o id de uma estação.
exemplo do arquivo:
02751025
02849035
02750004
02650032
02850015

Com o pyHidroweb e o interface.py na mesma pasta, rode o interface.py e selecione o arquivo que criou,
contendo os ids das estações.

