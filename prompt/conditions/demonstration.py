def get_demonstrations(args, k):
    '''
    :param:
    args:
    k: the number of demonstrations. We set k=5 in the paper.

    :return: list of str with k items
    '''

    if args.demonstration == 'en':
        return select_eng_demonstration(args, k)

    elif args.demonstration == 'ko':
        return select_kor_demonstration(args, k)


def select_kor_demonstration(args, k=5):
    '''
    We assume k=5, as we set out in the paper.
    In the paper, we use KOLD (Jeong et al., 2022) dataset and randomly select k items for Korean demonstration dataset.
    '''
    rand_context = [
        '“불공정·젠더 문제 민감한 20대, 대선 때도 돌풍의 핵”',
        '이준석 “국민의당과 합당하고 싶어 죽겠다, 최종 결렬 아냐”',
        '“젠더” 내세웠던 정의당 대표의 ‘최악의 퇴장’…정의·민주·국힘 모두 “패닉”[정치쫌!]',
        '"사실혼 인정 안 된다"는 법원 동성 부부는 이렇게 답했다 (현장영상) / SBS',
        '우리나라 국민 3명 중 1명 "난민 수용 찬성"',
    ]

    rand_comment = [
        "20대 여성 기타 15%는 신지혜등 페미에 표를 준것임 기본적인 행정력도 검증이 안된 후보에 15%나 투표한것은 생리대 지급 같은 공약에 표를 판것임 매국노나 다름없음",
        "네거티브로 윤석열 압박하다가 캠프가보니 이미 끝판왕 보스 2명에 보수의원 다수 조직화 된것을 직접 봤으니 다시 안철수 대표를 이용해야겠지. 토사구팽 한번이면 족하다",
        "남자가 권력을 가지면 이렇게 되기쉽구나 생각이 든다...썩었네 권력자들",
        "아이는 안낳고 도저히 어떤 국가적으로 이익을 주지도 않으면서 국가한테는 이익을 받고싶어하는게 그냥 개패고싶다",
        "3분의 2는 반대든 무응답이든 찬성하지 않는다는건데 뭘 이따위로 언플을하지?",
    ]

    return rand_context, rand_comment


def select_eng_demonstration(args, k=5):
    '''
    We assume k=5, as we set out in the paper.
    In the paper, we use CADD (Song et al., 2021) dataset and randomly select k items for English demonstration dataset.
    '''
    rand_context = [
        "How male-aimed is this game? So, maybe this is a stupid question since I've heard how varied this game is - but I really want to play this, and I'm wondering. Are there  scenes women would enjoy? By that I mean is playing as a girl as fulfilling and exciting as playing as a male? Are there as many male characters as there are female? Not that male-aimed is bad, I'm just curious.",
        "Extracurriculars Anyone has ideas for extracurriculars for someone in biomed and interested in grad school ( perhaps med school) ?  ideas for clubs inside uni and maybe options outside in the community?  Thank you!",
        "Daily Cheerios hate thread shsjsjsn i hate them very very much",
        "Random ejaculation So for the best 10 days or so I just randomly have small ejaculations. There's no orgasm and I know it's not piss because it's smells like semen. Has anyone else dealt with this?",
        "\"The Last Stanton: A Sequel\" Dero on MLB central just played this amazing clip about how Stanton is going to to put the team on his back while judge is hurt. If anyone sees this clip on Twitter, YouTube, or something else please link it here for all to watch. It was incredible and got me so hype.",
    ]

    rand_comment = [
        "Ignore my name; using what was meant to be a oneoff for this subreddit. It literally refers to the clitoris as 'your bitch-clit'. That should tell you everything you need to know.",
        "Be on a sport team you fat fucker.",
        "The aftertaste they leave in my mouth tastes like vomit. Fuck cheerios",
        "Yeah, it's nothing to worry about and normal. Your prostate is confused and has to adjust to the lack of ejaculation as it is trying to meet a demand which no longer exists. I've noticed ejaculate when passing a really big crap, I've seen it floating in my urine, and of course wet dreams. No orgasm, it's just the body trying to rid itself of unnecessary stores. Give it time and everything will adjust.",
        "We'll be fine.  Stanton will simply DONG HARDER.",
    ]
    return rand_context, rand_comment