import json
from baseJson import *

from recursos import *

class PostResultado:

    def __init__(self, bodyRequest):
        self.base = BaseJson()
        self.body = bodyRequest
                
        
    def postar(self): 
        self.base.salvarPaciente(self.body)
        return True
