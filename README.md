Projeto do site da "Transportadora Vietnã"

1º Instale o Python (https://python.org/downloads/)

2° Instale as dependências do programa, entre na raiz do protejo e utilize o comando:
    
    pip install -r requirements.txt

3º Via terminal, para visualizar o programa em execução digite o comando, estando no diretório raiz do projeto:
    
    python manage.py runserver
    
4º Para visualizar a aplicação, acesse no seu navegador: http://127.0.0.1:8000/

Passos Opcionais caso queira utilizar um banco de dados local para o projeto:
   
5º (Opcional) Instale o PosgreSQL se quiser utilizar um banco de dados local (O banco de dados padrão do programa está na nuvem)

    Windows: https://www.postgresql.org/download/windows/
    Linux: Digite os seguintes comandos: 
        sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
        wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
        sudo apt-get update
        sudo apt-get -y install postgresql

6º (Opcional) Crie um usuário caso não queira utilizar o padrão, e crie sua base de dados para 
    o projeto e modifique o arquivo "settings.py" colocando os dados do banco criado. O processo
    para toda esse processo pode ser feito acessando o terminal e digitando os seguintes comandos:
    
    (Windows):psql -U postgres
    (Linux): sudo -u postgres psql
    CREATE DATABASE "nomedobanco" WITH ENCODING 'UTF8';
    CREATE USER "nomedousuario" SUPERUSER INHERIT CREATEDB CREATEROLE;
    ALTER USER "nomedousuario" PASSWORD 'senha';
    GRANT ALL PRIVILEGES ON DATABASE "nomedobanco" TO "nomedousuario";
    
7º (Opcional) Após isto, adicione os dados iniciais para o banco de dados que fora criado utilizando o seguinte comando, 
    estando no diretório raiz do projeto:

    psql "nomedobanco" < transportadora_vietna
    
8º (Opcional) No arquivo "settings.py" modifique o campo "DATABASES" da seguinte forma:

    DATABASES = {
        'default':{
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'nomedobanco',
            'USER': 'nomedousuario',
            'PASSWORD': 'senha',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }
 
9º Salve o arquivo, e siga os passos 3 e 4 para visualizar a aplicação em funcionamento.






