# import necessary libraries
from flask import Flask, render_template,redirect
import pymongo
import scrape_mars


# create instance of Flask app
app = Flask(__name__)


client = pymongo.MongoClient()
db = client.mars_db


collection = db.mars
collection_image = db.mars
collection_weather = db.mars

collection_hemisphere = db.mars



# create route that renders index.html template
@app.route("/")
def home():


    News_dict= db.collection.find()

    feature_Image_dict = db.collection_image.find()

    weather_dict = db.collection_weather.find()

    # full_hemisphere_dict = db.collection_hemisphere.find()

    
    
    

    

    return render_template("index.html", News_dict = News_dict, 
                                        feature_Image_dict = feature_Image_dict,
                                        weather_dict = weather_dict)
                                        # full_hemisphere_dict = full_hemisphere_dict


@app.route("/scrape")
def scrape():
    db.collection.remove()

    News_dict = scrape_mars.mars_news_function()
    db.collection.insert_one(News_dict)

    db.collection_image.remove()
    feature_Image_dict = scrape_mars.Feature_Image_function()
    db.collection_image.insert_one(feature_Image_dict)

    db.collection_weather.remove()
    weather_dict = scrape_mars.Weather_function()
    db.collection_weather.insert_one(weather_dict)


    # db.collection_hemisphere.remove()
    # full_hemisphere_dict = scrape_mars.hemisphere_images()
    # db.collection_hemisphere.insert_one(full_hemisphere_dict)


   



    print('----------------')
    print('----------------')
    print(News_dict)
    print('----------------')
    print('----------------')
    print(feature_Image_dict)
    print('----------------')
    print('----------------')
    print(weather_dict)
    print('----------------')
    print('----------------')
    print(full_hemisphere_dict)
    




    

    
    return redirect("http://localhost:5000/", code=302)




if __name__ == "__main__":
    app.run(debug=True)