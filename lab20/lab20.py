import requests
import re
from urllib import parse, robotparser
# Used for determining which parts of a website you are permitted to access and not (robots.txt).


def get_domain(url):
    """
    Note: You may need to use some string manipulation in addition to urllib to acheive this functionality.
    :param url: a url
    :return: the full domain of the url (preceded by the scheme), or an empty string if there is no full domain
    in the url or if the scheme of the url is not valid (we'll consider http and https valid)
    >>> get_domain('https://cs111.byu.edu/lab/lab20/')
    'https://cs111.byu.edu'
    >>> get_domain('http://en.wikipedia.org/w/index.php')
    'http://en.wikipedia.org'
    >>> get_domain('proj/proj4/')  # returns an empty string
    ''
    """
    parsed = parse.urlparse(url)
    if parsed.scheme not in ['https', 'http'] or parsed.netloc == '':
        return ''
    return f'{parsed.scheme}://{parsed.netloc}'


def combine_paths(url, path):
    """
    You can expect that your function will only be given valid URLs and paths.
    :param url: url
    :param path: path to another page on the same website
    :return: the full url to the other page
    >>> combine_paths('https://cs111.byu.edu/lab/lab15/', '/lab/lab20/')
    'https://cs111.byu.edu/lab/lab20/'
    >>> combine_paths('https://cs111.byu.edu/hw/hw03/#part-2', '/articles/about/')
    'https://cs111.byu.edu/articles/about/'
    """
    return f'{get_domain(url)}{path}'


def combine_urls(base_url, url_to_join):
    """
    :return: the full URL of the webpage pointed to by the url to join
    >>> combine_urls('https://cs111.byu.edu/lab/lab15/', '/lab/lab20/')
    'https://cs111.byu.edu/lab/lab20/'
    >>> combine_urls('https://cs111.byu.edu/lab/lab08', 'lab20/')
    'https://cs111.byu.edu/lab/lab20/'
    >>> combine_urls('https://cs111.byu.edu/hw/hw05/', 'https://www.wikipedia.org')
    'https://www.wikipedia.org'
    >>> combine_urls('https://cs111.byu.edu/lab/lab20/assets/page1.html', 'page2.html')
    'https://cs111.byu.edu/lab/lab20/assets/page2.html'
    """
    p_base = parse.urlparse(base_url)
    p_join = parse.urlparse(url_to_join)
    if p_join.netloc == '':
        if url_to_join.startswith('/'):  # path
            return combine_paths(base_url, url_to_join)
        else:  # page
            if p_base.path == '':
                path = '/' + url_to_join
            else:
                path = re.findall(r'/.*/', p_base.path)[0] + url_to_join
            return combine_paths(base_url, path)
    elif p_base.netloc != p_join.netloc:  # different domain
        return url_to_join


def print_pages(url, paths, outfile):
    """
    visit each of those paths and pages and write the contents of ALL of the
    pages to the same output file. The start of each page should be written on
    its own line. Each new page/path should be combined with the full url of
    the previous page visited (e.g. the first path/page will need to be combined
    with the url that is passed into the function, and the second path/page will
    need to be combined with the full url of the first page, etc.)
    :param url: an url
    :param paths: a list of paths and pages
    :param outfile: an output file name
    :return:
    """
    with open(outfile, 'w') as outfile:
        link = combine_urls(url, paths[0])
        for path in paths:
            link = combine_urls(link, path)
            content = requests.get(link, stream=True).text
            outfile.writelines(content)
            outfile.writelines('\n')


def main():
    """
    Parts of a url
    scheme : Very beginning part, right before the www. Almost always https or http.
    netloc : Classic domain (e.g. cs111.byu.edu or www.google.com).
    path : Everything that comes after the domain. (eg /lab/lab20) Note that this path could also
        end in a file format such as /lectures/Stephens/Lecture30-Hyperlinks.pptx. In this case, your
        browser will often prompt you to download the file rather than redirect to a new webpage.
    query : Sometimes on websites some information about will be stored in the url using a ?. For
        example, on youtube if you click on a video, you will notice the url ends in /watch?v=<some
        characters>. We won't use url queries in this class, but they are what follows that ?.
    fragment : A fragment is the #<header name> part that is sometimes added to the end of a URL. It
        stores your location within a single webpage. Try clicking one of the links on the left side
        of this webpage, and you'll see the associated fragment added to your url.
    """
    # print(get_domain('https://cs111.byu.edu/lab/lab20/'))
    # print(get_domain('http://en.wikipedia.org/w/index.php'))
    # print(get_domain('proj/proj4/'))
    # print(combine_paths('https://cs111.byu.edu/lab/lab15/', '/lab/lab20/'))
    # print(combine_paths('https://cs111.byu.edu/hw/hw03/#part-2', '/articles/about/'))
    # print(combine_urls('https://cs111.byu.edu/lab/lab20/assets/page1.html', 'page2.html'))
    print_pages('https://cs111.byu.edu', ['/lab/lab20/assets/page1.html', 'page2.html'],
                'pages1.output.txt')  # no print output because you are just writing to the output file
    print_pages('https://cs111.byu.edu/proj/proj4/', ['/lab/lab20/assets/page1.html', 'page2.html'],
                'pages2.output.txt')


if __name__ == "__main__":
    main()

# run pytest with: python3 -m pytest -vv .
# doctests: python3 -m doctest lab01.py
