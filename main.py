import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

if __name__ == "__main__":

    aws_secret = REDACTED

    print(f"Accessed secret: {aws_secret}")

    # Access the secret from the environment variable
    secret = os.getenv("SECRET_KEY")

    if secret:
        print(f"Secret from environment: {secret}")
    else:
        print("No secret found in environment variables.")
        