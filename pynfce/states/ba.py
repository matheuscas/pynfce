CONSULTA_DANFE = "http://nfe.sefaz.ba.gov.br/\
                    servicos/nfce/modulos/geral/NFCEC_consulta_danfe.aspx"
CONSULTA_ABAS = "http://nfe.sefaz.ba.gov.br/\
                    servicos/nfce/modulos/geral/NFCEC_consulta_abas.aspx"


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

    ABA_EMITENTE_X_Y = {
        "btn_aba_emitente.x": 25,
        "btn_aba_emitente.y": 11,
        "hid_uf_dest": ""
    }
    ABA_PRODUTOS_X_Y = {
        "btn_aba_produtos.x": 46,
        "btn_aba_produtos.y": 8,
        "hid_uf_dest": ""
    }

    def __init__(self, session):
        self.session = session

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

    def _get_basic_hidden_form_data(self, response):
        return {
            "viewstate": response.html.find("#__VIEWSTATE", first=True),
            "viewstate_gen": response.html.find(
                "#__VIEWSTATEGENERATOR",
                first=True
            ),
            "event_validation": response.html.find(
                "#__EVENTVALIDATION",
                first=True
            )
        }

    def _navigateTo(self, response, tab):
        basic = self._get_basic_hidden_form_data(response)

        data = {
            "__VIEWSTATE": basic.get("viewstate").attrs["value"],
            "__VIEWSTATEGENERATOR": basic.get("viewstate_gen").attrs["value"],
            "__EVENTVALIDATION": basic.get("event_validation").attrs["value"],
        }

        payload = {**data, **tab}
        return self.session.post(CONSULTA_ABAS, data=payload)

    def _navigate_to_nfe_tab(self, response):
        basic = self._get_basic_hidden_form_data(response)

        data = {
            "__VIEWSTATE": basic.get("viewstate").attrs["value"],
            "__VIEWSTATEGENERATOR": basic.get("viewstate_gen").attrs["value"],
            "__EVENTVALIDATION": basic.get("event_validation").attrs["value"],
            "btn_visualizar_abas": "Visualizar em Abas"
        }

        return self.session.post(CONSULTA_DANFE, data=data)

    def _navigate_to_emitente_tab(self, response):
        self._navigateTo(response, self.ABA_EMITENTE_X_Y)

    def _navigate_to_produtos_tab(self, response):
        self._navigateTo(response, self.ABA_PRODUTOS_X_Y)

    def get_nfce(self, first_response):
        # click on "Visualizar Abas"
        nfe_tab_response = self._navigate_to_nfe_tab(first_response)
        # extract nfe
        nfe = self.extract_nfe(nfe_tab_response.html)

        # click on "Emitente"
        emitente_tab_response = self._navigate_to_emitente_tab(
            nfe_tab_response
        )
        # extract emitente
        emitente = self.extract_emitente(emitente_tab_response.html)

        # click on "Produtos"
        produtos_tab_resp = self._navigate_to_produtos_tab(nfe_tab_response)
        # extract produtos
        produtos = self.extract_produtos(produtos_tab_resp.html)

        return {
            **nfe,
            "emitente": emitente,
            "produtos": produtos
        }
