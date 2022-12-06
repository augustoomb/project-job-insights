from src.insights.jobs import read
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


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
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
