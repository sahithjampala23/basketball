import pandas as pd
from basketball_reference_scraper.teams import get_roster

try:
    from basketball_reference_scraper.constants import TEAM_TO_TEAM_ABBR, TEAM_SETS
    from basketball_reference_scraper.utils import remove_accents
except:
    from basketball_reference_scraper.constants import TEAM_TO_TEAM_ABBR, TEAM_SETS
    from basketball_reference_scraper.utils import remove_accents


ret_df = pd.DataFrame(columns=['YEAR', 'TEAM', 'NUMBER', 'PLAYER', 'POS', 'HEIGHT', 'WEIGHT', 'BIRTH_DATE',
                               'NATIONALITY', 'EXPERIENCE', 'COLLEGE'])
for year in range(1976, 2022):
    for team, team_abbr in TEAM_TO_TEAM_ABBR.items():
        curr_roster_year = get_roster(team_abbr,year)
        if curr_roster_year is not None:
            curr_roster_year['YEAR'] = year
            curr_roster_year['TEAM'] = team_abbr

            ret_df = pd.concat([ret_df, curr_roster_year])

    print(year)
ret_df.to_csv('data/rosters_all_time.csv')

