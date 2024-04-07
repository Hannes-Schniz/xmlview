import tkinter as tk
from tkinter import ttk
import xml.etree.ElementTree as ET

xmlValue=[]

#window 
window = tk.Tk()
window.geometry('600x400')
window.title('Treeview')

class xmlElement:
    def __init__(self,tag,attrib,text):
        self.tag=tag
        self.attrib=attrib
        self.text=text
        self.children=[]
    def add_child(self,child):
        self.children.append(child)
    def __str__(self):
        return self.tag
    def print_children_information(self):
        for child in self.children:
            if child.children:
                child.print_children_information()
        print(self.tag)
        print(self.attrib)
        print(self.text)
        
        
        

def parseXML(root):
    newElement = xmlElement(root.tag,root.attrib,root.text)
    for child in root:
        newElement.add_child(parseXML(child))
    return newElement

def findElement(element,tag):
    if element.tag==tag:
        return element
    for child in element.children:
        foundElement=findElement(child,tag)
        if foundElement:
            return foundElement
    return None

def import_button():
    importValue=ET.parse(entry.get())
    root=importValue.getroot()
    xmlValue.append(parseXML(root))    
    combobox.config(values=xmlValue)

#input
label= ttk.Label(master=window, text = 'Some text')
label.pack()

entry=ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text= 'import xml', command = import_button)
button.pack()

combobox = ttk.Combobox(master=window, values=xmlValue)
combobox.pack()

combobox.bind('<<ComboboxSelected>>', lambda e: print(findElement(xmlValue[combobox.current()],combobox.get()).print_children_information()))



#run
window.mainloop()