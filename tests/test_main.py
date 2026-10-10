import pygame

from snake import Apple, Snake


def test_snake_initialization():
    """Проверяет начальное состояние змейки."""
    snake = Snake()

    assert snake.length == 1
    assert len(snake.positions) == 1
    assert snake.get_head_position() == snake.positions[0]


def test_snake_moves():
    """Проверяет движение змейки вправо."""
    snake = Snake()
    old_position = snake.get_head_position()

    snake.direction = pygame.Vector2(1, 0)
    snake.move()

    assert snake.get_head_position() != old_position


def test_snake_grows():
    """Проверяет увеличение длины змейки."""
    snake = Snake()
    snake.length = 2

    snake.move()

    assert len(snake.positions) == 2


def test_snake_reset():
    """Проверяет сброс состояния змейки."""
    snake = Snake()
    snake.length = 5
    snake.positions.append((20, 20))

    snake.reset()

    assert snake.length == 1
    assert len(snake.positions) == 1
    assert snake.direction == pygame.Vector2(1, 0)
    assert snake.next_direction is None


def test_snake_does_not_reverse_direction():
    """Проверяет запрет разворота на 180 градусов."""
    snake = Snake()
    snake.direction = pygame.Vector2(1, 0)

    snake.next_direction = pygame.Vector2(-1, 0)
    snake.update_direction()

    assert snake.direction == pygame.Vector2(1, 0)


def test_apple_has_position():
    """Проверяет наличие позиции у яблока."""
    apple = Apple()

    assert apple.position is not None


def test_apple_position_is_on_grid():
    """Проверяет расположение яблока на игровой сетке."""
    apple = Apple()

    x, y = apple.position

    assert x % 20 == 0
    assert y % 20 == 0
