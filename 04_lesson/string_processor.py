class StringProcessor:
    @staticmethod
    def process(text: str) -> str:
        if not text:
            return "."
        processed_text = text[0].upper() + text[1:]
        if not processed_text.endswith("."):
            processed_text += "."
        return processed_text

class StringProcessor:
    @staticmethod
    def process(text: str) -> str:
        # Если строка пустая или состоит только из пробелов
        if not text or text.isspace():
            return "." if not text else text + "."

        # Делаем первую букву заглавной
        processed_text = text[0].upper() + text[1:]

        # Добавляем точку, если ее нет
        if not processed_text.endswith("."):
            processed_text += "."

        return processed_text
