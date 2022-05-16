
from faker import Faker
from src.domain.models import Persons

faker = Faker()


def mock_persons() -> Persons:
    """ Mocking Persons """

    return Persons(
        id=faker.random_number(digits=5), name=faker.name()
    )
