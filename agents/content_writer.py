import os
from dotenv import load_dotenv
import requests
load_dotenv()



def beautify_linkedin_post(post: str) -> str:
    """
    Enhance the LinkedIn post to be eye-catching and professional using formatting, emojis, and structure.
    """
    # Add a bold headline, emojis, and clear sections
    lines = post.strip().split('\n')
    headline = f"🚀 𝗧𝗿𝗲𝗻𝗱𝗶𝗻𝗴 𝗜𝗻𝘀𝗶𝗴𝗵𝘁𝘀"
    body = '\n'.join([f"👉 {line.strip()}" for line in lines if line.strip()])
    footer = "\n\n🔗 Comment Your Thoughts Below! #AI #Innovation #LinkedIn #Tech #Science"  
    return f"{headline}\n\n{body}{footer}"

def generate_posts(topic):
    prompt = f"""
    You are a Professional Linkedin Influencer. Write a professional LinkedIn post (50-100 words) about the following trending AI technology in 2025 topic: {topic}.
    Make it eye-catching, use bold statements, emojis, and a clear structure. Focus on impact, practical uses, and relevance for business or industry. Avoid beginner tips, challenges, or informal language. Do not include instructions for visuals.
    """
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {os.environ['OPENROUTER_API_KEY']}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "moonshotai/kimi-k2:free",
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.8,
        "top_p": 0.95
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    post = response.json()["choices"][0]["message"]["content"].strip()
    return beautify_linkedin_post(post)
