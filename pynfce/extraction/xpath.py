

class Bahia:
    # Aba de Emitente
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

    # Aba principal da NFE
    MODELO = "#NFe > table:nth-child(2) > tr > td:nth-child(1) > span"
    SERIE = "#NFe > table:nth-child(2) > tr > td:nth-child(2) > span"
    NUMERO = "#NFe > table:nth-child(2) > tr > td:nth-child(3) > span"
    VALOR = "#NFe > table:nth-child(2) > tr > td:nth-child(6) > span"
    CHAVE_ACESSO = "#lbl_chave_acesso"
