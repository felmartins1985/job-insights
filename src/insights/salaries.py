from typing import Union, List, Dict
from .jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    jobs = read(path)
    set_jobs = set()
    for job in jobs:
        if job["max_salary"] != "" and job["max_salary"].isdigit():
            set_jobs.add(int(job["max_salary"]))
    list_jobs = list(set_jobs)
    max_salary = max(list_jobs)
    return max_salary


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    jobs = read(path)
    set_jobs = set()
    for job in jobs:
        if job["min_salary"] != "" and job["min_salary"].isdigit():
            set_jobs.add(int(job["min_salary"]))
    list_jobs = list(set_jobs)
    min_salary = min(list_jobs)
    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("Job doesn't have min_salary or max_salary")
    if (
        not str(job["min_salary"]).isdigit()
        or not str(job["max_salary"]).isdigit()
    ):
        raise ValueError("Job min_salary or max_salary isn't a valid integer")
    if int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError("Job min_salary is greather than max_salary")
    if not str(salary).lstrip("-").isdigit():
        raise ValueError("Salary isn't a valid integer")
    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    list_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list_jobs.append(job)
        except ValueError as error:
            print(error)
    return list_jobs
