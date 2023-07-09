# Екатерина Михайлова, 6-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request

def test_get_order_by_track_number():
    # Создание нового заказа
    response = sender_stand_request.post_new_order()
    track_number = response.json()["track"]
    get_order_response = sender_stand_request.get_order_by_track_number(str(track_number))
    # Проверка кода ответа при поиске заказа по трек-номеру
    assert get_order_response.status_code == 200, "Заказ не был найден"