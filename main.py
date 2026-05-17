import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8821928224:AAGXD025lJH5VaJlkSgAwC1Q25pLOBm9uwk"

class Handler(BaseHTTPRequestHandler):
def do_GET(self):
self.send_response(200)
self.end_headers()
self.wfile.write(b"Bot is running")

def run_web():
port = int(os.environ.get("PORT", 10000))
server = HTTPServer(("0.0.0.0", port), Handler)
server.serve_forever()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
await update.message.reply_text("🔥 FloociBot is working!")

threading.Thread(target=run_web).start()

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot started...")
app.run_polling()
