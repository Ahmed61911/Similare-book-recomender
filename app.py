import pickle
import streamlit as st
import numpy as np

st.header("Projet Data mining: Systeme de recommendation des livres")

model = pickle.load(open('artifacts/model.pkl', 'rb'))
books_name = pickle.load(open('artifacts/books_name.pkl', 'rb'))
final_rating = pickle.load(open('artifacts/final_rating', 'rb'))
book_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb'))

suggetions_number = 9

def calculate_score(row):
    score = (row['rating'] * 0.7) + (row['num_of_rating'] * 0.3)
    return score

def fetch_poster(suggestion):
    book_name = []
    id_index = []
    poster_url = []

    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])

    for i in book_name[0] :
        id = np.where(final_rating['title'] == i)[0][0]   
        id_index.append(id)

    for ids in id_index:
        url = final_rating.iloc[ids]['img_url']
        poster_url.append(url)
    
    return poster_url


def recommend_books(book_name):
    book_list = []
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors= suggetions_number + 1 )
    
    poster_url = fetch_poster(suggestion)

    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for j in books:
            book_list.append(j)
    return book_list, poster_url

selected_books = st.selectbox(
    "Chercher un livre:",
    books_name
)

if st.button("Afficher les recommendation"):
    recommendations_books, poster_url = recommend_books(selected_books)
    for i in range(0, suggetions_number, 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < suggetions_number:
                with col:
                    st.text(recommendations_books[i + j])
                    st.image(poster_url[i + j], width=120)