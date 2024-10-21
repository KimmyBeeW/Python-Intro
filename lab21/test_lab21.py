from byu_pytest_utils import max_score, run_python_script, test_files, this_folder, ensure_missing


@ensure_missing(this_folder / 'sample.output.txt')
@max_score(6)
def test_sample_scavenger_hunt():
    with open(test_files / 'sample.key.png', 'r') as fin:
        expected = fin.read()

    run_python_script('lab21.py', 'https://cs111.cs.byu.edu/lab/lab21/assets/sample1.html',
                      'li', 'checkpoint1', this_folder / 'sample.output.txt')
    with open(this_folder / 'sample.output.txt', 'r') as fin:
        observed = fin.read()

    assert observed == expected


@ensure_missing(this_folder / 'mediumhunt.output.txt')
@max_score(7)
def test_medium_scavenger_hunt():
    with open(test_files / 'mediumhunt.key.png', 'r') as fin:
        expected = fin.read()

    run_python_script('lab21.py', 'https://cs111.cs.byu.edu/lab/lab21/assets/webpage1.html',
                      'p', 'mediumhunt-checkpoint1', this_folder / 'mediumhunt.output.txt')
    with open(this_folder / 'mediumhunt.output.txt', 'r') as fin:
        observed = fin.read()

    assert observed == expected


@ensure_missing(this_folder / 'longhunt.output.txt')
@max_score(7)
def test_long_scavenger_hunt():
    with open(test_files / 'longhunt.key.png', 'r') as fin:
        expected = fin.read()

    run_python_script('lab21.py', 'https://cs111.cs.byu.edu/lab/lab21/assets/webpage4.html',
                      'ul', 'longhunt-checkpoint1', this_folder / 'longhunt.output.txt')
    with open(this_folder / 'longhunt.output.txt', 'r') as fin:
        observed = fin.read()

    assert observed == expected
