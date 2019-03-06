BA = 0

_states_mapping = {}
_states_mapping[BA] = "Bahia"


def get_state_name(state=BA):
    return _states_mapping[state]


def load_state_class(state):
    state_name = get_state_name(state)
    module = __import__("states", globals(), locals(), [], 1)
    return getattr(module, state_name)


def get_available_states_indexes():
    return _states_mapping.keys()


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

    # Aba de produtos
    DESCRICOES = "#Prod > div > table > tr > td > table.toggle > tr \
        > td.fixo-prod-serv-descricao > span"

    QTDS = "#Prod > div > table > tr > td > table.toggle > tr \
        > td.fixo-prod-serv-qtd > span"

    UNIDADES_COMERCIAIS = "#Prod > div > table > tr > td > table.toggle > tr \
        > td.fixo-prod-serv-uc > span"

    VALORES_UNITARIOS = "table > tr > td > table:nth-child(2) > \
        tr:nth-child(4) > td:nth-child(1) > span"

    VALORES_TOTAIS = "#Prod > div > table > tr > td > table.toggle >\
        tr > td.fixo-prod-serv-vb > span"

    CODIGOS_NCM = "table > tr > td > table:nth-child(1) > tr.col-4 >\
        td:nth-child(2) > span"

    DESCONTOS = "table > tr > td > table:nth-child(1) > tr:nth-child(3) >\
        td:nth-child(1) > span"

    EANS = "#Prod > div > table > tr > td > table:nth-child(2) > tr > td >\
        table:nth-child(2) > tr:nth-child(2) > td:nth-child(1) > span"

    def _get_municipio(self, municipio):
        municipio_parts = municipio.split("-")
        return {
            "numero": municipio_parts[0].strip(),
            "nome": municipio_parts[1].strip()
        }

    def extract_emitente(self, html, first=True):
        municipio = html.find(self.MUNICIPIO, first=first).text
        return {
            "razao_social": html.find(self.RAZAO_SOCIAL, first=first).text,
            "nome_fantasia": html.find(self.NOME_FANTASIA, first=first).text,
            "cnpj": html.find(self.CNPJ, first=first).text,
            "municipio": self._get_municipio(municipio),
            "bairro": html.find(self.BAIRRO, first=first).text,
            "endereco": html.find(self.ENDERECO, first=first).text,
            "cep": html.find(self.CEP, first=first).text
        }

    def extract_nfe(self, html, first=True):
        return {
            "modelo": html.find(self.MODELO, first=first).text,
            "serie": html.find(self.SERIE, first=first).text,
            "numero": html.find(self.NUMERO, first=first).text,
            "valor": html.find(self.VALOR, first=first).text,
            "chave_acesso": html.find(self.CHAVE_ACESSO, first=first).text
        }

    def extract_produtos(self, html):

        descricoes = html.find(self.DESCRICOES, first=False)
        qtds = html.find(self.QTDS, first=False)
        unidades_comerciais = html.find(
            self.UNIDADES_COMERCIAIS,
            first=False
        )
        valores_unitarios = html.find(self.VALORES_UNITARIOS, first=False)
        valores_totais = html.find(self.VALORES_TOTAIS, first=False)
        ncms = html.find(self.CODIGOS_NCM, first=False)
        descontos = html.find(self.DESCONTOS, first=False)
        eans = html.find(self.EANS, first=False)

        result = []
        for index in list(range(len(descricoes))):
            result.append({
                "descricao": descricoes[index].text,
                "qtd": qtds[index].text,
                "unidade_comercial": unidades_comerciais[index].text,
                "valor_total": valores_totais[index].text,
                "valor_unitario": valores_unitarios[index].text,
                "ncm": ncms[index].text,
                "desconto": descontos[index].text,
                "ean": eans[index].text
            })
        return result
