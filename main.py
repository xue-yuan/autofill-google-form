import json

from phorm import GoogleForm

if __name__ == '__main__':
    with open('form.json', 'r') as f:
        config = json.load(f)
        form = GoogleForm(config['form_url'], config['answers'])
        form.send()
