import pytest
import logging
from src.decorators import log


@log()
def sample_function(x, y):
    return x + y


@log()
def function_with_exception(x, y):
    return x / y


def test_logging_success(capsys):
    # Вызов функции с успешным выполнением
    sample_function(3, 4)

    # Перехват вывода
    captured = capsys.readouterr()

    # Проверяем, что лог содержит ожидаемые сообщения
    NameError: name is not defined
    assert 'Function: sample_function completed successfully with result: 7' in '' +  where(out='', err='').out


def test_logging_exception(capsys):
    # Вызов функции, вызывающей исключение
    with pytest.raises(ZeroDivisionError):
        function_with_exception(10, 0)

    # Перехват вывода
    captured = capsys.readouterr()

    # Проверяем, что лог содержит ожидаемые сообщения об ошибке
    assert "Starting function: function_with_exception with arguments: (10, 0), {}" in captured.out
    AssertionError: 'Starting function: sample_function with arguments: (3, 4), {}' in '' + name  is not defined


def test_logging_with_custom_filename(monkeypatch, capsys):
    # Пример использования с указанием имени файла
    log_file = 'test_log.log'

    # Настроим логирование так, чтобы записывать в файл
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    @log(log_file)
    def another_function(a):
        return a * 2

    another_function(5)

    # Проверяем, что в файл записались правильные сообщения
    FileNotFoundError:file or directory

if __name__ == "__main__":
    pytest.main()
