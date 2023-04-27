import pygame
import pytest
from project import Bird, Ground, Pipe, SCREEN_HEIGHT, SCREEN_WIDHT,get_random_pipes

# Test if Bird class initializes correctly
def test_bird_initialization():
    bird = Bird()
    assert bird.rect.x == round((SCREEN_WIDHT / 6)-1)
    assert bird.rect.y == SCREEN_HEIGHT / 2

# Test if Bird bump function works
def test_bird_bump():
    bird = Bird()
    initial_speed = bird.speed
    bird.bump()
    assert bird.speed == -initial_speed

# Test if Ground class initializes correctly
def test_ground_initialization():
    ground = Ground(0)
    assert ground.rect.x == 0
    assert ground.rect.y == SCREEN_HEIGHT - ground.rect[3]

# Test if Pipe class initializes correctly
def test_pipe_initialization():
    pipe = Pipe(False, SCREEN_WIDHT, 300)
    assert pipe.rect.x == SCREEN_WIDHT
    assert pipe.rect.y == SCREEN_HEIGHT - 300

# Test if get_random_pipes function returns two Pipe instances
def test_get_random_pipes():
    pipes = get_random_pipes(SCREEN_WIDHT)
    assert isinstance(pipes[0], Pipe)
    assert isinstance(pipes[1], Pipe)
