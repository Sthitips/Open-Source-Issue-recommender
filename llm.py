import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key= os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model=genai.GenerativeModel("gemini-2.5-flash")

def explain_recommendation(user_profile, issue_title, issue_text):
    prompt=f"""You are helping explain why a github issue was recommended.
    
    User profile:
    {user_profile}

    Issue Title:
    {issue_title}

    Issue description:
    {issue_text}

    Explain in EXACTLY 2 concise bullet points why this issue is relevant to the user.
    
    Do not mention embeddings, cosine similarity, vectors or recommendation systems."""

    response=model.generate_content(prompt)

    return response.text

if __name__ == "__main__":

    result = explain_recommendation(
        "Python Machine Learning Beginner",
        "Improve TensorFlow Training",
        "Optimize model training performance"
    )

    print(result)