import streamlit as st
from transformers import pipeline

from src.preprocess import clean_review

SENTIMENT_MODEL = "MoritzLaurer/mDeBERTa-v3-base-xnli-m multilingual-nli-2mil7".replace(" ", "")


@st.cache_resource
def _get_classifier():
    """Load the model once per Streamlit process, using CPU-only inference."""
    return pipeline(
        "zero-shot-classification",
        model=SENTIMENT_MODEL,
        device=-1,
    )


def analyze_review(raw_text: str) -> dict:
    cleaned_text = clean_review(raw_text)
    classifier = _get_classifier()

    sentiment_labels = ["positive review", "negative review", "neutral review"]
    sentiment_res = classifier(cleaned_text, candidate_labels=sentiment_labels)
    top_sentiment = sentiment_res["labels"][0].replace(" review", "").capitalize()
    confidence = round(sentiment_res["scores"][0] * 100, 1)

    topic_labels = [
        "delivery and shipping",
        "product quality",
        "mpesa and payment",
        "customer service",
    ]
    topic_res = classifier(cleaned_text, candidate_labels=topic_labels)
    top_topic = topic_res["labels"][0].title()

    return {
        "original_text": raw_text,
        "cleaned_text": cleaned_text,
        "sentiment": top_sentiment,
        "confidence": confidence,
        "category": top_topic,
    }
