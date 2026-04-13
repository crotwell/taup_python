
import pytest
import taup


@pytest.fixture(scope="module")
def taupserver():
    TAUP_PATH="~/Code/seis/TauP/build/install/TauP/bin/taup"
    with taup.TauPServer(TAUP_PATH, verbose=True) as taup_server:
        yield taup_server
