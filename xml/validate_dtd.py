from lxml import etree

xml_file = "library.xml"
with open(xml_file, "rb") as f:
    xml_data = f.read()


dtd_file = "library.dtd"
dtd = etree.DTD(dtd_file)

#xml doğrulama 
xml_tree = etree.XML(xml_data)
if dtd.validate(xml_tree):
    print("xml dtd'ye uygun")
else:
    print("xml dtd'ye uygun değil")