import json
import openai
import os

for NAME in ['all_1d_move_1p','all_1d_move_2p','all_1d_move_3p']:
    for suffix in ['']:
        NAME = NAME + suffix
        for N in [5]:
            INPUT = './' + NAME +'/' + 'demos_' + str(N) + '_s2l_004.json'
            # INPUT = './' + NAME +'/' + 'demos_' + str(N) + '_s2l_prompt_004.json'
            OUTPUT = './' + NAME +'/' + 'demos_' + str(N) + '_s2l_prompt_004.json'
            test_file = open(INPUT, 'r', encoding='utf-8')
            test_data = json.load(test_file)
            print(INPUT)
            for idx, task_json in enumerate(test_data):
                assert 'stl' in task_json.keys() and len(task_json['stl']) == 2*N + 1
                c=0
                stl_prompt=""
                print(task_json['prompt'])
                for p in task_json['prompt'].split('\n')[:-1]:
                    if p.strip()=="":
                        stl_prompt+='\n'
                        continue
                    stl_prompt += p.strip() + ' (' + task_json['stl'][c] + ')' + '\n'
                    c+=1
                stl_prompt += task_json['prompt'].split('\n')[-1]
                print(stl_prompt)

                task_json['s2l_prompt'] = stl_prompt
            with open(OUTPUT, 'w') as f:
                json.dump(test_data, f, indent=4)
                    