import inspect

import the_snake


def test_game_object_exists():
    """Проверяет наличие класса GameObject."""
    assert hasattr(the_snake, 'GameObject')
    assert inspect.isclass(the_snake.GameObject)


def test_snake_exists():
    """Проверяет наличие класса Snake."""
    assert hasattr(the_snake, 'Snake')
    assert issubclass(the_snake.Snake, the_snake.GameObject)


def test_apple_exists():
    """Проверяет наличие класса Apple."""
    assert hasattr(the_snake, 'Apple')
    assert issubclass(the_snake.Apple, the_snake.GameObject)


def test_main_exists():
    """Проверяет наличие функции main."""
    assert hasattr(the_snake, 'main')
    assert callable(the_snake.main)


def test_snake_has_required_methods():
    """Проверяет необходимые методы класса Snake."""
    assert callable(getattr(the_snake.Snake, 'update_direction', None))
    assert callable(getattr(the_snake.Snake, 'move', None))
    assert callable(getattr(the_snake.Snake, 'draw', None))
    assert callable(getattr(the_snake.Snake, 'get_head_position', None))
    assert callable(getattr(the_snake.Snake, 'reset', None))


def test_game_object_has_draw_method():
    """Проверяет наличие метода отрисовки."""
    assert callable(getattr(the_snake.GameObject, 'draw', None))


def test_apple_has_randomize_position():
    """Проверяет наличие метода изменения позиции яблока."""
    assert callable(
        getattr(the_snake.Apple, 'randomize_position', None)
    )
