import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

df=pd.read_csv("og_issues.csv")

df["text"]= (df["title"].fillna(" ")+" "+df["body"].fillna(" ")+" "+df["labels"].fillna(" "))

model=SentenceTransformer("all-MiniLM-L6-v2")

issue_embeddings= model.encode(df["text"].tolist())

def recommend(skills, experience,interest):

    user_profile= (skills+" "+experience+" "+interest)

    user_embedding= model.encode(user_profile)

    scores= cosine_similarity(
        [user_embedding],
        issue_embeddings
    )[0]

    top_indices= scores.argsort()[::-1][:5]

    return top_indices,scores

if __name__=="__main__":
    skills=input("Skills: ")
    experience=input("Experience: ")
    interest=input("Interests: ")

    top_indices, scores= recommend(skills,experience,interest)

    for idx in top_indices:
        print("="*50)

        print("Title:")
        print(df.iloc[idx]["title"])

        print("\nRepo:")
        print(df.iloc[idx]["repo"])

        print("\nSimilarity:")
        print(f"{scores[idx]*100:.2f} %")

        print("\nURL:")
        print(df.iloc[idx]["url"])

        print()