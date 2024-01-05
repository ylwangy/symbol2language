import json
import openai
import os

for NAME in ['all_1d_move_1p','all_1d_move_2p','all_1d_move_3p']:
    for suffix in ['']:
        NAME = NAME + suffix
        for N in [5]:
            INPUT = './' + NAME +'/' + 'demos_' + str(N) + '.json'
            # INPUT = './' + NAME +'/' + 'demos_' + str(N) + '_s2l_004.json'
            OUTPUT = './' + NAME +'/' + 'demos_' + str(N) + '_s2l_004.json'
            test_file = open(INPUT, 'r', encoding='utf-8')
            test_data = json.load(test_file)
            print(INPUT)
            for idx, task_json in enumerate(test_data):
                if 'stl' in task_json.keys() and len(task_json['stl']) == 2*N + 1:
                    continue
                else:
                    print(idx, len(test_data))
                    
                    all_seq = task_json['prompt'].split('\n')[:-1]
                    all_stl = []
                    for seq in all_seq:
                        if seq.strip()=="":
                            continue
                        prompt = "Describe the sequence of digits using language.\n"
                        # prompt = "Use language to precisely describe the following number sequence.\n"
                        prompt += seq.split(':')[1].strip().replace(',',', ')
                        print(prompt)
                        try:
                            responses = openai.ChatCompletion.create(
                                model="gpt-4-0613",
                                messages=[
                                    # {"role": "system", "content": system_prompt},
                                    {"role": "user", "content": prompt}
                                ],
                                max_tokens=1024,
                                temperature=0
                            )
                            print(responses['choices'][0]['message']['content'])
                            all_stl.append(responses['choices'][0]['message']['content'])
                        except:
                            break
                    if len (all_stl) == 2*N + 1:
                        task_json['stl'] = all_stl
                    



            with open(OUTPUT, 'w') as f:
                json.dump(test_data, f, indent=4)