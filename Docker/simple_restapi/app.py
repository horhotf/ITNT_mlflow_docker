from flask import Flask, request

# Для обработки запросов к приложения вначале необходимо создать 
# объект приложения с помощью конструктора Flask из пакета Flask
app = Flask(__name__)

# К нашей функции применяется специальный декоратор в виде метода app.get(). 
# В него передается шаблон маршрута, по которому функция будет обрабатывать запросы
@app.route('/', methods=['GET'])
# После декоратора app.get идет собственно определение функции, которая обрабатывает запрос. 
# Это обычная функция python. Она называется service_info (имя произвольное). 
def service_info(): 
    # Вернет словарь 
    return {"service": "My REST API service"}

# Добавим еще один entrypoint нашего сервиса с некоторой информацией о нас
@app.route('/about', methods=['GET'])
def about():
    # Вернет информацию обо мне
    return {"My name": "Igor Rytsarev", "Company": "GlowByte, AA"}

# Добавим entrypoint для метода умножения чисел
@app.route('/calc_multiplication', methods=['GET', 'POST'])
def multiplication():
    if request.method == 'GET':
        # Вернет информацию обо методе (что нужно использовать POST, передавать параметры при помощи JSON )
        return {"info": "Гse the POST method to multiply two numbers", "Exapmple_POST": "{'a' = 5, 'b' = 3}"}
    if request.method == 'POST':
        request_data = request.get_json()
        a = request_data['a']
        b = request_data['b']
        # Вернет результат умножения чисел
        return {"result": a*b}
    
if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")




    