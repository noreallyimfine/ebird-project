# Is this bird rare?
Analyze eBird data and draw insights. Build model to classify bird sightings as by rarity ('Common', 'Uncommon', 'Rare')


### Data

Data drawn from [eBird by Cornell Lab of Ornithology](https://ebird.org/data/download)


### Purpose

* Fun to look at bird data
* Keep my pipeline skills fresh
* Learn PySpark
* Deploy a nice end product


### Stage 1

Before diving in to PySpark and working with the entire dataset, I wanted to get comfortable with the data itself and get a sense of how I wanted to approach this project. 

Working locally in **Jupyter Notebooks**, I used **Pandas**, **Matplotlib**, and **Scikit-Learn** to explore, visualize, and model a sample portion of the dataset. 

After fiddling and testing a bunch, I landed on a *data-cleaning pipeline* that led to a *Random Forest* model using features encoded with *CatBoost Encoder* from **category_encoders**


### To Run
Steps:
- get data from ebird
- run data through prepare_and_label.py
- model using random_forest.py
- can take pickled models to use going forward

