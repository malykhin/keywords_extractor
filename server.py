from flask import Flask, jsonify, abort, request, make_response, url_for
import keywords
import os

app = Flask(__name__)


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/api/keywords', methods=['POST'])
def retrieve_keywords():
    if not request.json or not 'text' in request.json or not 'number' in request.json:
        abort(400)
    return jsonify({'keywords': keywords.get_keywords_list(request.json['text'], request.json['number'])}), 200


@app.route('/api/keyphrases', methods=['POST'])
def retrieve_keyphrases():
    if not request.json or not 'text' in request.json or not 'number' in request.json:
        abort(400)
    return jsonify({'keyphrases': keywords.get_keyphrases_list(request.json['text'], request.json['number'])}), 200


@app.route('/api/named_entities', methods=['POST'])
def retrieve_named_entities():
    if not request.json or not 'text' in request.json or not 'number' in request.json:
        abort(400)
    return jsonify({'named_entities': keywords.get_named_entities(request.json['text'], request.json['number'])}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('EXTRACTOR_PORT', 5000)), debug=os.getenv('EXTRACTOR_DEBUG', False))
