from .states import BA, get_state_name


def extract_produtos(html, state=BA):
    state_name = get_state_name(state)
    module = __import__("xpath", globals(), locals(), [], 1)
    state_class = getattr(module, state_name)

    descricoes = html.find(state_class.DESCRICOES, first=False)
    qtds = html.find(state_class.QTDS, first=False)
    unidades_comerciais = html.find(
        state_class.UNIDADES_COMERCIAIS,
        first=False
    )
    valores_unitarios = html.find(state_class.VALORES_UNITARIOS, first=False)
    valores_totais = html.find(state_class.VALORES_TOTAIS, first=False)
    ncms = html.find(state_class.CODIGOS_NCM, first=False)
    descontos = html.find(state_class.DESCONTOS, first=False)
    eans = html.find(state_class.EANS, first=False)

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
