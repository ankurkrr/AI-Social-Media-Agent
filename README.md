# AI Social Media Agent

Automate daily LinkedIn posts about trending AI technology topics using free large language models and GitHub Actions.

## Features
- Selects a trending AI technology topic using OpenRouter (free model)
- Generates a professional, eye-catching LinkedIn post
- Posts automatically to LinkedIn via LinkedIn API
- Runs daily via GitHub Actions

## Project Structure
```
main.py                  # Entry point
agents/
  topic_selector.py      # Gets trending AI topic
  content_writer.py      # Generates and beautifies LinkedIn post
  posting_agent.py       # Posts to LinkedIn
utils/
  config.py              # Loads environment variables
requirements.txt         # Python dependencies
.github/workflows/       # GitHub Actions workflow
```

## Setup
### 1. Clone the repository
```
git clone https://github.com/ankurkrr/socailagents.ai.git
cd socailagents.ai
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Configure API keys and secrets
**Do NOT commit your `.env` file!**
- Add `.env` to `.gitignore`.
- Store secrets in GitHub repository settings under `Settings > Secrets and variables > Actions`.
  - `OPENROUTER_API_KEY`: Your OpenRouter API key
  - `LINKEDIN_ACCESS_TOKEN`: Your LinkedIn API token
  - `LINKEDIN_PROFILE_ID`: Your LinkedIn profile URN (e.g., `urn:li:person:xxxx`)

### 4. Run locally
```
python main.py
```

### 5. Automate with GitHub Actions
Workflow file: `.github/workflows/linkedin-daily-post.yml`
- The workflow runs daily and posts to LinkedIn automatically.
- Make sure your secrets are set in GitHub.

## How It Works
1. **Topic Selection**: Uses OpenRouter's `deepseek/deepseek-r1-0528-qwen3-8b:free` model to get a trending AI topic.
2. **Content Generation**: Uses OpenRouter's `moonshotai/kimi-k2:free` model to generate a professional LinkedIn post.
3. **Beautification**: Formats the post with headline, emojis, and structure for maximum impact.
4. **Posting**: Publishes the post to LinkedIn using the LinkedIn API.
5. **Automation**: GitHub Actions runs the workflow daily.

## Adding More Features
- To post to other platforms, add new agents.
- To change models, update the model name in the agent files.
- To customize post style, edit `beautify_linkedin_post` in `content_writer.py`.

## Security
- Never commit API keys or secrets.
- Use GitHub Actions secrets for all credentials.

## License
MIT

---
Made with ❤️ by ankurkrr
