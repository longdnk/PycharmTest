from flask import Flask, render_template

app = Flask(__name__)

# index page
@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html')

# accordion page
@app.route('/accordion')
@app.route('/accordion.html')
def accordion():
    return render_template('accordion.html')

# basic-table page
@app.route('/basic-table')
@app.route('/basic-table.html')
def basictable():
    return render_template('basic-table.html')

# 404 not found
@app.route('/404')
@app.route('/404.html')
def notfound_404():
    return render_template('404.html')

# booitss trap ui
@app.route('/bootstrap-ui')
@app.route('/bootstrap-ui.html')
def bootsrap_ui():
    return render_template('bootstrap-ui.html')

# box shadow
@app.route('/box-shadow')
@app.route('/box-shadow.html')
def box_shadow():
    return render_template('box-shadow.html')

# button
@app.route('/button')
@app.route('/button.html')
def button():
    return render_template('button.html')

# color
@app.route('/color')
@app.route('/color.html')
def color():
    return render_template('color.html')

# float chart
@app.route('/float-chart')
@app.route('/float-chart.html')
def float_chart():
    return render_template('float-chart.html')

# forgot-password
@app.route('/forgot-password')
@app.route('/forgot-password.html')
def forgot_password():
    return render_template('forgot-password.html')

# form-elements-advance
@app.route('/form-elements-advance')
@app.route('/form-elements-advance.html')
def form_elements_advance():
    return render_template('/form-elements-advance.html')

# form-elements-bootstrap
@app.route('/form-elements-bootstrap')
@app.route('/form-elements-bootstrap.html')
def form_elements_bootstrap():
    return render_template('/form-elements-bootstrap.html')

# label-badge
@app.route('/label-badge')
@app.route('/label-badge.html')
def label_badge():
    return render_template('/label-badge.html')

# light-box
@app.route('/light-box')
@app.route('/light-box.html')
def light_box():
    return render_template('/light-box.html')

# login1
@app.route('/login1')
@app.route('/login1.html')
def login1():
    return render_template('/login1.html')

# morris-chart
@app.route('/morris-chart')
@app.route('/morris-chart.html')
def morris_chart():
    return render_template('morris-chart.html')

# notification
@app.route('/notification')
@app.route('/notification.html')
def notification():
    return render_template('notification.html')

# panels-wells
@app.route('/panels-wells')
@app.route('/panels-wells.html')
def panels_wells():
    return render_template('/panels-wells.html')

# register1
@app.route('/register1')
@app.route('/register1.html')
def register1():
    return render_template('register1.html')

# sample-page
@app.route('/sample-page')
@app.route('/sample-page.html')
def sample_page():
    return render_template('sample-page.html')

# tabs
@app.route('/tabs')
@app.route('/tabs.html')
def tabs():
    return render_template('tabs.html')

# tooltips
@app.route('/tooltips')
@app.route('/tooltips.html')
def tooltips():
    return render_template('tooltips.html')

# typography
@app.route('/typography')
@app.route('/typography.html')
def typography():
    return render_template('typography.html')

if __name__ == "__main__":
    app.run(debug=True)