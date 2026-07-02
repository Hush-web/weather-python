import requests
from datetime import datetime
import csv
timestamp= datetime.now().strftime('%d-%m-%Y %H:%M')


def weather_app():

 response= requests.get('https://wttr.in/Ado-ekiti?format=j1')
 weather= response.json()

 filename= 'weather_report.csv'

 feels= weather['current_condition'] [0] ["FeelsLikeC"]
 tempc= weather['current_condition'] [0] ["temp_C"]
 desc= weather ['current_condition'] [0] ["weatherDesc"] [0] ['value']


 if int(tempc) < 10:
  message= f'Today is a cold day, {tempc}℃ temperature, feels like{feels}, {desc}condition'

 else:
  message=f'Nice day, {tempc}℃ temperature, feels like {feels}, {desc} condition'

 print(f'{datetime.now():%H,%M}{message}')

 with open(filename,'a', newline='', encoding='utf-8')as f:
  writer= csv.writer(f)
  writer.writerow([timestamp, message])

  

  return message

result= weather_app()