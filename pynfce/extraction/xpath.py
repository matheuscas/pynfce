

class Bahia:
    RAZAO_SOCIAL = "#Emitente > table:nth-child(2) > \
                        tr.col-2 > td:nth-child(1) > span"
    NOME_FANTASIA = "#Emitente > table:nth-child(2) > \
                        tr.col-2 > td:nth-child(2) > span"
    CNPJ = "#Emitente > table:nth-child(2) > tr:nth-child(2) \
                        > td:nth-child(1) > span"
    MUNICIPIO = "#Emitente > table:nth-child(2) \
                    > tr:nth-child(4) > td:nth-child(1) > span"
    BAIRRO = "#Emitente > table:nth-child(2)  \
                > tr:nth-child(3) > td:nth-child(1) > span"
    ENDERECO = "#Emitente > table:nth-child(2) \
                    > tr:nth-child(2) > td:nth-child(2) > span"
    CEP = "#Emitente > table:nth-child(2) > \
                tr:nth-child(3) > td:nth-child(2) > span"
