# ebird-project
Analyze eBird bird sighting data to track migration patterns and build model to determine rareness of given bird sightings.


### Bird Migration
To read the blog post I wrote on this part of the project and some visualizations I made for it, go [here](https://medium.com/@avraham.jacobsohn/us-bird-migration-11e7e96cf2b5).
<br>
If you want to dive into the code, check out the `migration_analysis/` folder. I've condensed everything down to 1 Jupyter Notebook.


### Predictive Model
For the predictive model, I labelled bird sightings in my training set as either [**'Common'**, **'Uncommon'**, or **'Rare'**] based on the percentage of all bird sightings in their region during that season they represented. Then I trained a Random Forest Classifier to predict off new bird sightings.

You can check out the work done for this stage in the `rareness_predictor/` folder. 

### Lookup Model
Turned out, a predictive model was the wrong was to go. If someone would enter a bird that was never seen in that region during that season before, I know what I want that to return - Rare!

So I moved to a lookup table model. Here, I loaded the database with the percent of total sightings (in a region during a season) each bird was and return a label based on that.

The table used for this can be found at the end of the `prepare_and_label.py` module in `rareness_predictor/sample/`. The database itself is deployed as the backend below. 


### Backend
The backend API serves up rareness labels given a bird, region, and season.
Additionally, it serves a list of birds, states, counties, and seasons for input forms on the front-end. 

The code for the API is all inside the `backend/` folder, although the actual documentation is located [here](https://github.com/Bird-Check-1-2/Back-End).