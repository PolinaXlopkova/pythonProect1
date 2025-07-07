import logging
import pytest
from src.decorators import log

@pytest.fixture
def setup_logging():
    # Сброс настроек логгера перед каждым тестом
    logging.getLogger().handlers = []
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )
    logging.getLogger('root').propagate = False  # Предотвращает дублирование логов

def test_log_success(capsys, setup_logging):
    @log()
    def test_func(x, y):
        return x + y

    result = test_func(10, 20)
    assert result == 30

    # Добавляем задержку для асинхронных логов
    import time; time.sleep(0.1)

def test_log_error(capsys, setup_logging):
    @log()
    def failing_func():
        raise ValueError("Something went wrong")

    with pytest.raises(ValueError):
        failing_func()

    # Добавляем задержку для асинхронных логов
    import time; time.sleep(0.1)

    captured = capsys.readouterr()
    assert 'raised ValueError' in captured.err