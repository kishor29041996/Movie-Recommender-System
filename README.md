## 🎬 Movie Recommender System

## 📌 Project Overview

This project is a Content-Based Movie Recommender System built using the TMDB (The Movie Database) 5000 Movies Dataset. The recommendation engine suggests movies that are similar to a selected movie by analyzing features such as genres, keywords, cast, crew, and movie overview.

The project demonstrates the complete machine learning workflow, including data preprocessing, feature engineering, vectorization, similarity computation, and recommendation generation.

## 🚀 Features
- Content-Based Recommendation System
- Movie recommendations based on similarity
- Uses movie metadata instead of user ratings
- Interactive movie search
- Fast similarity lookup using cosine similarity
- Clean and simple interface (if deployed with Streamlit)

## 📂 Dataset
Dataset used:

- TMDB 5000 Movies Dataset
- TMDB 5000 Credits Dataset

Files:
- tmdb_5000_movies.csv
- tmdb_5000_credits.csv

## Main attributes used:
- Title
- Genres
- Keywords
- Overview
- Cast
- Crew (Director)

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Pickle
- Streamlit (Optional for deployment)
- Colab Notebook

## 📊 Project Workflow
# 1. Data Collection

  Load both TMDB datasets.
- movies = pd.read_csv("tmdb_5000_movies.csv")
- credits = pd.read_csv("tmdb_5000_credits.csv")
  
#2. Data Preprocessing
- Merge movies and credits datasets
-Handle missing values
- Remove unnecessary columns
-Extract useful information from JSON-like columns

# 3. Feature Engineering
   
Extract:
- Top 3 Cast Members
- Director
- Genres
- Keywords
- Overview
Create a combined feature called Tags.

Example:
Action Adventure Hero Space Alien JamesCameron SamWorthington

# 4. Text Processing
- Convert text to lowercase
- Remove spaces
- Apply stemming using Porter Stemmer

Example:

- Running
- Runs
- Runner

↓

- run
- run
- runner
  
# 5. Vectorization
   
Convert movie tags into numerical vectors using:
- CountVectorizer

# Parameters:
- max_features = 5000
- stop_words = 'english'
  
# 6. Similarity Calculation
Compute cosine similarity between movie vectors.

from sklearn.metrics.pairwise import cosine_similarity

Result:

Similarity Matrix
Every movie gets a similarity score with every other movie.

# 7. Recommendation Function

Input:
Movie Name

Output:
Top 4 most similar movies.

Example:

Input:
Avatar

Recommendations:

- Titanic
- John Carter
- Guardians of the Galaxy
- Star Trek
- The Fifth Element

# 📁 Project Structure

```text
Movie-Recommender-System/
│
├── .gitattributes          # Git attributes configuration
├── .gitignore              # Files ignored by Git
├── Procfile                # Deployment configuration (Render/Heroku)
├── app.py                  # Streamlit application
├── movies.pkl              # Preprocessed movie metadata
├── similarity.pkl          # Cosine similarity matrix
├── requirements.txt        # Python dependencies
├── runtime.txt             # Python runtime version
├── setup.sh                # Deployment setup script
└── README.md               # Project documentation
```
## 🧠 Machine Learning Concepts Used
- Content-Based Filtering
- Natural Language Processing (NLP)
- Feature Engineering
- Count Vectorization
- Cosine Similarity
- Text Preprocessing
- Stemming

## 🎯 Learning Outcomes

This project demonstrates practical skills in:
- Data preprocessing
- Feature engineering
- NLP techniques
- Recommendation system development
- Similarity-based machine learning
- Model serialization using Pickle
- Streamlit application deployment

## 📈 Future Improvements
- Hybrid recommendation system (Content + Collaborative Filtering)
- Movie poster integration using TMDB API
- Movie trailer support
- Personalized recommendations
- Genre-based filtering
- Similarity explanation (why a movie was recommended)
  
## 👤 Author
Kishor

Aspiring Data Scientist | Machine Learning | Deep Learning | NLP | Generative AI

If you found this project useful, consider giving the repository a ⭐ on GitHub.
