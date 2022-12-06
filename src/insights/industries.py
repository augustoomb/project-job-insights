from src.insights.jobs import read
from typing import List, Dict


def get_unique_industries(path: str) -> List[str]:
    data = read(path)

    set_industry = set()
    list_industry = []

    # salvar para um conjunto(set), pois ele ignora dados repetidos:
    for item_data in data:
        set_industry.add(item_data["industry"])

    # movendo do set para uma lista conforme solicitado
    for item_industry in set_industry:
        if item_industry != "":
            list_industry.append(item_industry)

    return list_industry

    # raise NotImplementedError


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError


# def main():
#     # requisito 3: utilização
#     print(get_unique_industries("../../tests/mocks/jobs_with_industries.csv"))


# main()
