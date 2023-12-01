import json
import openai
# [ { ( < ] } ) >
# open square bracket; 
# open curly bracket; 
# open parenthesis; 
# less than; 
# close square bracket; 
# close curly bracket; 
# close parenthesis; 
# greater than.

for N in [0,1,2,3,4,5]:
    INPUT = 'demos_' + str(N) + '.json'
    OUTPUT = 'demos_' + str(N) + '_s2l.json'
    test_file = open(INPUT, 'r', encoding='utf-8')
    test_data = json.load(test_file)
    for idx, task_json in enumerate(test_data):
        task_json['label'] = task_json['label'].replace('[','open square bracket').replace('{','open curly bracket').replace('(','open parenthesis').replace('<','less than').replace(']','close square bracket').replace('}','close curly bracket').replace(')','close parenthesis').replace('>','greater than')
        task_json['prompt'] = task_json['prompt'].replace('[','open square bracket;').replace('{','open curly bracket;').replace('(','open parenthesis;').replace('<','less than;').replace(']','close square bracket;').replace('}','close curly bracket;').replace(')','close parenthesis;').replace('>','greater than;')
        task_json['prompt'] = task_json['prompt'].replace(';\n','\n')
    with open(OUTPUT, 'w') as f:
        json.dump(test_data, f, indent=4, ensure_ascii=False)
