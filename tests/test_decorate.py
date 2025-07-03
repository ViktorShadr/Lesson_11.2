import pytest

from src.decorate import formate_txt


# Тестируемая функция
@formate_txt(max_length=4, symbol='!')
def get_text():
    return "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

# Тесты
def test_shortening():
    assert get_text() == "Lore! ipsu! dolo! sit amet! cons! adip! elit!"

def test_no_shortening():
    @formate_txt(max_length=10, symbol='!')
    def get_long_text():
        return "Lorem ipsum dolor sit amet"
    assert get_long_text() == "Lorem ipsum dolor sit amet"

def test_end_symbol():
    @formate_txt(max_length=3, symbol='?')
    def get_questioned_text():
        return "Lorem ipsum dolor"
    assert get_questioned_text() == "Lor? ips? dol?"

def test_different_lengths():
    @formate_txt(max_length=5, symbol='.')
    def get_different_length_text():
        return "Hello beautiful world"
    assert get_different_length_text() == "Hello beaut. world"
