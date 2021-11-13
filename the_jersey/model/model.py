from model.race import Race


class Model:
    def __init__(self, search_text: str, header: list[str], races: list[Race]):
        self.header = header
        self.races = races
        self._displayed_races = self.races[:]
        self.search_text = search_text.lower()

    @property
    def search_text(self) -> str:
        return self._search_text

    @search_text.setter
    def search_text(self, value: str):
        self._search_text = value.lower()
        self._displayed_races = [race for race in self.races if self._search_text in race.values_to_str()]
        # for race in [race for race in self.races if self.search_text in race.values_to_str()]:
        #     self._displayed_races.append(race)

    @property
    def races(self) -> list[Race]:
        return self._races

    @races.setter
    def races(self, value: list[Race]):
        self._races = value

    @property
    def displayed_races(self) -> list[Race]:
        return self._displayed_races

    @property
    def header(self) -> list[str]:
        return self._header

    @header.setter
    def header(self, value: list[str]):
        self._header = value
