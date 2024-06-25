
import streamlit as st
import spacy
import pickle

# Download and load spaCy model
import spacy.cli
spacy.cli.download('en_core_web_sm')
nlp = spacy.load('en_core_web_sm')

# Load processed data
with open('processed_data.pkl', 'rb') as f:
    processed_data = pickle.load(f)

# Function to summarize text using TextRank algorithm
def summarize(text, ratio=0.2):
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    num_sentences = max(1, int(len(sentences) * ratio))
    summary_sentences = sentences[:num_sentences]  # Simple selection of sentences for demonstration
    summary = ' '.join(summary_sentences)
    return summary

# Streamlit interface
st.title('Text Summarization app.')

method = st.selectbox('Choose a method', ['Summarize Paragraph'])

if method == 'Summarize Paragraph':
    paragraph = st.text_area('Enter a paragraph to summarize')

    if st.button('Summarize'):
        if paragraph:
            summary = summarize(paragraph)
            st.write('**Summary:**')
            st.write(summary)
        else:
            st.write('Please enter a paragraph.')

# Additional methods can be added here similarly
