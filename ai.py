import random
import json
import re
from datetime import datetime
import math


class SimpleAI:
    def __init__(self):
        self.name = "Помощник"
        self.knowledge_base = self.create_knowledge_base()
        self.conversation_history = []

    def create_knowledge_base(self):
        """Создаем базу знаний с ответами на частые вопросы"""
        return {
            "привет": [
                "Здравствуйте! Чем я могу вам помочь?",
                "Привет! Рад вас видеть!",
                "Здравствуйте! Задавайте свои вопросы."
            ],
            "как дела": [
                "У меня всё отлично! А у вас?",
                "Работаю в штатном режиме!",
                "Спасибо, хорошо! Чем могу помочь?"
            ],
            "пока": [
                "До свидания! Буду рад помочь снова!",
                "Всего хорошего! Обращайтесь ещё!",
                "До встречи!"
            ],
            "имя": [
                f"Меня зовут {self.name}",
                "Я ваш виртуальный помощник"
            ],
            "время": [
                f"Сейчас {datetime.now().strftime('%H:%M')}",
                f"Точное время: {datetime.now().strftime('%H:%M:%S')}"
            ],
            "дата": [
                f"Сегодня {datetime.now().strftime('%d.%m.%Y')}",
                f"Текущая дата: {datetime.now().strftime('%d %B %Y')}"
            ]
        }

    def calculate(self, expression):
        """Вычисление математических выражений"""
        try:
            # Удаляем пробелы и проверяем на безопасность
            expression = re.sub(r'[^0-9+\-*/().]', '', expression)
            result = eval(expression, {"__builtins__": {}}, {"math": math})
            return f"Результат: {result}"
        except:
            return None

    def get_weather_info(self, city):
        """Имитация получения погоды"""
        # В реальном приложении здесь был бы API запрос к сервису погоды
        weather_responses = [
            f"В городе {city} сейчас солнечно, температура +20°C",
            f"В {city} облачно с прояснениями, температура +15°C",
            f"В {city} идёт дождь, температура +10°C",
            "Извините, информация о погоде временно недоступна"
        ]
        return random.choice(weather_responses)

    def get_general_response(self, question):
        """Получение общего ответа на вопрос"""
        responses = [
            "Интересный вопрос. Дайте подумать...",
            f"Я думаю, что {question.lower()} - это хороший вопрос",
            "Мне нужно больше информации, чтобы ответить точно",
            "Возможно, вы найдете ответ в интернете",
            "Я не совсем уверен, но могу предположить..."
        ]
        return random.choice(responses)

    def process_question(self, question):
        """Обработка вопроса и поиск ответа"""
        question = question.lower().strip()

        # Сохраняем вопрос в историю
        self.conversation_history.append(("user", question))

        # Проверяем математические выражения
        if any(op in question for op in ['+', '-', '*', '/', '**', '%']):
            result = self.calculate(question)
            if result:
                return result

        # Проверяем вопросы о погоде
        if 'погода' in question or 'погоду' in question:
            # Пытаемся извлечь название города
            cities = ['москва', 'питер', 'сочи', 'казань']
            for city in cities:
                if city in question:
                    return self.get_weather_info(city)
            return self.get_weather_info("вашем городе")

        # Проверяем прямые совпадения в базе знаний
        for key, responses in self.knowledge_base.items():
            if key in question:
                return random.choice(responses)

        # Если ничего не найдено, даем общий ответ
        return self.get_general_response(question)

    def chat(self):
        """Основной метод для общения с пользователем"""
        print(f"👋 Здравствуйте! Я {self.name}. Задавайте свои вопросы (для выхода напишите 'выход')")
        print("-" * 50)

        while True:
            try:
                user_input = input("Вы: ").strip()

                if not user_input:
                    print(f"{self.name}: Пожалуйста, напишите что-нибудь")
                    continue

                if user_input.lower() in ['выход', 'пока', 'до свидания']:
                    print(f"{self.name}: До свидания! Было приятно пообщаться!")
                    break

                # Получаем ответ
                response = self.process_question(user_input)

                # Сохраняем ответ в историю
                self.conversation_history.append(("assistant", response))

                print(f"{self.name}: {response}")
                print("-" * 50)

            except KeyboardInterrupt:
                print(f"\n{self.name}: До свидания!")
                break
            except Exception as e:
                print(f"{self.name}: Извините, произошла ошибка: {e}")


class AdvancedAI(SimpleAI):
    """Улучшенная версия ИИ с дополнительными функциями"""

    def __init__(self):
        super().__init__()
        self.user_name = None
        self.moods = ["дружелюбный", "весёлый", "серьёзный", "загадочный"]
        self.current_mood = random.choice(self.moods)

    def remember_user(self, name):
        """Запоминает имя пользователя"""
        self.user_name = name
        return f"Приятно познакомиться, {name}! Я запомнил ваше имя."

    def tell_joke(self):
        """Рассказывает шутку"""
        jokes = [
            "Почему программисты путают Хэллоуин и Рождество? Потому что Oct 31 = Dec 25!",
            "Что говорит программист, когда у него день рождения? 'Happy birthday to me!'.format(me)",
            "Сколько программистов нужно, чтобы поменять лампочку? Ни одного, это аппаратная проблема!"
        ]
        return random.choice(jokes)

    def give_advice(self, topic):
        """Дает совет по теме"""
        advice = {
            "учеба": "Регулярные короткие перерывы помогают лучше усваивать информацию!",
            "работа": "Попробуйте метод Pomodoro: 25 минут работы, 5 минут отдыха.",
            "здоровье": "Не забывайте пить воду и делать зарядку каждый день!",
            "отношения": "Самое важное в общении - умение слушать и слышать собеседника."
        }

        for key, value in advice.items():
            if key in topic:
                return value

        return "Советую довериться своей интуиции в этом вопросе."

    def process_question(self, question):
        """Расширенная обработка вопросов"""
        question = question.lower()

        # Запоминаем имя пользователя
        if 'меня зовут' in question:
            name = question.replace('меня зовут', '').strip()
            return self.remember_user(name)

        # Рассказываем шутку
        if 'шутку' in question or 'анекдот' in question:
            return self.tell_joke()

        # Даем советы
        if 'совет' in question or 'посоветуй' in question:
            for topic in ['учеба', 'работа', 'здоровье', 'отношения']:
                if topic in question:
                    return self.give_advice(topic)
            return self.give_advice("общее")

        # Используем базовую обработку
        return super().process_question(question)

    def chat(self):
        """Улучшенный чат с дополнительными функциями"""
        print(f"🎭 Я {self.name} и сегодня я в {self.current_mood} настроении!")
        print("Я могу отвечать на вопросы, рассказывать шутки и давать советы!")
        print("(для выхода напишите 'выход')")
        print("=" * 50)

        super().chat()


# Пример использования
if __name__ == "__main__":
    print("Выберите версию ИИ:")
    print("1. Простой помощник")
    print("2. Продвинутый помощник")

    choice = input("Ваш выбор (1 или 2): ").strip()

    if choice == "2":
        ai = AdvancedAI()
    else:
        ai = SimpleAI()

    ai.chat()

    # Показываем историю разговора
    print("\n📝 История разговора:")
    for role, message in ai.conversation_history[-5:]:  # Последние 5 сообщений
        print(f"{role}: {message}")