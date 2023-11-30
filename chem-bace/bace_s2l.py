import json
import openai

INPUT = 'BACE_random_500.json'
INPUT = 'BACE_random_500_s2l.json'
OUTPUT = 'BACE_random_500_s2l.json'
test_file = open(INPUT, 'r', encoding='utf-8')
test_data = json.load(test_file)
for idx, task_json in enumerate(test_data):
    if 's2l-2' in task_json.keys():
        continue
    else:
        print(idx, len(test_data))
        # prompt = "explain the SMILES notation using plain texts:\n"   s2l
        prompt = "What does the following SMILES represent?\n"
        prompt += task_json['mol'].strip()
        print(task_json['mol'])
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
            task_json['s2l-2'] = responses['choices'][0]['message']['content']
        except:
            pass
        print('---'*10)
with open(OUTPUT, 'w') as f:
    json.dump(test_data, f, indent=4)