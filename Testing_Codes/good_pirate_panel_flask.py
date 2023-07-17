import os
import openai
import panel as pn
from dotenv import load_dotenv, find_dotenv
from flask import Flask
import concurrent.futures

_ = load_dotenv(find_dotenv())  # read local .env file
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def collect_messages(event):
    prompt = inp.value
    inp.value = ''
    context.append({'role': 'user', 'content': f"{prompt}"})
    panels[0][1] = pn.pane.Markdown(prompt, width=600)  # Update the user message
    response = get_completion_from_messages(context)
    context.append({'role': 'assistant', 'content': f"{response}"})
    panels[1][1] = pn.pane.Markdown(response, width=600, styles={'background-color': '#F6F6F6'})  # Update the assistant message
    text_pane.object = f"Chat Button Clicked {len(context)} times."

pn.extension()

inp = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')
button_conversation = pn.widgets.Button(name="Chat!")
text_pane = pn.pane.Str("Button clicked 0 times.")

button_conversation.on_click(collect_messages)

context = [{'role': 'system', 'content': """
Act like a viking pirate, talk like a one too."""}
        ]  # accumulate messages

panels = [
    pn.Row('User:', pn.pane.Markdown("", width=600)),
    pn.Row('Assistant:', pn.pane.Markdown("", width=600, styles={'background-color': '#F6F6F6'}))
]

dashboard = pn.Column(
    inp,
    pn.Row(button_conversation),
    pn.panel(text_pane, loading_indicator=True, height=300),
    *panels,
)

app = Flask(__name__)

@app.route('/')
def serve_dashboard():
    # Display the Panel dashboard using .show() instead of pn.serve()
    dashboard.show(title="Chatbot Dashboard")
    return pn.pane.HTML("")

if __name__ == "__main__":
    app.run(host='localhost', port=5999, debug=True)

