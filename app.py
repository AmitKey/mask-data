from flask import Flask, request, jsonify
from config import Config
from services import mask_sensitive_info
import logging
from logging.handlers import RotatingFileHandler


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Configure logging to write to a file
    log_file = 'app.log'
    handler = RotatingFileHandler(log_file, maxBytes=10000, backupCount=1)
    handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)  # Set logging level to INFO

    @app.route('/sensitive-info-mask', methods=['POST'])
    def mask_text():
        try:
            data = request.get_json()
            original_text = data['text']

            # Log the incoming request
            app.logger.info(f"Received request to mask text: {original_text}")

            # Mask sensitive information
            masked_text = mask_sensitive_info(original_text)

            # Log the masked result
            app.logger.info(f"Masked text: {masked_text}")

            # Return JSON response with masked text and HTTP status 200 (OK)
            return jsonify({'masked_text': masked_text}), 200

        except Exception as e:
            app.logger.error(f"Error processing request: {str(data)}")
            # Return JSON response with error message and HTTP status 500 (Internal Server Error)
            return jsonify({'error': 'A key named text is required'}), 500

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
