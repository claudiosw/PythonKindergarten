from typing import Type, Dict
from src.domain.use_cases import RegisterClassRoomInterface
from src.data.interfaces import ClassRoomRepositoryInterface
from src.domain.models import ClassRooms
from src.data.find_person import FindPerson


class RegisterClassRoom(RegisterClassRoomInterface):
    """ Class to define classroomcase: Register ClassRoom """

    def __init__(self, classroom_repository: Type[ClassRoomRepositoryInterface], find_person: Type[FindPerson]):
        self.classroom_repository = classroom_repository
        self.find_person = find_person

    def register(self, name: str, teacher_information: Dict[int, str]) -> Dict[bool, ClassRooms]:
        """Register classroom use case
        :param  - name: classroom name
                - teacher_information: Dictionaty with id and/or name
        :return - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(name, str)
        teacher = self.find_person.by_person_information(teacher_information)
        if validate_entry:
            response = self.classroom_repository.insert_classroom(name, teacher["Data"][0].id)

        return {"Success": validate_entry, "Data": response}
