import pytest
from model import Question


def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct

# NOVOS TESTES
def test_add_multiple_choices():
    q = Question('q')
    q.add_choice('a')
    q.add_choice('b')
    assert len(q.choices) == 2

def test_choice_ids():
    q = Question('q')
    c1 = q.add_choice('a')
    c2 = q.add_choice('b')
    assert c1.id == 1
    assert c2.id == 2

def test_remove_choice_by_id():
    q = Question('q')
    c = q.add_choice('a')
    q.remove_choice_by_id(c.id)
    assert len(q.choices) == 0

def test_remove_all_choices():
    q = Question('q')
    q.add_choice('a')
    q.add_choice('b')
    q.remove_all_choices()
    assert len(q.choices) == 0

def test_set_correct_choice():
    q = Question('q')
    c = q.add_choice('a')
    q.set_correct_choices([c.id])
    assert c.is_correct

def test_select_correct_choice():
    q = Question('q')
    c = q.add_choice('a', is_correct=True)
    selected = q.select_choices([c.id])
    assert selected == [c.id]

def test_select_incorrect_choice():
    q = Question('q')
    c = q.add_choice('a', is_correct=False)
    selected = q.select_choices([c.id])
    assert selected == []

def test_select_too_many_choices_raises():
    q = Question('q', max_selections=1)
    c1 = q.add_choice('a', True)
    c2 = q.add_choice('b', True)
    with pytest.raises(Exception):
        q.select_choices([c1.id, c2.id])

def test_create_choice_invalid_text_empty():
    q = Question('q')
    with pytest.raises(Exception):
        q.add_choice('', False)

def test_create_choice_text_too_long():
    q = Question('q')
    with pytest.raises(Exception):
        q.add_choice('a'*101, False)