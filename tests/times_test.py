import pytest
import taup
from .conftest import taupserver

class TestTauPTime:
    def test_amp(self, taupserver):
        eventLatLons = [ [35, -50], [-29, 45]]
        staLatLons = [ [34, -80], [35, -81]]
        params = taup.TimeQuery()
        params.phase(["S","P"])
        params.model('ak135fcont')
        params.amp()
        params.event( *eventLatLons[0] ) # splat to expand list into function args
        params.sourcedepth([100])
        for sta in staLatLons:
            params.station( *sta )
        ans = params.calc(taupserver)
