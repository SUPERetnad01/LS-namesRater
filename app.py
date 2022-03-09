from email import message
from flask import Flask, render_template, request
import random
import pandas as pd
from nltk.corpus import words
import nltk
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

ls_names = pd.read_csv("ls_names.csv")
nltk.download("words")

y = ls_names.rating
print(ls_names.columns)
X = ls_names.drop(["rating", "name"], axis=1)

rfc = RandomForestClassifier(random_state=0)  # prediction model

# train and test set
X_train, X_test, y_train, y_test = train_test_split(
    X.values, y.values, test_size=0.33, random_state=42
)

# fit the model
rfc.fit(X_train, y_train)

# Predict the Test set results
y_pred = rfc.predict(X_test)

# Check accuracy score


print(
    "Model accuracy score with 10 decision-trees : {0:0.4f}".format(
        accuracy_score(y_test, y_pred)
    )
)


@app.route("/")
def hello_world():
    return render()


def extract_letters(name):
    letterlist = ls_names.columns.tolist()[4:]
    print(letterlist)
    i = {}
    for letter in letterlist:
        i[letter] = [name.count(letter.lower())]
    return i


@app.route("/predict", methods=("GET", "POST"))
def predict_name():
    name = request.args["ign"]
    name_ratings = {
        "name": [],
        "is_in_dict": [],
        "name_lenght": [],
        "first_letter_vowle": [],
        "last_letter_vowle": [],
    }
    if name is not None:
        name = str(name).lower()
        name_ratings["name"].append(name)
        name_ratings["is_in_dict"].append(name in words.words())
        name_ratings["name_lenght"].append(len(name))
        name_ratings["first_letter_vowle"].append(name[0] in "aeiuo")
        name_ratings["last_letter_vowle"].append(name[-1] in "aeiuo")
        df = pd.DataFrame.from_dict(dict(name_ratings, **extract_letters(name)))
        df = df.drop("name", axis=1)
        prediction = rfc.predict(df.values.tolist())
        prediction_message = generate_prediction_message(prediction[0])
    return render_template(
        "index.html",
        rating=f"your rating: {prediction[0]}",
        message=f"{prediction_message}",
    )


def render():
    return render_template("index.html")


def generate_prediction_message(rating):
    messages = {
        "1": [
            "It is almost as good as reneckton B1.",
            "Playing lebanc is even beter",
            "You probably build Randuins",
            "You probably build Collector ",
        ],
        "2": [
            "you probably like ahri",
            "you probably build graves wrong",
            "you probably take second rift herald",
        ],
        "3": [
            "you probabley build LDR instead of Collector",
            "you are probably a ivern mid enjoyer",
            "you are probably a soraka mid enjoyer",
        ],
        "4": [
            "Almost as based as Joe Marsh",
            "you are probabley a frozen hearth enjoyer",
            "you are probabley a zilean enjoyer",
        ],
    }

    return f"{random.choice(messages[f'{rating}'])}"
