# query_gpt.py

import openai
import os
from ttl_ontology import ontology_data
from openai import OpenAI


openai.api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI()

def query_gpt_with_ttl_ontology(question):

    messages = [
        {"role": "system", "content": "Write a SPARQL query that answers the question. Do not explain the query. Return just the query, so it can be run verbatim from your response."},
        {"role": "system", "content": ontology_data},
        {"role": "user", "content": question}
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=messages,
            temperature=0.3,
            max_tokens=2048,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        assistant_message_content = response.choices[0].message.content
        return assistant_message_content
    except Exception as e:
        print(f"An error occurred: {e}")
        return None