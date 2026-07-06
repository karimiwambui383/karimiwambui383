#!/usr/bin/env python3
"""
🐍 Snake Game - A classic implementation
Play in your terminal!
"""

import random
import os
from collections import deque
from enum import Enum

class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

class SnakeGame:
    def __init__(self, width=20, height=10):
        self.width = width
        self.height = height
        self.snake = deque([(height // 2, width // 2)])
        self.food = self._generate_food()
        self.direction = Direction.RIGHT
        self.next_direction = Direction.RIGHT
        self.score = 0
        self.game_over = False

    def _generate_food(self):
        """Generate food at a random position not occupied by snake"""
        while True:
            food = (random.randint(0, self.height - 1), random.randint(0, self.width - 1))
            if food not in self.snake:
                return food

    def update(self):
        """Update game state"""
        if self.game_over:
            return

        self.direction = self.next_direction
        head_y, head_x = self.snake[0]
        dy, dx = self.direction.value
        new_head = (head_y + dy, head_x + dx)

        # Check wall collision
        if not (0 <= new_head[0] < self.height and 0 <= new_head[1] < self.width):
            self.game_over = True
            return

        # Check self collision
        if new_head in self.snake:
            self.game_over = True
            return

        self.snake.appendleft(new_head)

        # Check food collision
        if new_head == self.food:
            self.score += 10
            self.food = self._generate_food()
        else:
            self.snake.pop()

    def render(self):
        """Render the game board"""
        os.system('clear' if os.name == 'posix' else 'cls')
        board = [['·' for _ in range(self.width)] for _ in range(self.height)]

        # Draw snake
        for segment in self.snake:
            board[segment[0]][segment[1]] = '●'

        # Draw head
        head = self.snake[0]
        board[head[0]][head[1]] = '◉'

        # Draw food
        board[self.food[0]][self.food[1]] = '◆'

        # Print board
        print("╔" + "═" * self.width + "╗")
        for row in board:
            print("║" + "".join(row) + "║")
        print("╚" + "═" * self.width + "╝")
        print(f"Score: {self.score} | Length: {len(self.snake)}")

def play_demo():
    """Run a demo of the snake game"""
    game = SnakeGame(20, 10)
    print("🐍 Snake Game Demo - Auto Playing (10 moves)")
    
    moves = [
        Direction.RIGHT, Direction.RIGHT,
        Direction.DOWN, Direction.DOWN,
        Direction.LEFT, Direction.LEFT,
        Direction.UP, Direction.UP,
        Direction.RIGHT, Direction.RIGHT
    ]

    for i, direction in enumerate(moves):
        game.next_direction = direction
        game.update()
        game.render()
        print(f"Move {i+1}/10")
        
    if not game.game_over:
        print("✅ Demo completed! Game still going strong!")
    else:
        print("💀 Game Over!")

if __name__ == "__main__":
    play_demo()
