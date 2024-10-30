import json
import os
from datetime import datetime

# Путь к файлу для хранения заметок
NOTES_FILE = 'notes.json'

# Функция для загрузки заметок из файла
def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r') as file:
            return json.load(file)
    return []

# Функция для сохранения заметок в файл
def save_notes(notes):
    with open(NOTES_FILE, 'w') as file:
        json.dump(notes, file, indent=4)

# Функция для создания новой заметки
def create_note():
    title = input("Введите заголовок заметки: ")
    content = input("Введите текст заметки: ")
    note = {
        "id": str(len(load_notes()) + 1),
        "title": title,
        "content": content,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    notes = load_notes()
    notes.append(note)
    save_notes(notes)
    print("Заметка создана.")

# Функция для чтения всех заметок
def read_notes():
    notes = load_notes()
    if not notes:
        print("Список заметок пуст.")
        return
    for note in notes:
        print(f"ID: {note['id']} | Заголовок: {note['title']} | Дата: {note['timestamp']}")

# Функция для редактирования заметки
def edit_note():
    note_id = input("Введите ID заметки для редактирования: ")
    notes = load_notes()
    for note in notes:
        if note['id'] == note_id:
            note['title'] = input("Введите новый заголовок: ")
            note['content'] = input("Введите новый текст: ")
            note['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка обновлена.")
            return
    print("Заметка с указанным ID не найдена.")

# Функция для удаления заметки
def delete_note():
    note_id = input("Введите ID заметки для удаления: ")
    notes = load_notes()
    notes = [note for note in notes if note['id'] != note_id]
    save_notes(notes)
    print("Заметка удалена.")

# Функция для просмотра заметки по дате
def view_notes_by_date():
    date = input("Введите дату (в формате ГГГГ-ММ-ДД): ")
    notes = load_notes()
    found_notes = [note for note in notes if note['timestamp'].startswith(date)]
    if not found_notes:
        print("Заметки на указанную дату не найдены.")
        return
    for note in found_notes:
        print(f"ID: {note['id']} | Заголовок: {note['title']} | Дата: {note['timestamp']}")

# Основное меню приложения
def main():
    while True:
        print("\n1. Создать заметку")
        print("2. Просмотреть все заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Просмотреть заметки по дате")
        print("0. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            create_note()
        elif choice == '2':
            read_notes()
        elif choice == '3':
            edit_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            view_notes_by_date()
        elif choice == '0':
            print("Выход из приложения.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
