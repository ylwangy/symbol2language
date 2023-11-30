import numpy as np
import json
from scipy import stats
anger=[]
anticipation=[]
disgust=[]
fear=[]
joy=[]
sadness=[]
surprise=[]
trust=[]

INPUT = "emoji_tag.json"
test_file = open(INPUT, 'r', encoding='utf-8')
test_data = json.load(test_file)
correct=0
for idx, task_json in enumerate(test_data):
    anger.append(float(task_json["anger"]))
    anticipation.append(float(task_json["anticipation"]))
    disgust.append(float(task_json["disgust"]))
    fear.append(float(task_json["fear"]))
    joy.append(float(task_json["joy"]))
    sadness.append(float(task_json["sadness"]))
    surprise.append(float(task_json["surprise"]))
    trust.append(float(task_json["trust"]))

anger_gpt4=[]
anticipation_gpt4=[]
disgust_gpt4=[]
fear_gpt4=[]
joy_gpt4=[]
sadness_gpt4=[]
surprise_gpt4=[]
trust_gpt4=[]

INPUT = "prediction_gpt4.json"
test_file = open(INPUT, 'r', encoding='utf-8')
test_data = json.load(test_file)
correct=0
for idx, task_json in enumerate(test_data):
    try:
        anger_gpt4.append(float((task_json["response"].lower().split('anger:')[1].split('\n')[0])))
    except:
        anger_gpt4.append(0.0)
    try:
        anticipation_gpt4.append(float((task_json["response"].lower().split('anticipation:')[1].split('\n')[0])))
    except:
        anticipation_gpt4.append(0.0)
    try:
        disgust_gpt4.append(float((task_json["response"].lower().split('disgust:')[1].split('\n')[0])))
    except:
        disgust_gpt4.append(0.0)
    try:
        fear_gpt4.append(float((task_json["response"].lower().split('fear:')[1].split('\n')[0])))
    except:
        fear_gpt4.append(0.0)
    try:
        joy_gpt4.append(float((task_json["response"].lower().split('joy:')[1].split('\n')[0])))
    except:
        joy_gpt4.append(0.0)
    try:
        sadness_gpt4.append(float((task_json["response"].lower().split('sadness:')[1].split('\n')[0])))
    except:
        sadness_gpt4.append(0.0)
    try:
        surprise_gpt4.append(float((task_json["response"].lower().split('surprise:')[1].split('\n')[0])))
    except:
        surprise_gpt4.append(0.0)
    try:
        trust_gpt4.append(float((task_json["response"].lower().split('trust:')[1].split('\n')[0])))
    except:
        trust_gpt4.append(0.0)
    
    # aa=input()


res=[]
res.append(stats.spearmanr(np.array(anger), np.array(anger_gpt4))[0])
res.append(stats.spearmanr(np.array(anticipation), np.array(anticipation_gpt4))[0])
res.append(stats.spearmanr(np.array(disgust), np.array(disgust_gpt4))[0])
res.append(stats.spearmanr(np.array(fear), np.array(fear_gpt4))[0])
res.append(stats.spearmanr(np.array(joy), np.array(joy_gpt4))[0])
res.append(stats.spearmanr(np.array(sadness), np.array(sadness_gpt4))[0])
res.append(stats.spearmanr(np.array(surprise), np.array(surprise_gpt4))[0])
res.append(stats.spearmanr(np.array(trust), np.array(trust_gpt4))[0])
print(res)
print(sum(res)/len(res))



anger_gpt4=[]
anticipation_gpt4=[]
disgust_gpt4=[]
fear_gpt4=[]
joy_gpt4=[]
sadness_gpt4=[]
surprise_gpt4=[]
trust_gpt4=[]

INPUT = "prediction_gpt4_s2l.json"
test_file = open(INPUT, 'r', encoding='utf-8')
test_data = json.load(test_file)
correct=0
for idx, task_json in enumerate(test_data):
    try:
        anger_gpt4.append(float((task_json["response"].lower().split('anger:')[1].split('\n')[0])))
    except:
        anger_gpt4.append(0.0)
    try:
        anticipation_gpt4.append(float((task_json["response"].lower().split('anticipation:')[1].split('\n')[0])))
    except:
        anticipation_gpt4.append(0.0)
    try:
        disgust_gpt4.append(float((task_json["response"].lower().split('disgust:')[1].split('\n')[0])))
    except:
        disgust_gpt4.append(0.0)
    try:
        fear_gpt4.append(float((task_json["response"].lower().split('fear:')[1].split('\n')[0])))
    except:
        fear_gpt4.append(0.0)
    try:
        joy_gpt4.append(float((task_json["response"].lower().split('joy:')[1].split('\n')[0])))
    except:
        joy_gpt4.append(0.0)
    try:
        sadness_gpt4.append(float((task_json["response"].lower().split('sadness:')[1].split('\n')[0])))
    except:
        sadness_gpt4.append(0.0)
    try:
        surprise_gpt4.append(float((task_json["response"].lower().split('surprise:')[1].split('\n')[0])))
    except:
        surprise_gpt4.append(0.0)
    try:
        trust_gpt4.append(float((task_json["response"].lower().split('trust:')[1].split('\n')[0])))
    except:
        trust_gpt4.append(0.0)
    
res=[]
res.append(stats.spearmanr(np.array(anger), np.array(anger_gpt4))[0])
res.append(stats.spearmanr(np.array(anticipation), np.array(anticipation_gpt4))[0])
res.append(stats.spearmanr(np.array(disgust), np.array(disgust_gpt4))[0])
res.append(stats.spearmanr(np.array(fear), np.array(fear_gpt4))[0])
res.append(stats.spearmanr(np.array(joy), np.array(joy_gpt4))[0])
res.append(stats.spearmanr(np.array(sadness), np.array(sadness_gpt4))[0])
res.append(stats.spearmanr(np.array(surprise), np.array(surprise_gpt4))[0])
res.append(stats.spearmanr(np.array(trust), np.array(trust_gpt4))[0])
print(res)
print(sum(res)/len(res))