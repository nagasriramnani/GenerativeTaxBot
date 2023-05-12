import torch
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
from sentence_transformers import SentenceTransformer
from transformers import BartTokenizer, BartForConditionalGeneration
from torch.cuda.amp import autocast, GradScaler
from embeddings import read_all_files_in_folder, load_faiss_index, query_faiss
import warnings
warnings.filterwarnings("ignore")

TELEGRAM_BOT_TOKEN = 'YOUR BOT TOKEN'

device = 'cuda' if torch.cuda.is_available() else 'cpu'
retriever = SentenceTransformer("flax-sentence-embeddings/all_datasets_v3_mpnet-base", device=device)

folder_path = "taxinfo"
UK_TAX_DOCUMENT_TEXT = read_all_files_in_folder(folder_path)

EMBEDDINGS_FILE = "embeddings.pt"
QUESTIONS_FILE = "questions.txt"

faiss_index, questions = load_faiss_index(EMBEDDINGS_FILE, QUESTIONS_FILE)

tokenizer = BartTokenizer.from_pretrained('vblagoje/bart_lfqa')
generator = BartForConditionalGeneration.from_pretrained('vblagoje/bart_lfqa').to(device)

def format_query(query, context):
    context = [f"<P> {m['metadata']['paragraph']}" for m in context]
    context = " ".join(context)
    print("Context: {}".format(context))
    query = f"question: {query} context: {context}"
    return query

def generate_answer(query):
    scaler = GradScaler()
    inputs = tokenizer([query], max_length=1024, return_tensors="pt",truncation=True)
    with autocast():
        ids = generator.generate(input_ids=inputs["input_ids"].to(device),
                                 attention_mask=inputs["attention_mask"].to(device),
                                 min_length=26,
                                 max_length=256,
                                 do_sample=False, 
                                 early_stopping=True,
                                 num_beams=8,
                                 temperature=1.0,
                                 top_k=None,
                                 top_p=None,
                                 eos_token_id=tokenizer.eos_token_id,
                                 no_repeat_ngram_size=3,
                                 num_return_sequences=1)
    answer = tokenizer.batch_decode(ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
    return answer

GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up", "hey")
GOODBYE_KEYWORDS = ("bye", "goodbye", "see you later", "see you soon", "farewell", "adios", "ciao", "au revoir", "good night", "good day", "good morning", "good evening")

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}. I am a taxbot. Ask me a question about UK taxes and I will try to answer it based on the information provided. I am still learning so please be patient.')

async def start(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! I'm a Robert. I am here to help with your Tax issues.")

async def message(update: Update, context):
    print("Received message: " + update.message.text + " from " + update.effective_user.first_name)
    query = update.message.text
    if len(query.split(" ")) < 4:
        if any(word in query.lower() for word in GREETING_KEYWORDS):
            await update.message.reply_text(f'Hello {update.effective_user.first_name}. I am a taxbot. Ask me a question about UK taxes and I will try to answer it based on the information provided. I am still learning so please be patient.')
            return
        elif any(word in query.lower() for word in GOODBYE_KEYWORDS):
            await update.message.reply_text("Goodbye! Have a nice day!")
            return

    matches = query_faiss(retriever, faiss_index, questions, query, top_k=3)
    matches = [m for m in matches if m["score"] >= 0.1]
    if len(matches) == 0:
        await update.message.reply_text("Sorry, I don't know the answer to that question. Please try again.")
        return
    query = format_query(query, matches)
    await update.message.reply_text(generate_answer(query))

app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).connect_timeout(60).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(None, message))
print("Starting bot...")
print("Bot started!")
app.run_polling()

