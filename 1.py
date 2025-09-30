import subprocess
import csv
import requests
# 读取 prompts 文件
iprompts = ["1+1 = ?","1+2=?"]
import pickle

pk_path = './Amazon_Subjective_test_set.pk'

with open(pk_path, 'rb') as f:
    data = pickle.load(f)

nn = 0



with open('results.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['ID', 'Generated Response']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 写入CSV的表头
    writer.writeheader()
    for num,item in enumerate(data):
        nn += 1
        if nn == 5:
            break
        prompt = """
     You are a highly emotionally intelligent and experienced sales expert and customer service specialist. You need to generate answer templates for customer questions based on the product category and the customer’s inquiry. The template should include the following placeholders: 1.$<$aspectn$>$ where n can be 1, 2,…n, representing different aspects of the product. 2.$<$product$>$ representing the name of the product. 3.$<$space$>$ representing external knowledge that can be inserted. 4.$<$subjective opinion$>$ representing optimistic information. 5.$<$neutral opinion$>$ representing neutral viewpoints. 6.<negative opinion> representing pessimistic viewpoints.
     For example, a template could be:"Dear customer, $<$space$>$, here is a summary of your question: Firstly $<$aspect1$>$, secondly $<$aspect2$>$, ….Regarding the $<$product$>$ you mentioned, many users agree $<$subjective opinion$>$, however, some feel $<$neutral opinion$>$ and $<$negative opinion$>$." You need to provide a template that aligns with the characteristics of the question and product category.
     The product category that requires a template: {Product_class}
     The customer’s question: {Question}
     Answer templates must be extremely concise. You only need to provide a general outline. Do not add parentheses or speculative information. Please generate an answer template for the customer’s inquiry:
     """.format(Product_class = item['category'] ,Question = item['question'].strip())



    
        # 去除多余的空格和换行
        prompt = prompt.strip()#ls -l /mnt/data/home/sysu/yya/ollama/bin
      

        url = "http://localhost:11434/api/generate"
        payload = {
                "model": "deepseek-r1:70b",
    "prompt": prompt,
    "stream": False
        }

        res = requests.post(url, json=payload)
        print(res.json()["response"]) 
        # 调i用 ollama 并传递 prompt
            
        # 获取模型输出
        
        
        # 写入输出到文件
        
        writer.writerow({'ID': num, 'Generated Response': res.json()["response"]})
        print(f"Processed: {prompt}")

