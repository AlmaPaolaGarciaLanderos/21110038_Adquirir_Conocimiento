#Alma Paola Garcia Landeros
#21110038
#6E1
#Inteligencia Artificial
#Centro de Enseñanza Tecnica Industrial   
from flask import Flask, request, render_template

app = Flask(__name__)

# Respuestas precargadas
responses = {
    "Hola": "¡Hola! ¿Cómo estás?",
    "¿Cómo estás?": "Estoy bien, gracias. ¿De qué te gustaría hablar?",
    "¿De qué te gustaría hablar?": "Puedo hablar de muchas cosas. ¿Te gustaría aprender algo nuevo?"
}

# Base de datos para almacenar nuevos conocimientos
knowledge_base = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = responses.get(user_input)

    if response is None:
        response = "No tengo información sobre eso. ¿Te gustaría enseñarme algo nuevo? (Responde 'sí' o 'no')"
        # Pregunta para agregar conocimiento nuevo
        knowledge_base.append(user_input)  # Aquí se almacena el nuevo conocimiento

    return response

if __name__ == '__main__':
    app.run(debug=True)
