from dataclasses import dataclass

@dataclass
class Daz:
    deg: float
    az: float
    baz: float
    source: list
    receiver: list
    km: float|None = None

    @classmethod
    def from_json(cls, jsonObj):
        daz = Daz(jsonObj['deg'],
                      jsonObj['az'],jsonObj['baz'],
                      [jsonObj['source']['lat'], jsonObj['source']['lon']],
                      [jsonObj['receiver']['lat'], jsonObj['source']['lon']])
        if "km" in jsonObj:
            daz.km = jsonObj['km']
        return daz
