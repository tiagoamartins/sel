from gpiozero import LED
from flask import Blueprint, render_template, request, redirect, url_for, flash

bp = Blueprint('project', __name__, url_prefix='/project')

coffee = LED(24)
lamp = LED(25)

leds = {
    'coffee maker': coffee,
    'lamp': lamp
}


@bp.route('/', methods=['GET', 'POST'])
def project():
    if request.method == 'GET':
        return render_template('project.html', leds=leds)

    for btn, value in request.form.items():
        return redirect(url_for('.action', name=btn, action=value))


# The function below is executed when someone requests a URL
# with the pin number and action in it:
@bp.route('/<name>/<action>')
def action(name, action):
    # Convert the pin from the URL into an integer:
    led_name = name.replace('_', ' ')
    led = leds[led_name]

    # If the action part of the URL is "on," execute the code indented below:
    if action == 'on':
        led.on()
        # Save the status message to be passed into the template:
        flash('Turned ' + led_name + ' on.', 'success')
    elif action == "off":
        led.off()
        flash('Turned ' + led_name + " off.", 'danger')
    elif action == 'toggle':
        # Read the pin and set it to whatever it isn't (that is, toggle it):
        led.toggle()
        flash('Toggled ' + led_name + '.', 'info')

    return redirect(url_for('.project'))
