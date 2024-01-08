import json
import openai

INPUT = 'raw_test_trump_2way_s2l.json'
INPUT = 'final2.json'
OUTPUT = 'final2.json'
test_file = open(INPUT, 'r', encoding='utf-8')
test_data = json.load(test_file)
for idx, task_json in enumerate(test_data):
    if 'response' in task_json.keys():
        continue
    else:
        print(idx, len(test_data))
        prompt = "Stance classification. Target: Donald Trump. Please answer with only Favor or Against.\n"
        prompt += task_json['Tweet'].strip() + '\n'
        prompt += '(' + task_json['s2l'].strip() + ')'
        prompt += "\n\nLet's think step by step.\n"
        print(prompt)
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
            task_json['response'] = responses['choices'][0]['message']['content']
        except:
            pass
        print('---'*10)
with open(OUTPUT, 'w') as f:
    json.dump(test_data, f, indent=4)