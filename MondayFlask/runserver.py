"""
This script runs the MondayFlask application using a development server.
"""

from os import environ
from MondayFlask import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)