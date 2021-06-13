Projeto do site da "Transportadora Vietnã"

Foi desenvolvido como parte da avaliação da disciplina Sistemas Distribuídos da UNIVASF, sendo uma aplicação de gerência de uma 
transportadora que atua também como um e-commerce com o registro de produtos pelos fornecedores, alteração e deleção dos mesmos,
e para os clientes a vizualição dos prdodutos já comprados. Na página de filiadas, com acesso exclusivo do fornecedor, o mesmo 
pode adicionar novas transportadoras, como também alterar ou excluir as já existentes. Por último, há a gerência dos pedidos, onde
os fornecedores e clientes podem visualizar os pedidos de acordo com sua perspectiva, onde os funcionários podem alterar as etapas
do rastreamento do produto, enquanto os clientes podem fazer pedidos e pagar pelo mesmo portal de pedidos. A conta teste para o 
pagamento no paypal pode ser criada acessando https://developer.paypal.com/home e criando uma conta, se já não tiver no paypal, 
para acessar os recurosos e criar uma conta de cliente para fazer os testes de pagamento e a devida vizualização do que ocorre com
os pedidos em sua totalidade. Importante salientar que o programa pode ser modificado sobre a licença GPL 3.0 e qualquer dúvida que
surga, ou sugestões de melhorias, podem ser feitas a qualquer momento via github.

O site pode ser acessado através do seguinte link: http://transportadora-vietna.herokuapp.com/

1º Instale o Python (https://python.org/downloads/)

2° Instale as dependências do programa, entre na raiz do protejo e utilize o comando:
    
    pip install -r requirements.txt

2.1º ( Apenas para Windows) É necessário instalar a libmagic1 (pré instalada para MacOS e Linux) no windows, e isto
     é feito pelo comando abaixo:

     pip install python-magic-bin
   
3º Instale o PosgreSQL se quiser utilizar um banco de dados local (O banco de dados padrão do programa está na nuvem)

    Windows: https://www.postgresql.org/download/windows/
    Linux: Digite os seguintes comandos: 
        sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
        wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
        sudo apt-get update
        sudo apt-get -y install postgresql

4º Crie um usuário caso não queira utilizar o padrão, e crie sua base de dados para 
    o projeto e modifique o arquivo "settings.py" colocando os dados do banco criado. O processo
    para toda esse processo pode ser feito acessando o terminal e digitando os seguintes comandos:
    
    (Windows):psql -U postgres
    (Linux): sudo -u postgres psql
    CREATE DATABASE "nomedobanco" WITH ENCODING 'UTF8';
    CREATE USER "nomedousuario" SUPERUSER INHERIT CREATEDB CREATEROLE;
    ALTER USER "nomedousuario" PASSWORD 'senha';
    GRANT ALL PRIVILEGES ON DATABASE "nomedobanco" TO "nomedousuario";
    
5º Após isto, adicione os dados iniciais para o banco de dados que fora criado utilizando o seguinte comando, 
    estando no diretório raiz do projeto:

    psql "nomedobanco" < transportadora_vietna
    
6º  Renomeie o arquivo .env.example como . env e modifique as linhas, conforme abaixo: 

    # configurações do banco de dados, seguindo o feito no README.md
    DATABASE_NAME =nomedobanco
    DATABASE_USER =nomedousuario
    DATABASE_PASSWORD =senha
    DATABASE_HOST =127.0.0.1
    DATABASE_PORT =5432

6.1º (Opcional) Caso não use a AWS, vá no arquivos "settings.py" e faça o que é citado como comentário nas linha 172:

    # Comente o bloco de cima, da 156 à 170 e descomente as linhas 174 à 178 para usar arquivos locais
     
 
7º Crie um super usuário para acessar o campo Administrador, com o seguinte comando e seguindo as instruções que 
   virão com o mesmo, também detalhado abaixo:

    python manage.py createsuperuser
    
    Username: nomedousuario
    Email address: (opcional)
    Password: digitesuasenha
    Password (again): digitesuasenha
    
    Caso apareça algum warning, dependendo de sua senha, ignore a sugestão (digite y) ou faça a modificação.
    
    Superuser created successfully.
    
8º Renomeie o arquivo .env.example para .env e coloque os seus dados, conforme descrito nesse mesmo arquivo, para configuração dos
   dados sensíveis da aplicação. Olhe o arquivo "settings.py" também, fazendo as devidas modificações, caso não queira fazer
   o programa funcionar utilizando AWS.

9º Via terminal, para visualizar o programa em execução digite o comando, estando no diretório raiz do projeto:
    
    python manage.py runserver

10º Para visualizar a aplicação, acesse no seu navegador: http://127.0.0.1:8000/

11º Para acessar como cliente ou fornecedor, está disponível duas imagens com logins pré-configurados para acesso
   na aplicação em seus respectivos campos (cliente ou fornecedor), e para logar como administrador, use o 
   superusuário que fora criado.
    






