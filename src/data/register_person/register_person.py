from typing import Type, Dict
from src.domain.use_cases import RegisterPersonInterface
from src.data.interfaces import PersonRepositoryInterface as PersonRepository
from src.domain.models import Persons


class RegisterPerson(RegisterPersonInterface):
    """ Class to define personcase: Register Person """

    def __init__(self, person_repository: Type[PersonRepository]):
        self.person_repository = person_repository

    def register(self, name: str) -> Dict[bool, Persons]:
        """Register person use case
        :param - name: person name
        :return - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(name, str)

        if validate_entry:
            response = self.person_repository.insert_person(name)

        return {"Success": validate_entry, "Data": response}
