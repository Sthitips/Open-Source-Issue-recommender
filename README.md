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

## Demonstration
<img width="1764" height="940" alt="image" src="https://github.com/user-attachments/assets/aaf09e4b-d19a-42d3-8030-82db03ac9a99" />
<img width="1712" height="1242" alt="image" src="https://github.com/user-attachments/assets/4b20f7b0-f7c8-42af-b719-e5427a1cb86c" />



## Installation

pip install -r requirements.txt

streamlit run app.py
