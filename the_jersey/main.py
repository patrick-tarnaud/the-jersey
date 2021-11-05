from pprint import pprint

from model.race import Race
import os

def main():
    tdf_list = Race.load_races_from_file(os.path.join(os.getcwd(), 'data', 'TDF.csv'))
    pprint(tdf_list)

if __name__ == '__main__':
    main()