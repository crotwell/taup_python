import pytest
import taup
from .conftest import taupserver
from requests.exceptions import HTTPError

class TestParseError:
    def test_bad(self, taupserver):
        """
        Check to make sure bad calls create exception.
        Negative seconds should not be allowed.
        """
        with pytest.raises(HTTPError) as e_info:
            params = taup.TimeQuery()
            params.phase(["S","P"])
            params.model('ak135fcont')
            params.seconds([-10, 10])
            ans = params.calc(taupserver)
        assert e_info.value.args[0].startswith("500 Server Error: Time seconds should be >=0")
