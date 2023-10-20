""" 
    In this assignment, you will be creating a Linguist application that aims to facilitate the language learning process. 
    The application will allow users to create decks of flashcards, 
    each containing a word in English and its translation in Ukrainian, along with a tip to help them remember it.

    You will create three models: User, Deck, and Card, along with functions to support basic CRUD (Create, Read, Update, Delete) functionality.

    MODELS
    USER
        id (integer)
        name (string)
        email (string)
        password (string)
    DECK
        id (integer)
        name (string)
        user_id (integer)
    CARD
        id (integer)
        user_id (integer)
        word (string, English)
        translation (string, Ukrainian)
        tip (string)
    FUNCTIONS
    USER
        user_create(name, email, password) -> User: Creates a new user and returns the User object.
        user_get_by_id(user_id) -> User: Retrieves a user by their ID and returns the User object.
        user_update_name(user_id, name) -> User: Updates the name of a user and returns the User object.
        user_change_password(user_id, old_password, new_password) -> bool: Changes the password of a user and returns a Boolean value indicating success or failure.
        user_delete_by_id(user_id) -> bool: Deletes a user by their ID and returns a Boolean value indicating success or failure.
    DECK
        deck_create(name, user_id) -> Deck: Creates a new deck belonging to a user and returns the Deck object.
        deck_get_by_id(deck_id) -> Deck: Retrieves a deck by its ID and returns the Deck object.
        deck_update(deck_id, name) -> Deck: Updates the name of a deck and returns the Deck object.
        deck_delete_by_id(deck_id) -> bool: Deletes a deck by its ID and returns a Boolean value indicating success or failure.
    CARD
        card_create(user_id, word, translation, tip) -> Card: Creates a new flashcard and returns the Card object.
        card_get_by_id(card_id) -> Card: Retrieves a flashcard by its ID and returns the Card object.
        card_filter(sub_word) -> tuple[Card]: Retrieves all flashcards containing a substring in either the word, translation, or tip fields and returns a tuple of Card objects.
        card_update(card_id, word=None, translation=None, tip=None) -> Card: Updates the fields of a flashcard and returns the Card object.
        card_delete_by_id(card_id) -> bool: Deletes a flashcard by its ID and returns a Boolean value indicating success or failure.
    INSTRUCTIONS
    Set up a new Python project and create a file named linguist.py.
    Define the User, Deck, and Card models with the appropriate fields.
    Implement each of the functions listed in the Functions section of this assignment. Use Python docstrings to document each function.
"""
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, update
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import mapper, relationship, sessionmaker, declarative_base, Session
from sqlalchemy.ext.automap import automap_base

engine = create_engine('sqlite:///linguist.db', echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, nullable=False)
    email = Column('email', String, nullable=False, unique=True)
    password = Column('password', String, nullable=False)
    
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
    def __repr__(self) -> str:
        return f'User({self.id}, {self.name}, {self.email}, {self.password})'
    
    def __str__(self) -> str:
        return f'User name: {self.name}, email: {self.email})'

class Deck(Base):
    __tablename__ = 'decks'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, nullable=False)
    user_id = Column('user_id', Integer, ForeignKey('users.id'))
    
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
    
    def __repr__(self) -> str:
        return f'Deck({self.id}, {self.name}, {self.user_id})'
    
class Card(Base):
    __tablename__ = 'cards'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    user_id = Column('user_id', Integer, ForeignKey('users.id'))
    word = Column('word', String, nullable=False)
    translation = Column('translation', String, nullable=False)
    tip = Column('tip', String)
    
    def __init__(self, user_id, word, translation, tip):
        self.user_id = user_id
        self.word = word
        self.translation = translation
        self.tip = tip
    
    def __repr__(self) -> str:
        return f'Card({self.id}, {self.user_id}, {self.word}, {self.translation}, {self.tip})'
    
    
Base.metadata.create_all(engine)
session = Session()

def user_create(name, email, password) -> User:
    """
        Creates new user, 
        saves user information to database,
        returns User object.
    """
    user = User(name, email, password)
    session.add(user)
    session.commit()
    return user

def user_get_by_id(user_id) -> User:
    """
        Retrieves a user by their ID and returns the User object.    
    """
    return session.query(User).filter(User.id == user_id).first()
    #return session.query(User).get(user_id)

def user_update_name(user_id, name) -> User:
    """
        Updates the name of a user and returns the User object.
    """
    user = session.query(User).filter(User.id == user_id).first()
    user.name = name
    session.commit()
    return user

def user_change_password(user_id, old_password, new_password) -> bool:
    """
        Changes the password of a user and returns a Boolean value indicating success or failure.
    """
    user = session.query(User).filter(User.id == user_id).first()
    if user.password == old_password:
        user.password = new_password
        session.commit()
        return True
    return False


