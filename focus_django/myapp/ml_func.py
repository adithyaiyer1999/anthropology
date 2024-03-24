from bs4 import BeautifulSoup
import requests
import anthropic

MAX_TOKEN_LEN = 160000

def function_need(url,prompt):
    content = get_response_from_url(url)
    return call_anthropic_api(content, prompt)

def chunk_text(text, max_token_length):
    sentences = text.split('. ')  # Simple split by sentences
    chunks = []
    current_chunk = ""

    # Adi - We always try to max out token lengths so we can do least number of parallel api calls
    # this way we max out the tokens per gpt4 api call.
    approxNumberOfTotTokens = len(text)/4

    if approxNumberOfTotTokens > max_token_length:
        return text[:(max_token_length*4)]

    return text


def get_response_from_url(url):
    response = requests.get(url)
    # soup = BeautifulSoup(parsed_data['Item 1']['Content'], 'html.parser')
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract text from h1, h2, and other text
    tags = [
        'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
        'p',
        'ul', 'ol', 'li',
        'a',
        'img',
        'table', 'thead', 'tbody', 'tfoot', 'tr', 'th', 'td',
        'form', 'input', 'textarea', 'button', 'select', 'option',
        'div', 'section', 'article', 'header', 'footer', 'nav', 'aside',
        'br', 'hr', 'label',
    ]
    text = ' '.join([tag.get_text() for tag in soup.find_all(tags)])
    return chunk_text(text, MAX_TOKEN_LEN)


def call_anthropic_api(content,prompt):

    prompt_text = prompt + "\n\n Text: " + content
    client = anthropic.Anthropic(
        # defaults to os.environ.get("ANTHROPIC_API_KEY")
        api_key="<API_KEY>",
    )
    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        temperature=0,
        system="You are a website stalker, you follow your user's website history. Given a prompt by user and the webpage content, help user find appropriate information in most crisp and summarized way. Most importantly if you think the website visisted by the user is not relevant to the prompt, then simply return one word \"Irrelevant\"",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt_text
                    }
                ]
            }
        ]
    )
    print("debug : ", message.content)
    return message.content[0].text

