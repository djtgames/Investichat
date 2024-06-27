Investichat



app.py:

This is the main Flask application file where the backend logic resides.
It defines routes (/, /api/get_openai_response) and handles HTTP requests.
The application integrates with OpenAI's API to generate AI responses based on user input.
It also includes a web scraping function to fetch financial news headlines from Yahoo Finance based on user queries.
Responses from OpenAI and scraped news headlines are combined and returned as JSON data to the frontend.
templates/:

This directory contains the HTML templates used by Flask for rendering web pages.
index.html is the template for the chat interface, styled with CSS and enhanced with JavaScript for user interaction.
It includes a chat box where messages (both user and bot responses) are displayed dynamically.
An input field allows users to type messages and a send button triggers sending the message to the Flask backend.
.env:

This file stores sensitive environment variables, such as the OpenAI API key (OPENAI_API_KEY).
It is loaded into the Flask application using the dotenv module to keep sensitive information secure.
Functionality Overview
User Interface (index.html):

Provides a clean and responsive chat interface styled with CSS.
Uses JavaScript to handle user interactions, such as sending messages and displaying responses.
Backend (app.py):

Flask Routes:
/: Renders the index.html template to display the chat interface.
/api/get_openai_response (POST method):
Receives JSON data containing the user's message from the frontend.
Sends the user's message to OpenAI's API (davinci engine) to generate an AI response.
Uses web scraping to fetch relevant financial news headlines from Yahoo Finance based on the user's query.
Combines the AI-generated response and scraped news headlines into a JSON object.
Returns the combined JSON object as the HTTP response.
Integration with OpenAI:

Uses the requests module to send HTTP POST requests to OpenAI's API endpoint (https://api.openai.com/v1/engines/davinci/completions).
Includes the OpenAI API key in the request headers for authentication (Authorization: Bearer {OPENAI_API_KEY}).
Processes the response to extract and format the AI-generated message from OpenAI.
Web Scraping with BeautifulSoup:

Utilizes requests to fetch HTML content from Yahoo Finance's news search page (https://finance.yahoo.com/news/search/?q={query}).
Parses the HTML content using BeautifulSoup to extract relevant news headlines (h3.title elements).
Returns a list of the top 3 headlines related to the user's query.
Notes
Security: Ensure to securely manage and protect sensitive information such as API keys (OPENAI_API_KEY) and other credentials.
Error Handling: Implement robust error handling to manage potential exceptions during HTTP requests, API responses, and web scraping operations.
Scalability: Consider scaling the application by optimizing performance, caching responses, and potentially deploying it on a cloud platform for reliability and scalability.
This setup provides a comprehensive structure for building a Flask-based chatbot application that integrates AI-powered responses from OpenAI and real-time web scraping of financial news from Yahoo Finance, enhancing user engagement with up-to-date information and responses tailored to their queries.







