import re
import course

# Takes in a string and converts it to a coursereq object

def parse(req):
    # req is a string
    # easiest case: the prereq is a single course
    course_res = re.findall("(?:[A-Z]){2,7}(?:\s)*(?:[0-9]+)(?:;.*)*", req)
    if len(course_res) == 1:
        # Create a simplified course
        # We should only get to this option AFTER the others have been exhausted
        res = course_res[0]
        markindx = req.find("%")
        if markindx == -1:
            mark = -1
        else:
            mark = req[markindx - 2:markindx]
        return [course.SimplifiedCourse(res[:res.index(' ')], res[res.index(' ') + 1:]), mark]

# testing
print(parse("Prereq: PMATH 351 with a grade of at least of 60%")[0].__dict__)