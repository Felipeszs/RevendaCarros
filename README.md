# Projeto Revenda de Carros

Sistema de gerenciamento de conteúdo (CMS) para um site de revenda de veículos. Este projeto foi desenvolvido com foco no aprendizado do framework Django, implementando operações CRUD (Create, Read, Update, Delete) e gerenciamento de mídia.

## Tabela de Conteúdos
* [Funcionalidades](#funcionalidades)
* [Tecnologias Utilizadas](#tecnologias-utilizadas)
* [Como Rodar o Projeto](#como-rodar-o-projeto)
* [Uso](#uso)
* [Autor](#autor)

---

## Funcionalidades
*  **Autenticação:** Acesso ao painel de gerenciamento protegido por senha.
*  **Painel de Admin:** Interface administrativa completa (Django Admin) para gerenciar o catálogo.
*  **Adicionar Veículos:** Cadastro de novos carros, incluindo nome, modelo, ano, preço e upload de fotos.
*  **Editar Veículos:** Atualização de todas as informações de veículos já cadastrados.
*  **Remover Veículos:** Exclusão de veículos do catálogo.
*  **Gerenciamento de Mídia:** Upload e processamento de imagens de veículos (utilizando a biblioteca Pillow).

---

## Tecnologias Utilizadas
* **Backend:** Python 3
* **Framework:** Django
* **Banco de Dados:** SQLite3 (padrão de desenvolvimento do Django)
* **Bibliotecas Python:** Pillow (para processamento de imagens)
* **Frontend:** HTML / CSS (utilizados no Django Templates)

---

## Como Rodar o Projeto

Siga os passos abaixo para configurar e executar o projeto em sua máquina local.


Crie e Ative o Ambiente Virtual (venv)
# Criar a venv
python -m venv venv

# Ativar no Windows
.\venv\Scripts\activate

# Ativar no macOS/Linux
source venv/bin/activate

# Instale as Dependências
pip install -r requirements.txt

# Aplique as Migrações do Banco de Dados
python manage.py migrate


# Crie um Superusuário Você precisará de um administrador para acessar o painel de gerenciamento.
# se preferir pode utilizar sem o Superusuário para ter a experiencia que um usuário comum teria 
python manage.py createsuperuser

# Agora rode o servidor
python manage.py runserver

Acesse o Projeto! O site estará disponível em http://127.0.0.1:8000/cars.

Autor
Desenvolvido por Felipe Medeiros de Souza.

Estudante de Análise e Desenvolvimento de Sistemas na FATEC.

LinkedIn: www.linkedin.com/in/felipe-medeiros-31486b254