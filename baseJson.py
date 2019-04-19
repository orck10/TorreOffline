import json

class BaseJson():
    def __init__(self):
        self.base = []
        with open("base.json") as jsonFile:
            try:
                data = json.load(jsonFile)
                for i in data['pacientes']:
                    self.base.append(i)
                print(self.base)
            except:
                print("Base Vasia")
            
    
    def getAllPacientes(self):
        return self.base
    
    def getPacientePorNome(self, nome):
        for i in self.base:
            if i['nome'] == nome:
                return i
        return ""

    def salvarPaciente(self, paciente):
        jsonFile = {}
        jsonFile['pacientes'] = []
        for i in self.base:
            jsonFile['pacientes'].append(i)

        jsonFile['pacientes'].append(paciente)
        print(jsonFile)

        with open("base.json", "w") as escrita:
            json.dump(jsonFile, escrita) 