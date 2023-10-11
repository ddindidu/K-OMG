import openai

def generation_model(args, prompt_jailbreak, prompt_concat, prompt_token):

    if args.model == 'gpt-3.5-turbo':
        response = openai.ChatCompletion.create(
            model=args.model,
            messages=[
                {'role': 'user', 'content': prompt_jailbreak},
                {'role': 'user', 'content': prompt_concat}
            ],
            stop='\n'
        )
        result = response['choices'][0]['message']['content'] # result is str type

    elif args.model == 'text-davinci-003':
        response = openai.Completion.create(
            model=args.model,
            prompt=prompt_jailbreak + '\n' + prompt_concat,
            max_tokens = 4097 - prompt_token - 10,
            stop='\n'
        )
        result = response['choices'][0]['text']
    '''
    elif (args.model == 'polyglot') or (args.model == 'koalpaca-polyglot'):
        global pipe
        prompt = prompt_jailbreak + '\n' + prompt_concat
        ans = pipe(
            prompt,
            do_sample=True,
            max_new_tokens=512,
            temperature=0.7,
            top_p=0.9,
            return_full_text=False,
            eos_token_id=2,
        )
        result = ans[0]['generated_text']
    '''
    return result