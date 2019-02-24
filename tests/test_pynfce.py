import os
from pynfce import __version__
from pynfce.extraction.emitente import extract_emitente
from requests_html import HTMLSession
from requests_file import FileAdapter

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


def test_version():
    assert __version__ == '0.1.0'


def test_extract_emitente():
    html = _get_mock_data_to_emitente().html
    emitente = extract_emitente(html)
    assert emitente is not None
