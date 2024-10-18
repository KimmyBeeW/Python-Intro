import requests
import bs4
import sys
import re
from RequestGuard import RequestGuard
from image_processing import sepia, grayscale, flipped, mirror
import shutil
from byuimage import Image
import matplotlib.pyplot as plt


def fix_link(url_, old):  # from lab 21
    if url_.startswith('#'):
        return old
    elif "#" in url_:
        return re.findall(r'(.*)#', url_)[0]
    elif url_.startswith("/"):
        domain = re.findall(r'(https://[\w.]*)/', old)[0]
        return domain + url_
    else:
        new = re.findall(r'https://.*/', old)[0]
        return new + url_


def search_web(url, elem, att):
    og = url
    links = []
    tags = bs4.BeautifulSoup(requests.get(url).content, features="html.parser").find_all(elem)
    for tag in tags:
        if att in tag.attrs:
            url = tag.get(att)
        else:
            print("Error: Attribute not found in the HTML element.")
        if not url.startswith("http") or "#" in url:
            url = fix_link(url, og)
        links.append(url)
    return links


def count_links(url, rg) -> dict:
    """Link counting - starting at the home page of a website created for the class, you'll find all the links and
    load all the linked pages from the site, and repeat that until you've loaded every linked page. During that time
    your program will record how many times links to each webpage. At the end, you'll produce a histogram showing the
    number of pages that have been seen once, twice, etc. This information will be saved to output files."""
    links_to_visit = []
    llv_index = 0
    if rg.can_follow_link(url):
        links_to_visit.append(url)
    link_counts = {}

    while llv_index < len(links_to_visit):
        start_link = links_to_visit[llv_index]
        links = search_web(url=start_link, elem='a', att='href')
        if start_link not in link_counts:
            link_counts[start_link] = 1
        llv_index += 1
        for link in links:
            if link in link_counts:
                link_counts[link] += 1
            elif link not in links_to_visit:
                link_counts[link] = 1
                if rg.can_follow_link(link):
                    links_to_visit.append(link)
    return link_counts


def create_histogram(link_counts, hist_file, data_csv):
    counts = list(link_counts.values())
    bins = [ij for ij in range(min(counts), max(counts) + 2)]
    values, bin_nums, item = plt.hist(counts, bins)
    plt.savefig(hist_file)
    plt.clf()

    with open(data_csv, 'w') as outfile:
        for i in range(len(values)):
            outfile.writelines(f'{bin_nums[i]},{values[i]}\n')


def plot_data(url, data_plot, data_csv, rg):
    """find a specific table on a specified web page and read the data
    from the table, plot it, and save the data to a CSV file."""
    if not rg.can_follow_link(url):
        print("Error. Webcrawler is unable to follow link.")
    elif requests.get(url).status_code != 200:
        print(f"Error: Page not found (Status code: {requests.get(url).status_code})")
        sys.exit(1)
    else:
        table = bs4.BeautifulSoup(requests.get(url).content, features="html.parser").find('table', id='CS111-Project4b')
        rows = table.find_all('tr')
        x_vals = []
        y_vals_list = []
        for i in range(len(rows)):
            data = rows[i].find_all('td')
            x = float(data[0].text)
            x_vals.append(x)
            y_vals = []
            for j in range(1, len(data)):
                y = float(data[j].text)
                y_vals.append(y)
            y_vals_list.append(y_vals)
        if len(y_vals_list[0]) >= 1:
            y1_points = [item[0] for item in y_vals_list]
            plt.plot(x_vals, y1_points, 'b')
            if len(y_vals_list[0]) >= 2:
                y2_points = [item[1] for item in y_vals_list]
                plt.plot(x_vals, y2_points, 'g')
                if len(y_vals_list[0]) >= 3:
                    y3_points = [item[2] for item in y_vals_list]
                    plt.plot(x_vals, y3_points, 'r')
                    if len(y_vals_list[0]) == 4:
                        y4_points = [item[3] for item in y_vals_list]
                        plt.plot(x_vals, y4_points, 'k')
            plt.savefig(data_plot)

            with open(data_csv, 'w') as outfile:
                for k in range(len(x_vals)):
                    y_vals2 = y_vals_list[k][:len(y_vals_list[0])]
                    outfile.writelines(f'{x_vals[k]},{",".join(map(str, y_vals2))}\n')
        else:
            print("Error: no y-values found")


