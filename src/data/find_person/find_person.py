from typing import Type, Dict, List
from src.domain.use_cases import FindPersonInterface
from src.data.interfaces import PersonRepositoryInterface
from src.domain.models import Persons


class FindPerson(FindPersonInterface):
    """ Class to define use case Find Person """

    def __init__(self, person_repository: Type[PersonRepositoryInterface]):
        self.person_repository = person_repository

    def by_id(self, person_id: int) -> Dict[bool, List[Persons]]:
        """Select Person By id
        :param - person_id: id of the person
        :param - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(person_id, int)

        if validate_entry:
            response = self.person_repository.select_person(person_id=person_id)

        return {"Success": validate_entry, "Data": response}

    def by_name(self, name: str) -> Dict[bool, List[Persons]]:
        """Select Person By name
        :param - name: name of the person
        :param - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(name, str)

        if validate_entry:
            response = self.person_repository.select_person(name=name)

        return {"Success": validate_entry, "Data": response}

    def by_id_and_name(self, person_id: int, name: str) -> Dict[bool, List[Persons]]:
        """Select Person By id and name
        :param - person_id: id of the person
               - name: name of the person
        :param - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(name, str) and isinstance(person_id, int)

        if validate_entry:
            response = self.person_repository.select_person(person_id=person_id, name=name)

        return {"Success": validate_entry, "Data": response}
