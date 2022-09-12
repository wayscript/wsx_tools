from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def sql_table():
    return render_template('sql-data.html')

if __name__ == '__main__':
    app.run()
