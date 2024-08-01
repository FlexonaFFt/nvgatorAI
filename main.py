import replicate
from dotenv import load_dotenv
import os

load_dotenv()
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")


class Commands:
    def __init__(self):
        self.history = []  # Список для хранения истории диалога

    def add_to_history(self, message):
        self.history.append(message)

    def get_history(self):
        return "\n".join(self.history)

    def fast_prompt(self, prompt):
        full_prompt = self.get_history() + "\n" + prompt  # Добавляем историю к текущему запросу
        for event in replicate.stream(
            "meta/meta-llama-3-70b-instruct",
            input={
                "prompt": full_prompt
            },
        ):
            print(str(event), end="")

if __name__ == '__main__':
    assistant = Commands()  # Создаем экземпляр класса
    print("Как я могу вам помочь?")
    
    while True:
        user_input = input("Вы: ")
        if user_input.lower() in ['выход', 'exit']:
            print("Помощник завершил работу.")
            break
        assistant.add_to_history(f"Вы: {user_input}")  # Сохраняем пользовательский ввод
        assistant.fast_prompt(user_input)  # Отправляем запрос в модель