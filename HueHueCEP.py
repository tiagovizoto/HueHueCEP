import requests
import json

class HueHueCEP:
    
    def __init__(self, cep):
        self.cep = cep.replace('-','') 
        
        
    def result_address(self):
        resp = requests.get("http://cep.republicavirtual.com.br/web_cep.php?cep=%s&formato=json" % self.cep)
        data = json.loads(resp.text)
        return data
