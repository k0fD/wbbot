import re
import requests

url = str(input("Введите ссылку бренда"))

match = re.search(r'brands/([^/]+)', url)
if match:
    brand_name = match.group(1)
    json_url = f"https://static-basket-01.wb.ru/vol0/data/brands/{brand_name}.json"
    json_response = requests.get(json_url)

    if json_response.status_code == 200:
        json_data = json_response.json()
        id_value = json_data['id']
        name_value = json_data['name']
        print(f"id: {id_value}, Бренда: {name_value}")
    else:
        print("Не удалось загрузить JSON-файл")
else:
    print("Не удалось извлечь имя бренда")
