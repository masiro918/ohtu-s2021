from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        data = str(toml.loads(content))
        
        print(data)
        
        blocks = data.split("'dependencies':")
        
        dependencies = blocks[1].split("'},")
        dependencies[0] = dependencies[0] + "'}"
        
        blocks2 = blocks[1].split("dev-dependencies':")
        dev_dependencies = blocks2[1].split("}}, '")
        
        str1 = dependencies[0].replace("{", "")
        str1 = str1.replace("}", "")
        str1 = str1.replace("'", "")
        
        str2 = dev_dependencies[0].replace("{", "")
        str2 = str2.replace("}", "")
        str2 = str2.replace("'", "")
        
        deps = str1.split(",")
        dev_deps = str2.split(",")
        
        return_deps = []
        return_dev_deps = []
        
        i = 0
        
        while (i < (len(deps))):
            s = deps[i]
            s = s.split(":")
            
            return_deps.append(s[0].replace(" ", ""))
            i = i + 1
            
        i = 0
        
        while (i < (len(dev_deps))):
            s = dev_deps[i]
            s = s.split(":")
            
            # TODO: tee oliot!
            
            return_dev_deps.append(s[0].replace(" ", ""))
            i = i + 1
            
        
            
        return Project("Test name", "Test description", return_deps, return_dev_deps)
