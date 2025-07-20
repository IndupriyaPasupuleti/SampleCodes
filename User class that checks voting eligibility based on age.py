class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def can_vote(self):
        return self.age >= 18


# Test cases using pytest
def test_can_vote_true():
    user = User("Praveen", 25)
    assert user.can_vote() is True

def test_can_vote_false():
    user = User("Child", 15)
    assert user.can_vote() is False
