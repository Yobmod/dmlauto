
import re
bystr = b'%PDF-1.4\n%\x93\x8c\x8b\x9e ReportLab Generated PDF document http://www.reportlab.com\n1 0 obj\n<<\n/F1 2 0 R\n>>\nend'
r = re.compile(bR"\\")
print(r)
print(bystr)

hkl = str(bystr[2:-1])
print(hkl)

bewstr = ""
for char in bystr:
    if char != b'\\':
        bewstr += str(char)

print(bewstr)