from faker import Faker
from tests.infra.spy import ClassRoomRepositorySpy, PersonRepositorySpy
from tests.data.spy import FindPersonSpy
from src.data.register_classroom import RegisterClassRoom


faker = Faker()


def test_register():
    """ Testing registry method """

    classroom_repo = ClassRoomRepositorySpy()
    find_person = FindPersonSpy(PersonRepositorySpy())
    register_classroom = RegisterClassRoom(classroom_repo, find_person)

    attributes = {
        "name": faker.name(),
        "teacher_information": {
            "id": faker.random_number(digits=5),
            "name": faker.name(),
        },
    }

    response = register_classroom.register(
        name=attributes["name"],
        teacher_information=attributes["teacher_information"],
    )

    # Testing inputs
    assert classroom_repo.insert_classroom_params["name"] == attributes["name"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]

    # Testing Inputs
    assert classroom_repo.insert_classroom_params["name"] == attributes["name"]

    # Testing FindPerson Inputs
    assert (
        find_person.by_id_and_name_param["id"]
        == attributes["teacher_information"]["id"]
    )
    assert (
        find_person.by_id_and_name_param["name"]
        == attributes["teacher_information"]["name"]
    )
