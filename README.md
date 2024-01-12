## Инструкция по установке, развертыванию и запуску проекта.


1. Отркойте терминал. Введите следующее для клонирования репозитория:
	- git clone https://github.com/tilekbai/test_work_oracle_digital.git

2. Войдите в папку со скачанным только что проектом, выполнив команду:
	- cd test_work_oracle_digital

3. Создайте виртуальное окружение:
	- python -m venv venv
	
4. Активируйте виртуальное окружение:
	- source venv/bin/activate
	
5. В корне проекта на одном уровне с weather_api, weather, Dockerfile создайте 2 файла:
	- config.py
	- .env

6. В файле - config.py, пропишите api ключ, предварительно полученный на сайте - "openweathermap.org". Пример написания ключа:
	- api_key = "<ваш апи ключ>"
	
7. В файле - .env. Пропишите название, пользователя, пароль, относящиеся к вашей базе данных PostgreSQL. Пример написания:
	- POSTGRES_HOST=db
	- POSTGRES_PORT=5432
	- POSTGRES_NAME=postgresdb
	- POSTGRES_USER=postgresuser
	- POSTGRES_PASSWORD=password

8. Собрать и запустить докер контейнер:
	- sudo docker-compose up --build

9. Postman. GET запрос на адрес - http://localhost:8000/api/weather?city=bishkek (вместо "bishkek" можно ставить любой город)
