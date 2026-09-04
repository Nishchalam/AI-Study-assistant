from google import genai

from config import GEMINI_API_KEY, MODEL_NAME


def main():
    client = genai.Client(api_key=GEMINI_API_KEY)

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents="Explain what a Transformer is in one sentence.",
    )

    print(response.text)


if __name__ == "__main__":
    main()