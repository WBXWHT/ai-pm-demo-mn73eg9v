#!/usr/bin/env python3
"""
AI产品助手 Demo
我曾参与“AI艺术工坊”C端小程序的项目实习。作为产品实习生，我主要负责用户反馈的收集与分析，并基于此优化文生图功能的提示词推荐模块。通过引入ComfyUI工作流思路简化了用户操作路径，并协同技术同学测试了多种Lora模型的效果。迭代上线后
"""
import json
from datetime import datetime

class AIProductAssistant:
    def __init__(self):
        self.queries = 0
        self.start_time = datetime.now().isoformat()

    def analyze_intent(self, text):
        keywords = {"分析": "analyze", "推荐": "recommend", "查询": "query", "帮我": "assist"}
        for kw, intent in keywords.items():
            if kw in text:
                return {"intent": intent, "confidence": 0.88}
        return {"intent": "general", "confidence": 0.75}

    def respond(self, user_input):
        self.queries += 1
        result = self.analyze_intent(user_input)
        return f"[{result['intent']}] 已处理：{user_input}"

def main():
    print("=== AI产品助手 Demo ===")
    bot = AIProductAssistant()
    demos = ["帮我分析用户增长数据", "推荐AI功能方向", "查询本月活跃用户"]
    for q in demos:
        print(f"用户: {q}")
        print(f"AI: {bot.respond(q)}\n")
    print(json.dumps({"queries": bot.queries, "uptime": bot.start_time}, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
