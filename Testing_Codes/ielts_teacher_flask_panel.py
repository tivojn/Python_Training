from flask import Flask, render_template, request
import panel as pn
import openai

# Set the OpenAI API key
openai.api_key = "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"

# Your existing functions and code...
# (get_completion_from_messages, collect_messages, etc.)
def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,  # this is the degree of randomness of the model's output
    )
    #     print(str(response.choices[0].message))
    return response.choices[0].message["content"]


def collect_messages(_):
    prompt = inp.value_input
    inp.value = ''
    
    context.append({'role': 'user', 'content': f"{prompt}"})
    response = get_completion_from_messages(context)
    context.append({'role': 'assistant', 'content': f"{response}"})
    panels.append(
        pn.Row('Stan_gary_teresa_as_User:', pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row('IELTS_teacher_as_Assistant:', pn.pane.Markdown(response, width=600, styles={'background-color': '#F6F6F6'})))

    return pn.Column(*panels)

# Create the Flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def chat():
    global context, panels, inp, button_conversation, interactive_conversation, dashboard

    if request.method == 'POST':
        user_input = request.form['user_input']
        context.append({'role': 'user', 'content': user_input})
        try:
            response = get_completion_from_messages(context)
        except openai.error.APIConnectionError:
            return "Error communicating with OpenAI. Please try again later."
        context.append({'role': 'assistant', 'content': response})
        panels.append(pn.Row('Stan_gary_teresa_as_User:', pn.pane.Markdown(user_input, width=600)))
        panels.append(pn.Row('IELTS_teacher_as_Assistant:', pn.pane.Markdown(response, width=600, styles={'background-color': '#F6F6F6'})))
        content = pn.Column(*panels).get_root()
        return render_template('index.html', content=content.decode())

    # If it's a GET request, initialize the conversation
    context = [{'role': 'system', 'content': """
    Act as a senior IELTS teacher, \
    you will assist the user in improving the user’s IELTS speaking skills. \
    You can conduct a mock IELTS Speaking test with the user, provide feedback and guidance, \
    and help the user identify areas of strength and weakness. \
    You can also provide the user with tips and strategies to improve the user performance in the test.
    """}]

    inp = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')
    button_conversation = pn.widgets.Button(name="Chat!")

    interactive_conversation = pn.bind(collect_messages, button_conversation)

    dashboard = pn.Column(
        pn.panel(interactive_conversation, loading_indicator=False, height=300),
        inp,
        pn.Row(button_conversation),
    )

    content = pn.Column(*panels).get_root()
    return render_template('index.html', content=content.decode())

if __name__ == "__main__":
    app.run(debug=True)
