
# Author: Luis Moreno
# Company: Softtek
# Date: Jan 30 2017
# Version 1.0

import xml.etree.ElementTree as ET
tree = ET.parse('LincesReportFindBugs.xml')
root = tree.getroot()
lines_seen = set()
filename = ('categories.txt')
variable = 1

for headTag in root.getchildren():
    if headTag.tag == 'BugInstance' and headTag.attrib['category'] == 'SECURITY':
		variable += 1
		if headTag.attrib['type'] not in lines_seen:
			lines_seen.add(headTag.attrib['type'])
			linea = headTag.attrib['type']

			print linea 
			with open(filename, 'a') as file_object:
				file_object.write(linea + "\n")
