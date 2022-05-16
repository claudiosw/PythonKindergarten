from faker import Faker
from tests.infra.spy import PersonRepositorySpy
from src.data.register_person import RegisterPerson

faker = Faker()


def test_register():
    """ Testing registry method """

    person_repo = PersonRepositorySpy()
    register_person = RegisterPerson(person_repo)

    attributes = {"name": faker.name()}

    response = register_person.register(
        name=attributes["name"]
    )

    # Testing inputs
    assert person_repo.insert_person_params["name"] == attributes["name"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_fail():
    """ Testing registry method in fail """

    person_repo = PersonRepositorySpy()
    register_person = RegisterPerson(person_repo)

    attributes = {"name": faker.random_number(digits=2)}

    response = register_person.register(
        name=attributes["name"]
    )

    print(response)

    # Testing inputs
    assert person_repo.insert_person_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
