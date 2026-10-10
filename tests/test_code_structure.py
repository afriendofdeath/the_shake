import inspect

import snake


def test_game_object_exists():
    """Проверяет наличие класса GameObject."""
    assert hasattr(snake, 'GameObject')
    assert inspect.isclass(snake.GameObject)


def test_snake_exists():
    """Проверяет наличие класса Snake."""
    assert hasattr(snake, 'Snake')
    assert issubclass(snake.Snake, snake.GameObject)


def test_apple_exists():
    """Проверяет наличие класса Apple."""
    assert hasattr(snake, 'Apple')
    assert issubclass(snake.Apple, snake.GameObject)


def test_main_exists():
    """Проверяет наличие функции main."""
    assert hasattr(snake, 'main')
    assert callable(snake.main)


def test_snake_has_required_methods():
    """Проверяет необходимые методы класса Snake."""
    assert callable(getattr(snake.Snake, 'update_direction', None))
    assert callable(getattr(snake.Snake, 'move', None))
    assert callable(getattr(snake.Snake, 'draw', None))
    assert callable(getattr(snake.Snake, 'get_head_position', None))
    assert callable(getattr(snake.Snake, 'reset', None))


def test_game_object_has_draw_method():
    """Проверяет наличие метода отрисовки."""
    assert callable(getattr(snake.GameObject, 'draw', None))


def test_apple_has_randomize_position():
    """Проверяет наличие метода изменения позиции яблока."""
    assert callable(
        getattr(snake.Apple, 'randomize_position', None)
    )
