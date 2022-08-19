from transformers import T5Tokenizer, AutoModelForCausalLM
import random

class GetSentence:
    max_length = 140
    num_sequences = 1
    special_token = {'bos_token': '<s>',
        'cls_token': '[CLS]',
        'eos_token': '</s>',
        'mask_token': '[MASK]',
        'pad_token': '[PAD]',
        'sep_token': '[SEP]',
        'unk_token': '<unk>'}
    def get_sentence(self, prefix):
        tokenizer = T5Tokenizer.from_pretrained("rinna/japanese-gpt2-small") 
        #model = AutoModelForCausalLM.from_pretrained("../work/otoboku_output/")
        #model = AutoModelForCausalLM.from_pretrained("../work/little_output/")
        #model = AutoModelForCausalLM.from_pretrained("rinna/japanese-gpt2-small") 
        #model = AutoModelForCausalLM.from_pretrained("../work/all_output/") 
        
        list_model = ["../work/otoboku_output/", "../work/little_output/", "rinna/japanese-gpt2-small", "../work/all_output/"]
        model = AutoModelForCausalLM.from_pretrained(random.choice(list_model)) 
        
        # 推論
        prefix = self.special_token['bos_token'] + prefix + self.special_token['eos_token']
        input = tokenizer.encode(prefix, return_tensors="pt") 
        output = model.generate(
            input, 
            do_sample=True, 
            max_length=self.max_length, 
            num_return_sequences=self.num_sequences
        ) 
        return tokenizer.batch_decode(output)

    def get_message(self, sentence):
         temp = sentence.split(self.special_token['eos_token'])
         temp2 = temp[1].replace(self.special_token['unk_token'], '')
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

    


