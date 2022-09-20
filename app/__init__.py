from flask import Flask, request, render_template, jsonify
from . import tracker

my_app = Flask(__name__)
    
@my_app.route('/', methods=['GET', 'POST'])
def run_script():
    if request.method == 'POST':
        input_url = request.get_json().get('url')
        input_price = request.get_json().get('price')
        input_mail = request.get_json().get('email')
        retour = tracker.inputInfos(input_url,input_price,input_mail)
        return jsonify({'url': input_url,'price': input_price,'email':input_mail,'retour':retour})
    else:
        return render_template('homepage.html')

@my_app.route('/mes-alertes')
def mesalertes():
    return render_template('mes-alertes.html')

if __name__ == '__main__':
    my_app.run()