"""Once you've created the plot save it to the file specified as <output file 1> in the command line arguments.
After you've saved the plot, you should create the CSV file containing the data. This will be saved in the file 
specified by <output file 2> in the command line arguments. Each line should have the x-value, followed by each of 
the y-values for that x-value, separated by commas. They should be presented in the same order they appeared in the 
table on the web page."""


def filter_img(flag, outfile, prefix):
    if flag == "-s":
        sepia(Image(outfile)).save(prefix + outfile)
    elif flag == "-g":
        grayscale(Image(outfile)).save(prefix + outfile)
    elif flag == "-f":
        flipped(Image(outfile)).save(prefix + outfile)
    elif flag == "-m":
        mirror(Image(outfile)).save(prefix + outfile)


def image(url, prefix, flag, rg):
    """for finding and manipulating an image. The URL is the page where we want to extract images. The output file
    prefix is a string that will be prepended to the name of every image manipulated to produce the name of the output
    image file. The filter to run will be a flag specifying which filter from your image manipulation program to run.
    Specifically, your program should handle the following filter flags:
    -s - sepia filter
    -g - grayscale filter
    -f - vertical flip
    -m - horizontal flip (mirror)

    This function will be finding all the images on the page specified by the <url> command line argument, downloading
    them, applying the specified filters to them using image_processing, and writing the new images to the disk.
    """
    if flag != "-s" and flag != "-g" and flag != "-f" and flag != "-m":
        print("Invalid arguments: flag must be -s, -g, -f, or -m")
    else:
        image_links = []
        if rg.can_follow_link(url):
            links = search_web(url, 'img', 'src')
            for link in links:
                if link not in image_links and rg.can_follow_link(link):
                    image_links.append(link)
        for link in image_links:
            img = re.search(r"[\w.\-]+\.(png|jpeg|gif|pdf|tiff|psd|svg|heif|raw|bmp)", link)
            if img:
                output_filename = img[0]
                response = requests.get(link, stream=True)
                with open(output_filename, 'wb') as out_file:
                    shutil.copyfileobj(response.raw, out_file)
                del response

                filter_img(flag, output_filename, prefix)


def main(args):
    """valid args:
        -c <url> <output filename 1> <output filename 2>
        -p <url> <output filename 1> <output filename 2>
        -i <url> <output file prefix> <filter to run>
        """
    if len(args) == 4 and (args[0] == "-c" or args[0] == "-p" or args[0] == "-i"):  # check if valid
        domain = re.findall(r'https://[\w.]+', args[1])[0]
        rg = RequestGuard(domain)
        if args[0] == "-c":
            links_counts = count_links(args[1], rg)
            create_histogram(links_counts, args[2], args[3])
        elif args[0] == "-p":
            plot_data(args[1], args[2], args[3], rg)
        elif args[0] == "-i":
            image(args[1], args[2], args[3], rg)
    else:
        print("Invalid arguments. Commands need to be in the form:\n"
              "      <tag> <url> <output filename1 or file prefix> <output filename2 or filter to run>"
              "\nWhere tag is one of three options: \n"
              "     -c - count links\n"
              "     -p - extract and plot data\n"
              "     -i - find and manipulate an image\n")


if __name__ == "__main__":
    main(sys.argv[1:])  # terminal entry

    # Tests:
    # main(["-c", "https://cs111.byu.edu/proj/proj4/assets/page1.html", "hist.png", "hist_data.csv"])
    # main(["-p", "https://cs111.byu.edu/proj/proj4/assets/data.html", "outfile1.png", "outfile2.txt"])  # test -p
    # main(["-i", "https://cs111.byu.edu/proj/proj4/assets/", "sepia_", "-s"])
