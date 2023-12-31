import json
import openai
import os

for NAME in ['all_1d_move_1p','all_1d_move_2p','all_1d_move_3p']:
    for suffix in ['_123']:
        NAME = NAME + suffix
        for N in [3,5,8]:
            INPUT = './' + NAME +'/' + 'demos_' + str(N) + '_stl_prompt.json'
            # INPUT = './004/' + NAME +'_demos_' + str(N) + '_stl_prompt.json'
            OUTPUT = './004/' + NAME +'_demos_' + str(N) + '_stl_prompt.json'
            test_file = open(INPUT, 'r', encoding='utf-8')
            test_data = json.load(test_file)
            print(INPUT)
            for idx, task_json in enumerate(test_data):
                if 'response' in task_json.keys():
                    continue
                else:
                    print(idx, len(test_data))
                    # system_prompt="Assistant is a chatbot that capable of doing human-level reasoning and inference. Solver will try to solve some puzzles and answer the steps as concisely as possible."
                    prompt="Let's play some puzzles that focus on reasoning and logic. In each puzzle, you will be provided a few demonstrations of how an \"input grid\" gets transformed into a corresponding \"output grid\". At the end, you will get a brand new \"input grid\", then you must answer the corresponding \"output grid\".\n"
                    prompt += task_json['stl_prompt']
                    print(prompt)
                    try:
                        responses = openai.ChatCompletion.create(
                            model="gpt-4-0613",
                            messages=[
                                # {"role": "system", "content": system_prompt},
                                {"role": "user", "content": prompt}
                            ],
                            max_tokens=3072,
                            temperature=0
                        )

                        print(responses['choices'][0]['message']['content'])
                        task_json['response'] = responses['choices'][0]['message']['content']
                    except:
                        pass


            with open(OUTPUT, 'w') as f:
                json.dump(test_data, f, indent=4)