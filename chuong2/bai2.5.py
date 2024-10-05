import xml.dom.minidom

doc= xml.dom.minidom.parse("chuong2\\sample.xml")

elements = doc.getElementsByTagName("*")

print("danh sách các phần tử: ")
for phan_tu in elements:
    print(phan_tu.tagName)

    