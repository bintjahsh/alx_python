from sqlalchemy import Column, Integer, String
class State(Base):
    """Creation of class State that inherits from Base and links to
    the MySQL table states. State has the following attributes:
        + attribute id that represents a column of an auto-generated,
        unique integer, not null and is a primary key
        + attribute name that represents a column of a string with
        maximum 128 characters and is not null
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)