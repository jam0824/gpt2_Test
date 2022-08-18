import random

class MakeHardPrompt:
    def get_tag(self):
        tag = ['セガサターン']
        return random.choice(tag)

    def get_hard_prompt(self, tag):
        editorial = ["って最高だよね？"]
        hard_prompt = tag + "についての会話です。"
        hard_prompt += "AとBの2人の会話です。"
        hard_prompt += "A「こんにちは。ゆっくり霊夢です」"
        hard_prompt += "B「ゆっくり魔理沙だぜ」"
        hard_prompt += "A「" + tag + random.choice(editorial) + "」"
        hard_prompt += "B「"
        return hard_prompt