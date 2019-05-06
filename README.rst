==============
Pynfce
==============

Descrição:
----------
Pacote python que extrai os dados de uma NFCe a partir da URL do QRCode da nota.

**Somente Python 3!**
.. image:: https://travis-ci.org/matheuscas/pynfce.svg?branch=master
    :target: https://travis-ci.org/matheuscas/pynfce
.. image:: https://codecov.io/gh/matheuscas/pynfce/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/matheuscas/pynfce
.. image:: https://badge.fury.io/py/pynfce.svg
    :target: https://badge.fury.io/py/pynfce


Projetos relacionados:
----------------------
- `pycpfcnpj <https://github.com/matheuscas/pycpfcnpj>`_ - Módulo python para validar e gerar números de CPF e CNPJ.
- `pycnpj-crawler <https://github.com/matheuscas/pycnpj-crawler>`_ - Python module that crawls data for a given CNPJ on the government website of each state (please check the supported states).

Como instalar:
--------
.. code-block:: shell

   pip install pynfce

Como usar:
----------
.. code-block:: python

   from pynfce import get_nfce
   QRCODE_URL = "https://..."
   # o estado da Bahia é padrão
   nfce = get_nfce(QRCODE_URL)

Exemplo de retorno dos dados de uma NFCe:
-----------------------------------------
.. code-block:: python

    {
        "modelo":"",
        "serie": "",
        "numero": "",
        "valor": "",
        "chave_acesso": "",
        "emitente": {
            {
                "razao_social":"",
                "nome_fantasia":"",
                "cnpj":"",
                "municipio": {
                    "numero":"",
                    "nome":""
                },
                "bairro":"",
                "endereco":"",
                "cep":""
            }
        },
        "produtos":[
            {
                "descricao":"",
                "qtd":"",
                "unidade_comercial":"",
                "valor_total":"",
                "valor_unitario":"",
                "ncm":"",
                "desconto":"",
                "ean":""
            }
        ]
    }

Nem todos os dados podem estar disponíveis, pois depende de cada estado. 

Estados disponíveis:
--------------------
- Bahia (ba) 

Esse é um **trabalho em progresso** e toda ajuda é bem vinda. 
