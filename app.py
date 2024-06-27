import os
os.system("Flask, request, jsonify, render_template, bs4, requests")
from flask import Flask, request, jsonify, render_template

import requests
from bs4 import BeautifulSoup


app = Flask(__name__)
app.config['SECRET_KEY'] = 'JnIwaZG7ps'  # Replace with a secure secret key

# Load your OpenAI API key and other necessary variables from environment variable

openai_api_key = 'sk-proj-Ep1gJhWNJDXLdJd8OQbeT3BlbkFJ7RUiHt3prcHn6pVEABru'
openai_api_url = "https://api.openai.com/v1/engines/davinci/completions"

def scrape_yahoo_finance_news(query):
    url = f'https://finance.yahoo.com/news/search/?q={query}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        news_headlines = [headline.text.strip() for headline in soup.select('h3.title')]
        return news_headlines[:3]  # Return top 3 headlines
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/get_openai_response', methods=['POST'])
def get_openai_response():
    data = request.json
    user_message = data.get('message')
    
    # Get AI response from OpenAI
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {openai_api_key}',
    }
    payload = {
        'prompt': f"User: {user_message}\nAI:",
        'max_tokens': 150
    }
    
    try:
        response = requests.post(openai_api_url, headers=headers, json=payload)
        response.raise_for_status()
        ai_message = response.json()['choices'][0]['text'].strip()
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500
    except KeyError as e:
        return jsonify({'error': f'Unexpected response format from OpenAI: {str(e)}'}), 500
    
    # Scrape financial news related to user's query from Yahoo Finance
    scraped_news = scrape_yahoo_finance_news(user_message)
    
    # Prepare response
    response_data = {
        'ai_response': ai_message,
        'scraped_news': scraped_news
    }
    
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
