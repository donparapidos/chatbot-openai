# chatbot-openai

1. create `.env` file in this repo and add our `OPENAI_API_KEY` to it
2. `run docker-compose up -d`
3. open your browser on http://127.0.0.1 and start chatting

# Params
Additionally you can specify as environment vars in `.env`
- `FLASK_SECRET_KEY` - create random string
- `TEMPERATURE` - defaults to 0.1
- `TOKENS` - defaults to 2048
- `PROMPT` - crate initial greeting and context for bot ( ex. "Hey, I am Jim, super smart bot. How can I help you?")
- `AI_NAME` - AI name for chatting (AI, bot, Jim, etc...)
- `USER_REFERENCE` - your user name (I, me, etc..)
- `ENGINE` - defaults to `text-davinci-003`

# Specific commands
say `clear history` to cleanup bot's conversation memory if he starts to act weird
