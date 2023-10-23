import re
import requests

url = "https://www.wildberries.ru/brands/moccoty/all"

match = re.search(r'brands/([^/]+)/all', url)
if not match:
    print("Не удалось извлечь имя бренда")
else:
    brand_name = match.group(1)

    # Формируем URL для загрузки JSON-файла
    json_url = f"https://static-basket-01.wb.ru/vol0/data/brands/{brand_name}.json"

    # Отправляем GET-запрос к JSON-файлу
    json_response = requests.get(json_url)

    if json_response.status_code != 200:
        print("Не удалось загрузить JSON-файл")
    else:
        # Загружаем JSON-файл и парсим его
        json_data = json_response.json()

        # Извлекаем id и name из JSON-запроса
        id_value = json_data.get('id')
        name_value = json_data.get('name')

        if id_value is not None and name_value is not None:
            # Вывод id и name
            print(f"id: {id_value}, name: {name_value}")

            # Извлекаем {id} из полученного JSON
            id_match = id_value
            if id_match:
                id_value = id_match
                # Формируем URL для загрузки второго JSON-файла
                second_json_url = (f"https://catalog.wb.ru/brands/m/catalog?TestGroup=control&appType=1"
                                   f"&brand={id_value}&dest=12358487")

                # Отправляем GET-запрос ко второму JSON-файлу
                second_json_response = requests.get(second_json_url)

                if second_json_response.status_code == 200:
                    # Загружаем второй JSON-файл и парсим его
                    second_json_data = second_json_response.json()

                    # Извлекаем все значения 'id' и 'name' из второго JSON
                    products = second_json_data.get("data", {}).get("products", [])
                    for product in products:
                        product_id = product.get("id")
                        product_name = product.get("name")
                        print(f"id: {product_id}, name: {product_name}")
                else:
                    print("Не удалось загрузить второй JSON-файл")
            else:
                print("Не удалось извлечь {id} из второго JSON")
        else:
            print("Не удалось извлечь id и name из первого JSON")
