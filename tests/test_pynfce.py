from pynfce import __version__, get_nfce
from pynfce.states.states import (
    BA,
    get_available_states_indexes,
    load_state_class
)
from pynfce.states.ba import Bahia
import pytest
import mock
from .util import (
    _get_mock_data_to_emitente,
    _get_mock_data_to_nfe,
    _get_mock_data_to_produtos,
    session
)
from .mocks import BahiaMock


def test_version():
    assert __version__ == '0.3.1'


@pytest.fixture
def states():
    return get_available_states_indexes()


def test_extract_emitente(states):
    html = _get_mock_data_to_emitente().html
    for state_index in states:
        state = load_state_class(state_index)
        emitente = state(state).extract_emitente(html)
        keys = [
            "razao_social",
            "nome_fantasia",
            "cnpj", "municipio",
            "bairro",
            "endereco",
            "cep"
        ]
        for key in keys:
            assert key in emitente.keys()
            assert emitente.get(key, None) is not None


def test_extract_nfe(states):
    html = _get_mock_data_to_nfe().html
    for state_index in states:
        state = load_state_class(state_index)
        nfe = state(state).extract_nfe(html)
        keys = [
            "modelo",
            "serie",
            "numero",
            "valor",
            "chave_acesso"
        ]
        for key in keys:
            assert key in nfe.keys()
            assert nfe.get(key, None) is not None


def test_extract_produtos(states):
    html = _get_mock_data_to_produtos().html
    for state_index in states:
        state = load_state_class(state_index)
        produtos = state(state).extract_produtos(html)
        assert len(produtos) > 0
        keys = [
            "descricao",
            "qtd",
            "unidade_comercial",
            "valor_unitario",
            "valor_total",
            "ncm",
            "desconto",
            "ean"
        ]
        for key in keys:
            assert key in produtos[0].keys()
            assert produtos[0].get(key, None) is not None


@mock.patch.object(
    Bahia,
    '_navigate_to_nfe_tab',
    new=BahiaMock.mock_navigate_to_nfe_tab
)
@mock.patch.object(
    Bahia,
    '_navigate_to_emitente_tab',
    new=BahiaMock.mock_navigate_to_emitente_tab
)
@mock.patch.object(
    Bahia,
    '_navigate_to_produtos_tab',
    new=BahiaMock.mock_navigate_to_produtos_tab
)
def test_extract_ncfe_ba(states):
    response = mock.Mock()
    state = load_state_class(BA)
    nfce = state(session).get_nfce(response)
    keys = [
        "emitente",
        "produtos",
        "modelo",
        "serie",
        "numero",
        "valor",
        "chave_acesso"
    ]
    for key in keys:
        assert key in nfce.keys()
        assert nfce.get(key, None) is not None


def test_unavailable_state():
    url = "any url"
    state = "bb"
    error_msg = f"No module named 'pynfce.states.{state}'"
    with pytest.raises(ModuleNotFoundError, match=error_msg):
        get_nfce(url, state)
