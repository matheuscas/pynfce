from .util import (
    _get_mock_data_to_emitente,
    _get_mock_data_to_nfe,
    _get_mock_data_to_produtos,
)


class BahiaMock:
    def mock_navigate_to_nfe_tab(self, *args):
        return _get_mock_data_to_nfe()

    def mock_navigate_to_emitente_tab(self, *args):
        return _get_mock_data_to_emitente()

    def mock_navigate_to_produtos_tab(self, *args):
        return _get_mock_data_to_produtos()
