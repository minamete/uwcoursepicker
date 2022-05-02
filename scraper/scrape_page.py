import requests # you have to install this
import sys
import re
import pymongo
import unicodedata
from bs4 import BeautifulSoup # you have to install this
import upload_data

# TODO:
# Write a parser for pre/co/antireqs, course offering times, crosslisted courses

deptDict = {
    "ARTS": ['AFM','ASL','ANTH','APPLS','ARABIC','ARTS','ARBUS','BLKST','CDNST','CHINA','CMW','CLAS','COGSCI','CROAT',
        'CI','DAC','DUTCH','EASIA','ECON','ENGL','FINE','FR','GSJ','GER','GBDA','GRK','HIST','HRM','HRTS','HUMSC',
        'INDENT','INDG','INTST','ITAL','ITALST','JAPAN','JS','KOREA','LAT','LS','MGMT','MEDVL','MENN','MOHAWK',
        'MUSIC','PACS','PHIL','PSCI','PORT','PSYCH','RS','RUSS','REES','SMF','SDS','SOCWK','SOC','SPAN','SPCOM',
        'SI','THPERF','VCULT'],
    "MATH": ['ACTSC','AMATH','CO','COMM','CS','MATBUS','MATH','MTHEL','PMATH','STAT'],
    "ENG": ['AE','ARCH','BME','BET','CHE','CIVE','ECE','ENVE','GENE','GEOE','MSCI','ME','MTE','NE','PDARCH','SYDE'],
    "SCI" : ['BIOL','CHEM','EARTH','MNS','OPTOM','PHARM','PHYS','PDPHRM','SCI','SCBUS'],
    "ENV" : ['ENVS','ENBUS','ERS','GEOG','INDEV','INTEG','PLAN'],
    "HEALTH" : ['GERON','HEALTH','KIN','HLTH','REC'],
    "REN" : ['BASE','EMLS','SWREN'],
    "WLU" : ['BUS'],
    "VPA" : ['AVIA','CFM','COOP','PD','STV','SE','SFM','UNIV','WKRPT']
}

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

def scrape(dept, fac):
    URL = "https://ucalendar.uwaterloo.ca/2223/COURSE/course-" + dept + ".html"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    course_cards = soup.find_all("center")
    course_list = []
    for course in course_cards:
        course_list.append(parse(course, dept, fac))
    upload_data.serialize_multiple_courses(course_list)

def parse(crs_crd, dept, fac):
    course_name = crs_crd.find(class_="divTableCell colspan-2").text
    course_desc = crs_crd.findAll(class_="divTableCell colspan-2")[1].text
    temp_num = crs_crd.find("div", class_="divTableCell").find("a")["name"]
    course_num = re.search("([0-9]+)[^\s]*", temp_num)
    if course_num is not None:
        course_num = course_num.group(0)
    print(temp_num)
    course_creds = re.search("(\.*\d+)(?!.*\d)", crs_crd.find("strong").text)
    if course_creds is not None:
        course_creds = course_creds.group(0)
    course_offered = crs_crd.find("em", string=lambda text: None if text is None else "Offered:" in text)
    if not course_offered is None:
        offered = course_offered.text[course_offered.text.index('Offered:') + 9: course_offered.text.index(']')]
    else:
        offered = None
    cross_listed = crs_crd.findAll("em", string=lambda text: None if text is None else "Cross-listed" in text)
    prereqs = crs_crd.findAll("em", string=lambda text: None if text is None else "Prereq:" in text)
    coreqs = crs_crd.findAll("em", string=lambda text: None if text is None else "Coreq:" in text)
    antireqs = crs_crd.findAll("em", string=lambda text: None if text is None else "Antireq:" in text)
    if len(cross_listed) > 0:
        cross_listed = cross_listed[0].text[
                       cross_listed[0].text.index('Cross-listed') + 18:cross_listed[0].text.index(')')]
    if len(prereqs) > 0:
        prereqs = prereqs[0].text[prereqs[0].text.index('Prereq:') + 8:]
    if len(coreqs) > 0:
        coreqs = coreqs[0].text[coreqs[0].text.index('Coreq:') + 7:]
    if len(antireqs) > 0:
        antireqs = antireqs[0].text[antireqs[0].text.index('Antireq:') + 9:]
    return CrudeCourse(course_name, course_desc, dept, fac, course_num, course_creds, offered, cross_listed, prereqs, antireqs, coreqs)

for facs in deptDict.keys():
    for dept in deptDict[facs]:
        scrape(dept, facs)

