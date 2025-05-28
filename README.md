# 🎌 Anime Recommender System 🎥

An intelligent recommendation system built using **Python**, **Machine Learning**, and **Streamlit** that suggests the top 20 most similar anime based on user input. The app also provides **trailers via YouTube**, offering an engaging user experience.

[![Watch the Demo Video](https://img.shields.io/badge/Watch-Demo%20Video-red?style=for-the-badge&logo=youtube)](https://drive.google.com/file/d/1yy45KNDyu7gMazjjEhgI55odh37RUcWu/view?usp=drive_link)

---

## 🔍 Features

- 🔁 **Recommends 20 similar anime** based on your favorite.
- 🧠 Powered by **Machine Learning**, using TF-IDF and Cosine Similarity.
- 🎞️ **Watch trailers instantly** via YouTube integration.
- 💻 **Interactive Streamlit UI** for smooth and intuitive user interaction.
- 🌐 Exposed as a **REST API** for integration and extension.

---

## 📸 Screenshot

![Anime Recommender Screenshot] ![image](https://github.com/user-attachments/assets/c0e42017-3d9c-41a3-a9a7-cea3931eeb88)
 <!-- Replace with your actual screenshot URL -->

---

## 🧠 Tech Stack

| Tool / Library      | Purpose                              |
|---------------------|--------------------------------------|
| **Python**          | Core language                        |
| **pandas / numpy**  | Data processing                      |
| **scikit-learn**    | TF-IDF Vectorizer + Cosine Similarity|
| **Streamlit**       | Frontend UI                          |
| **YouTube Data API**| Fetching trailers                    |
| **Flask (Optional)**| REST API backend                     |

---

## ⚙️ How It Works

1. **Data Preprocessing**:  
   Cleaned and processed anime data (genre, synopsis, etc.)

2. **Text Vectorization**:  
   Used `TfidfVectorizer` to convert textual data into numerical form.

3. **Similarity Calculation**:  
   Computed pairwise similarity using `cosine_similarity()`.

4. **Recommendation Engine**:  
   When a user selects an anime, it returns the **top 20 similar titles**.

5. **Trailer Fetching**:  
   Automatically searches YouTube and embeds trailers in the UI.

---

## 🚀 Getting Started

### 🔧 Prerequisites

```bash
pip install -r requirements.txt