def user_delete_by_id(user_id) -> bool:
    """
        Deletes a user by their ID and returns a Boolean value indicating success or failure.
    """
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        session.delete(user)
        session.commit()
        return True
    return False

def deck_create(name, user_id) -> Deck:
    """
        Creates a new deck belonging to a user and returns the Deck object.
    """
    deck = Deck(name, user_id)
    session.add(deck)
    session.commit()
    return deck

def deck_get_by_id(deck_id: int) -> Deck:
    """
        Retrieves a deck by its ID and returns the Deck object.
    """
    return session.query(Deck).filter(Deck.id == deck_id).first()

def deck_update(deck_id, name) -> Deck:
    """
        Updates the name of a deck and returns the Deck object.
    """
    deck = session.query(Deck).filter(Deck.id == deck_id).first()
    deck.name = name
    session.commit()
    return deck

def deck_delete_by_id(deck_id) -> bool:
    """
        Deletes a deck by its ID and returns a Boolean value indicating success or failure.
    """
    deck = session.query(Deck).filter(Deck.id == deck_id).first()
    if deck:
        session.delete(deck)
        session.commit()
        return True
    return False

def card_create(user_id, word, translation, tip) -> Card:
    """
        Creates a new flashcard belonging to a user and returns the Card object.
    """
    card = Card(user_id, word, translation, tip)
    session.add(card)
    session.commit()
    return card

def card_get_by_id(card_id) -> Card:
    """
        Retrieves a flashcard by its ID and returns the Card object.
    """
    return session.query(Card).filter(Card.id == card_id).first()

def card_update(card_id, word, translation, tip) -> Card:
    """
        Updates the word, translation, and tip for a flashcard and returns the Card object.
    """
    card = session.query(Card).filter(Card.id == card_id).first()
    card.word = word
    card.translation = translation
    card.tip = tip
    session.commit()
    return card

def card_delete_by_id(card_id) -> bool:
    """
        Deletes a flashcard by its ID and returns a Boolean value indicating success or failure.
    """
    card = session.query(Card).filter(Card.id == card_id).first()
    if card:
        session.delete(card)
        session.commit()
        return True
    return False

def card_filter(sub_word) -> tuple[Card]:
    """
        Retrieves all flashcards containing a substring in either the word, translation, or tip fields 
        and returns a tuple of Card objects.
    """
    cards = session.query(Card).where(Card.word.like(f'%{sub_word}%') | Card.translation.like(f'%{sub_word}%') | Card.tip.like(f'%{sub_word}%')).all()
    return tuple(cards)

def main():
    """
        Test your functions by creating users, decks, and cards.
        Performs various CRUD operations. 
        Use Python's assert statement to verify that the expected values are returned by each function.
        Make any necessary revisions to your implementation based on the results of your testing.    
    """
    user_1 = user_create('user_1', 'andy.dorokhin@gmail.com', '123')
    user_2 = user_create('user_2', 'user_2@gmail.com', '456')
    user_3 = user_create('user_3', 'user_3@gmail.com', '789')
    for user in session.query(User).all():
        print(user)
        print(user.__repr__())
        
    assert isinstance(user_update_name(1, 'Andy Dorokhin'), User)
    assert user_change_password(1, '123', '$eKKreT123')
    print(user_get_by_id(1))
    
    assert user_change_password(2, '123', '$eKKreT123') == False
    assert user_delete_by_id(3)
    for user in session.query(User).all():
        print(user.__repr__())

    
    deck_1 = deck_create('deck_1', 1)
    deck_2 = deck_create('deck_2', 1)
    deck_3 = deck_create('deck_3', 2)
    for deck in session.query(Deck).all():
        print(deck.__repr__())

    assert isinstance(deck_update(1, 'First Deck'), Deck)
    assert deck_delete_by_id(3)
    for deck in session.query(Deck).all():
        print(deck.__repr__())

    
    card_1 = card_create(1, 'word_1', 'translation_1', 'tip_1')
    card_2 = card_create(1, 'word_2', 'translation_2', 'tip_2')
    card_3 = card_create(2, 'word_3', 'translation_3', 'top_3')
    card_3 = card_create(2, 'word_4', 'translation_4', 'top_4')
    for card in session.query(Card).all():
        print(card.__repr__())
    
    assert isinstance(card_update(1, 'Ukraine', 'Україна', 'tip_1'), Card)
    assert card_delete_by_id(4)
    for card in card_filter('tip'):
        print(card.__repr__())
    
    session.close()
    
if __name__ == '__main__':
    main()
    