from locust import FastHttpUser, task, between
import random
from datetime import datetime

class WebsiteTestUser(FastHttpUser):
    @task(1)
    def weatherapi_get_cities(self):
        #http://91.185.85.213
        wait_time = between(0.5, 3)
        headers = {
            "accept": "text/plain",
            "Host": "ismakhar.weather-api.example"
        }
        #1 Получаем список городов
        url = "/Cities"
        self.client.request(method="GET", url=url, headers=headers)


    @task(5)
    def weatherapi_post_forecast(self):
        #2 Добавляем данные о погоде
        headers = {
            "Connection": "keep-alive",
            "Host": "ismakhar.weather-api.example"
        }
        city_id = random.randrange(1, 1000, 1)
        weather_time = str((datetime.now() - datetime(1970, 1, 1)).total_seconds())[:10]
        temperature = random.randrange(-40, 40, 1)
        summary_list = ['warm', 'cold', 'comf', 'hot']
        summary = random.choice(summary_list)
        url = "/Forecast/"+str(city_id)
        body = {
            "cityId": str(city_id),
            "dateTime": weather_time,
            "temperature": str(temperature),
            "summary": summary
        }
        self.client.request(method="POST", url=url, headers=headers, json=body)