import csv
from functools import lru_cache
from typing import List, Dict

# requisito 1
# https://courses.cs.washington.edu/courses/cse140/13wi/csv-parsing.html


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8") as file:
        content = csv.DictReader(file, delimiter=",", quotechar='"')

        list_dict = []

        for item in content:
            list_dict.append(item)

        return list_dict

    raise NotImplementedError


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError


# def main():
#     # requisito 1: utilização:
#     print(read("../../tests/mocks/jobs.csv"))


# main()
