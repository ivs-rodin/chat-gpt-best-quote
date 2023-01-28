import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_answer(question: str) -> str:
    """
    Generates a response to a given question using the OpenAI API.
    :param question: The question to be answered.
    :return: The answer generated by the API.
    """
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=question,
        max_tokens=1024,
        temperature=0.5,
    )
    return response["choices"][0]["text"]

def generate_quote_answer(quote: str) -> str:
    """
    Generates a motivational text based on the given quote.
    :param quote: The quote to be used as inspiration.
    :return: The generated motivational text.
    """
    question = f"Today's quote is: '{quote}'. Can you compose a brief motivational text that incorporates this quote?"
    answer = generate_answer(question)
    return answer

if __name__ == '__main__':
    quote = "The best way to predict your future is to create it."
    answer = generate_quote_answer(quote)
    print(answer)