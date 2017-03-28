import requests
import xml.dom.minidom
import json

cep = 81460320
a = requests.get("http://cep.republicavirtual.com.br/web_cep.php?cep=%i&formato=json" % cep)
b = requests.get("http://api.postmon.com.br/v1/cep/%i" % cep)

data = json.loads(a.text)
data2 =json.loads(b.text)
print(type(data))
print(data2)

print(data['cidade'])

from datetime import datetime
import logging
import re

from lxml.html import fromstring


class CepTracker():

    def __init__(self):
        self.url = 'http://m.correios.com.br/movel/buscaCepConfirma.do'

    def _request(self, cep):
        response = requests.post(self.url, data={
            'cepEntrada': cep,
            'tipoCep': '',
            'cepTemp': '',
            'metodo': 'buscarCep'
        }, timeout=10)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as ex:
            logger.exception('Erro no site dos Correios')
            raise ex
        return response.text

a = CepTracker()
print(a._request(81460320))
