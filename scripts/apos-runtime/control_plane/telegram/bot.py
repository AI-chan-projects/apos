from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from main import run_once
from core.approval.approval_store import approval_store

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "APOS Control Plane Online\n/run <goal>\n/approve <id>\n/reject <id>"
    )


async def run(update: Update, context: ContextTypes.DEFAULT_TYPE):
    goal = " ".join(context.args)

    result = run_once(goal)

    await update.message.reply_text(str(result))


async def approve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    approval_id = context.args[0]

    result = approval_store.approve(approval_id)

    if result:
        await update.message.reply_text(f"APPROVED: {approval_id}")
    else:
        await update.message.reply_text("Invalid approval id")


async def reject(update: Update, context: ContextTypes.DEFAULT_TYPE):
    approval_id = context.args[0]

    result = approval_store.reject(approval_id)

    if result:
        await update.message.reply_text(f"REJECTED: {approval_id}")
    else:
        await update.message.reply_text("Invalid approval id")


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("run", run))
    app.add_handler(CommandHandler("approve", approve))
    app.add_handler(CommandHandler("reject", reject))

    print("APOS Control Plane running...")
    app.run_polling()


if __name__ == "__main__":
    main()