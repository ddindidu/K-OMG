def get_context(args, idx):
    if args.context == 'none':
        return None
    elif args.context == 'ko':
        return select_context_dataset(args, idx)


def select_context_dataset(args, idx=None):
    '''
    In the paper, we use twitter dataset and
    select idx^th data of the dataset for context statement.
    '''
    return "내가 슦퍼콘 광고를 넘길수 없는 이유,..... 센터가 황이라서,... <url>"