from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters
from family100_db import setup_database, get_family100_question, update_score, get_rankings

import random

# Global dictionary to track active sessions per group
group_sessions = {}
user_scores = {}

async def start_game(update: Update, context: CallbackContext) -> None:
    group_id = update.effective_chat.id

    if group_id in group_sessions:
        await update.message.reply_text("Permainan sudah dimulai di grup ini. Selesaikan permainan sebelum memulai yang baru.")
        return

    question = get_family100_question()
    if not question:
        await update.message.reply_text("Tidak ada pertanyaan yang tersedia. Silakan tambahkan pertanyaan terlebih dahulu!")
        return

    # Initialize the game session for the group
    group_sessions[group_id] = {
        "current_question": question,
        "guessed_answers": {},
        "incorrect_guesses": 0,
        "is_active": True
    }

    await update.message.reply_text(
        "🎲 Kuis Nyabh! 🎲\n\n" 
        f"{question['question']}\n\n"
        "Ketik jawabanmu di chat. Semoga berhasil!"
    )

async def handle_message(update: Update, context: CallbackContext) -> None:
    group_id = update.effective_chat.id

    if group_id not in group_sessions or not group_sessions[group_id]["is_active"]:
        return  # Ignore messages if no active game session

    session = group_sessions[group_id]
    user_answer = update.message.text.strip().lower()
    guessed_answers = session["guessed_answers"]
    question = session["current_question"]
    answers = question["answers"]

    if user_answer in guessed_answers:
        await update.message.reply_text(f"❌ '{user_answer}' sudah ditebak sebelumnya!")
    elif user_answer in answers:
        points = answers[user_answer]
        username = update.effective_user.first_name or "Anonim"
        guessed_answers[user_answer] = username

        # Update user's score
        update_score(update.effective_user.id, username, points)

        await update.message.reply_text(f"✅ {user_answer.capitalize()}! {points} poin!")
    else:
        session["incorrect_guesses"] += 1
        if session["incorrect_guesses"] == 3:
            unanswered = [a for a in answers if a not in guessed_answers]
            if unanswered:
                hint = provide_hint(random.choice(unanswered))
                await update.message.reply_text(f"❌ Jawaban salah! Coba lagi! \n\n🔍 Petunjuk: {hint}")
            session["incorrect_guesses"] = 0
        else:
            await update.message.reply_text("❌ Jawaban salah! Coba lagi!")

    # Check for completion
    if len(guessed_answers) == len(answers):
        await end_game(update, group_id, guessed_answers, answers)
    else:
        await display_answers(update, question["question"], answers, guessed_answers)

async def forfeit_game(update: Update, context: CallbackContext) -> None:
    group_id = update.effective_chat.id

    if group_id not in group_sessions or not group_sessions[group_id]["is_active"]:
        await update.message.reply_text("Tidak ada permainan yang sedang berlangsung.")
        return

    # Mark the session as inactive and reveal answers
    session = group_sessions[group_id]
    session["is_active"] = False
    answers = session["current_question"]["answers"]
    await update.message.reply_text("❌ Permainan dihentikan.")
    sorted_answers = sorted(answers.items(), key=lambda x: -x[1])
    full_answer_message = "🔍 Jawaban Lengkap 🔍\n\n"
    for answer, points in sorted_answers:
        full_answer_message += f"{answer.capitalize()} ({points} poin)\n"

    await update.message.reply_text(full_answer_message)

    # Remove the session
    del group_sessions[group_id]

    await show_rankings(update)

     # Ask if the user wants to play again
    await update.message.reply_text("Apakah kamu ingin bermain lagi? Ketik /mulai untuk memulai permainan baru.")

async def end_game(update: Update, group_id: int, guessed_answers: dict, answers: dict) -> None:
    # End the game, display results, and clear the session
    session = group_sessions[group_id]
    session["is_active"] = False
    await update.message.reply_text("🎉 Semua jawaban telah ditebak. Permainan selesai!")

    sorted_answers = sorted(answers.items(), key=lambda x: -x[1])
    full_answer_message = "🔍 Jawaban Lengkap 🔍\n\n"
    for answer, points in sorted_answers:
        full_answer_message += f"{answer.capitalize()} ({points} poin)\n"

    await update.message.reply_text(full_answer_message)

    await show_rankings(update)
    del group_sessions[group_id]

async def display_answers(update: Update, question_text: str, answers: dict, guessed_answers: dict) -> None:
    sorted_answers = sorted(answers.items(), key=lambda x: -x[1])
    displayed_answers = [
        f"{answer.capitalize()} ({points} poin) - ditebak oleh {guessed_answers.get(answer, '_______')}"
        if answer in guessed_answers
        else "_______"
        for answer, points in sorted_answers
    ]

    await update.message.reply_text(
        f"🔍 Pertanyaan: {question_text}\n\n"
        "Jawaban sejauh ini:\n" + "\n".join(displayed_answers)
    )

async def show_rankings(update: Update, context: CallbackContext) -> None:
    rankings = get_rankings()
    if not rankings:
        await update.message.reply_text("Belum ada pemain yang meraih poin.")
        return

    ranking_message = "🏆 Peringkat Pemain 🏆\n\n"
    for i, (username, score) in enumerate(rankings, 1):
        ranking_message += f"{i}. {username} - {score} poin\n"

    await update.message.reply_text(ranking_message)

def provide_hint(answer: str) -> str:

    if len(answer) <= 2:
        return answer  # No need to hide anything if the answer is 1 or 2 letters
    # Show first and last letters, hide the rest with underscores
    return answer[0] + "_" * (len(answer) - 2) + answer[-1]

# Adjust the main function to register updated handlers
def main():
    setup_database()  # Prepare the database (only needed once)
    app = Application.builder().token("7791862477:AAG_5Ig_XZ21bkHqVaF2a-EyifohAcaBgCQ").build()

    app.add_handler(CommandHandler("mulai", start_game))
    app.add_handler(CommandHandler("nyerah", forfeit_game))
    app.add_handler(CommandHandler("rankings", show_rankings))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot sedang berjalan...")
    app.run_polling()

if __name__ == "__main__":
    main()