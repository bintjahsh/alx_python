from sqlalchemy import Column, Integer, String
class State():
    """Creation of class State that inherits from Base and links to
    the MySQL table states. State has the following attributes:
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)