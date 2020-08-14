from ebird.models import Region, Season, Bird, Lookup


def get_rareness(bird_sighting):
    region = Region.query.filter_by(county_id=bird_sighting['county']).first()
    season = Season.query.filter_by(id=bird_sighting['season']).first()
    bird = Bird.query.filter_by(id=bird_sighting['bird']).first()
    result = Lookup.query.filter_by(region=region.region,
                                    season=season.name,
                                    bird=bird.name).first()
    return result


def rareness_to_label(rareness):
    if rareness.pct_of_total > 0.005:
        return "Common"
    elif rareness.pct_of_total > 0.001:
        return "Uncommon"
    else:
        return "Rare"
