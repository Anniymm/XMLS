import tkinter as tk
from tkinter import filedialog
from lxml import etree

def remove_comments_xml(input_file, output_file):
    # xml parsingi
    parser = etree.XMLParser(remove_comments=True)
    tree = etree.parse(input_file, parser)

    # axal file-shi chawera
    with open(output_file, 'wb') as f:
        f.write(etree.tostring(tree, pretty_print=True, xml_declaration=True, encoding='UTF-8'))
    
    print(f"Comments have removed. Cleaned XML saved to {output_file}")  # filebis  menejmentistvis
def blank_removal(output_file):
    with open(output_file, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w') as file:
        for line in lines:
            if line.strip():  
                file.write(line)

# file-is martivad sherchevistvis ubralod GUI designi
def select_file():
    input_file = filedialog.askopenfilename(
        title="Select XML File", 
        filetypes=[("XML Files", "*.xml")]
    )
    
    if input_file:
        # sad da rogor sheinaxos axali file(ukomentaro)
        output_file = filedialog.asksaveasfilename(
            title="Save Cleaned XML As", 
            defaultextension=".xml", 
            filetypes=[("XML Files", "*.xml")]
        )
        
        if output_file:
            # moshoreba da saboloo shenaxva 
            remove_comments_xml(input_file, output_file)
            blank_removal(output_file)
            print("Extra blank lines have been removed.")


# GUI
root = tk.Tk()
root.title("Remove Comments from XML")

# Guis ghilaki
btn_select_file = tk.Button(root, text="Select XML File", command=select_file)
btn_select_file.pack(pady=40)
root.mainloop()

