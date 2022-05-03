class Course:
    def __init__(self, name, desc, dept, faculty, course_num, credits, offered, crosslisted, prereqs, antireqs, coreqs):
        self.name = name
        self.desc = desc
        self.dept = dept
        self.faculty = faculty
        self.course_num = course_num # this is not actually a num, but a string, to account for Ls and Es
        self.credits = credits
        self.offered = offered # 0 = fall, 1 = winter, 2 = spring
        self.crosslisted = crosslisted # List of tuples
        self.prereqs = prereqs # This is a list of tuples: [[req enum (Choose ANY of these), # of things], [req, # of things] (Choose ALL of these)]
        self.antireqs = antireqs # Same with this
        self.coreqs = coreqs # and this


# You can use this to test things
cs_135 = Course("cs135", "...", "CS", "Math", "135", "0.5", "", "", "", "", "")

def parse_offered(course: Course) -> Course:
    """This function changes the format of the 'offered' attribute
    of a course, assumed to be a string of the form "F, W, S" or something similar,
    into a boolean array of length 4"""

    offered = course.offered
    arr = [False, False, False, False]

    # If the offered data is not a string, the offering period is not specified
    if not(isinstance(offered, str)):
        arr[3] = True
        course.offered = arr
        return course
    
    # Detection
    for s in offered:
        if s == "F":
            arr[0] = True
        if s == "W":
            arr[1] = True
        if s == "S":
            arr[2] = True
    
    # If the course is not held in any term, it must be held flexibly
    state = True
    for i in arr:
        if i == True:
            state = False
    
    
    arr[3] = state
    course.offered = arr
    return course

parse_offered(cs_135)
for i in cs_135.offered:
    print(i)

