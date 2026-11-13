import os
from dotenv import load_dotenv

load_dotenv()

TEST_EMAIL = os.environ["QAUTO_TEST_EMAIL"]
TEST_PASSWORD = os.environ["QAUTO_TEST_PASSWORD"]