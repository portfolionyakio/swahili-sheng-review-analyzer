import streamlit as st

from src.predict import analyze_review


st.set_page_config(page_title="Swahili-Sheng Review Analyzer", page_icon="🛍️")
st.title("Swahili-Sheng Review Analyzer")
st.write("Analyze the sentiment and topic of an e-commerce review.")

with st.form("review_form"):
    review = st.text_area("Enter a review", placeholder="Andikeni review hapa...")
    submitted = st.form_submit_button("Analyze review")

if submitted:
    if not review.strip():
        st.warning("Please enter a review before analyzing it.")
    else:
        try:
            result = analyze_review(review)
        except Exception as exc:
            st.error(f"The review could not be analyzed: {exc}")
        else:
            sentiment_col, confidence_col, category_col = st.columns(3)
            sentiment_col.metric("Sentiment", result["sentiment"])
            confidence_col.metric("Confidence", f"{result['confidence']}%")
            category_col.metric("Topic", result["category"])
            st.caption("Normalized review")
            st.write(result["cleaned_text"])
