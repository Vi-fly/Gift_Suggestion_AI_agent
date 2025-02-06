from dotenv import load_dotenv
import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
import re

# Load environment variables
load_dotenv()

# Define the Gift Suggestion Agent
gift_suggestion_agent = Agent(
    name="Gift Suggestion Agent",
    role="Provide personalized gift suggestions",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=[
        """Consider the person's age, gender, occasion, hobbies, interests, and budget. Use the DuckDuckGo tool to search for relevant gift ideas. Provide a list of gift suggestions tailored to the provided information. Include a brief explanation and source for each suggestion. Ensure the suggestions are appropriate for the specified occasion and within the budget range."""
    ],
    markdown=True,
)

def clean_output(output):
    # Regular expression to remove content between "## Instructions" and the next "##"
    output = re.sub(r'## Instructions.*?##', '', output, flags=re.DOTALL)
    
    # Remove everything from "name=None" and onwards
    output = re.sub(r'name=None.*', '', output, flags=re.DOTALL)
    
    return output

def main():
    st.title("Personalized Gift Suggestion with Web Search( AI Agent )")

    with st.form(key='gift_form'):
        age = st.number_input("Enter the person's age:", min_value=0, max_value=120, step=1)
        gender = st.selectbox("Select the person's gender:", options=["Male", "Female", "Other"])
        occasion = st.text_input("Enter the occasion:")
        hobbies = st.text_area("Enter the person's hobbies and interests (optional):")
        budget = st.text_input("Enter your budget range in INR (e.g., 500-1000):")
        submit_button = st.form_submit_button(label='Get Gift Suggestions')

    if submit_button:
        prompt = (
            f"Suggest gift ideas for a {age}-year-old {gender} for {occasion}."
            f" Hobbies and interests: {hobbies if hobbies else 'Not specified'}."
            f" Budget: {budget} INR."
        )
        try:
            # Get assessment result as a string
            suggestions = gift_suggestion_agent.run(prompt)
            assessment_str = str(suggestions)
            if assessment_str.startswith("content="):
                assessment_str = assessment_str.replace('content="', "", 1)

            # Clean up the output by removing the "## Instructions" section and content after "name=None"
            cleaned_assessment_str = clean_output(assessment_str)

            # Clean and decode the assessment string for display
            cleaned_assessment_str = cleaned_assessment_str.encode('utf-8').decode('unicode-escape')

            # Display the cleaned response
            st.subheader("Gift Suggestions")
            st.balloons()
            st.markdown(cleaned_assessment_str)

        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
