import streamlit as st

from recommender import recommend,df
from llm import explain_recommendation

@st.cache_data
def get_explanation(
    user_profile,
    issue_title,
    issue_text
):
    return explain_recommendation(
        user_profile,
        issue_title,
        issue_text
    )

st.title("Open Source Issue Recommender")
st.write("Find GitHub issues that match your skills and interests")

skills= st.text_input("Skills")
experience= st.selectbox("Experience Level",["Beginner","Intermediate","Advanced"])
interests=st.text_input("Interests")
user_profile=(skills+" "+experience+" "+interests)

if st.button("Recommend issues",disabled=not(skills.strip() or interests.strip())):
    top_indices, scores= recommend(skills,experience,interests)

    st.subheader("Recommended issues")

    for idx in top_indices:

        with st.container(border=True):

            st.subheader(df.iloc[idx]["title"])

            st.write(f"Repository: {df.iloc[idx]["repo"]}")
            st.metric("Similarity",f"{scores[idx]*100:.2f}%")
            with st.expander("Why Recommended?"):
                issue_title=df.iloc[idx]["title"]
                issue_text=(str(df.iloc[idx]["title"])+" "+str(df.iloc[idx]["body"])+" "+str(df.iloc[idx]["labels"]))

                explanation= get_explanation(user_profile, issue_title, issue_text)

                st.write(explanation)
            st.link_button("Visit issue",df.iloc[idx]["url"])