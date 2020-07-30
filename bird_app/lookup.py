import pandas as pd
from bird_app.util import cs_to_region, lookup


def rareness_lookup(form):
    # parse data
    bird = form.bird.data
    season = form.season.data
    state = form.state.data
    county = form.county.data

    # TODO: Map State,county to region
    cs = f'{county},{state}'
    region = cs_to_region[cs]

    # encode features
    message = f"You saw {bird} in {county},{state} in {season}"
    return message
