
# 🎬 Movie Reccomendation System - Content Based Filtering


_A content-based movie reccomender that suggests similar movies using NLP and Cosine Sinilarity.The system processes mmovie metadata such as overview, genres, cast, crew and keywords to recommend movie with similar content._

---

## 📌 Table of Contents
- <a href="#overview">Overview</a>
- <a href="#problem-statement">Problem-Statement</a>
- <a href="#dataset">Dataset</a>
- <a href="#tools--technologies">Tools & Technologies</a>
- <a href="#project-structure">Project Structure</a>
- <a href="#data-preprocessing">Data Preprocessing</a>
- <a href="#model-building">Model Building</a>
- <a href="#recommendation-System">Recommendation System</a>
- <a href="#streamlit-application">Streamlit Application</a>
- <a href="#how-to-run-this-project">How to Run This Project</a>
- <a href="#future-improvements">Future Improvements</a>
- <a href="#author--contact">Author & Contact</a>

---
<h2><a class="anchor" id="overview"></a>Overview</h2>

This project builds a content-based movie recommendation system using the TMDB 5000 movie dataset. The system analyzes movie attributes such as:
- Overview (movie-description)
- Genres
- Keywords
- Cast
- Crew (director)
These features are combined into a single text representation ("tags"), which iis then transformed into numerical vexctors using CountVectorizer. Movie similarity is calculated using Cosine Similarity, allowing the system to recommend movies similar to a selected one.

The project also includes a Streamlit web interface for interactive recommendation.

---
<h2><a class="anchor" id="problem-statement"></a>Problem-Statement</h2>

With thousands of movie available, user often struggle to discover new content that matches their preferences.

The goal of this project is to:
- Recommend movies based on similarity of content.
- Build an NLP pipeline to process movie metadata.
- Calculate similarity between movies using vectorization.
- Provide an interactive recommendation interface.
  
---
<h2><a class="anchor" id="dataset"></a>Dataset</h2>

The project uses the TMDB 5000 Movie Dataset, which contains metadata about movies including cast, crew, genres, keywords and overview.

Dataset files:
- tmdb_5000_movie.cvs
- tmd_5000_credits.csv
These datasets are merged and processed during prepocessing.

Dataset location:
dataset/raw/

---

<h2><a class="anchor" id="tools--technologies"></a>Tools & Technologies</h2>

Programming & Libraries
- Python
- Pandas
- Numpy
- Scikit-Learn
- NLTK

Machine Learning/NLP
- CountVecotrizer
- Cosine Similarity
- Porter Stemmer 

Application
- Steamlit

Others
- Pickle
- Jupyter Notebook (VS Code Jupyter Extension)
- Git & GitHub
  
---
<h2><a class="anchor" id="project-structure"></a>Project Structure</h2>

```
movie_reccomendation/
│
├── app/
│   └── streamlit_app.py        # Streamlit web application
│
├── dataset/
│   └── raw/                    # Original dataset files
│
├── models/
│   ├── model.pkl               # Cosine similarity matrix
│   └── movies.pkl              # Processed movie dataframe
│
├── notebook/
│   └── recommendation.ipynb    # Experimentation & model development
│
├── src/
│   ├── __init__.py
│   ├── predict.py              # Recommendation function
│   ├── preprocessing.py        # Data preprocessing pipeline
│   ├── train.py                # Model training pipeline
│   └── utils.py                # Text preprocessing utilities (stemming)
│
└── README.md

```

---
<h2><a class="anchor" id="data-preprocessing"></a>Data Preprocessing</h2>

The preprocessing pipeline prepares the dataset for the recommendation model.

Key steps include.
1. Data Merging
   - Merge movies and creadits datasets on the title column.

2. Feature Selection
   Selected columns:
   - movie_id
   - title
   - overview
   - genres
   - keywords
   - cast
   - crew

3. Handling Missing Values
   - Remoev rows with missing values.

4. Feature Conversion
   Columns such as genres, keywords, cast and crew converted into list using:
   - ast.literal_eval()

5. Feature Engineering
   Extracted important information:
   - Top 3 cast members
   - Director from crew

6. Text Processing
   - Convert overview to word lists
   - Remove spaces from names
   - Combine all features into a single tags column
   Example:
     overview + genres + keywords + cast + crew

7. Lowercasing
   All text convertedto lowercase to maintain consistency.

8. Stremming
   Appied Porter Stemmer to reduce words to root form.
   Eample:
     runnig -> run

---
<h2><a class="anchor" id="model-building"></a>Model Building</h2>

After preprocessing, the text features arre converted into numerical vectors.


**Count Vecorization:**
ContVectorizer(max_features=5000, stop_words='english)

This convert movies tags into 5000 dimentional feature vector.

Example:
  Movie Tags-> Text
  text -> Vector
  Vector -> Similarity

---
<h2><a class="anchor" id="recommendation-System"></a>Recommendation System</h2>

The recommendation system works using Cosine Similarity.
Cosine similarity measure the angle between two vectors.
Steps:
  - Convert movie tags into vectors.
  - Calculate cosine similarity between all movies.
  - Store similarity matrix.
  - Find the most similar movies.

Recommendation process:
  User selects movie
        ↓
  Find movie index
        ↓
  Get similarity scores
        ↓
  Sort movies by similarity
        ↓
  Return top 5 similar movies

---
<h2><a class="anchor" id="streamlit-application"></a>Streamlit Application</h2>

A simple Streamlit web application allows users to interact with the recommendation system.

Features:
  - Select a movie from dropdown
  - Clcik Recommend
  - Display top 5 simialr movies

Run interface:
  - streamlit run app/streamlit_app.py

---
<h2><a class="anchor" id="how-to-run-this-project"></a>How to Run This Project</h2>

1. Clone the repository:
```bash
git clone https://github.com/yourusername/movie-recommendation-system.git
```
2. Install Dependencies:
```bash
pip install -r requirements.txt
```
3. Train the Model
```bash
python src/train.py
```
This will generate:
  models/movies.pkl
  models/model.pkl
  
4. Run the Streamlit App:
```bash
streamlit run app/streamlit_app.py
```
5. Use the App:
  - Write the movie name
  - Click Recommend
  - Get simiar movie instantly
---
<h2><a class="anchor" id="future-improvements"></a>Future Improvements</h2>

- Add movie posters 
- Deploy application cloud
- Imrove recommendation system using TF-IDF
- Include user rating and collaboration filtering

---
<h2><a class="anchor" id="author--contact"></a>Author & Contact</h2>

**Ritresh Kumar**  
BCA Student | Aspiring Data Scientist 

Skills:
- Python  
- Machine Learning  
- Natural Language Processing  
- Data Analysis  
- Deep Learning 
📧 Email: ritresh273@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/feed/)  
🔗 [GitHub](https://github.com/Ritresh/Ritresh)
