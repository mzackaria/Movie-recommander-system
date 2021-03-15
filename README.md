## IMDB database - Build a personalized movie recommender system



This project is about building a movie recommender system based on the IMDB dataset. A few clusering  method are exposed and the K-means algorithm has been chosen to expose our solution: **building a personable movie recommender system**. 



You will find in this project:



  - An [EDM notebook](https://github.com/mzackaria/Movie-recommander-system/blob/master/notebooks/Movie%20Recommendation%20System%20-%20EDA%20-%20Part%201.ipynb)



  - A [research notebook](https://github.com/mzackaria/Movie-recommander-system/blob/master/notebooks/Movie%20recommendation%20system%20study%20-%20Part%202.ipynb) -  **'Movie recommendation system study - Part 2'**: toward finding a personable recommendation system,  how to go beyond applying a simple black box solution to actually make the data fit the problem at hand. If you are looking for a way to improve your item to item recommendation system you can look at the section **"Improvement of the model"**. 



  - The [code](https://github.com/mzackaria/Movie-recommander-system/tree/master/code) to preprocess the data and run the model

    

  - Slides to present the work that has been done. Video : https://youtu.be/k47at5Dl-Ag



  If you want to test the recommender ti is exposed at the REST API (takes a little bit to load for the first time) :  https://best-recommender.herokuapp.com/recommend/1

 **number = film_id**, change it if you want to make another prediction.



examples: 

https://best-recommender.herokuapp.com/recommend/1

```
{
  "film": {
    "id": "1", 
    "title": "Pirates of the Caribbean: At World's End"
  }, 
  "results": [
    {
      "id": "54", 
      "title": "Indiana Jones and the Kingdom of the Crystal Skull"
    }, 
    {
      "id": "1180", 
      "title": "The Medallion"
    }, 
    {
      "id": "163", 
      "title": "Gods of Egypt"
    }, 
    {
      "id": "2751", 
      "title": "Dungeons & Dragons: Wrath of the Dragon God"
    }, 
    {
      "id": "831", 
      "title": "Ghost Rider: Spirit of Vengeance"
    }
  ]
}
```

![Pirates of the Caribbean: At World's End]

https://github.com/mzackaria/Movie-recommander-system/blob/dev/images/[5.jpg](https://github.com/mzackaria/Movie-recommander-system/blob/dev/images/5.jpg)

