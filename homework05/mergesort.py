import sys


def readfile(filename):
    with open(filename, 'r') as infile:
        lines = infile.readlines()
    strpd_lines = []
    for line in lines:
        line = line.strip()
        strpd_lines.append(line)
    return strpd_lines


def writefile(lines, filename):
    returned_lines = []
    for line in lines:
        line = line + '\n'
        returned_lines.append(line)
    with open(filename, 'w') as out_file:
        out_file.writelines(returned_lines)


def merge_lists(lst1, lst2):
    """Takes two sorted lists and returns a single merged list that is still sorted.
    Looks at the first element of each list, picks the smallest, removes it from
    the list (or move a pointer to the next index) and stores that smallest value in the new list to be returned.
    Continues to do this until one of the lists is empty. At that point, it copies all the remaining elements
    from the other list into the merged list which is then returned.
    Doctests: python -m doctest mergesort.py
    >>> merge_lists([1, 3, 5],[2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge_lists([2, 4, 6], [1, 3, 5])
    [1, 2, 3, 4, 5, 6]
    >>> merge_lists([7, 8, 9], [1, 2, 3])
    [1, 2, 3, 7, 8, 9]
    >>> merge_lists([2, 8, 9], [1, 3, 5])
    [1, 2, 3, 5, 8, 9]
    >>> merge_lists([1, 5, 9], [3, 11, 14])
    [1, 3, 5, 9, 11, 14]
    >>> merge_lists([], [])
    []
    >>> merge_lists(["b", "d", "f"], ["a", "c", "e"])
    ['a', 'b', 'c', 'd', 'e', 'f']
    """
    merged = []
    if len(lst1) > 0 and len(lst2) > 0:
        while len(lst1) > 0 and len(lst2) > 0:
            if lst1[0] <= lst2[0]:
                merged.append(lst1[0])
                lst1 = lst1[1:]
            elif lst1[0] > lst2[0]:
                merged.append(lst2[0])
                lst2 = lst2[1:]
    if lst1 is not None:
        for item in lst1:
            merged.append(item)
    if lst2 is not None:
        for item in lst2:
            merged.append(item)
    return merged


def is_sorted(lst) -> bool:
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True


def sort_txt(lines):
    """Takes a list and returns a sorted list.
    Splits the list in half, recursively calls the function on both
    parts and then calls merge_lists to merge the two sorted halves.
    Base case is (how do you absolutely know that an arbitrary list is sorted?)
    Doctests: python -m doctest mergesort.py
    >>> sort_txt([4, 3, 7, 8, 2])
    [2, 3, 4, 7, 8]
    >>> sort_txt([1, 2, 3, 4, 5, 6])
    [1, 2, 3, 4, 5, 6]
    >>> sort_txt([])
    []
    >>> sort_txt([91, 37, 26, 3, 45, 90, 100, 13, 0, 81])
    [0, 3, 13, 26, 37, 45, 81, 90, 91, 100]
    >>> sort_txt([1003, 15, 0, 104, 6, 10002])
    [0, 6, 15, 104, 1003, 10002]
    """
    if is_sorted(lines) or len(lines) <= 1:
        return lines

    mid = len(lines) // 2
    lst1 = lines[:mid]
    lst2 = lines[mid:]

    s_lst1 = sort_txt(lst1)
    s_lst2 = sort_txt(lst2)

    return merge_lists(s_lst1, s_lst2)


if __name__ == "__main__":
    txt = readfile(sys.argv[1])
    sorted_txt = sort_txt(txt)
    writefile(sorted_txt, sys.argv[2])
