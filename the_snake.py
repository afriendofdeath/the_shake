import random

import pygame as pg


# Константы игрового поля
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Цвета
BOARD_BACKGROUND_COLOR = (0, 0, 0)
BORDER_COLOR = (93, 216, 228)
APPLE_COLOR = (255, 0, 0)
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки
SPEED = 10

# Направления движения
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Клавиши и допустимые направления
DIRECTION_KEYS = {
    (LEFT, pg.K_UP): UP,
    (RIGHT, pg.K_UP): UP,
    (LEFT, pg.K_DOWN): DOWN,
    (RIGHT, pg.K_DOWN): DOWN,
    (UP, pg.K_LEFT): LEFT,
    (DOWN, pg.K_LEFT): LEFT,
    (UP, pg.K_RIGHT): RIGHT,
    (DOWN, pg.K_RIGHT): RIGHT,
}

screen = None


class GameObject:
    """Базовый класс игровых объектов."""

    def __init__(self, body_color=None):
        self.position = (
            SCREEN_WIDTH // 2 // GRID_SIZE * GRID_SIZE,
            SCREEN_HEIGHT // 2 // GRID_SIZE * GRID_SIZE,
        )
        self.body_color = body_color

    def draw_cell(self, position, color, border_color=None):
        """Отрисовывает одну клетку игрового поля."""
        rectangle = pg.Rect(position, (GRID_SIZE, GRID_SIZE))
        pg.draw.rect(screen, color, rectangle)
        if border_color is not None:
            pg.draw.rect(screen, border_color, rectangle, 1)

    def draw(self):
        """Отрисовывает игровой объект."""
        raise NotImplementedError(
            'В дочернем классе нужно переопределить метод draw().'
        )


class Apple(GameObject):
    """Класс яблока."""

    def __init__(self, occupied_positions=None):
        super().__init__(body_color=APPLE_COLOR)
        self.randomize_position(occupied_positions or [])

    def randomize_position(self, occupied_positions=None):
        """Выбирает случайную свободную клетку для яблока."""
        occupied_positions = occupied_positions or []
        free_positions = [
            (x * GRID_SIZE, y * GRID_SIZE)
            for x in range(GRID_WIDTH)
            for y in range(GRID_HEIGHT)
            if (x * GRID_SIZE, y * GRID_SIZE) not in occupied_positions
        ]
        if free_positions:
            self.position = random.choice(free_positions)

    def draw(self):
        """Отрисовывает яблоко."""
        self.draw_cell(self.position, self.body_color, BORDER_COLOR)


class Snake(GameObject):
    """Класс змейки."""

    def __init__(self):
        super().__init__(body_color=SNAKE_COLOR)
        self.reset()

    def update_direction(self):
        """Обновляет направление движения змейки."""
        if self.next_direction is None:
            return

        current_direction = pg.Vector2(self.direction)
        next_direction = pg.Vector2(self.next_direction)

        if next_direction != -current_direction:
            self.direction = next_direction

        self.next_direction = None

    def move(self):
        """Перемещает змейку на одну клетку."""
        head_x, head_y = self.get_head_position()
        direction_x, direction_y = self.direction
        self.position = (
            (head_x + direction_x * GRID_SIZE) % SCREEN_WIDTH,
            (head_y + direction_y * GRID_SIZE) % SCREEN_HEIGHT,
        )
        self.positions.insert(0, self.position)

        if len(self.positions) > self.length:
            self.last = self.positions.pop()
        else:
            self.last = None

    def draw(self):
        """Обновляет изображение головы и хвоста змейки."""
        self.draw_cell(self.position, self.body_color, BORDER_COLOR)
        if self.last is not None:
            self.draw_cell(self.last, BOARD_BACKGROUND_COLOR)

    def get_head_position(self):
        """Возвращает координаты головы змейки."""
        return self.positions[0]

    def reset(self):
        """Сбрасывает змейку в начальное состояние."""
        start_position = (
            SCREEN_WIDTH // 2 // GRID_SIZE * GRID_SIZE,
            SCREEN_HEIGHT // 2 // GRID_SIZE * GRID_SIZE,
        )
        self.position = start_position
        self.length = 1
        self.positions = [start_position]
        self.direction = pg.Vector2(RIGHT)
        self.next_direction = None
        self.last = None


def handle_keys(game_object):
    """Обрабатывает события клавиатуры и закрытия окна."""
    for event in pg.event.get():
        if event.type == pg.QUIT:
            raise SystemExit
        if event.type == pg.KEYDOWN and isinstance(game_object, Snake):
            new_direction = DIRECTION_KEYS.get(
                (game_object.direction, event.key)
            )
            if new_direction is not None:
                game_object.next_direction = new_direction


def main():
    """Запускает основной игровой цикл."""
    global screen

    pg.display.init()
    pg.display.set_caption('Змейка')
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()

    screen.fill(BOARD_BACKGROUND_COLOR)
    snake = Snake()
    apple = Apple(snake.positions)
    snake.draw()
    apple.draw()
    pg.display.update()

    try:
        while True:
            clock.tick(SPEED)
            handle_keys(snake)

            snake.update_direction()
            snake.move()

            if snake.get_head_position() == apple.position:
                snake.length += 1
                apple.randomize_position(snake.positions)
                apple.draw()
            elif snake.get_head_position() in snake.positions[1:]:
                screen.fill(BOARD_BACKGROUND_COLOR)
                snake.reset()
                apple.randomize_position(snake.positions)
                snake.draw()
                apple.draw()
            else:
                snake.draw()

            pg.display.update()
    except SystemExit:
        pass
    finally:
        pg.quit()


if __name__ == '__main__':
    main()
