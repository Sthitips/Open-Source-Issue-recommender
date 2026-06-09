# Open Source Issue Recommender

## Overview
An AI-powered recommendation system that helps developers discover relevant GitHub issues based on their skills and interests.

## Features
- GitHub API integration
- Semantic search using Sentence Transformers
- Cosine similarity-based retrieval
- Gemini-powered recommendation explanations
- Interactive Streamlit interface

## Tech Stack
- Python
- Streamlit
- Sentence Transformers
- Scikit-learn
- Gemini API
- Pandas

## How It Works
1. Collect GitHub issues from multiple repositories
2. Generate embeddings for issue descriptions
3. Generate embedding for user profile
4. Compute cosine similarity
5. Return top matching issues
6. Generate AI explanations using Gemini

## Installation

pip install -r requirements.txt

streamlit run app.py
