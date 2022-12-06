from src.pre_built.sorting import sort_by

job1 = {"min_salary": 1000, "max_salary": 2000, "date_posted": "2019-01-01"}
job2 = {"min_salary": 2000, "max_salary": 3000, "date_posted": "2019-01-02"}
job3 = {"min_salary": 3000, "max_salary": 4000, "date_posted": "2019-01-03"}
job4 = {"min_salary": 5000, "max_salary": "", "date_posted": "2019-01-05"}
job5 = {"min_salary": 6000, "max_salary": 5000, "date_posted": ""}
job6 = {"min_salary": "", "max_salary": 6000, "date_posted": "2019-01-04"}

job_mock_min = [job1, job2, job3, job4, job5, job6]
job_mock_max = [job1, job2, job3, job4, job5, job6]
job_mock_date = [job1, job2, job3, job4, job5, job6]


def test_sort_by_criteria():
    sort_by(job_mock_min, "min_salary")
    assert job_mock_min == [job1, job2, job3, job4, job5, job6]
    sort_by(job_mock_max, "max_salary")
    assert job_mock_max == [job6, job5, job3, job2, job1, job4]
    sort_by(job_mock_date, "date_posted")
    assert job_mock_date == [job4, job6, job3, job2, job1, job5]
