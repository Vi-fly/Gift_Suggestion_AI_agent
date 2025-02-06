# Personalized Gift Suggestion App

A web-based app built with Streamlit that provides personalized gift suggestions based on a person's age, gender, occasion, hobbies, and budget. The app uses an AI agent powered by Groq for generating suggestions, and DuckDuckGo for web search.

## Features

- Provide personalized gift suggestions based on:
  - Age
  - Gender
  - Occasion
  - Hobbies and Interests
  - Budget
- Use of DuckDuckGo to gather relevant gift ideas.
- Display suggestions in a formatted way for easy readability.

## Requirements

- Python 3.8+
- Required packages listed in `requirements.txt`

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/personalized-gift-suggestion-app.git
   ```

2. Navigate to the project directory:

   ```bash
   cd personalized-gift-suggestion-app
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Add your environment variables (e.g., API keys) to a `.env` file in the root directory.

## Running the App

To run the Streamlit app locally, use the following command:

```bash
streamlit run app.py
```
5. Set up environment variables in a .env file in the root directory. Add the following variables:

Example .env file:
```bash
GROQ_API_KEY - Your own Groq API key to use the Groq model.
DUCKDUCKGO_API_KEY - Your DuckDuckGo API key (if needed).
```
Make sure you replace your_groq_api_key with your actual key.

This will start the app and open it in your default web browser.

## How it Works

The app provides a form where users can enter the following information:
- Age
- Gender
- Occasion
- Hobbies and interests
- Budget

Once the form is submitted, the app will use an AI agent to generate personalized gift suggestions based on the input. The suggestions are gathered using DuckDuckGo, and the app processes the results to clean up any irrelevant content and format the suggestions in a readable manner.

## Code Overview

- **app.py**: The main application script that handles the Streamlit UI and integrates with the AI agent for gift suggestion generation.
- **requirements.txt**: A file that lists the required dependencies for the project.
- **.env**: A file to store environment variables like API keys.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Groq](https://groq.com) for the AI model used for generating gift suggestions.
- [DuckDuckGo](https://duckduckgo.com) for the search tool used to gather gift ideas.

## Contributions

Feel free to submit issues and pull requests to improve this project. Contributions are welcome!
