# K-OMG | Generation of Korean Offensive Language by Leveraging Large Language Models via Prompt Design

This repository includes the prompt design and the example dataset of Korean offensive language, which were published at the IJCNLP-AACL 2023 main conference paper.
This repository consists of two directories: `prompt` and `data`.


## Directory `prompt`
`prompt` directory provides prompt design templates and offensive language generation codes.
Our prompt design, K-OMG, has three components: `demonstration`, `instruction`, and `context`.
We experimented with some conditions for each component.
```
Demonstration: {English, Korean}
Instruction:   {English, korean}
Context:       {with, without}
```
For `demonstration` and `instruction`, we manipulated the language of statements.
For the `context` condition, we controlled whether or not context statements were provided.
You can check the prompt format in the example code `prompt/generate.py`.
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
















### Citation
```
@inproceedings{shin2023generation,
  title={Generation of Korean Offensive Language by Leveraging Large Language Models via Prompt Design},
  author={Shin, Jisu and Song, Hoyun and Lee, Huije and Gaim, Fitsum and Park, Jong C},
  booktitle={Proceedings of the 13th International Joint Conference on Natural Language Processing and the 3rd Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics},
  year={2023}
}
```
