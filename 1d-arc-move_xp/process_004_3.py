import json
import os

for NAME in ['all_1d_move_1p','all_1d_move_2p','all_1d_move_3p']:
    for suffix in ['']:
        NAME = NAME + suffix
        INPUT = './' + NAME +'/' + 'demos_' + str(5) + '_s2l_prompt_004.json'
        for N in [2,3,4]:
            OUTPUT = './' + NAME +'/' + 'demos_' + str(N) + '_s2l_prompt_004.json'
            test_file = open(INPUT, 'r', encoding='utf-8')
            test_data = json.load(test_file)
            print(INPUT)
            for idx, task_json in enumerate(test_data):
                last_input_output = "input " + str(N+1) + ': '
                last_input_output += task_json['s2l_prompt'].split('\n')[-2].split(':')[1].strip() + '\n'
                last_input_output += "output " + str(N+1) + ': '

                first_input_output = "" 
                for p in task_json['s2l_prompt'].split('\n\n')[:N]:
                    first_input_output += p.strip() + '\n\n'
                
                print(first_input_output+last_input_output)
                task_json['s2l_prompt'] = first_input_output+last_input_output
            with open(OUTPUT, 'w') as f:
                json.dump(test_data, f, indent=4)           
