# 🐦 Sabiá – Assistente de Estudos com IA

O **SABIÁ** é um assistente de estudos inteligente que ajuda você a organizar sua rotina de estudos, planejar matérias, receber recomendações personalizadas com IA e manter o foco no seu aprendizado.


--- **Esse projeto terá mais atualizações futuramente**

## 📸 Demonstração

![image](https://github.com/user-attachments/assets/99b89444-9f72-45c6-a31c-cac488ad0980)
![image](https://github.com/user-attachments/assets/a0c415dd-c09a-456e-800a-744da6c6b9ca)
![image](https://github.com/user-attachments/assets/c6c91869-3609-4ba4-8966-9d302111105e)
![image](https://github.com/user-attachments/assets/2064875f-12b0-4893-99f5-5a95ecfc91bf)

> Interface amigável, dark mode e IA para ajudar nos estudos.

---

## 🚀 Funcionalidades

- 📚 **Adicionar Matérias**: Cadastre matérias com nome e tempo de estudo.
- 📅 **Cronograma Visual**: Veja todas as matérias organizadas em cards, com nome e tempo.
- 🗑 **Remover Matérias**: Remova matérias do cronograma com um clique e confirmação.
- 🧠 **Dicas da IA**: Receba recomendações personalizadas, desafios semanais e perguntas reflexivas usando a API do Google Gemini.
- ✨ **Interface Responsiva**: Design moderno e leve com Bootstrap 5.
- 💾 **Armazenamento Local**: Dados armazenados localmente em `database.json`.

---

## 🛠️ Tecnologias Usadas

- **Python** + **Flask**
- **Bootstrap 5**
- **HTML5/CSS3**
- **API Gemini (Google AI)**
- **Jinja2** (Template Engine)

---

## 📂 Como Rodar Localmente

```bash
# Clone o repositório
git clone https://github.com/DaviGrilo/SABIA.git
cd SABIA

# Crie e ative o ambiente virtual
python -m venv venv
# No Windows: venv\Scripts\activate
source venv/bin/activate
# Mac/Linux:
source venv/bin/activate
       
# Instale as dependências
pip install -r requirements.txt

# Crie um arquivo .env com sua chave da API
echo "GOOGLE_API_KEY=sua_chave_aqui" > .env

# Execute a aplicação
python app.py
````
---

## 👤 **Autor**
- Desenvolvido por DAVI SANTANA.
