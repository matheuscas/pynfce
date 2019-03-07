import os
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


def _get_mock_data_to_nfe():
    return _get("nfe_mock.html")


def _get_mock_data_to_produtos():
    return _get("produtos_mock.html")
