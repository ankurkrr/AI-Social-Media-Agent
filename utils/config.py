import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HF_API_KEY = os.getenv("HF_API_KEY")
LINKEDIN_ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")
LINKEDIN_PROFILE_ID = os.getenv("LINKEDIN_PROFILE_ID")
ZAI_API_KEY = os.getenv("ZAI_API_KEY")
#IG_ACCESS_TOKEN = os.getenv("IG_ACCESS_TOKEN")
#IG_BUSINESS_ACCOUNT_ID = os.getenv("IG_BUSINESS_ACCOUNT_ID")
