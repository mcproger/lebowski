class TinkoffDataConverter:
    def __init__(self, raw_data: dict) -> None:
        self.raw_data = raw_data

    def __call__(self) -> dict:
        return {
            element['spendingCategory']['name']: element['amount']['value']
            for element in self.raw_data
        }
