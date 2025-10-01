import subprocess
import csv
import requests
# 读取 prompts 文件

import pickle


nn = 0

modelname = "deepseek-r1_70b"

with open('g_t_a_dataset_enhance_t.csv', 'r', newline='', encoding='gbk') as csvfile_1:
    with open('result_g_t_a_{}_noenhance.csv'.format(modelname), 'w', newline='', encoding='gbk') as csvfile:
        reader = csv.DictReader(csvfile_1)
        fieldnames = ['ID', 'Generated Response']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # 读取CSV文件内容
        nn = 0
        for row in reader:
            print(row['e_template_change'])


            prompt = """
            You are a template-filling expert. Given a template and a set of control conditions, where placeholders in the template are denoted by ‘<>’, and a question, please fill in the control conditions into the template in a fluent and logically coherent manner, ensuring the generated content effectively answers the question. You may modify the template appropriately when necessary.The answer should include statistical values of the emotions given in the conditions
            Template: {template}
            Control Conditions: {conditions}
            Question: {question}
            Please generate:
            """.format(template = row['e_template_change'].strip() ,conditions = row['conditions'].strip(),question =  row['Question'].strip())

            

            url = "http://localhost:11434/api/generate"
            payload = {
                        "model": "deepseek-r1:70b",
            "prompt": prompt,
            "stream": False
                }

            res = requests.post(url, json=payload)

                
            writer.writerow({'ID': nn, 'Generated Response': res.json()["response"]})

            nn += 1
            if nn == 30:
                break
