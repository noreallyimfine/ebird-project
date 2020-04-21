import pandas as pd
from bird_app.util import encoder, model, cs_to_region


def rare_pred(form):
    # parse data
    bird = form.bird.data
    season = form.season.data
    state = form.state.data
    county = form.county.data

    # TODO: Map State,county to region
    cs = f'{county},{state}'
    region = cs_to_region[cs]

    # encode features
    X = pd.DataFrame({
        'name': [bird],
        'season': [season],
        'RegionName': [region]
    })
    X_encoded = encoder.transform(X)
    # get prediction
    pred = model.predict(X_encoded)
    return pred[0]
