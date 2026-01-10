import sys
import pytest
from unittest.mock import AsyncMock, patch, MagicMock

sys.path.append('../')
import main

class DummyUser:
    def __init__(self, id):
        self.id = id

class DummyMessage:
    def __init__(self, text, user_id):
        self.text = text
        self.from_user = DummyUser(user_id)
        self.reply_text = AsyncMock()

class DummyUpdate:
    def __init__(self, text, user_id=1234):
        self.message = DummyMessage(text, user_id)

class DummyContext:
    pass

@pytest.mark.asyncio
@patch('db.add_book')
async def test_add_correct(mock_add_book):
    from main import add 
    update = DummyUpdate("/add Title, Author, Genre, читаю")
    context = DummyContext()
    await add(update, context)
    mock_add_book.assert_called_once_with(1234, "Title", "Author", "Genre", "читаю")
    update.message.reply_text.assert_awaited_with("Книга добавлена!")

@pytest.mark.asyncio
@patch('db.add_book')
async def test_add_wrong_format(mock_add_book):
    from main import add
    update = DummyUpdate("/add wrong format")
    context = DummyContext()
    await add(update, context)
    mock_add_book.assert_not_called()
    update.message.reply_text.assert_awaited_with("Формат: /add Название, Автор, Жанр, Статус")

@pytest.mark.asyncio
@patch('db.get_books')
async def test_list_books_page_and_empty(mock_get_books):
    from main import list_books
    mock_get_books.return_value = [
        {"id": 1, "title": "T1", "author": "A1", "genre": "G1", "status": "прочитано"},
        {"id": 2, "title": "T2", "author": "A2", "genre": "G2", "status": "в планах"},
    ]
    update_with_page = DummyUpdate("/list 2")
    update_no_page = DummyUpdate("/list")
    context = DummyContext()

    await list_books(update_with_page, context)
    mock_get_books.assert_called_with(1234, 2)
    update_with_page.message.reply_text.assert_awaited_with(
        "1. T1 - A1 [G1] (прочитано)\n2. T2 - A2 [G2] (в планах)"
    )

    mock_get_books.return_value = []
    await list_books(update_no_page, context)
    update_no_page.message.reply_text.assert_awaited_with("Нет книг на этой странице.")

@pytest.mark.asyncio
@patch('db.search_books')
async def test_search(mock_search_books):
    from main import search
    mock_search_books.return_value = [
        {"id": 1, "title": "T1", "author": "A1", "genre": "G1", "status": "прочитано"}
    ]
    update = DummyUpdate("/search T1")
    context = DummyContext()

    await search(update, context)
    mock_search_books.assert_called_with(1234, "T1")
    update.message.reply_text.assert_awaited_with("1. T1 - A1 [G1] (прочитано)")

    mock_search_books.return_value = []
    update2 = DummyUpdate("/search NoResult")
    await search(update2, context)
    update2.message.reply_text.assert_awaited_with("Не найдено.")

@pytest.mark.asyncio
@patch('db.edit_book')
async def test_edit(mock_edit_book):
    from main import edit
    update_correct = DummyUpdate("/edit 1, title=Новое название, status=читаю")
    update_wrong = DummyUpdate("/edit 1")
    context = DummyContext()

    await edit(update_wrong, context)
    update_wrong.message.reply_text.assert_awaited_with("Формат: /edit id, поле=значение,...")

    await edit(update_correct, context)
    mock_edit_book.assert_called_once_with(1, {"title": "Новое название", "status": "читаю"})
    update_correct.message.reply_text.assert_awaited_with("Запись обновлена.")

@pytest.mark.asyncio
@patch('db.delete_book')
async def test_delete(mock_delete_book):
    from main import delete
    update = DummyUpdate("/delete 1")
    context = DummyContext()

    await delete(update, context)
    mock_delete_book.assert_called_once_with(1)
    update.message.reply_text.assert_awaited_with("Книга удалена.")

@pytest.mark.asyncio
@patch('db.get_stats')
async def test_stats(mock_get_stats):
    from main import stats
    mock_get_stats.return_value = 5
    update = DummyUpdate("/stats")
    context = DummyContext()

    await stats(update, context)
    mock_get_stats.assert_called_once_with(1234)
    update.message.reply_text.assert_awaited_with("Прочитано книг за месяц: 5")

@pytest.mark.asyncio
async def test_start_and_help():
    from main import start, help_command
    update = DummyUpdate("/start")
    context = DummyContext()

    await start(update, context)
    update.message.reply_text.assert_awaited_with(
        "Привет! Это бот-дневник читателя. /help для инструкций."
    )

    update.message.reply_text.reset_mock()

    await help_command(update, context)
    expected_msg = (
        "/add <название>, <автор>, <жанр>, <статус:прочитано|читаю|в планах>\n"
        "/list <страница>\n"
        "/search <автор/название>\n"
        "/edit <id>, поле=значение,...\n"
        "/delete <id>\n"
        "/stats\n"
    )
    update.message.reply_text.assert_awaited_with(expected_msg)
