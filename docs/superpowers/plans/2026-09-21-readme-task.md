# README Task Specification Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the draft `README.md` with a concise Russian-language technical assignment for the terminal FAQ bot.

**Architecture:** This is a documentation-only change. `README.md` will become the single entry point for the assignment, while development workflow details remain in `docs/DEVELOPMENT_PLAN.md` and `CONTRIBUTING.md`.

**Tech Stack:** Markdown, Git

---

### Task 1: Rewrite the assignment README

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Replace the draft with the approved assignment**

Use the following complete content:

````markdown
# FAQ-бот на пять вопросов

## Задача

Разработать простой чат-бот для терминала, который отвечает на вопросы о
репетиции. Бот должен распознавать пять заранее заданных тем и находить наиболее
подходящий ответ по ключевым словам.

## Функциональные требования

1. Добавьте в репозиторий файл `faq.txt` с пятью парами «вопрос — ответ».
2. Подготовьте ответы по следующим темам:
   - время репетиции;
   - команда;
   - выбранный трек;
   - порядок сдачи работы;
   - призы.
3. Пользователь вводит вопрос в терминале, после чего бот:
   - находит наиболее близкий вопрос из `faq.txt` и выводит соответствующий
     ответ;
   - выводит `не знаю`, если введённый вопрос не относится ни к одной известной
     теме.
4. Диалог должен позволять задать несколько вопросов подряд без повторного
   запуска программы.

## Пример работы

```text
Вы: Когда начнётся репетиция?
Бот: Репетиция начнётся в 18:00.

Вы: Какая сегодня погода?
Бот: не знаю
```

Точные формулировки вопросов и ответов команда выбирает самостоятельно.

## Технические ограничения

- Язык программирования и библиотеки можно выбрать самостоятельно.
- Для поиска ответа достаточно сопоставления по ключевым словам.
- Использовать RAG, векторную базу данных или языковую модель не требуется.
- Решение должно запускаться локально и работать в терминале.

## Что сдавать

Результат сдаётся в виде командного репозитория. В нём должны находиться:

- исходный код бота;
- файл `faq.txt` с пятью парами «вопрос — ответ»;
- инструкция по запуску;
- краткое описание получившегося решения.

## Критерии готовности

- В `faq.txt` представлены все пять обязательных тем.
- Бот отвечает на вопросы, совпадающие с известными темами по ключевым словам.
- На несвязанный вопрос бот отвечает `не знаю`.
- Пользователь может вести диалог с ботом в терминале.
- В README указано, как запустить готовое решение и что было реализовано.
````

- [ ] **Step 2: Check Markdown and whitespace**

Run:

```bash
git diff --check
```

Expected: the command exits with status 0 and prints no errors.

- [ ] **Step 3: Verify all source requirements are present**

Run:

```bash
rg -n 'faq\.txt|время|команд|трек|сдач|приз|не знаю|ключев|RAG|репозитор' README.md
```

Expected: every required concept appears in the matching lines.

- [ ] **Step 4: Review the rendered structure**

Read `README.md` from start to finish and confirm that it contains no launch
command or implementation claim for software that does not exist yet.

- [ ] **Step 5: Commit the README**

```bash
git add README.md
git commit -m "docs: turn readme into faq bot assignment"
```
