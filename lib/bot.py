import openai
from time import time,sleep
from dotenv import load_dotenv
import os


load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
flask_secret_key = os.getenv("FLASK_SECRET_KEY", "changmetorandomkey")
temp = os.getenv("TEMPERATURE", 0.1)
tokens = os.getenv("TOKENS", 2048)
session_prompt = os.getenv("PROMPT", "Jaz sem Jože. Sem brihtna glava ki vse ve, vprašaj me karkoli.\n")
ai_name = os.getenv("AI_NAME", "Jože")
chatter_ref = os.getenv("USER_REFERENCE", "Jaz")
start_sequence = "\n%s: " % ai_name
restart_sequence = "\n%s: " % chatter_ref


def bot(prompt, chat_log, engine='text-davinci-003', temp=temp, tokens=tokens, n=1, stop=["\n"]):
    """main function for calling openai bot"""
    max_retry = 1
    retry = 0
    prompt_text = f'{chat_log}{restart_sequence}: {prompt}{start_sequence}:'
    print(len(prompt_text))
    # print(prompt_text)

    while True:
        try:
            response = openai.Completion.create(
                engine=engine,
                prompt=prompt_text,
                temperature=temp,
                max_tokens=tokens,
                n=n,
                stop=["\n"])
            text = response['choices'][0]['text'].strip()
            print(text)
            return text
        except Exception as e:
            retry += 1
            if retry >= max_retry:
                return "Error: %s" % e
            print('Error with OpenAI:', e)
            sleep(1)


def append_interaction_to_chat_log(question, answer, chat_log=None):
  """create log so that bot knows the context of the conversation"""
  if chat_log is None:
    chat_log = session_prompt
  return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
