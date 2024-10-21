import requests
import bs4


def download(url, output_filename):
    response_object = requests.get(url)
    with open(output_filename, 'w') as output_file:
        output_file.write(response_object.text)


def make_pretty(url, output_filename):
    response_object = requests.get(url)
    soup = bs4.BeautifulSoup(response_object.content, features="html.parser")
    with open(output_filename, 'w') as output_file:
        output_file.write(soup.prettify())


def find_paragraphs(url, output_filename):
    response_object = requests.get(url)
    soup = bs4.BeautifulSoup(response_object.content, features="html.parser")
    p_tags = soup.find_all('p')
    with open(output_filename, 'w') as output_file:
        for par in p_tags:
            output_file.write(f'{par}\n')


def find_links(url, output_filename):
    response_object = requests.get(url)
    soup = bs4.BeautifulSoup(response_object.content, features="html.parser")
    l_tags = soup.find_all('a')
    with open(output_filename, 'w') as output_file:
        for lin in l_tags:
            output_file.write(f'{lin.get("href")}\n')


def practice():
    response_object = requests.get("https://cs111.byu.edu")
    print(response_object.url)
    # print(response_object.status_code)
    # print(response_object.headers)

    soup_object = bs4.BeautifulSoup(response_object.content, features="html.parser")
    pretty = soup_object.prettify()  # .prettify() returns a string of all the web page's HTML nicely indented+formatted
    list_of_tags = soup_object.find_all('p')  # .find_all('tag') takes a string w/ the tag, returns list of tag objects.

    img_tag = soup_object.find('img')  # .find returns one tag instead of a list of tags
    width = img_tag.get('width')
    print(width)

    data = '<p style="font-size: 12px; font-color: blue;" id="this_id">Hello, World</p>'
    soup = bs4.BeautifulSoup(data, features="html.parser")
    tag = soup.find('p')
    print(tag.attrs)  # {'style': 'font-size: 12px; font-color: blue;', 'id': 'this_id'}
    print(tag.attrs['style'])  # 'font-size: 12px; font-color: blue;'
    print(tag.get('style'))  # 'font-size: 12px; font-color: blue;'


if __name__ == "__main__":
    # practice()
    # download('https://cs111.byu.edu/articles/pair-programming/', 'download_lab19_test.txt')
    # make_pretty('https://cs111.byu.edu/articles/pair-programming/', 'pretty_lab19_test.txt')
    # find_paragraphs('https://cs111.byu.edu/articles/pair-programming/', 'paragraph_lab19_test.txt')
    find_links('https://cs111.byu.edu/articles/pair-programming/', 'links_lab19_test.txt')
