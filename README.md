## Preparando o Ambiente de Desenvolvimento (Linux)

# Atualização do sistema
sudo apt-get update && sudo apt-get upgrade

# Pacotes para python 2x e 3x
sudo apt-get install -y python-pip python3-pip build-essential git python python3  python-dev python3-dev libsdl2-dev  libsdl2-image-dev  libsdl2-mixer-dev  libsdl2-ttf-dev libportmidi-dev  libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev ffmpeg

# Caso ocorra erro na instalação do ffmpeg
sudo apt-get install libav-tools

# Instalação/atualização do pip, virtualenv e setuptools
sudo pip install --upgrade pip virtualenv setuptools

# Instalação do virtualenvwrapper
sudo pip install virtualenvwrapper

<b>adicionar no final do arquivo “~/.bashrc”</b>
<b>local onde os ambientes serão armazenados</b>
export WORKON_HOME=~/.virtualenvs
<b>script de ativação do virtualenvwrapper</b>
source /usr/local/bin/virtualenvwrapper.sh (este caminho pode ser diferente dependendo de sua distribuição)
<b>define que não será utilizado os pacotes instalados no python default</b>
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages'
<b>define que não é possível utilizar o pip fora de algum ambiente virtual</b>
export PIP_REQUIRE_VIRTUALENV=true
  
Após este procedimento, crie um ambiente virtual com: mkvirtualenv (nome do ambiente) -p (versão do python)
Obs.: Se uma versão não for definida, ele utiliza a versão padrão do Sistema.
<b>mkvirtualenv mooc -p python3</b>
ou
<b>mkvirtualenv mooc -p /usr/bin/python3</b> (pode ser alterado caso utilize outra versão do Python)

Finalmente, para ativar o ambiente virtual, utilize: workon (nome do ambiente)
<b>workon mooc</b>
Para desativar, utilize: deactivate

Com o ambiente ativado, instale o Django e o Pillow (para trabalhar com imagens):
<b>pip install django Pillow</b>

-------------------------------------------------------------------------------------------------------------

# <b>SIMPLE MOOC - Simple Massive Open Online Course</b>

O Simple MOOC é uma plataforma para ensino à distância, focada em cursos abertos e massivos.
<br>Será desenvolvida em Python 3.6 e Django 1.11.

<b>Funcionalidades:</b>
* Sistema de Aulas
* Fórum de Dúvidas
* Exercícios de submissão
* Sistema de avisos
* Sistema de contas (usuários) 

<b>Sistema de Aulas</b>
- Criação, edição e remoção de aulas e módulos
- As aulas serão compostas por:
- Vídeo-aulas (Youtube)
- Materiais para download (Códigos, pdf’s, slides…)
- Quizzes
- As aulas estarão associadas a um curso

<b>Fórum de Dúvidas</b>
- Um fórum aberto
- Tópicos separados por Categoria
- Usuários precisam estar logados

<b>Exercícios de Submissão</b>
- Exercícios que os alunos poderão enviar sua solução via arquivo
- Poderá conter algum tipo de validação automática
- As submissões irão gerar notas para os alunos

<b>Sistema de Avisos</b>
- Um mural de avisos
- Os avisos serão enviados para os alunos por e-mail
- Terão uma página onde poderão receber comentários

<b>Sistema de Contas</b>
- Os usuários poderão se cadastrar e logar no sistema
- Os usuários poderão alterar o seu perfil
- Os usuários terão um perfil público

Conteúdo aprendido na Udemy.<br>
Curso: Python 3 na Web com Django (Básico e Intermediário)
