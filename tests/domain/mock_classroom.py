
from faker import Faker
from src.domain.models import ClassRooms

faker = Faker()


def mock_classrooms() -> ClassRooms:
    """ Mocking ClassRooms """

    return ClassRooms(
        id=faker.random_number(digits=5),
        name=faker.name(),
        teacher_id=faker.random_number(digits=5),
    )
