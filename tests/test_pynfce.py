import os
from pynfce import __version__
from pynfce.extraction.produtos import extract_produtos
from pynfce.extraction.states import (
    get_available_states_indexes,
    load_state_class
)
from requests_html import HTMLSession
from requests_file import FileAdapter
import pytest

session = HTMLSession()
session.mount('file://', FileAdapter())


def _get(mock_file_name):
    path = os.path.sep.join(
        (
            os.path.dirname(os.path.abspath(__file__)),
            f"mock_data/{mock_file_name}"
        )
    )
    url = 'file://{}'.format(path)
    return session.get(url)


def _get_mock_data_to_emitente():
    return _get("emitente_mock.html")


def _get_mock_data_to_nfe():
    return _get("nfe_mock.html")


def _get_mock_data_to_produtos():
    return _get("produtos_mock.html")


def test_version():
    assert __version__ == '0.3.0'


@pytest.fixture
def states():
    return get_available_states_indexes()


def test_extract_emitente(states):
    html = _get_mock_data_to_emitente().html
    for state_index in states:
        state = load_state_class(state_index)
        emitente = state().extract_emitente(html)
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
        nfe = state().extract_nfe(html)
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


def test_extract_produtos():
    html = _get_mock_data_to_produtos().html
    produtos = extract_produtos(html)
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
