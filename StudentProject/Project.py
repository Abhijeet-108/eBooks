import streamlit as st
import glob
import plotly.express as px

from nltk.sentiment.vader import SentimentIntensityAnalyzer

filepaths = sorted(glob.glob("diary/*.txt"))

analyzer = SentimentIntensityAnalyzer()

negative = []
postive = []
for filepath in filepaths:
    with open(filepath) as file:
        content = file.read()
    scores = analyzer.polarity_scores(content)
    postive.append(scores["pos"])
    negative.append(scores["neg"])

dates = [name.strip(".txt").strip("diary/") for name in filepaths]

st.title("Diary Tone")
st.subheader("Postivity")
pos_figure = px.line(x=dates,y=postive,labels={"x":"Dates","y":"Positivity"})
st.plotly_chart(pos_figure)

st.subheader("Negativity")
neg_figure = px.line(x=dates,y=negative,labels={"x":"Dates","y":"Negativity"})
st.plotly_chart(neg_figure)