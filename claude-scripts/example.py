from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
from dotenv import load_dotenv
import os

load_dotenv()

anthropic = Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

my_prompt = """
{HUMAN_PROMPT} I will provide you with an article about a contentious issue:

<article>{ARTICLE_TEXT}</article>

Please provide up to 10 potentially divisive or controversial statements derived from the article. The statements should be divisive to a UK audience. If you cannot find 10 suitable statements, you are welcome to return fewer. The statements should be short and atomic, and should try to capture the same tone as the the source sentences. Each statement should be a singular atomic thought, and if a source sentence has mulitple atomic points, please split it into multiple statements. Each statement should be no longer than 300 characters. Each statement should be rephrased into the first person, so that a reader could read it and determine if it speaks for their own opinion. Favour starting statements with "I feel..." when there's otherwise no personal pronoun.

{AI_PROMPT}
"""

ARTICLE_TEXT = open("article.txt", "r").read()

completion = anthropic.completions.create(
    model="claude-2",
    max_tokens_to_sample=300,
    prompt=my_prompt.format(ARTICLE_TEXT=ARTICLE_TEXT, HUMAN_PROMPT=HUMAN_PROMPT, AI_PROMPT=AI_PROMPT)
)
print(completion.completion)
