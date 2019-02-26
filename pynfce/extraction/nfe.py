from .states import BA, get_state_name
from .util import find_element


def extract_nfe(html, state=BA):
    state_name = get_state_name(state)
    module = __import__("xpath", globals(), locals(), [], 1)
    state_class = getattr(module, state_name)
    return {
        "modelo": find_element(html, state_class.MODELO),
        "serie": find_element(html, state_class.SERIE),
        "numero": find_element(html, state_class.NUMERO),
        "valor": find_element(html, state_class.VALOR),
        "chave_acesso": find_element(html, state_class.CHAVE_ACESSO),
    }
