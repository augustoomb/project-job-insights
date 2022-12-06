from src.insights.jobs import read

# from jobs import read
from typing import Union, List, Dict


def get_max_salary(path: str) -> int:
    data = read(path)

    set_salary = set()

    for item_data in data:
        if item_data["max_salary"].isnumeric():
            set_salary.add(int(item_data["max_salary"]))

    return max(set_salary)

    # raise NotImplementedError


def get_min_salary(path: str) -> int:
    data = read(path)

    set_salary = set()

    for item_data in data:
        if item_data["min_salary"].isnumeric():
            set_salary.add(int(item_data["min_salary"]))

    return min(set_salary)

    # raise NotImplementedError


def check_if_is_number(value):
    if type(value) == int or type(value) == float:
        return True
    if type(value) == str:
        return value.isnumeric()


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if ("min_salary" not in job) or ("max_salary" not in job):
        raise ValueError("chaves min_salary e max_salary devem ser informadas")

    if not check_if_is_number(salary):
        raise ValueError("salary deve ser número")

    if (not check_if_is_number(job["min_salary"])) or (
        not check_if_is_number(job["max_salary"])
    ):
        raise ValueError("min_salary e max_salary devem ser números")

    if job["min_salary"] > job["max_salary"]:
        raise ValueError("min_salary deve ser menor que max_salary")

    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])

    raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError


# def main():
#     print(matches_salary_range({"max_salary": 1500, "min_salary": 0}, "5"))


# main()
