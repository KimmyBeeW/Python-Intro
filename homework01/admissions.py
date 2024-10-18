# Provided code
# This function checks to ensure that a list is of length
# 8 and that each element is type float
# Parameters:
# row - a list to check
# Returns True if the length of row is 8 and all elements are floats
def check_row_types(row):
    if len(row) != 8:
        print("Length incorrect! (should be 8): " + str(row))
        return False
    ind = 0
    while ind < len(row):
        if type(row[ind]) != float:
            print("Type of element incorrect: " + str(row[ind]) + " which is " + str(type(row[ind])))
            return False
        ind += 1
    return True


# define your functions here
def convert_row_type(nums):
    return [float(num) for num in nums]


def calculate_score(scores):
    sat, gpa, interest, hs_quality = scores
    return ((sat / 160) * 0.3) + ((gpa * 2) * 0.4) + (interest * 0.1) + (hs_quality * 0.2)


def write_file(new_txt, filename):
    with open(filename, 'w') as out_file:
        out_file.writelines(new_txt)


def is_outlier(scores):
    """It should check that:
        if the demonstrated interest score is 0 or
        if the normalized GPA that is more than 2 points higher than the normalized SAT score.
    If either of these conditions is true, it should return True (because this student is an outlier);
    otherwise, the function returns False."""
    sat, gpa, interest, hs_quality = scores
    if interest == 0 or (gpa*2) > (2 + sat/160):
        return True
    else:
        return False


def calculate_score_improved(scores):
    """calculates a student score, checks if it is an outlier, and returns True if the student has a score of
    6 or higher OR was flagged as an outlier; otherwise, return False."""
    if calculate_score(scores) >= 6 or is_outlier(scores):
        return True
    else:
        return False


def grade_outlier(grades):
    """takes in a list of grades (of any length) and returns True if one single number is more than 20 points lower
    than all other numbers by sorting the list from lowest to highest, and checking for the difference between the
    two lowest grades; otherwise, returns False."""
    ordered = sorted(grades)
    if ordered[0] < ordered[1] - 20:
        return True
    else:
        return False


def grade_improvement(grades):
    """returns True if the average score of each semester is
    higher than or equal to each previous semester and False otherwise."""
    if grades[0] <= grades[1] <= grades[2] <= grades[3]:
        return True
    else:
        return False


def main():
    filename = "admission_algorithms_dataset.csv"
    input_file = open(filename, "r")    

    print("Processing " + filename + "...")
    # grab the line with the headers
    headers = input_file.readline()
    
    # TODO: loop through the rest of the file
    student_scores = []
    chosen = []
    outliers = []
    chosen_improved = []
    better_improved = []
    composite_chosen = []

    for line in input_file:
        line = line.strip('\n').split(',')
        student = line[0]
        nums = convert_row_type(line[1:9])
        if not check_row_types(nums):
            print('Error')

        scores = nums[0:4]
        score = calculate_score(scores)
        student_scores.append(f"{student},{score:.2f}\n")
        if score >= 6:
            chosen.append(f'{student}\n')
        if is_outlier(scores):
            outliers.append(f'{student}\n')
        if score >= 6 or (is_outlier(scores) and score >= 5):
            chosen_improved.append(f'{student}\n')
        if calculate_score_improved(scores):
            sat, gpa, interest, hs_quality = scores
            better_improved.append(f'{student},{sat},{gpa},{interest},{hs_quality}\n')

        grades = nums[4:8]
        grade_outlier(grades)
        grade_improvement(grades)

        if score >= 6 or (score >= 5 and (is_outlier(scores) or grade_outlier(grades) or grade_improvement(grades))):
            composite_chosen.append(f'{student}\n')

    write_file(student_scores, 'student_scores.csv')
    write_file(chosen, 'chosen_students.csv')
    write_file(outliers, 'outliers.csv')
    write_file(chosen_improved, 'chosen_improved.csv')
    write_file(better_improved, 'better_improved.csv')
    write_file(composite_chosen, 'composite_chosen.csv')

    # TODO: make sure to close all files you've opened!
    input_file.close()
    print("done!")


# this bit allows us to both run the file as a program or load it as a
# module to just access the functions
if __name__ == "__main__":
    main()
