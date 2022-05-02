import requests # you have to install this
import sys
import re

sys.path.append('../')

from scraper import course
from bs4 import BeautifulSoup # you have to install this

# TODO:
# Scrape descriptions, prerequisites, corequisites and antirequisites

dept = "CS";
URL = "https://ucalendar.uwaterloo.ca/2223/COURSE/course-" + dept + ".html"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
course_cards = soup.find_all("center")
course_list = []
course_ind = 0

for crs_crd in course_cards:
    #course_name = crs_crd.find(class_="divTableCell colspan-2").text
    #course_num = re.search("/([0-9]+)[^\s]*/", tmp_name)
    #course_creds = re.search("(\.*\d+)(?!.*\d)", crs_crd.find("strong").text)
    #course_offered = crs_crd.find("em", string= lambda text: "Offered:" in text)
    #if course_offered is None:
    #    offered = None
    #else:
    #    offered = course_offered.text[course_offered.text.index('Offered:') + 9: course_offered.text.index(']')]
    #cross_listed = crs_crd.findAll("em", string = lambda text: None if text is None else "Cross-listed" in text)
    #if len(cross_listed) > 0:
    #    cross_listed = cross_listed[0].text[cross_listed[0].text.index('Cross-listed') + 18:cross_listed[0].text.index(')')]
    #print(cross_listed)
    #course_list.append(Course(tmp_name), dept, "MATHEMATICS", course_num)

#print(course_cards)