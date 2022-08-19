from transformers import T5Tokenizer, AutoModelForCausalLM
import random

class GetSentence:
    max_length = 100
    num_sequences = 1
    def get_sentence(self, prefix):
        tokenizer = T5Tokenizer.from_pretrained("rinna/japanese-gpt2-small") 
        #model = AutoModelForCausalLM.from_pretrained("../work/little_output/")
        model = AutoModelForCausalLM.from_pretrained("rinna/japanese-gpt2-small") 
        # 推論 
        input = tokenizer.encode(prefix, return_tensors="pt") 
        output = model.generate(
            input, 
            do_sample=True, 
            max_length=self.max_length, 
            num_return_sequences=self.num_sequences
        ) 
        return tokenizer.batch_decode(output)

    def get_message(self, sentence):
         temp = sentence.split('</s>')
         temp2 = temp[1].replace('<unk>', '')
         temp2 = self.exchage_words(temp2, ['」', '。', ' '], '\n')
         temp2 = temp2.replace('「', '\n')
         list_mesages = temp2.split('\n')
         list_mesages = list(filter(None, list_mesages))
         list_mesages = list(set(list_mesages))
         list_mesages = self.delete_list_min_message(list_mesages, 4)
         return list_mesages

    def add_yukkuri(self, list_messages):
        list_messages.insert(0, "こんにちは。ゆっくり霊夢です")
        list_messages.insert(1, "ゆっくり魔理沙だぜ")
        return list_messages


    def exchage_words(self, text, list_target_word, exchange_word):
        for w in list_target_word:
            text = text.replace(w, exchange_word)
        return text

    def delete_list_min_message(self, list_messages, min_word):
        list_return = []
        for w in list_messages:
            if len(w) > min_word:
                list_return.append(w)
        return list_return

    


