# tests/test_all.py

import pytest
from python_exercises import (
    find_duplicates,
    difference_set,
    square_tuple,
    merge_dicts,
    ToDo,
    flatten_list_once
)

# List Exercise
def test_find_duplicates():
    assert set(find_duplicates([1,2,2,3,4,4,5])) == {2,4}
    assert find_duplicates([1,2,3]) == []

# Set Exercise
def test_difference_set():
    assert difference_set({1,2,3},{2,3,4}) == {1}
    assert difference_set({1},{1}) == set()

# Tuple Exercise
def test_square_tuple():
    assert square_tuple((1,2,3)) == (1,4,9)
    assert square_tuple(()) == ()

# Dictionary Exercise
def test_merge_dicts():
    d1 = {'a':1,'b':2}
    d2 = {'b':3,'c':4}
    assert merge_dicts(d1,d2) == {'a':1,'b':5,'c':4}

# OOP Exercise
def test_todo_class():
    todo = ToDo()
    todo.add_task("task1")
    todo.add_task("task2")
    assert todo.list_tasks() == ["task1","task2"]
    todo.remove_task("task1")
    assert todo.list_tasks() == ["task2"]

# Flatten list exercise
def test_flatten_list_once():
    assert flatten_list_once([[1,2],[3,4],5]) == [1,2,3,4,5]
    assert flatten_list_once([]) == []