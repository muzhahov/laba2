import requests
import datetime

city = "Moscow,RU"
appid = "f6611cb4d5074df89089c09156551d03"

res = requests.get("http://api.openweathermap.org/data/2.5/weather",
	params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()


print("Город:", city)
print("Дата:", datetime.date.today())
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура:", data['main']['temp_max'])
print("Скорость ветра:", data['wind']['speed']) #ТУТ ВЫВОД СКОРОСТИ СЕГОДНЯ
print("Видимость:", round((data['visibility'] / 10000) * 100), "%", ">") #ТУТ ВЫВОД ВИДИМОСТИ СЕГОДНЯ
print('==================================================')
print('==================================================')
print('==================================================')


res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
	params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
	print("Дата <", i['dt_txt'], "> \r\nТемпература <",
'{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <",
i['weather'][0]['description'], ">", "\r\nСкорость ветра <", i['wind']['speed'], "м/c >",
"\r\nВидимость <", round((i['visibility'] / 10000) * 100), "%", ">")
	print("____________________________")

#ДОМАШНИМ ЗАДАНИЕМ БЫЛО СДЕЛАТЬ ВЫВОД СКОРОСТИ ВЕТРА И ВИДИМОСТИ
#Я НЕ СТАЛ ПИСАТЬ НОВЫЙ КОД, А ПРОСТО ВНЕДРИЛ ЕГО ВНУТРЬ ЭТОГО
#ВНЕДРЕННЫЙ КОД ПОМЕЧЕН
