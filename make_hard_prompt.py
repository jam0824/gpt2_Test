import random

class MakeHardPrompt:
    def get_tag(self):
        tag = ['セガサターン', '異世界', 'セガ', 'コミケ']
        return random.choice(tag)

    def get_hard_prompt(self, tag):
        editorial = ["って面白いよね", "っていいよね","ってどうなの？","って最高だよね"]
        hard_prompt = tag + "についての会話です。"
        hard_prompt += "AとBのふたりの会話です。"
        hard_prompt += "A「" + tag + random.choice(editorial) + "」"
        hard_prompt += "B「"
        return hard_prompt