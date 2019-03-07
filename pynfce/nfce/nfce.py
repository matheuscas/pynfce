from requests_html import HTMLSession
from ..states.states import BA, load_state_class


def get_nfce(url, state=BA):
    session = HTMLSession()
    response = session.get(url)

    state = load_state_class(state)
    return state(session).get_nfce(response)
