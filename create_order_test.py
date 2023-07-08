# Екатерина Михайлова, 6-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request

def get_order_by_track_number():
    # Создание нового заказа
    response = sender_stand_request.post_new_order()

    if response.status_code == 201:
        track_number = response.json()["track"]
        # Получение заказа по трек-номеру
        get_order_response = sender_stand_request.get_order_by_track_number(str(track_number))
        if get_order_response.status_code == 200:
            # Вывод результатов GET-запроса, если заказ был найден
            print(f'Заказ с номером {str(track_number)} был найден')
            print(get_order_response.json())
            print(get_order_response.status_code)
        else:
            # Вывод результатов GET-запроса, если заказ не был найден
            print(f'Заказ с номером {str(track_number)} не был найден')
            print(get_order_response.json())
            print(get_order_response.status_code)

    else:
        # Если при создании заказа получен ответ != 201
        print("Заказ не был создан")
        print(response.status_code)
        print(response.json())


get_order_by_track_number()