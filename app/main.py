class Person:
    people = {}

    def __init__(self, name: str, age: int, **kwargs) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        name = person["name"]
        age = person["age"]
        result.append(Person(name, age))

    for index, person in enumerate(people):
        current_name = Person.people[person["name"]]
        if "wife" in person and person["wife"] is not None:
            current_name.wife = Person.people.get(person["wife"])
        if "husband" in person and person["husband"] is not None:
            current_name.husband = Person.people.get(person["husband"])
    return result
