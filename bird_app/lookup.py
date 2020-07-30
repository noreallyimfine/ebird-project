import pandas as pd
from bird_app.util import cs_to_region, lookup


# def season_region_bird_rarity(bird, region, season):
#     bird_percent = season_region_ct[(region, season)][bird] / season_region_ct[(region, season)].sum()
#     if bird_percent > 0.005:
#         return "Common"
#     elif bird_percent > 0.001:
#         return "Uncommon"
#     else:
#         return "Rare"

def rareness_lookup(form):
    # parse data
    bird = form.bird.data
    season = form.season.data
    state = form.state.data
    county = form.county.data

    # TODO: Map State,county to region
    cs = f'{county},{state}'
    region = cs_to_region[cs]

    # lookup value in table as percent of total
    bird_percent = lookup[(region, season)][bird] / lookup[(region, season)].sum()
    if bird_percent > 0.005:
        return "Common"
    elif bird_percent > 0.001:
        return "Uncommon"
    else:
        return "Rare"

    # encode features
    message = f"You saw {bird} in {county},{state} in {season}, and the percent is {bird_percent}"
    return message
