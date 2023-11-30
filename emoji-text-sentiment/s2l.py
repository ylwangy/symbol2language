import json
import openai

INPUT = 'emoji_text.json'
INPUT = 'emoji_text_s2l.json'
OUTPUT = 'emoji_text_s2l.json'
test_file = open(INPUT, 'r', encoding='utf-8')
test_data = json.load(test_file)
for idx, task_json in enumerate(test_data):
    if 's2l' in task_json.keys():
        continue
    else:
        print(idx, len(test_data))
        # prompt = "Transfer the tweet and emoji to plain texts:\n"
        prompt = "Transfer to plain text tweets:\n"
        prompt += task_json['emoji_text'].strip()
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
            task_json['s2l'] = responses['choices'][0]['message']['content']
        except:
            pass
        print('---'*10)
with open(OUTPUT, 'w') as f:
    json.dump(test_data, f, indent=4, ensure_ascii=False)