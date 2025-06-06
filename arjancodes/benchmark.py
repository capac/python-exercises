import time
from typing import TypedDict


class User(TypedDict):
    name: str
    age: int


def main() -> None:
    users: list[User] = [
        {"name": "User" + str(i), "age": i % 50}
        for i in range(10_000_000)  # increase size
    ]

    # for loop
    start = time.perf_counter()
    adult_names: list[str] = []
    for user in users:
        if user["age"] >= 18:
            adult_names.append(user["name"].upper())
    end = time.perf_counter()
    print("For loop:", end - start)

    # map/filter
    start = time.perf_counter()
    adult_users = filter(lambda u: u["age"] >= 18, users)
    adult_names = list(map(lambda u: u["name"].upper(), adult_users))
    end = time.perf_counter()
    print("Map/filter:", end - start)

    # list comprehension
    start = time.perf_counter()
    adult_names = [u["name"].upper() for u in users if u["age"] >= 18]
    end = time.perf_counter()
    print("List comprehension:", end - start)


if __name__ == "__main__":
    main()
