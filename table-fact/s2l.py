import json
import openai

INPUT = 'tablefact_500.json'
INPUT = 'tablefact_500_s2l_3.json'
OUTPUT = 'tablefact_500_s2l_3.json'
test_file = open(INPUT, 'r', encoding='utf-8')
test_data = json.load(test_file)
for idx, task_json in enumerate(test_data):
    if 's2l' in task_json.keys():
        continue
    else:
        print(idx, len(test_data))
        # prompt = "Describe the table to plain texts:\n" #s2l
        # prompt = "Describe all the details of the table:\n" #s2l_2
        prompt = "Describe the table row by row:\n" #s2l_3
        prompt += task_json['table']
        print(task_json['table'])
        try:
            responses = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                max_tokens=4096,
                temperature=0
            )
            print(responses['choices'][0]['message']['content'])
            task_json['s2l'] = responses['choices'][0]['message']['content']
        except:
            pass
        print('---'*10)
with open(OUTPUT, 'w') as f:
    json.dump(test_data, f, indent=4)
