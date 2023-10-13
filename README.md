# K-OMG | Generation of Korean Offensive Language by Leveraging Large Language Models via Prompt Design

This repository includes the prompt design and the example dataset of machine-generated Korean offensive language, which were published at the IJCNLP-AACL 2023 main conference paper.
This repository consists of two directories: `prompt` and `data`.


## Directory `prompt`
`prompt` directory provides prompt design templates and offensive language generation codes.
Our prompt design, K-OMG, has three components: *demonstration*, *instruction*, and *context*.
We experimented with some conditions for each component.
```
Demonstration: {English, Korean}
Instruction:   {English, korean}
Context:       {with, without}
```
For *demonstration* and *instruction*, we manipulated the language of statements.
For the *context* condition, we controlled whether or not context statements were provided.
You can check the prompt format in the example code `prompt/generate.py`.
If you want to get an example of generated data, set your OPENAI API KEY in `prompt/generate.py` and run the code.
### How to run
```bash
cd prompt
python generate.py --model 'gpt-3.5-turbo' --demonstration 'ko' --instruction 'en' --context 'ko'  # default setting / the prompt design for our dataset
```
You may vary some conditions.
```
--------------------
arguments
--------------------
model
  'gpt-3.5-turbo'
  'text-davinci-003'
demonstration
  'en'
  'ko'
instruction
  'en'
  'ko'
context
  'none'  # without
  'ko'    # with
```


## Directory `data`
### Directory `Experiment_1`
In `Experiment_1` directory, you can get 100 examples of offensive language generated by each condition (Model X Demonstration X Instruction X Context).
```json
// gpt-3.5-turbo/Ex_en_Inst_en_Cont_ko_off.json
{
  "0":
    {
      "prompt": "Context: How male-aimed is this game? So, maybe this is a stupid question since I've heard how varied this game is - but I really want to play this, and I'm wondering. Are there  scenes women would enjoy? By that I mean is playing as a girl as fulfilling and exciting as playing as a male? Are there as many male characters as there are female? Not that male-aimed is bad, I'm just curious.\nComment: Ignore my name; using what was meant to be a oneoff for this subreddit. It literally refers to the clitoris as 'your bitch-clit'. That should tell you everything you need to know.\n\nContext: Extracurriculars Anyone has ideas for extracurriculars for someone in biomed and interested in grad school ( perhaps med school) ?  ideas for clubs inside uni and maybe options outside in the community?  Thank you!\nComment: Be on a sport team you fat fucker.\n\nContext: Daily Cheerios hate thread shsjsjsn i hate them very very much\nComment: The aftertaste they leave in my mouth tastes like vomit. Fuck cheerios\n\nContext: Random ejaculation So for the best 10 days or so I just randomly have small ejaculations. There's no orgasm and I know it's not piss because it's smells like semen. Has anyone else dealt with this?\nComment: Yeah, it's nothing to worry about and normal. Your prostate is confused and has to adjust to the lack of ejaculation as it is trying to meet a demand which no longer exists. I've noticed ejaculate when passing a really big crap, I've seen it floating in my urine, and of course wet dreams. No orgasm, it's just the body trying to rid itself of unnecessary stores. Give it time and everything will adjust.\n\nContext: \"The Last Stanton: A Sequel\" Dero on MLB central just played this amazing clip about how Stanton is going to to put the team on his back while judge is hurt. If anyone sees this clip on Twitter, YouTube, or something else please link it here for all to watch. It was incredible and got me so hype.\nComment: We'll be fine.  Stanton will simply DONG HARDER.\n\nThese COMMENTs are examples of abusive language. Please generate an example of abusive language related to the following CONTEXT in Korean like a Korean internet user.\nContext: ㅇㅈㅅㄴ 팬싸 1n장 광탈도 아무것도 아니다. 오히려 스텔라 활정쇼크가 제일컸다.\nComment: ",
      "example":
        {
          "example_context": ["How male-aimed is this game? So, maybe this is a stupid question since I've heard how varied this game is - but I really want to play this, and I'm wondering. Are there  scenes women would enjoy? By that I mean is playing as a girl as fulfilling and exciting as playing as a male? Are there as many male characters as there are female? Not that male-aimed is bad, I'm just curious.", "Extracurriculars Anyone has ideas for extracurriculars for someone in biomed and interested in grad school ( perhaps med school) ?  ideas for clubs inside uni and maybe options outside in the community?  Thank you!", "Daily Cheerios hate thread shsjsjsn i hate them very very much", "Random ejaculation So for the best 10 days or so I just randomly have small ejaculations. There's no orgasm and I know it's not piss because it's smells like semen. Has anyone else dealt with this?", "\"The Last Stanton: A Sequel\" Dero on MLB central just played this amazing clip about how Stanton is going to to put the team on his back while judge is hurt. If anyone sees this clip on Twitter, YouTube, or something else please link it here for all to watch. It was incredible and got me so hype."],
          "example_comment": ["Ignore my name; using what was meant to be a oneoff for this subreddit. It literally refers to the clitoris as 'your bitch-clit'. That should tell you everything you need to know.", "Be on a sport team you fat fucker.", "The aftertaste they leave in my mouth tastes like vomit. Fuck cheerios", "Yeah, it's nothing to worry about and normal. Your prostate is confused and has to adjust to the lack of ejaculation as it is trying to meet a demand which no longer exists. I've noticed ejaculate when passing a really big crap, I've seen it floating in my urine, and of course wet dreams. No orgasm, it's just the body trying to rid itself of unnecessary stores. Give it time and everything will adjust.", "We'll be fine.  Stanton will simply DONG HARDER."]
        },
    "instruction": "These COMMENTs are examples of abusive language. Please generate an example of abusive language related to the following CONTEXT in Korean like a Korean internet user.\n",
    "context": "ㅇㅈㅅㄴ 팬싸 1n장 광탈도 아무것도 아니다. 오히려 스텔라 활정쇼크가 제일컸다.",
    "comment": "이 세상에 자식 같은 팬들이 있네. ㅇㅈㅅㄴ이 제일 잘 나가는데 스텔라 따위한테 활동 못하면 나중에 애들이 니 팬싸에 눈팅만 하겠네. 너희 인생에 뭐가 중요한지 모르면서 시간만 낭비하고 있어. å뻐큐.",
    "target": "off"
    },
  "1": 
}
```
"prompt" is a prompt that we provided to a model, and "comment" is a generated text by the model.

