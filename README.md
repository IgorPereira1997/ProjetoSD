Projeto do site da "Transportadora Vietnã"

1º Instale o Python (https://python.org/downloads/)

2° Instale as dependências do programa, entre na raiz do protejo e utilize o comando:
    
    pip install -r requirements.txt
    
3º Crie um super usuário para acessar o campo Administrador, com o seguinte comando e seguindo as instruções que 
   virão com o mesmo, também detalhado abaixo:

    python manage.py createsuperuser
    
    Username: nomedousuario
    Email address: (opcional)
    Password: digitesuasenha
    Password (again): digitesuasenha
    
    Caso apareça algum warning, dependendo de sua senha, ignore a sugestão (digite y) ou faça a modificação.
    
    Superuser created successfully.
    

4º Via terminal, para visualizar o programa em execução digite o comando, estando no diretório raiz do projeto:
    
    python manage.py runserver
    
5º Para visualizar a aplicação, acesse no seu navegador: http://127.0.0.1:8000/

Passos Opcionais caso queira utilizar um banco de dados local para o projeto:
   
6º (Opcional) Instale o PosgreSQL se quiser utilizar um banco de dados local (O banco de dados padrão do programa está na nuvem)

    Windows: https://www.postgresql.org/download/windows/
    Linux: Digite os seguintes comandos: 
        sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
        wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
        sudo apt-get update
        sudo apt-get -y install postgresql

7º (Opcional) Crie um usuário caso não queira utilizar o padrão, e crie sua base de dados para 
    o projeto e modifique o arquivo "settings.py" colocando os dados do banco criado. O processo
    para toda esse processo pode ser feito acessando o terminal e digitando os seguintes comandos:
    
    (Windows):psql -U postgres
    (Linux): sudo -u postgres psql
    CREATE DATABASE "nomedobanco" WITH ENCODING 'UTF8';
    CREATE USER "nomedousuario" SUPERUSER INHERIT CREATEDB CREATEROLE;
    ALTER USER "nomedousuario" PASSWORD 'senha';
    GRANT ALL PRIVILEGES ON DATABASE "nomedobanco" TO "nomedousuario";
    
8º (Opcional) Após isto, adicione os dados iniciais para o banco de dados que fora criado utilizando o seguinte comando, 
    estando no diretório raiz do projeto:

    psql "nomedobanco" < transportadora_vietna
    
9º (Opcional) No arquivo "settings.py" modifique o campo "DATABASES" da seguinte forma:

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
 
10º (Opcional) Salve o arquivo, e siga os passos 3 à 5 para visualizar a aplicação em funcionamento.






