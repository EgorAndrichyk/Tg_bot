import telebot
import os
from telebot import types
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
# my_chat_id =
bot = telebot.TeleBot(TOKEN)


# Главное меню
@bot.message_handler(commands=["start"])
def get_text_messages(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Дэл-150")
    btn2 = types.KeyboardButton("Куб-2")
    btn3 = types.KeyboardButton("Котельные")
    btn4 = types.KeyboardButton("Переносной газик")
    btn5 = types.KeyboardButton("Схемы")
    markup.row(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, "Напиши, что тебе нужно", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    # Главное меню
    if message.text == "Главное меню" or message.text == "🔙 Главное меню":
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton("Дэл-150")
        btn2 = types.KeyboardButton("Куб-2")
        btn3 = types.KeyboardButton("Котельные")
        btn4 = types.KeyboardButton("Переносной газик")
        btn5 = types.KeyboardButton("Схемы")
        markup.row(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id, "Выбери нужное", reply_markup=markup)

        # Дэл-150
    elif message.text == "Дэл-150" or message.text == "🔙 вернуться в раздел Дэл-150":
        markup = types.ReplyKeyboardMarkup()
        btn0 = types.KeyboardButton("🔙 Главное меню")
        btn1 = types.KeyboardButton("Как поменять адрес датчика")
        btn2 = types.KeyboardButton("Как поменять порог")
        btn3 = types.KeyboardButton("Как обнулить значения газа")
        btn4 = types.KeyboardButton("Список адересов")
        btn5 = types.KeyboardButton("Тарировка дола")
        btn6 = types.KeyboardButton("Настройка ПК")
        btn7 = types.KeyboardButton("Распайки")
        btn8 = types.KeyboardButton("Блокировки")
        btn9 = types.KeyboardButton("Съемник ДН-130")
        btn10 = types.KeyboardButton("Обнуление")
        btn11 = types.KeyboardButton("Импорт/экспорт истории")
        btn12 = types.KeyboardButton("Монтаж моментомера")
        markup.add(
            btn1,
            btn2,
            btn3,
            btn4,
            btn5,
            btn6,
            btn7,
            btn8,
            btn9,
            btn10,
            btn11,
            btn12,
            btn0,
        )
        bot.send_message(message.chat.id, "Выбери нужное", reply_markup=markup)

        # Дэл-150
    elif message.text == "Как поменять адрес датчика":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 вернуться в раздел Дэл-150")
        markup.add(button)
        bot.send_message(
            message.chat.id,
            "Адрес датчика на дэл-150, меняется путем освобождения нужного адреса(если он занят), затем переходим в меню -> подключенные устройства -> выбираем нужный датчик стрелками -> нажимаем SHIFT+1 -> меняем на нужный адрес и подтверждаем(снизу будет написано на какой датчик будет заменено)",
            reply_markup=markup,
        )

        # Дэл-150
    elif message.text == "Как поменять порог":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 вернуться в раздел Дэл-150")
        markup.add(button)
        bot.send_message(
            message.chat.id,
            "Максимальное значение меняется: enter -> рабочие параметры -> нужный датчик -> изменяем максимальное значение. Для подтвержения порога выйти на главный экран",
            reply_markup=markup,
        )

        # Дэл-150
    elif message.text == "Как обнулить значения газа":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 вернуться в раздел Дэл-150")
        markup.add(button)
        bot.send_video(
            message.chat.id,
            open("./del150/obnulenie.mp4", "rb"),
            reply_markup=markup,
            caption="(Идет загрузка видео)С ДЭЛ-150: enter -> рабочие параметры -> выбираем нужный датчик газа -> установака нуля\n"
            "С Датчика: зажимаем меню -> градуировка -> пгу-1 -> устанвока нуля -> пароль 0007 -> ввод",
            parse_mode="html",
        )

        # Дэл-150
    elif message.text == "Список адересов":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 вернуться в раздел Дэл-150")
        markup.add(button)
        bot.send_photo(
            message.chat.id,
            open("./del150/adresa.jpg", "rb"),
            reply_markup=markup,
            caption="https://www.pla.ru/service/tehpodderzhka/instrukciya-po-nastroike/tablica-adresov-del-150/",
            parse_mode="html",
        )

        # Дэл-150
    elif message.text == "Тарировка дола":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 вернуться в раздел Дэл-150")
        markup.add(button)
        bot.send_photo(
            message.chat.id,
            open("./del150/shem/del_dol_kolibrovka.png", "rb"),
            reply_markup=markup,
            caption="с двумя точками: enter -> рабочие параметры -> скорость сп -> калировка датчика -> установка нуля -> отбиваем верхнюю точку (25м)",
            parse_mode="html",
        )

        # Дэл-150
    elif message.text == "Настройка ПК":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 вернуться в раздел Дэл-150")
        markup.add(button)
        bot.send_video(
            message.chat.id,
            open("./del150/nastroiki_pc.mp4", "rb"),
            reply_markup=markup,
            caption="(Идет загрузка видео)взять айпишник с компа мастера, в той же программе",
            parse_mode="html",
        )

        # Дэл-150
    elif message.text == "Импорт/экспорт истории":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 вернуться в раздел Дэл-150")
        markup.add(button)
        bot.send_video(
            message.chat.id,
            open("./del150/ecsport_import.mp4", "rb"),
            reply_markup=markup,
            caption="(Идет загрузка видео)Инструкция как снять или загрузить данные с программы",
            parse_mode="html",
        )

        # Дэл-150
    elif message.text == "Монтаж моментомера":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 вернуться в раздел Дэл-150")
        markup.add(button)
        bot.send_photo(
            message.chat.id,
            open("./del150/shem/del_moment.png", "rb"),
            reply_markup=markup,
        )
        bot.send_photo(
            message.chat.id,
            open("./del150/shem/del_moment2.png", "rb"),
            reply_markup=markup,
        )

        # Дэл-150
    elif message.text == "Распайки" or message.text == "🔙 Распайки":
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton("Кабель связи")
        btn2 = types.KeyboardButton("Блокировка")
        btn3 = types.KeyboardButton("Пульт бурильщика")
        btn4 = types.KeyboardButton("Питающий")
        btn5 = types.KeyboardButton("Сирена")
        btn6 = types.KeyboardButton("Конвертор")
        btn7 = types.KeyboardButton("Датчик ВБИ")
        btn8 = types.KeyboardButton("Датчик ДОЛ(контакты внутри)")
        # btn9 = types.KeyboardButton("Съемник ДН-130")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, "Выбери нужное", reply_markup=markup)

        # Дэл-150
    elif message.text == "Кабель связи":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 Распайки")
        markup.add(button)
        bot.send_photo(
            message.chat.id,
            open("./del150/shem/kabel svaz.jpg", "rb"),
            reply_markup=markup,
        )

        # Дэл-150
    elif message.text == "Блокировка":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 Распайки")
        markup.add(button)
        bot.send_photo(
            message.chat.id,
            open("./del150/shem/blokirovka.jpg", "rb"),
            reply_markup=markup,
        )

        # Дэл-150
    elif message.text == "Пульт бурильщика":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 Распайки")
        markup.add(button)
        bot.send_photo(
            message.chat.id,
            open("./del150/shem/pult_buril.jpg", "rb"),
            reply_markup=markup,
        )

        # Дэл-150
    elif message.text == "Питающий":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 Распайки")
        markup.add(button)
        bot.send_photo(
            message.chat.id,
            open("./del150/shem/pitanie.jpg", "rb"),
            reply_markup=markup,
        )

        # Дэл-150
    elif message.text == "Сирена":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 Распайки")
        markup.add(button)
        bot.send_photo(
            message.chat.id,
            open("./del150/shem/sirena_svet_zvyk.jpg", "rb"),
            reply_markup=markup,
        )

        # Дэл-150
    elif message.text == "Конвертор":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 Распайки")
        markup.add(button)
        bot.send_photo(
            message.chat.id,
            open("./del150/shem/konvertor(mama).jpg", "rb"),
            reply_markup=markup,
        )
        bot.send_photo(
            message.chat.id,
            open("./del150/shem/konvertor(papa).jpg", "rb"),
            reply_markup=markup,
        )

        # Дэл-150
    elif message.text == "Датчик ВБИ":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 Распайки")
        markup.add(button)
        bot.send_photo(
            message.chat.id,
            open("./del150/shem/dat VBI.jpg", "rb"),
            reply_markup=markup,
        )

        # Дэл-150
    elif message.text == "Блокировки":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 Распайки")
        markup.add(button)
        bot.send_photo(
            message.chat.id,
            open("./del150/blokirovki.jpg", "rb"),
            reply_markup=markup,
            caption="при необходимости поменять разомкнутый на замкнутый(или наоборот)",
            parse_mode="html",
        ),

        # Дэл-150
    elif message.text == "Съемник ДН-130":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 вернуться в раздел Дэл-150")
        markup.add(button)
        bot.send_photo(
            message.chat.id,
            open("./del150/semnik.jpg", "rb"),
            reply_markup=markup,
        ),

        # Дэл-150
    elif message.text == "Обнуление":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 вернуться в раздел Дэл-150")
        markup.add(button)
        bot.send_message(
            message.chat.id,
            "SHIF + ENTER => SHIFT + 0 => SHIFT + нужный датчик(список есть на крышке ДЭЛ-150)",
            reply_markup=markup,
            parse_mode="html",
        ),

        # Дэл-150
    elif message.text == "Датчик ДОЛ(контакты внутри)":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 Распайки")
        markup.add(button)
        bot.send_photo(
            message.chat.id,
            open("./del150/shem/del_dat_lebed.jpg", "rb"),
            reply_markup=markup,
        )

        # Куб-2
    elif message.text == "Куб-2" or message.text == "🔙 Куб-2":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn0 = types.KeyboardButton("🔙 Главное меню")
        btn1 = types.KeyboardButton("Что проверить при неисправности датчика, табла")
        btn2 = types.KeyboardButton("Схемы, распайки")
        btn3 = types.KeyboardButton("Как обнулить датчик давления")
        btn4 = types.KeyboardButton("Настройка ПК геоскан")
        btn5 = types.KeyboardButton("Прошивка МК платы")
        markup.add(btn1, btn2, btn3, btn4, btn0)
        bot.send_message(message.chat.id, "Выбери нужное", reply_markup=markup)

        # Куб-2
    elif message.text == "Что проверить при неисправности датчика, табла":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 Куб-2")
        markup.add(button)
        bot.send_message(
            message.chat.id,
            "1) Индикация на ЦУПе. Посмотреть индикацию на платах внутри ЦУПа: для датчиков(с синим кондером): индикация постоянно горит(в работе), индикация моргает(не в работе), нет индикации (не работает кроссплата или мк);\n"
            "для табло(с розовым кондером): нет индикации (в работе), индикация моргает(не в работе);/n"
            "2) Проверить целостность кабеля, прозвонить кабель;\n"
            "3) Осмотреть внешне датчик",
            reply_markup=markup,
        )

        # Куб-2
    elif message.text == "Схемы, распайки":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 Куб-2")
        markup.add(button)
        bot.send_photo(
            message.chat.id,
            open("./kub2/raspaiki_dat.jpg", "rb"),
            reply_markup=markup,
        )

        # Куб-2
    elif message.text == "Как обнулить датчик давления":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 Куб-2")
        markup.add(button)
        bot.send_message(
            message.chat.id,
            "Перед обнулением следует уменьшить значение на самом датчике максимально до 0 и не больше 5. Для этого нужно вскрыть датчик(не выключая), затем немного открутить 2 болта, отрегулировать положение крепления(ориентироваться по датчику), зафиксировать болты после регулировки, далее закрываем датчик и кнопками обнуляем: ввод -> стрелками выбираем -0- -> зажимаем ввод для обнуления",
            reply_markup=markup,
        )

        # Куб-2
    elif message.text == "Настройка ПК геоскан":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 Куб-2")
        markup.add(button)
        bot.send_message(
            message.chat.id,
            "Включить геоскан => вид => связь => подключить СОМ порт",
            reply_markup=markup,
        )

        # Куб-2
    elif message.text == "Прошивка МК платы":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 Куб-2")
        markup.add(button)
        bot.send_video(
            message.chat.id,
            open("./del150/obnulenie.mp4", "rb"),
            caption="(Идет загрузка видео)",
            reply_markup=markup,
        )

        # Котельная
    elif message.text == "Котельные" or message.text == "🔙 Котельные":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn0 = types.KeyboardButton("🔙 Главное меню")
        btn1 = types.KeyboardButton("Аргусы")
        btn2 = types.KeyboardButton("Новые щиты")
        btn3 = types.KeyboardButton("Схемы, распайки котельная")
        markup.add(btn1, btn2, btn3, btn0)
        bot.send_message(message.chat.id, "Выбери нужное", reply_markup=markup)

        # Котельная
    elif message.text == "Аргусы" or message.text == "🔙 Аргусы":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Наладка Аргус")
        btn2 = types.KeyboardButton("Ошибки Аргус")
        btn3 = types.KeyboardButton("Схемы Аргус")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, "Выбери нужное", reply_markup=markup)

        # Котельная
    elif message.text == "Наладка Аргус":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 Аргусы")
        markup.add(button)
        bot.send_message(
            message.chat.id,
            "Нужно отрегулировать:\n"
            "1) Платы уровня(светофором) вместе с котельщиком, те уровни какие нужны ему\n"
            "2) Проверить все блокировки",
            reply_markup=markup,
            parse_mode="html",
        ),

        # Котельная
    elif message.text == "Ошибки Аргус":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 Аргусы")
        markup.add(button)
        bot.send_message(
            message.chat.id,
            "Если аргус не включается:\n"
            "1) проверить приходит ли напряжение на аргус\n"
            "2) проверить предохранители(снаружи и внутри)\n"
            "3) подключить кабеля на соседний аргус и проверить работоспособность кабелей(перед этим точно убедиться что нет короткого замыкания)\n"
            "4) заменить плату питания(справа)\n"
            "Если аргус включился и не отрабатывает: \n"
            "1) проверить предохранители\n"
            "2) подключить кабеля на соседний аргус и проверить работоспособность кабелей\n"
            "3) заменить плату логики(слева)\n"
            "Если уровни не отрабатывают как надо:\n"
            "1) проверить целостность кабеля(можно светофором, можно прозвонить)\n"
            "2) проверить целостность платы уровня(светофором)\n"
            "3) переключить кабеля на другой аргус и проверить\n"
            "Если отсекатель не работает:\n"
            "1) проверить напряжение на концах отсекателя\n"
            "2) проверить сопротивление катушки(нормально от 6 Ом)\n"
            "3) проверить предохранитель внутри\n"
            "Если экм не отрабатывает:\n"
            "1) проверить правильность подключения концов на экм(1, 3 контакт)\n"
            "2) проверить целостность кабеля\n"
            "Если не работает пламя:\n"
            "1) проверить кабель\n"
            "2) поставить заведомо рабочий датчик пламени с соседнего котла",
            reply_markup=markup,
            parse_mode="html",
        ),

        # Котельная
    elif message.text == "Схемы Аргус":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 Аргусы")
        markup.add(button)
        bot.send_photo(
            message.chat.id,
            open("./kotel/shem_argus.jpg", "rb"),
            reply_markup=markup,
        )

        # Котельная
    elif message.text == "Новые щиты" or message.text == "🔙 Новые щиты":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Наладка Щиты")
        btn2 = types.KeyboardButton("Ошибки Щиты")
        btn3 = types.KeyboardButton("Схемы и длина кабелей Щиты")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, "Выбери нужное", reply_markup=markup)

        # Котельная
    elif message.text == "Наладка Щиты":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 Новые щиты")
        markup.add(button)
        bot.send_message(
            message.chat.id,
            "При наладке щита:\n"
            "1) включать автоматы последовательно слева направо(и наоборот при выключении)\n"
            "2) для настройки уровней можно не включать маленький автомат(отвечает за блокировки, включение/выключение насосов)\n"
            "3) очень чувствительное пламя, возможно придется корректировать направление трубки пламени",
            reply_markup=markup,
            parse_mode="html",
        ),

        # Котельная
    elif message.text == "Ошибки Щиты":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 Новые щиты")
        markup.add(button)
        bot.send_message(
            message.chat.id,
            "1) Ошибки сбрасываются кнопкой СБРОС, при условии, что датчик пламени и экм работают стабильно и не находятся в сработке.\n"
            "2) Нижний и верхний аварийный сбрасываются автоматически при наборе/сбросе воды.\n"
            "3) Сирену можно выключить, выключив маленький автомат(отвечает за блокировки, включение/выключение насосов), при этом насосы не будут включаться и выключаться, на отсекателе должен стоять болт",
            reply_markup=markup,
            parse_mode="html",
        ),

        # Котельная
    elif message.text == "Схемы и длина кабелей Щиты":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 Новые щиты")
        markup.add(button)
        bot.send_photo(
            message.chat.id,
            open("./kotel/dlina_kabel.jpg", "rb"),
            reply_markup=markup,
        )

        bot.send_message(
            message.chat.id,
            """Распайка пламени: 1 - плюс 2 - ничего 3 - минус 4 - реле 5 - реле""",
            reply_markup=markup,
            parse_mode="html",
        ),

        # Котельная
    elif (
        message.text == "Схемы, распайки котельная"
        or message.text == "🔙 Схемы, распайки котельная"
    ):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("схема того")
        btn2 = types.KeyboardButton("схема этого")
        btn3 = types.KeyboardButton("и того и этого")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, "Выбери нужное", reply_markup=markup)

        # Котельная
    elif message.text == "схема того":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 Схемы, распайки котельная")
        markup.add(button)
        bot.send_photo(
            message.chat.id,
            open("./Снимок-экрана-2021-09-07-в-19.48.05.jpg", "rb"),
            reply_markup=markup,
        )

        # Котельная
    elif message.text == "схема этого":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 Схемы, распайки котельная")
        markup.add(button)
        bot.send_photo(
            message.chat.id,
            open("./Снимок-экрана-2021-09-07-в-19.48.05.jpg", "rb"),
            reply_markup=markup,
        )

        # Котельная
    elif message.text == "и того и этого":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 Схемы, распайки котельная")
        markup.add(button)
        bot.send_photo(
            message.chat.id,
            open("./Снимок-экрана-2021-09-07-в-19.48.05.jpg", "rb"),
            reply_markup=markup,
        )

        # Переносной газик
    elif message.text == "Переносной газик" or message.text == "🔙 Переносной газик":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn0 = types.KeyboardButton("🔙 Главное меню")
        btn1 = types.KeyboardButton("Как обнулить")
        btn2 = types.KeyboardButton("Как от тарировать")
        # btn3 = types.KeyboardButton("и того и этого")
        markup.add(btn1, btn2, btn0)
        bot.send_message(message.chat.id, "Выбери нужное", reply_markup=markup)

        # Переносной газик
    elif message.text == "Как обнулить":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 Переносной газик")
        markup.add(button)
        bot.send_photo(
            message.chat.id,
            open("./Снимок-экрана-2021-09-07-в-19.48.05.jpg", "rb"),
            reply_markup=markup,
        )

        # Переносной газик
    elif message.text == "Как от тарировать":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 Переносной газик")
        markup.add(button)
        bot.send_photo(
            message.chat.id,
            open("./Снимок-экрана-2021-09-07-в-19.48.05.jpg", "rb"),
            reply_markup=markup,
        )

        # Схемы
    elif message.text == "Схемы" or message.text == "🔙 Схемы":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn0 = types.KeyboardButton("🔙 Главное меню")
        btn1 = types.KeyboardButton("Схема блокировки по штропам")
        btn2 = types.KeyboardButton("Схемы2, Схемы")
        btn3 = types.KeyboardButton("Схемы3, Схемы, Схемы")
        markup.add(btn1, btn2, btn3, btn0)
        bot.send_message(message.chat.id, "Выбери нужное", reply_markup=markup)

        # Схемы
    elif message.text == "Схема блокировки по штропам":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 Схемы")
        markup.add(button)
        bot.send_photo(
            message.chat.id,
            open("./shemi/blockirovki_shtropa.jpg", "rb"),
            reply_markup=markup,
        )

        # Схемы
    elif message.text == "Схемы2, Схемы":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 Схемы")
        markup.add(button)
        bot.send_photo(
            message.chat.id,
            open("./Снимок-экрана-2021-09-07-в-19.48.05.jpg", "rb"),
            reply_markup=markup,
        )
        # Схемы
    elif message.text == "Схемы3, Схемы, Схемы":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🔙 Схемы")
        markup.add(button)
        bot.send_photo(
            message.chat.id,
            open("./Снимок-экрана-2021-09-07-в-19.48.05.jpg", "rb"),
            reply_markup=markup,
        )

    else:
        message.text == "Информация о боте"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_info_0 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn_info_0)
        bot.send_message(
            message.from_user.id,
            "Переходи в главное меню",
            reply_markup=markup,
        )


if __name__ == "__main__":
    bot.polling(none_stop=True, interval=1)
