"""Терминальный интерфейс FAQ-бота."""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path


FAQ_PATH = Path(__file__).with_name("faq.txt")
EXIT_COMMANDS = frozenset({"выход", "выйти", "exit", "quit", "q"})

InputFunction = Callable[[str], str]
OutputFunction = Callable[[str], None]
FindAnswerFunction = Callable[[str, list[dict]], str | None]


def run_chat(
    entries: list[dict],
    find_answer: FindAnswerFunction,
    *,
    input_fn: InputFunction = input,
    output_fn: OutputFunction = print,
) -> int:
    """Запустить диалог с пользователем и вернуть код завершения."""

    output_fn("FAQ-бот готов. Задайте вопрос или напишите «выход».")

    while True:
        try:
            user_text = input_fn("Вы: ").strip()
        except (EOFError, KeyboardInterrupt):
            output_fn("\nДо встречи!")
            return 0

        if user_text.casefold() in EXIT_COMMANDS:
            output_fn("До встречи!")
            return 0

        if not user_text:
            output_fn("Введите вопрос или команду «выход».")
            continue

        answer = find_answer(user_text, entries)
        output_fn(answer if answer is not None else "не знаю")


def main() -> int:
    """Загрузить FAQ и запустить терминальный интерфейс."""

    try:
        from matcher import find_answer, load_faq
    except ModuleNotFoundError as error:
        if error.name != "matcher":
            raise
        print("Ошибка: модуль matcher.py ещё не добавлен.")
        return 1

    try:
        entries = load_faq(str(FAQ_PATH))
    except (OSError, ValueError) as error:
        print(f"Ошибка загрузки FAQ: {error}")
        return 1

    if not entries:
        print("Ошибка загрузки FAQ: список вопросов пуст.")
        return 1

    return run_chat(entries, find_answer)


if __name__ == "__main__":
    raise SystemExit(main())
