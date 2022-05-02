import requests # you have to install this
import sys
import re
import pymongo

from bs4 import BeautifulSoup # you have to install this

# TODO:
# Scrape prerequisites, corequisites and antirequisites
# Write a parser for pre/co/antireqs

class CrudeCourse:
    # All of these are unparsed strings.
    def __init__(self, crs_name, crs_desc, crs_dept, crs_fac, crs_num, crs_cre, crs_off, crs_cross, crs_pre, crs_anti, crs_co):
        self.name = crs_name
        self.desc = crs_desc
        self.dept = crs_dept
        self.faculty = crs_fac
        self.course_num = crs_num
        self.credits = crs_cre
        self.offered = crs_off
        self.crosslisted = crs_cross
        self.prereqs = crs_pre
        self.antireqs = crs_anti
        self.coreqs = crs_co

dept = "CS";
URL = "https://ucalendar.uwaterloo.ca/2223/COURSE/course-" + dept + ".html"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
course_cards = soup.find_all("center")
course_list = []
course_ind = 0

for crs_crd in course_cards:
    course_name = crs_crd.find(class_="divTableCell colspan-2").text
    course_desc = crs_crd.findAll(class_="divTableCell colspan-2")[1].text
    course_num = re.search("/([0-9]+)[^\s]*/", course_name)
    course_creds = re.search("(\.*\d+)(?!.*\d)", crs_crd.find("strong").text)
    course_offered = crs_crd.find("em", string= lambda text: "Offered:" in text)
    if not course_offered is None:
        offered = course_offered.text[course_offered.text.index('Offered:') + 9: course_offered.text.index(']')]

    cross_listed = crs_crd.findAll("em", string = lambda text: None if text is None else "Cross-listed" in text)
    prereqs = crs_crd.findAll("em", string = lambda text: None if text is None else "Prereq:" in text)
    coreqs = crs_crd.findAll("em", string = lambda text: None if text is None else "Coreq:" in text)
    antireqs = crs_crd.findAll("em", string = lambda text: None if text is None else "Antireq:" in text)

    if len(cross_listed) > 0:
        cross_listed = cross_listed[0].text[cross_listed[0].text.index('Cross-listed') + 18:cross_listed[0].text.index(')')]
    if len(prereqs) > 0:
        prereqs = prereqs[0].text[prereqs[0].text.index('Prereq:') + 8]
    if len(coreqs) > 0:
        coreqs = coreqs[0].text[coreqs[0].text.index('Coreq:') + 7]
    if len(antireqs) > 0:
        antireqs = antireqs[0].text[antireqs[0].text.index('Antireq:') + 9]
    course_list.append(CrudeCourse(course_name, course_desc, dept, "MATHEMATICS", course_num, course_creds, course_offered, cross_listed, prereqs, antireqs, coreqs))

print(course_list)