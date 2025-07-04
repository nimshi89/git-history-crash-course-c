import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

if __name__ == "__main__":

    secrets_list = []

    aws_secret = REDACTED

    secrets_list.append(aws_secret)

    # Access the secret from the environment variable
    secret = os.getenv("SECRET_KEY")

    if secret:
        secrets_list.append(secret)
    else:
        print("No secret found in .env file.")

    # Print the secrets
    for i, secret in enumerate(secrets_list):
        print(f"Secret {i+1}: {secret}")
        