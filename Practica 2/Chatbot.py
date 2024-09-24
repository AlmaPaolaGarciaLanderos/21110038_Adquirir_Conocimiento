#Alma Paola Garcia Landeros
#21110038
#7E1
#Inteligencia Artificial
#Centro de Enseñanza Tecnica Industrial 

class Chatbot:
    def __init__(self):
        # Base de datos de preguntas y respuestas
        self.database = {
            "hola": "¡Hola! ¿Cómo estás?",
            "como estas?": "Estoy bien, gracias. ¿De qué te gustaría hablar?",
            "puedes contarme un dato curioso?": "¡Por supuesto! ¿Sabías que los pulpos tienen tres corazones? Dos bombean sangre a las branquias y uno al resto del cuerpo. Interesante, ¿verdad?"
        }

    def get_response(self, user_input):
        # Buscamos una respuesta en la base de datos
        response = self.database.get(user_input.lower())
        
        if response:
            return response
        else:
            # Si no hay match, pedimos nuevo conocimiento
            return self.ask_for_new_knowledge(user_input)

    def ask_for_new_knowledge(self, user_input):
        new_response = input(f"No tengo una respuesta para: '{user_input}'. ¿Cuál debería ser la respuesta? ")
        self.database[user_input.lower()] = new_response
        return f"Gracias, he aprendido algo nuevo: '{user_input}' significa '{new_response}'."

def main():
    print("¡Bienvenido al chatbot de Alma!")
    chatbot = Chatbot()
    
    while True:
        user_input = input("Tú: ")
        if user_input.lower() in ["salir", "exit"]:
            print("¡Hasta luego!")
            break
        response = chatbot.get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
