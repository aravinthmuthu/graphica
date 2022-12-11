file = open("data/treemap_test.csv","w")

def parse_data(root, children):
    for node in children:
        if "children" not in node.keys():
            file.write(root+"."+node["name"].replace(" ","-").replace(",","-")+","+str(node["value"])+"\n")
        else:
            file.write(root+"."+node["name"]+",\n")
            parse_data(root+"."+node["name"].replace(" ","-").replace(",","-"), node["children"])


import json
flare_data = json.load(open("data/treemap_test.json"))
file.write("name,size\n")
file.write(flare_data["name"].replace(" ","-")+",\n")
parse_data(flare_data["name"].replace(" ","-").replace(",","-"), flare_data["children"])
file.close()
