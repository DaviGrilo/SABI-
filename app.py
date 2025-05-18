from flask import Flask, render_template, request, redirect
import json, os
import markdown
from dotenv import load_dotenv
import google.generativeai as genai
from gemini_api import (
    get_recommendations, get_motivation,
    get_weekly_challenge, get_reflection_question,
    get_study_routine, gerar_conteudo
)

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

app = Flask(__name__)
DB_FILE = "database.json"

def load_data():
    if not os.path.exists(DB_FILE):
        return {"subjects": []}
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add', methods=['GET', 'POST'])
def add_subject():
    if request.method == 'POST':
        name = request.form['name']
        time = request.form['time']
        data = load_data()
        data["subjects"].append({"name": name, "time": time})
        save_data(data)
        return redirect('/schedule')
    return render_template("add_subject.html")

@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    data = load_data()
    subjects = data["subjects"]

    edit_index = request.args.get('edit', default=None, type=int)

    if request.method == 'POST':
        index = int(request.form['index'])
        subjects[index]['name'] = request.form['name']
        subjects[index]['time'] = request.form['time']
        save_data(data)
        return redirect('/schedule')

    return render_template("schedule.html", subjects=subjects, edit_index=edit_index)

@app.route('/remover', methods=['POST'])
def remover():
    index = int(request.form['index'])
    data = load_data()
    if 0 <= index < len(data["subjects"]):
        removido = data["subjects"].pop(index)
        save_data(data)
        print(f"Matéria removida: {removido['name']}")
    return redirect('/schedule')

@app.route('/recomendacoes', methods=['GET', 'POST'])
def recomendacoes():
    user_answer = None
    if request.method == 'POST':
        prompt = request.form.get('user_prompt')
        user_answer = gerar_conteudo(prompt)

    challenge_md = get_weekly_challenge()
    challenge_html = markdown.markdown(challenge_md)

    return render_template("recomendacoes.html",
                           tips=get_recommendations(),
                           motivation=get_motivation(),
                           challenge=challenge_html,
                           reflection=get_reflection_question(),
                           routine=get_study_routine(),
                           user_answer=user_answer)

if __name__ == "__main__":
    app.run(debug=True)
