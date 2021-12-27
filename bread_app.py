from flask import Flask, redirect, render_template
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/recipe/")
def link():
    links = [
        "https://butterwithasideofbread.com/homemade-english-muffins/",
        "https://butterwithasideofbread.com/fabulous-french-bread/",
        "https://butterwithasideofbread.com/orange-juice-bread/",
        "https://butterwithasideofbread.com/no-yeast-dinner-rolls/",
        "https://butterwithasideofbread.com/glazed-strawberry-bread/",
        "https://butterwithasideofbread.com/easy-lemon-bread/",
        "https://butterwithasideofbread.com/breakfast-rolls/",
        "https://butterwithasideofbread.com/homemade-cornbread-recipe/",
        "https://butterwithasideofbread.com/pineapple-quick-bread/",
        "https://butterwithasideofbread.com/cheesy-breadsticks/",
        "https://butterwithasideofbread.com/dutch-apple-bread/",
        "https://butterwithasideofbread.com/no-yeast-wheat-bread/",
        "https://butterwithasideofbread.com/caramel-apple-bread/",
        "https://butterwithasideofbread.com/bread-recipes/",
        "https://butterwithasideofbread.com/double-chocolate-banana-bread/",
        "https://butterwithasideofbread.com/lemon-poppy-seed-bread/",
        "https://butterwithasideofbread.com/braided-sweet-bread/",
        "https://butterwithasideofbread.com/chocolate-chip-oatmeal-bread/",
        "https://thekitchenpaper.com/quick-naan-without-yeast/",
        "https://www.thekitchn.com/easier-no-knead-bread-in-a-hurry-40653",
        "https://www.thekitchn.com/focaccia-recipe-261454",
        "https://sallysbakingaddiction.com/homemade-flatbread-pizza-recipe/#tasty-recipes-83167",
        "https://sallysbakingaddiction.com/homemade-cheese-bread/#tasty-recipes-74015"
    ]

    return redirect(random.choice(links))

if __name__ == "__main__":
    app.run(debug = True)
