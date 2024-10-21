from byu_pytest_utils import max_score, test_files, this_folder, with_import, ensure_missing

@max_score(5)
@with_import('lab20', 'get_domain')
def test_get_domain(get_domain):
    assert get_domain('https://cs111.byu.edu/lab/lab20/') == 'https://cs111.byu.edu'
    assert get_domain('http://en.wikipedia.org/w/index.php') == 'http://en.wikipedia.org'
    assert get_domain('/lab/lab20/') == ''
    assert get_domain('lab/lab20/') == ''
    assert get_domain('asdf') == ''
    assert get_domain('blah://cs111.byu.edu/lab/lab20/') == ''
    assert get_domain('cs111.byu.edu/lab/lab20/') == ''


@max_score(5)
@with_import('lab20', 'combine_paths')
def test_combine_paths(combine_paths):
    assert combine_paths('https://cs111.byu.edu/lab/lab15/', '/lab/lab20/') == 'https://cs111.byu.edu/lab/lab20/'
    assert combine_paths('https://cs111.byu.edu/hw/hw03/#part-2', '/articles/about/') == 'https://cs111.byu.edu/articles/about/'
    assert combine_paths('http://en.wikipedia.org/w/index.php', '/wiki/Main_Page') == 'http://en.wikipedia.org/wiki/Main_Page'
    assert combine_paths('https://cs111.byu.edu/lab/lab20/', '/lab/lab20/assets/page1.html') == 'https://cs111.byu.edu/lab/lab20/assets/page1.html'


@max_score(5)
@with_import('lab20', 'combine_urls')
def test_combine_urls(combine_urls):
    assert combine_urls('https://cs111.byu.edu/lab/lab15/', '/lab/lab20/') == 'https://cs111.byu.edu/lab/lab20/'
    assert combine_urls('https://cs111.byu.edu/hw/hw03/#part-2', '/articles/about/') == 'https://cs111.byu.edu/articles/about/'
    assert combine_urls('http://en.wikipedia.org/w/index.php', '/wiki/Main_Page') == 'http://en.wikipedia.org/wiki/Main_Page'
    assert combine_urls('https://cs111.byu.edu/lab/lab20/', '/lab/lab20/assets/page1.html') == 'https://cs111.byu.edu/lab/lab20/assets/page1.html'
    assert combine_urls('https://cs111.byu.edu/lab/lab08', 'lab20/assets/page1.html') == 'https://cs111.byu.edu/lab/lab20/assets/page1.html'
    assert combine_urls('https://cs111.byu.edu/lab/lab20/assets/page1.html', 'page2.html') == 'https://cs111.byu.edu/lab/lab20/assets/page2.html'
    assert combine_urls('https://cs111.byu.edu/lab/lab20/', 'https://www.wikipedia.org') == 'https://www.wikipedia.org'


@ensure_missing(this_folder / 'paths.output.txt')
@max_score(5)
@with_import('lab20', 'print_pages')
def test_print_pages(print_pages):
    with open(test_files / 'paths.key.txt') as fin:
        expected = fin.read()

    print_pages('https://cs111.byu.edu/pages/about/',
                ['/lab/lab20/assets/page1.html', 'page2.html', '/lab/lab20/assets/more_pages/page3.html', '/lab/lab20/assets/page4.html'],
                this_folder / 'paths.output.txt')
    with open(this_folder / 'paths.output.txt') as fin:
        observed = fin.read()

    assert observed.strip() == expected.strip()
