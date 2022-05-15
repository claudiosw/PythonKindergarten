from sqlalchemy import Column, String, Integer
from src.infra.config import Base


class PersonsModel(Base):
    """ Persons Entity """

    __tablename__ = "persons"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return f"Person [name={self.name}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.name == other.name
        ):
            return True
        return False
