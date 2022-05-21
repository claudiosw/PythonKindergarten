from sqlalchemy import Column, String, Integer, ForeignKey
from src.infra.config import Base


class ClassRoomsModel(Base):
    """ ClassRooms Entity """

    __tablename__ = "class_rooms"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    teacher_id = Column(Integer, ForeignKey("persons.id"))

    def __rep__(self):
        return f"ClassRoom [name={self.name}, teacher_id={self.teacher_id}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.name == other.name
            and self.teacher_id == other.teacher_id
        ):
            return True
        return False
