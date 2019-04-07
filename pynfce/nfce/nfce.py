from requests_html import HTMLSession
from ..states.states import BA, load_state_class


def get_nfce(url, state=BA):
    """
    Busca no site da SEFAZ do estado os dados da nfce

    Args:
        url (str): url extraída da leitura do QR Code da NFCe
        state (str): estado referente a URL

    Returns:
        nfce (obj)

    """

    state = load_state_class(state)
    session = HTMLSession()
    response = session.get(url)

    return state(session).get_nfce(response)
