from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from main import run_once  # heartbeat 1-cycle 실행

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"


# -------------------------
# /start
# -------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "APOS Control Plane online.\nCommands:\n/run <goal>\n/status"
    )


# -------------------------
# /run
# -------------------------
async def run(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /run <goal>")
        return

    goal = " ".join(context.args)

    await update.message.reply_text(f"Running APOS with goal:\n{goal}")

    result = run_once(goal)

    await update.message.reply_text(result)


# -------------------------
# /status
# -------------------------
async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("APOS is alive. Event store active.")


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("run", run))
    app.add_handler(CommandHandler("status", status))

    print("Telegram Control Plane running...")
    app.run_polling()


if __name__ == "__main__":
    main()