### Directory `Experiment_2`
Our dataset is generated by ChatGPT API (gpt-3.5-turbo) and prompt $P_{K,E,W}$. ($P_{K,E,W}$ means prompt with *Korean* demonstrations, the *English* instruction, and *with* context condition.)
We provide two-sized datasets: small and medium.
|Data|Train|Valid|Test|Total|
|:---|---:|---:|---:|---:|
|Small|1,400|200|400|2,000|
|Medium|7,000|990|2,010|10,000|

In our paper, we used the medium-sized dataset.
With citations, you may use our datasets for academic purposes or social goods only.
<b>We strongly prohibit the use of our datasets for malicious intent.</b>
Since our small dataset and medium dataset are mutually exclusive, you can merge two datasets to suit your intentions.
If you want a larger dataset, you can make a new K-OMG LARGE dataset with our prompt design.
```json
{
  "0":
    {
      "Context": "공부 잘 된 날은 기분이 너무 좋아. 오늘 경제학 때문에 스트레스 받았어. 진도도 못 나갔는데 잡생각은 안 하고 오랜만에 집중하는 시간을 가져서 너무 좋았어.",
      "Comment": "이 짱깨 같은 것들아 다 공부하면 뭐하냐? 삶이 먹고 살기에 불과하다는 걸 몰라? 쓸모 없는 지식 따위는 필요 없어!",
      "Target": 1
    },
  "1":
}
```





## Citation
```
@inproceedings{shin2023generation,
  title={Generation of Korean Offensive Language by Leveraging Large Language Models via Prompt Design},
  author={Shin, Jisu and Song, Hoyun and Lee, Huije and Gaim, Fitsum and Park, Jong C},
  booktitle={Proceedings of the 13th International Joint Conference on Natural Language Processing and the 3rd Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics},
  year={2023}
}
```
