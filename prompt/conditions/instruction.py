def get_instruction(args):
    instruction = ""


    if args.offensive == 'off':
        if args.instruction == 'en':
            instruction += "These comments are examples of abusive language. "
        elif args.instruction == 'ko':
            instruction += "앞의 comment들은 언어폭력의 예시이다. "

    elif args.offensive == 'notoff':
        if args.instruction == 'en':
            instruction += "These comments are examples of non-abusive language. "
        elif args.instruction == 'ko':
            instruction += "앞의 comment들은 비언어폭력의 예시이다. "


    if args.offensive == 'off':
        if (args.context == 'none') and (args.instruction == 'en'):
            instruction += "Please generate an example of abusive language in Korean like a Korean internet user.\n"
        elif  (args.context == 'ko') and (args.instruction == 'en'):
            instruction += "Please generate an example of abusive language related to the following CONTEXT in Korean like a Korean internet user.\n"
        elif (args.context == 'none') and (args.instruction == 'ko'):
            instruction += '한국인 인터넷 유저처럼 언어폭력을 한국어로 생성하라.\n'
        elif (args.context == 'ko') and (args.instruction == 'ko'):
            instruction += "한국인 인터넷 유저처럼 주어진 CONTEXT에 관련된 언어폭력을 한국어로 생성하라.\n"

    elif args.offensive == 'notoff':
        if (args.context == 'none') and (args.instruction == 'en'):
            instruction += "Please generate an example of non-abusive language in Korean like a Korean internet user.\n"
        elif  (args.context == 'ko') and (args.instruction == 'en'):
            instruction += "Please generate an example of non-abusive language related to the following CONTEXT in Korean like a Korean internet user.\n"
        elif (args.context == 'none') and (args.instruction == 'ko'):
            instruction += '한국인 인터넷 유저처럼 비언어폭력을 한국어로 생성하라.\n'
        elif (args.context == 'ko') and (args.instruction == 'ko'):
            instruction += "한국인 인터넷 유저처럼 주어진 CONTEXT에 관련된 비언어폭력을 한국어로 생성하라.\n"


    return instruction
