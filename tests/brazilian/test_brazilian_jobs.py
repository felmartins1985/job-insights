from src.pre_built.brazilian_jobs import read_brazilian_file

BRAZILIAN_FILE_PATH = "tests/mocks/brazilians_jobs.csv"


def test_brazilian_jobs():
    assert isinstance(read_brazilian_file(BRAZILIAN_FILE_PATH), list)
    assert isinstance(read_brazilian_file(BRAZILIAN_FILE_PATH)[0], dict)
    assert len(read_brazilian_file(BRAZILIAN_FILE_PATH)) == 15
    test_brazilian_jobs_rename_keys()
    test_brazilian_jobs_removed_keys()


def test_brazilian_jobs_rename_keys():
    assert "title" in read_brazilian_file(BRAZILIAN_FILE_PATH)[0]
    assert "salary" in read_brazilian_file(BRAZILIAN_FILE_PATH)[0]
    assert "type" in read_brazilian_file(BRAZILIAN_FILE_PATH)[0]


def test_brazilian_jobs_removed_keys():
    assert "titulo" not in read_brazilian_file(BRAZILIAN_FILE_PATH)[0]
    assert "salario" not in read_brazilian_file(BRAZILIAN_FILE_PATH)[0]
    assert "tipo" not in read_brazilian_file(BRAZILIAN_FILE_PATH)[0]
