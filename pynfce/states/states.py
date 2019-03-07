BA = "ba"

_states_mapping = {}
_states_mapping[BA] = "Bahia"


def get_state_name(state):
    return _states_mapping[state]


def load_state_class(state):
    state_name = get_state_name(state)
    module = __import__(f"{state}", globals(), locals(), [], 1)
    return getattr(module, state_name)


def get_available_states_indexes():
    return _states_mapping.keys()
