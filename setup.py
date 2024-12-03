from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

REPO_NAME = "Book-Recommendation-System"
AUTHOR_USER_NAME = "Ahmed"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit', 'numpy']


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="Book recommender system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/Ahmed61911/Similare-book-recomender",
    author_email="ahmed.baba.ab.96@gmail.com",
    packages=[SRC_REPO],
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)
