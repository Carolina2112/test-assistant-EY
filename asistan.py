import openai
import requests
import datetime
import time
import threading

def calculator():
    try:
        expression = input("Ingrese una operación matemática (ej: 2+2): ")
        result = eval(expression)
        print(f"Resultado: {result}")
    except Exception as e:
        print("Error en la operación matemática.")

def manipulate_text():
    text = input("Ingrese un texto: ")
    print("1. Convertir a mayúsculas")
    print("2. Convertir a minúsculas")
    print("3. Contar palabras")
    option = input("Seleccione una opción: ")
    
    if option == "1":
        print(text.upper())
    elif option == "2":
        print(text.lower())
    elif option == "3":
        print(f"Número de palabras: {len(text.split())}")
    else:
        print("Opción inválida.")

def ask_ai():
    response = requests.get("https://api.openai.com/v1/models")
    print(response.status_code, response.text)
    #La api key tiene un limite de uso(version gratuitala configuracion para hacer consultas a una IA
    openai.api_key = "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"
    try:
        question = input("¿Qué quieres preguntar?: ")
        answer = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}]
        )
        print("Respuesta de la IA:", answer['choices'][0]['message']['content'])
    except Exception as e:
        print("Error al conectar con la API.")

def set_alarm():
    try:
        alarm_time = input("Ingrese la hora de la alarma (HH:MM): ")
        hour, minute = map(int, alarm_time.split(':'))
        now = datetime.datetime.now()
        alarm = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
        
        if alarm < now:
            alarm = alarm.replace(day=now.day + 1)
        
        print(f"Alarma configurada para las {alarm_time}")
        
        def alarm_thread():
            while True:
                now = datetime.datetime.now()
                if now >= alarm:
                    print("¡Alarma!")
                    break
                time.sleep(60)
        threading.Thread(target=alarm_thread, daemon=True).start()
            
    except ValueError:
        print("Formato de hora inválido.")


def menu():
    while True:
        print("\nAsistente de IA")
        print("1. Realizar cálculos matemáticos")
        print("2. Manipular texto")
        print("3. Preguntar a la IA")
        print("4. Configurar alarma")
        print("5. Salir")
        option = input("Seleccione una opción: ")
        
        if option == "1":
            calculator()
        elif option == "2":
            manipulate_text()
        elif option == "3":
            ask_ai()
        elif option == "4":
            set_alarm()
        elif option == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    menu()