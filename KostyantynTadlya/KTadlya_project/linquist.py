from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, update
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import mapper, relationship, sessionmaker, declarative_base, Session
from sqlalchemy.ext.automap import automap_base

Base = declarative_base()
#Base = automap_base()
engine = create_engine(r'sqlite+pysqlite:///D:\Флешк\Ольчик\КурcSoftServe\SQLalchem\venw1\sqliteDB1.db', echo=False)

class User(Base):
    __tablename__='user'

    u_id = Column('id', Integer, primary_key=True)
    name = Column('name', String, nullable=False)
    email = Column('email', String, unique=True)
    password = Column('password', String)

    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self) -> str:
        return f'{self.u_id} {self.name} {self.email} {self.password}'
    
class Deck(Base):
    __tablename__='deck'
    d_id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    user_id = Column('user_id', ForeignKey('user.id'))

    def __init__(self, name, user_id) -> None:
        self.name = name
        self.user_id = user_id
    def __repr__(self) -> str:
        return f'{self.d_id} {self.name} {self.user_id}'

class Card(Base):
    __tablename__='cards'
    c_id = Column("id", Integer, primary_key=True)
    user_id = Column("user_id", ForeignKey("user.id"))
    word = Column("word", String)
    translation = Column("translation", String)
    tip = Column("tip", String)

    def __init__(self, user_id, word, translation, tip) -> None:
        self.user_id = user_id
        self.word = word
        self.translation = translation
        self.tip = tip
    def __repr__(self) -> str:
        return f'{self.c_id} {self.word} {self.translation} {self.tip}'

#Base.prepare(autoload_with=engine)
# User = Base.classes.user
# Deck = Base.classes.deck
# Card = Base.classes.cards
Session = sessionmaker(bind=engine)
dbsession = Session()

def add_rows(session: Session, row: Base):
    """
    Function that add rows to the tables
    """
    session.add(row)
    session.commit()

def user_create(name: str, email: str, password: str) -> User:
    """
    Function user_create creates new user in SQLiteDB
    """
    new_user = User(name, email, password)
    add_rows(dbsession, new_user)
    return new_user
def user_get_by_id(user_id: int) -> User:
    """
    Function finds a user by their ID
    """
    return dbsession.get(User, user_id)
def user_update_name(user_id: int, name: str) -> User:
    """
    Function updates the name of a user
    """
    row = user_get_by_id(user_id)
    row.name = name
    dbsession.commit()
    return row
def user_change_password(user_id: int, old_password: str, new_password: str) -> bool:
    """
    Changes the password of a user 
    """
    row = user_get_by_id(user_id)
    if old_password == row.password:
        row.password = new_password
        dbsession.commit() 
    else: return False
    return True
def user_delete_by_id(user_id: int) -> bool:
    """
    Deletes a user by their ID 
    """ 
    try:
        row = user_get_by_id(user_id)
        dbsession.delete(row)
        dbsession.commit()
    except:
        return False
    return True  


def deck_create(name: str, user_id: int) -> Deck:
    """
    Function creating a new deck 
    """     
    new_deck = Deck(name, user_id)
    add_rows(dbsession, new_deck)
    return new_deck
def deck_get_by_id(deck_id: int) -> Deck:
    """
    Function Retrieves a deck by its ID
    """
    return dbsession.get(Deck, deck_id)   
def deck_update(deck_id: int, name: str) -> Deck:
    """
    Function updates the name of a deck
    """
    row = deck_get_by_id(deck_id)
    row.name = name
    dbsession.commit()
    return row
def deck_delete_by_id(deck_id: int) -> bool:
    """
    Function deleting a deck by its ID
    """
    try:
        row = deck_get_by_id(deck_id)
        dbsession.delete(row)
        dbsession.commit()
    except:
        return False
    return True 
def card_create(user_id: int, word: str, translation: str, tip: str) -> Card:
    """
    Function creates a new flashcard
    """
    new_card = Card(user_id, word, translation, tip)
    add_rows(dbsession, new_card)
    return new_card
def card_get_by_id(card_id: int) -> Card:
    """
    Function retrieves a flashcard by its ID
    """
    return dbsession.get(Card, card_id)
def card_filter(sub_word) -> tuple[Card]:
    """
    Function retrieves all flashcards containing a substring in either the word, translation, or tip fields
    """
    r = tuple(dbsession.query(Card).where(Card.word == sub_word or 
                                          Card.translation == sub_word or 
                                          Card.tip == sub_word))
    return r
def card_update(card_id, word=None, translation=None, tip=None) -> Card:
    """
    Function updates the fields of a flashcard
    """
    row = card_get_by_id(card_id)
    row.word = word
    row.translation = translation
    row.tip = tip
    dbsession.commit()
    return row
def card_delete_by_id(card_id) -> bool:
    """
    Function deletes a flashcard by its ID
    """
    try:
        row = card_get_by_id(card_id)
        dbsession.delete(row)
        dbsession.commit()
    except:
        return False
    return True  


# l = user_get_by_id(2)
# print('ffff', type(l))
#user_change_password(3, "qwerty", "qwerty111")
# deck_create('один', 1)
# deck_create('два', 1)
# deck_create('один', 2)
# deck_create('два', 2)
# deck_create('один', 3)
# deck_create('два', 3)
# card_create(1, "word", "слова", "Some tip")
# card_create(1, "card", "картка", "Some tip")
# card_create(2, "one", "один", "Some tip")
# card_create(2, "two", "два", "Some tip")
# card_create(2, "three", "три", "Some tip")
# card_create(3, "four", "чотири", "Some tip")
# card_create(3, "five", "пять", "Some tip")
# card_create(3, "six", "шість", "Some tip")

            
assert isinstance(user_create("Sergiyko", "sergiyko22@gmail.com", "qwerty22"), User)
assert isinstance(user_get_by_id(2), User)
assert not user_change_password(1, "old_password", "new_password")
assert user_delete_by_id(4)

assert isinstance(deck_create('три', 1), Deck)
assert isinstance(deck_get_by_id(7), Deck)
assert isinstance(deck_update(7, 'чотири'), Deck)
assert deck_delete_by_id(7)

assert card_create(3, "seven", "сім", "Some tip"), Card
assert isinstance(card_get_by_id(8), Card)
assert isinstance(card_update(1), Card)
assert isinstance(card_filter('six'), tuple)
assert card_delete_by_id(9)

results = dbsession.query(User).all()
print(results)

results = dbsession.query(Deck).all()
print(results)

results = dbsession.query(Card).all()
print(results)

