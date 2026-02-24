import dataclasses, json

class DataClassJsonEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            d = dataclasses.asdict(o)
            return {k:v for k,v in d.items() if v is not None}
        return super().default(o)
