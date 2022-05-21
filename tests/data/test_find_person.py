from faker import Faker
from tests.infra.spy import PersonRepositorySpy
from src.data.find_person.find_person import FindPerson

faker = Faker()


def test_by_id():
    """ Testing by_id method in FindPerson """

    person_repo = PersonRepositorySpy()
    find_person = FindPerson(person_repo)

    attribute = {"id": faker.random_number(digits=2)}
    response = find_person.by_id(person_id=attribute["id"])

    # Testing Input
    assert person_repo.select_person_params["person_id"] == attribute["id"]

    # Testing Outputs
    assert response["Success"] is True
    assert response["Data"]


def test_fail_by_id():
    """ Testing by_id fail method in FindPerson """

    person_repo = PersonRepositorySpy()
    find_person = FindPerson(person_repo)

    attribute = {"id": faker.word()}
    response = find_person.by_id(person_id=attribute["id"])

    # Testing Input
    assert person_repo.select_person_params == {}

    # Testing Outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_name():
    """ Testing by_name method in FindPerson """

    person_repo = PersonRepositorySpy()
    find_person = FindPerson(person_repo)

    attribute = {"name": faker.word()}
    response = find_person.by_name(name=attribute["name"])

    # Testing Input
    assert person_repo.select_person_params["name"] == attribute["name"]

    # Testing Outputs
    assert response["Success"] is True
    assert response["Data"]


def test_fail_by_name():
    """ Testing by_name fail method in FindPerson """

    person_repo = PersonRepositorySpy()
    find_person = FindPerson(person_repo)

    attribute = {"name": faker.random_number(digits=2)}
    response = find_person.by_name(name=attribute["name"])

    # Testing Input
    assert person_repo.select_person_params == {}

    # Testing Outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_id_and_name():
    """ Testing by_id_and_name method in FindPerson """

    person_repo = PersonRepositorySpy()
    find_person = FindPerson(person_repo)

    attribute = {"person_id": faker.random_number(digits=2), "name": faker.word()}

    response = find_person.by_id_and_name(
        person_id=attribute["person_id"], name=attribute["name"]
    )

    # Testing Input
    assert person_repo.select_person_params["person_id"] == attribute["person_id"]
    assert person_repo.select_person_params["name"] == attribute["name"]

    # Testing Outputs
    assert response["Success"] is True
    assert response["Data"]


def test_fail_by_id_and_name():
    """ Testing by_id_and_name fail method in FindPerson """

    person_repo = PersonRepositorySpy()
    find_person = FindPerson(person_repo)

    attribute = {
        "person_id": faker.random_number(digits=2),
        "name": faker.random_number(digits=2),
    }

    response = find_person.by_id_and_name(
        person_id=attribute["person_id"], name=attribute["name"]
    )

    # Testing Input
    assert person_repo.select_person_params == {}

    # Testing Outputs
    assert response["Success"] is False
    assert response["Data"] is None
