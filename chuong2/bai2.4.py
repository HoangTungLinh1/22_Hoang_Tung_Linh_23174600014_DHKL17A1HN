import xml.dom.minidom

def main():
    doc=xml.dom.minidom.parse("chuong2\\sample.xml")
    
    print(doc.nodeName)
    print(doc.firstChild.tagName)
if __name__=="__main__":
    main()