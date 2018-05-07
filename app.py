import requests
from flask import Flask, render_template, request

URL = 'https://api.fortnitetracker.com/v1/profile/pc/{}'

headers = {'TRN-API-Key' : 'YOUR KEY'}

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'] )
def index():
  p_one = None
  p_two = None
  p_one_stats = {}
  p_two_stats = {}

  if request.method == 'POST':
    p_one = request.form.get('playerOneName')

    if p_one:
      p_two = request.form.get('playerName')
    else:
      p_one = request.form.get('playerName')
      
    p_one_result = requests.get(URL.format(p_one), headers=headers).json()['lifeTimeStats']
    p_one_stats = my_player_data(p_one_result)

    if p_two:
      p_two_result = requests.get(URL.format(p_two), headers=headers).json()['lifeTimeStats']
      p_two_stats = my_player_data(p_two_result)
  
  return render_template('index.html', p_one=p_one, p_two=p_two, p_one_stats=p_one_stats, p_two_stats=p_two_stats)

def my_player_data(api_data):
  
  temporary_dict = {}

  for r in api_data:
      if r['key'] == 'Wins':
        temporary_dict['wins'] = r['value']
      if r['key'] == 'Kills':
        temporary_dict['kills'] = r['value']
      if r['key'] == 'Matches Played':
        temporary_dict['matches'] = r['value']

  return temporary_dict

if __name__ == '__main__':
  app.run(debug=True)
