from getContent import getContent
from getURL import getURL
import MySQLdb


codeDescriptionList = [line.strip() for line in open("job_id_titles.txt", "r")]
file = open("job_id_title_description", "w+")
for each_item in codeDescriptionList:
    gensimIndex = each_item.index(',')
    code = each_item[:gensimIndex].strip()
    jobtitles = each_item[gensimIndex + 1:]
    try:
        url = getURL(code)
        description = getContent(url)
        file.write(code + "|" + jobtitles + "|" + description + '\n')
    except ValueError:
        print "value err"


file.close()