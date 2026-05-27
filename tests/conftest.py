
import pytest
import taup
import dataclasses


@pytest.fixture(scope="module")
def taupserver():
    TAUP_PATH="~/Code/seis/TauP/build/install/TauP/bin/taup"
    with taup.TauPServer(TAUP_PATH, verbose=True) as taup_server:
        yield taup_server

def jsonMatchDataclass(jsonObj, dcObj):
    for jk, jv in jsonObj.items():
        found = False
        for k in dataclasses.fields(dcObj):
            print(f"{jk}  ?  {k.name}  {jk == k.name}")
            if jk == k.name:
                found = True
        assert found, f"{jk} {jv}"

    for jk, jv in jsonObj.items():
        if isinstance(jv, dict):
            jsonMatchDataclass(jv, getattr(dcObj, jk))

