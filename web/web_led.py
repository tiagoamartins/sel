from gpiozero import LED
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


# Create a dictionary called pins to store the pin number, name, and pin state:
pins = {
    'coffee maker': LED(24),
    'lamp': LED(25)
}

# Set each pin as an output and make it low:
for pin in pins.values():
    pin.off()


@app.route("/", methods=['GET', 'POST'])
def main():
    # Pass the template data into the template web_led.html
    # and return it to the user
    if request.method == 'GET':
        return render_template('web_led.html', pins=pins)

    for btn, value in request.form.items():
        return redirect(url_for('action', name=btn, action=value))


# The function below is executed when someone requests a URL
# with the pin number and action in it:
@app.route("/<name>/<action>")
def action(name, action):
    # Convert the pin from the URL into an integer:
    pin_name = name.replace("_", " ")
    pin = pins[pin_name]
    # If the action part of the URL is "on," execute the code indented below:
    if action == "on":
        pin.on()
        # Save the status message to be passed into the template:
        message = "Turned " + pin_name + " on."
    if action == "off":
        pin.off()
        message = "Turned " + pin_name + " off."
    if action == "toggle":
        # Read the pin and set it to whatever it isn't (that is, toggle it):
        pin.toggle()
        message = "Toggled " + pin_name + "."

    # Along with the pin dictionary, put the message
    # into the template data dictionary:
    data = {
        'message': message,
        'pins': pins
    }

    return render_template('web_led.html', **data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
