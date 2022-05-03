from enum import Enum

class PrereqType(Enum):
    SINGLEPREREQ = 1
    MULTIPLEPREQS = 2 # This is for courses with 2 or 3 prereqs
    NUMBERRANGEPREREQ = 3 # This is for courses that require, say, CS 440-489
    COURSELEVELPREREQ = 4 # This is for courses that require 4XX or 3XX
    INDEPTPREREQ = 5 # For courses that say "Computer science students only"
    NOTINDEPTPREREQ = 6 # For courses that say "Not honours mathematics students only"
    INFACULTYPREREQ = 7
    NOTINFACULTYPREREQ = 8
    DEGREELEVELPREREQ = 9 # For courses that require 3A or something
    DEPTCONSENTPREREQ = 10 # Department Consent Required

class CourseReq:
    def __init__(self, reqtype, params):
        # reqcourse should always be an array
        match reqtype:
            case PrereqType.SINGLEPREREQ:
                self.reqcourse = [params] # passes a single [course, mark] tuple. Mark will be -1 in most cases
            case PrereqType.MULTIPLEPREQS:
                self.reqcourse = params # assumes that params are a list of [course, mark] tuples
            case PrereqType.NUMBERRANGEPREREQ:  # params: [dept, faculty, lowerbound, upperbound, mark]
                self.dept = params[0]
                self.faculty = params[1]
                self.lowerBound = params[2]
                self.upperBound = params[3]
                self.mark = params[4]
            case PrereqType.COURSELEVELPREREQ:
                self.dept = params[0]
                self.faculty = params[1]
                self.courselevel = params[2] # so 0 for 0XX, 1 for 1XX and so on
                self.mark = params[3]
            case PrereqType.INDEPTREQ:
                self.dept = params[0]
                self.faculty = params[1]
                self.mark = params[2]
            case PrereqType.NOTINDEPTPREREQ:
                self.dept = params[0]
                self.faculty = params[1]
                self.mark = params[2]
            case PrereqType.INFACULTYPREREQ:
                self.faculty = params[0]
                self.mark = params[1]
            case PrereqType.NOTINFACULTYPREREQ:
                self.faculty = params[0]
                self.mark = params[1]
            case PrereqType.DEGREELEVELPREREQ:
                self.degreelevel = params[0]
                self.mark = parmas[1]
            case PrereqType.DEPTCONSENTPREREQ:
                self.deptconsent = true

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

