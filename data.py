import requests

parameters = {
    'amount': 10,
    'type': 'boolean'
}
question_data = requests.get(url='https://opentdb.com/api.php', params=parameters).json()['results']
