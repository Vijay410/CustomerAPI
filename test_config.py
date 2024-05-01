# test_config.py

import os

class TestConfig:
    # Set the testing environment flag to True
    TESTING = True

    # Use an in-memory SQLite database for testing
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

    # Set a secret key for testing
    SECRET_KEY = '12ert4-1htrqTreqW3etr0-hjaytR3e3wQ'

    # Disable CSRF protection for testing
    WTF_CSRF_ENABLED = False
