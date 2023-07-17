import panel as pn
from flask import Flask, render_template_string

app = Flask(__name__)

# Create a counter to keep track of button clicks
click_count = 0

# Function to update the text when the button is clicked
def on_button_click(event):
    global click_count
    click_count += 1
    text.object = f"Button clicked {click_count} times."

# Create the Panel widgets
button = pn.widgets.Button(name="Click Me!")
text = pn.pane.Str("Button clicked 0 times.")

# Bind the button click event to the function
button.on_click(on_button_click)

# Create the Panel layout
dashboard = pn.Column(
    text,
    button,
)

# Serve the Panel dashboard as a standalone server
panel_server = pn.serve(dashboard, show=False, title="Button Click Counter")

# Flask route to serve the dashboard
@app.route("/")
def serve_dashboard():
    return render_template_string('<iframe src="/panel" width="800" height="400" style="border: none;"></iframe>')

# Flask route to serve the embedded Panel dashboard
@app.route("/panel")
def serve_panel():
    return panel_server.modify_doc()

if __name__ == "__main__":
    app.run(debug=True)

