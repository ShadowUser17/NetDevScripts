class RouterOS:
    @classmethod
    def parse_as_value(self, output: str) -> dict:
        '''
        "key=val;..." -> ["key=val", ...] -> {key: val, ...}
        '''
        return dict(map(lambda item: item.split("="), output.split(";")))
