import random

class MakeHardPrompt:
    def get_tag(self):
        tag = ['セガサターン']
        return random.choice(tag)

    def get_hard_prompt(self, tag):
        hard_prompt = tag + "についての会話です。"
        hard_prompt += "2人の会話です。"
        hard_prompt += "A「こんにちは。ゆっくり霊夢です」"
        hard_prompt += "B「ゆっくり魔理沙だぜ」"
        hard_prompt += "A「"
        return hard_prompt

    def get_message(self, tag):
        editorial = ["って最高だよね？"]
        return tag + random.choice(editorial)


    def add_hard_prompt(self, history, text, hanashite):
        hard_prompt = history + text + '」'
        if hanashite == 0:
            hard_prompt += "B「"
        else:
            hard_prompt += "A「"
        return hard_prompt
