from flask import Flask, request, jsonify
from config import Config
from services import mask_sensitive_info


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # update

    @app.route('/sensitive-info-mask', methods=['POST'])
    def mask_text():
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({'error': 'No key called text provided'}), 400

        original_text = data['text']
        masked_text = mask_sensitive_info(original_text)
        return jsonify({'masked_text': masked_text})

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
