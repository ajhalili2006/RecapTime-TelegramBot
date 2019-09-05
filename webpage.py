from flask import Flask, render_template
app = Flask(__name__)

@app.route('/html')
  def static_page():
  return render_template('page.html')

if __name__ == '__main__':
  app.run()