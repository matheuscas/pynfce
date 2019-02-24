from .states import BA, get_state_name
from .util import find_element


def _get_municipio(municipio):
    municipio_parts = municipio.split("-")
    return {
        "numero": municipio_parts[0].strip(),
        "nome": municipio_parts[1].strip()
    }


def extract_emitente(html, state=BA):
    state_name = get_state_name(state)
    module = __import__("xpath", globals(), locals(), [], 1)
    state_class = getattr(module, state_name)
    municipio = find_element(html, state_class.MUNICIPIO)
    return {
        "razao_social": find_element(html, state_class.RAZAO_SOCIAL),
        "nome_fantasia": find_element(html, state_class.NOME_FANTASIA),
        "cnpj": find_element(html, state_class.CNPJ),
        "municipio": _get_municipio(municipio),
        "bairro": find_element(html, state_class.BAIRRO),
        "endereco": find_element(html, state_class.ENDERECO),
        "cep": find_element(html, state_class.CEP)
    }
