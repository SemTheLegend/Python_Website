from flask import render_template
from __init__ import create_app

app = create_app()


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)
    