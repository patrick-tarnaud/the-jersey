from typing import Optional

# Année;Edition;Maillot jaune;Deuxième;Troisième;Equipe;Vélo;Dérailleur;Nb étapes;Distance;Vitesse moy.;Maillot à poids;Maillot vert;Meilleur jeune;Meilleur combattant
COL_YEAR = 0
COL_EDITION = 1
COL_FIRST_WINNER = 2
COL_SECOND_WINNER = 3
COL_THIRD_WINNER = 4
COL_TEAM = 5
COL_BIKE = 6
COL_TRANSMISSION = 7
COL_NB_STEPS = 8
COL_DISTANCE = 9
COL_AVERAGE_SPEED = 10
COL_MOUNTAN_WINNER = 11
COL_POINTS_WINNER = 12
COL_YOUNG_WINNER = 13
COL_FIGHT_WINNER = 14


class Race:
    def __init__(self, year: int, edition: int, first_winner: str, second_winner: Optional[str] = "",
                 third_winner: Optional[str] = "", team: Optional[str] = "", bike: Optional[str] = "",
                 transmission: Optional[str] = "", nb_steps: Optional[int] = None, distance: Optional[float] = None,
                 average_speed: Optional[float] = None, mountain_winner: Optional[str] = "",
                 points_winner: Optional[str] = "", young_winner: Optional[str] = "", fight_winner: Optional[str] = ""):
        self.year = year
        self.edition = edition
        self.first_winner = first_winner
        self.second_winner = second_winner
        self.third_winner = third_winner
        self.team = team
        self.bike = bike
        self.transmission = transmission
        self.nb_steps = nb_steps
        self.distance = distance
        self.average_speed = average_speed
        self.mountain_winner = mountain_winner
        self.points_winner = points_winner
        self.young_winner = young_winner
        self.fight_winner = fight_winner

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(year={self.year}, edition={self.edition},"
                f"first_winner={self.first_winner}, second_winner={self.second_winner}, third_winner={self.third_winner},"
                f"team={self.team}, bike={self.bike}, transmission={self.transmission}, nb_steps={self.nb_steps}, distance={self.distance},"
                f"average_speed={self.average_speed}, moutain_winner={self.mountain_winner}, "
                f"points_winer={self.points_winner}, yong_winner={self.young_winner}, fight_winner={self.fight_winner})")

    @classmethod
    def load_races_from_file(cls, file: str) -> tuple[list[str], list['Race']]:
        races = []
        with open(file, 'r') as f:
            for nbline, strline in enumerate(f):
                strline = strline.strip()
                line = strline.split(';')
                if nbline == 0:  # header
                    header = line
                else:  # data
                    races.append(
                        Race(int(line[COL_YEAR]),
                             int(line[COL_EDITION]) if line[COL_EDITION] else None,
                             line[COL_FIRST_WINNER].strip(),
                             line[COL_SECOND_WINNER].strip(),
                             line[COL_THIRD_WINNER].strip(),
                             line[COL_TEAM].strip(),
                             line[COL_BIKE].strip(),
                             line[COL_TRANSMISSION].strip(),
                             int(line[COL_NB_STEPS]) if line[COL_NB_STEPS] else None,
                             float(line[COL_DISTANCE]) if line[COL_DISTANCE] else None,
                             float(line[COL_AVERAGE_SPEED]) if line[COL_AVERAGE_SPEED] else None,
                             line[COL_MOUNTAN_WINNER].strip(),
                             line[COL_POINTS_WINNER].strip(),
                             line[COL_YOUNG_WINNER].strip(),
                             line[COL_FIGHT_WINNER].strip()))
        return header, races

    def __len__(self):
        return len(vars(self))

    def values_to_str(self)->str:
        return ''.join([str(v).lower() for v in tuple(vars(self).values())])