import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")

def gerar_conteudo(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Erro: {e}")
        return "Desculpe, não consegui gerar esse conteúdo no momento."

def get_recommendations():
    return gerar_conteudo("Me dê 5 dicas rápidas de estudo para estudantes do ensino médio e superior.")

def get_motivation():
    return gerar_conteudo("Me dê uma frase motivacional curta e impactante para estudantes.")

def get_weekly_challenge():
    return gerar_conteudo("Crie um desafio leve e motivador de estudos para esta semana.")

def get_reflection_question():
    return gerar_conteudo("Crie uma pergunta reflexiva sobre hábitos de estudo para estudantes.")

def get_study_routine():
    return gerar_conteudo("Sugira uma rotina de estudos de 2 horas com pausas, ideal para estudantes.")
