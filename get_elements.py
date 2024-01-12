import os
import tools
directories = list(os.walk('elements'))

with(open("load_elements.py", 'w', encoding='utf-8') as f):
    f.write("from emploid import Emploid\nfrom api import API\nfrom time import sleep\nemp = Emploid()\n")
    if(len(directories)):
        for dir in directories:
            for png in dir[2]:
                if(png[-4:]==".png"):
                    line = "element_"+png[:-4]+"=emp.import_image(\""+dir[0].replace("\\", "/")+"/"+png+"\")\n"
                    line = line.replace("elements/", "")
                    f.write(line)
        else:
            print("no")
content = tools.f_read("load_elements.py")

tools.f_write("load_elements.py", content)
