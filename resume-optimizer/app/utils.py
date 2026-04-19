import os
import requests


def call_deepseek(prompt: str, model: str = "deepseek-chat") -> str:
    """调用 DeepSeek API 生成响应"""
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError("请设置 DEEPSEEK_API_KEY 环境变量")

    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"API 调用失败: {str(e)}")


def generate_analysis_prompt(resume: str, jd: str) -> str:
    """生成简历分析 Prompt"""
    return f"""你是一名专业的简历优化顾问。请分析以下简历与目标职位的匹配度，并严格按照格式输出。

【简历内容】
{resume}

【目标职位JD】
{jd}

【输出格式】
### 1. 匹配亮点
- 分点列出简历与JD高度匹配的内容

### 2. 主要缺口
- 分点列出简历中缺失或不符合要求的关键项

### 3. 具体优化建议
- 针对缺口提出可操作的优化建议，语言要专业"""


def generate_optimize_prompt(resume: str, jd: str, analysis: str) -> str:
    """生成简历优化 Prompt"""
    return f"""你是一名专业的简历优化顾问。请根据以下信息优化简历。

【原始简历】
{resume}

【目标职位JD】
{jd}

【匹配分析】
{analysis}

【优化要求】
1. 保持简历真实性，不虚构经历
2. 突出与JD匹配的亮点，用量化语言描述
3. 针对缺口合理调整表述（如强调技能迁移性）
4. 保持结构清晰，使用 Markdown 格式排版

请直接输出优化后的完整简历。"""