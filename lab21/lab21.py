import requests
import bs4
import sys
import re  # use https://regex101.com/ to doublecheck regex patterns


def fix_link(url_, old):
    if "#" in url_:
        return re.findall(r'(.*)#', url_)[0]
    elif url_.startswith("/"):
        domain = re.findall(r'(https://[\w.]*)/', old)[0]
        return domain + url_
    else:
        new = re.findall(r'https://.*/', old)[0]
        return new + url_


def main(args):
    """The program should load the page specified by the given URL and find the HTML element
    with the specified attribute. This same attribute will contain the next URL, HTML element,
    and attribute (in that order) to look for. The information is stored as a comma-separated list.
    This searching loop will continue until an attribute called final is found.
    Once final is found, write the tag's attribute content to the output file."""
    url, elem, att, outfile = args
    old_url = url
    while att != 'final':
        tags = bs4.BeautifulSoup(requests.get(url).content, features="html.parser").find_all(elem)
        check = False
        for tag in tags:
            if att in tag.attrs:
                url, elem, att = tag.get(att).split(',')
                check = True
        if not check:
            print("Attribute not found in the HTML element.")
            break
        if not url.startswith("https://") or "#" in url:
            url = fix_link(url, old_url)
        old_url = url
    tags = bs4.BeautifulSoup(requests.get(url).content, features="html.parser").find_all(elem)
    for tag in tags:
        if att in tag.attrs:
            with open(outfile, 'w') as output_file:
                output_file.write(tag.get(att))


if __name__ == "__main__":
    """This program will take command line arguments containing a 
    URL, an HTML element, an attribute, and an output file name."""
    if len(sys.argv) != 5:
        print("Usage: python script.py <URL> <HTML element> <Attribute> <Output file name>")
    else:
        main(sys.argv[1:5])

    """test inputs:
python lab21.py https://cs111.cs.byu.edu/lab/lab21/assets/sample1.html li checkpoint1 output.txt
python lab21.py https://cs111.byu.edu/lab/lab21/assets/webpage1.html p mediumhunt-checkpoint1 output.txt
python lab21.py https://cs111.byu.edu/lab/lab21/assets/webpage4.html ul longhunt-checkpoint1 output.txt
python3 lab21.py https://cs111.cs.byu.edu/lab/lab21/assets/webpage10.html footer link-checkpoint1 output.txt
    """
