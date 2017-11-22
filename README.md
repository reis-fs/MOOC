# Preparando o Ambiente de Desenvolvimento (Linux)

### Atualização do sistema
<code>sudo apt-get update && sudo apt-get upgrade</code>

### Pacotes para python 2x e 3x
<code>sudo apt-get install -y python-pip python3-pip build-essential git python python3  python-dev python3-dev libsdl2-dev  libsdl2-image-dev  libsdl2-mixer-dev  libsdl2-ttf-dev libportmidi-dev  libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev ffmpeg</code>

### Caso ocorra erro na instalação do ffmpeg
<code>sudo apt-get install libav-tools</code>

### Instalação/atualização do pip, virtualenv e setuptools
<code>sudo pip install --upgrade pip virtualenv setuptools</code>

### Instalação do virtualenvwrapper
<code>sudo pip install virtualenvwrapper</code>

#### adicionar no final do arquivo “~/.bashrc”
<code>#local onde os ambientes serão armazenados</code><br>
<code>export WORKON_HOME=~/.virtualenvs</code><br>
<code>#script de ativação do virtualenvwrapper</code><br>
<code>source /usr/local/bin/virtualenvwrapper.sh</code> (este caminho pode ser diferente dependendo de sua distribuição)<br>
<code>#define que não será utilizado os pacotes instalados no python default</code><br>
<code>export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages'</code><br>
<code>#define que não é possível utilizar o pip fora de algum ambiente virtual</code><br>
<code>export PIP_REQUIRE_VIRTUALENV=true</code><br>
  
Após este procedimento, crie um ambiente virtual com: mkvirtualenv (nome do ambiente) -p (versão do python)<br>
Obs.: Se uma versão não for definida, ele utiliza a versão padrão do Sistema.<br>
<code>mkvirtualenv mooc -p python3</code><br>
ou<br>
<code>mkvirtualenv mooc -p /usr/bin/python3</code> (pode ser alterado caso utilize outra versão do Python)<br>

Finalmente, para ativar o ambiente virtual, utilize: workon (nome do ambiente)<br>
<code>workon mooc</code><br>
Para desativar, utilize: <code>deactivate</code><br>

Com o ambiente ativado, instale o Django e o Pillow (para trabalhar com imagens):<br>
<code>pip install django Pillow</code><br>

#### Baixe o projeto e através do terminal navegue até a pasta "simplemooc" onde contém o arquivo manage.py e execute os comandos:<br>
<code>python manage.py makemigrations</code><br>
<code>python manage.py migrate</code><br>
<code>python manage.py runserver</code><br>

-------------------------------------------------------------------------------------------------------------

# SIMPLE MOOC - Simple Massive Open Online Course

O Simple MOOC é uma plataforma para ensino à distância, focada em cursos abertos e massivos.
<br>Será desenvolvida em Python 3.6 e Django 1.11.

Funcionalidades:
* Sistema de Aulas
* Fórum de Dúvidas
* Exercícios de submissão
* Sistema de avisos
* Sistema de contas (usuários) 

Sistema de Aulas
- Criação, edição e remoção de aulas e módulos
- As aulas serão compostas por:
- Vídeo-aulas (Youtube)
- Materiais para download (Códigos, pdf’s, slides…)
- Quizzes
- As aulas estarão associadas a um curso

Fórum de Dúvidas
- Um fórum aberto
- Tópicos separados por Categoria
- Usuários precisam estar logados

Exercícios de Submissão
- Exercícios que os alunos poderão enviar sua solução via arquivo
- Poderá conter algum tipo de validação automática
- As submissões irão gerar notas para os alunos

Sistema de Avisos
- Um mural de avisos
- Os avisos serão enviados para os alunos por e-mail
- Terão uma página onde poderão receber comentários

Sistema de Contas
- Os usuários poderão se cadastrar e logar no sistema
- Os usuários poderão alterar o seu perfil
- Os usuários terão um perfil público

Conteúdo aprendido na Udemy.<br>
Curso: Python 3 na Web com Django (Básico e Intermediário)
