from transformers import T5Tokenizer, AutoModelForCausalLM 
# 接頭辞（Prefix） 
PREFIX_TEXT = "パンについての会話です。A「こんにちは」B「"
# トークナイザーとモデルの準備 
tokenizer = T5Tokenizer.from_pretrained("rinna/japanese-gpt2-medium") 
model = AutoModelForCausalLM.from_pretrained("rinna/japanese-gpt2-medium") 
# 推論 
input = tokenizer.encode(PREFIX_TEXT, return_tensors="pt") 
output = model.generate(input, do_sample=True, max_length=60, num_return_sequences=1) 
print(tokenizer.batch_decode(output))