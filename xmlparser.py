
# Author: Luis Moreno
# Company: Softtek
# Date: Jan 30 2017
# Version 1.0

import xml.etree.ElementTree as ET
tree = ET.parse('LincesReportFindBugs.xml')
root = tree.getroot()
import ntpath
from pprint import pprint
fileread = ('categories.txt')
filewrite = ('findbugs-security.txt')
#sourcefile = root.findall(".//SourceLine/[@sourcefile]")
variable = 1

with open(fileread) as f:
			for line in f:
				line = line.rstrip()
				print line
				with open(filewrite, 'a') as file_object:
					file_object.write(line + "\n")

				for headTag in root.getchildren():
					if headTag.tag == 'BugInstance' and headTag.attrib['type'] == line:
						for bodyTag in headTag.getchildren():
							if bodyTag.tag == 'SourceLine': 
					
								sourcepath=bodyTag.attrib['sourcepath'].title()
								linea=bodyTag.attrib['start'].title()
					
						ruta, archivo = ntpath.split(sourcepath)
						lineafinal = (ruta + "," + archivo + "," + linea + "\n")
	
						with open(filewrite, 'a') as file_object:
							file_object.write(lineafinal)
	


