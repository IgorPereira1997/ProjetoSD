Projeto do site da "Transportadora Vietnã"

1º Instale o Python (https://python.org/downloads/)

2º Instale o Django pip install Django==2.2

3º Instale o XAMPP (https://www.apachefriends.org/xampp-files/8.0.5/xampp-windows-x64-8.0.5-0-VS16-installer.exe)

4º Entre no XAMPP como administrador e dê 'Start' nos módulos Apache e MySql

5º Abra um terminal do Windows como administrador e digite:
    mysql

6º No MySql do terminal, digite os segintes comandos para criar o usuário projetoSD:
    CREATE USER 'projetoSD'@'localhost' IDENTIFIED BY 'projetoSD2021';
    GRANT ALL PRIVILEGES ON *.* TO 'projeto'@'localhost' WITH GRANT OPTION;
    
7º Descompacte o arquivo "ProjetoSD.zip" na pasta C:\xampp\htdocs\

8º Agora vai ser preciso importar a base de dados.
   Entre no navegador, digite (http://localhost/phpmyadmin)

9º Crie um novo banco de dados com o nome 'transportadora_vietna' em novo,
   mude a codificação para 'utf8_general_ci' e clique criar 

10º Clique na base de dados que foi criada e vá na guia importar, lá escolha o arquivo
   "transportadora_vietna.sql" da base do projeto e vá em Executar

11º Abra um terminal na raiz do diretório e rode os seguintes comandos:
    python manage.py runserver

12º No navegador, digite (127.0.0.1:8000/inicial/) e navegue pelas guias Entrar como Cliente ou Entrar como Administrador




