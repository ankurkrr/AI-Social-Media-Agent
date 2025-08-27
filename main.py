from agents.topic_selector import get_daily_topic
from agents.content_writer import generate_posts
from agents.posting_agent import post_to_linkedin

def run_daily():
    print("🚀 Running AI Social Media Agent...")
    topic = get_daily_topic()
    print("Topic:", topic)

    posts = generate_posts(topic)
    linkedin_post = posts.replace("1.", "").strip()
    post_to_linkedin(linkedin_post)

if __name__ == "__main__":
    run_daily()