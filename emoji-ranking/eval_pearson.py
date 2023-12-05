import json
import re
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# 从prediction_gpt3-5_description.json文件中提取相关值
data = []
with open('prediction_gpt3-5_cot_edit.json', 'r') as json_file:
    data = json.load(json_file)

emotion_labels = ["anger", "anticipation", "disgust", "fear", "joy", "sadness", "surprise", "trust"]

# 计算Pearson相关系数
Pearson_corr_results = {}

for emotion in emotion_labels:
    # 初始化每个情感类别的列表
    emotion_values = []
    response_values = []

    for entry in data:
        # 从response中找到每个情感所在的行
        response_lines = entry['response'].split('\n')
        emotion_line = next((line for line in response_lines if f"{emotion.capitalize()}:" in line), None)

        # 如果找到了情感所在的行
        if emotion_line:
            # 使用正则表达式从行中提取最后一个浮点数
            emotion_value_match = re.findall(r"[-+]?\d+\.\d+|\d+", emotion_line)
            if emotion_value_match:
                emotion_value = float(emotion_value_match[-1])
                # print(emotion, " ", emotion_value)
                emotion_values.append(emotion_value)
            else:
                # 如果无法提取浮点数，则默认为0.00
                print(emotion, " ", emotion_line, " ", entry['emoji'])
                emotion_values.append(0.00)
        else:
            # 如果没有找到情感所在行，则默认为0.00
            print(emotion, " ", entry['emoji'])
            emotion_values.append(0.00)

        # 提取每个情感类别的值
        response_values.append(float(entry[emotion]))

    # 计算Pearson相关系数
    pearson_corr, _ = stats.pearsonr(emotion_values, response_values)
    Pearson_corr_results[emotion] = pearson_corr


# 输出每个情感的Pearson相关系数
for emotion, Pearson_corr in Pearson_corr_results.items():
    print(f"Pearson相关系数 ({emotion.capitalize()}): {Pearson_corr}")

# 计算所有Pearson相关系数的平均值
average_Pearson_corr = sum(Pearson_corr_results.values()) / len(Pearson_corr_results)
print(f"所有情感的Pearson相关系数平均值: {average_Pearson_corr}")
