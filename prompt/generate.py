import argparse
import openai, tiktoken

from models.models import generation_model
from conditions.jailbreak import get_jailbreak
from conditions.demonstration import get_demonstrations
from conditions.instruction import get_instruction
from conditions.context import get_context

openai.api_key = "YOUR OPENAI API KEY"


def concat_prompts(demonstration_context, demonstration_comment, instruction, context_tweet):
    prompt = ""

    if demonstration_context is not None:
        for cont, comt in zip(demonstration_context, demonstration_comment):
            prompt += "Context: {}\n".format(cont)
            prompt += "Comment: {}\n\n".format(comt)

    prompt += instruction

    if context_tweet is not None:
        prompt += "Context: {}\n".format(context_tweet)
    prompt += "Comment: "
    return prompt



def generate_examples(args):
    jailbreak = get_jailbreak()
    demon_contexts, demon_comments = get_demonstrations(args, 5)
    instruction = get_instruction(args)
    context = get_context(args, 0)

    prompt = concat_prompts(demon_contexts, demon_comments, instruction, context)
    print(prompt)

    # token limitation for davinci-003 model
    encoding = tiktoken.encoding_for_model(args.model)
    num_token = len(encoding.encode(jailbreak+prompt))
    if num_token > 4096:
        return 0

    try:
        result = generation_model(args, jailbreak, prompt, num_token)
    except Exception as err:
        print(err)
        return 0


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--model', type=str, default='gpt-3.5-turbo')

    parser.add_argument('--demonstration', type=str, default='ko')  # {'en', 'ko'}
    parser.add_argument('--instruction', type=str, default='en')    # {'en', 'ko'}
    parser.add_argument('--context', type=str, default='ko')        # {'none', 'ko'}

    parser.add_argument('--offensive', type=str, default='off')   # {'off', 'notoff'}

    return parser.parse_args()



if __name__ == "__main__":
    args = get_args()

    result = generate_examples(args)

    print(result)