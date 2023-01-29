import requests
import os

#TODO: Add wrapper for cache (1 day - 1 quote)
def get_quote(category: str, count: int) -> list[dict]:
    """
    Retrieve a quote from the Andruxnet Random Famous Quotes API.

    :param category: The category of quote to retrieve (e.g. "movies", "famous")
    :param count: The number of quotes to retrieve
    :return: The response from the API
    """

    # Set API key and host as environment variables
    api_key = os.getenv("andruxnet_random_famous_quotes_API_KEY")
    api_host = os.getenv("andruxnet_random_famous_quotes_API_HOST")

    # Set base URL for API
    url = "https://andruxnet-random-famous-quotes.p.rapidapi.com/"

    # Set headers for API request
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": api_host
    }

    # Set query parameters for API request
    querystring = {"cat": category, "count": count}

    # Send POST request to API
    response = requests.request("POST", url, headers=headers, params=querystring)

    return response

if __name__ == '__main__':
	# Example usage
	response = get_quote("famous", 1)
	print(response.text)