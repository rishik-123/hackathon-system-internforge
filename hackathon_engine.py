from dynamic_evaluator import evaluate
from plagiarism_detector import check_plagiarism
from shortlist_engine import select_top_students
from result_mailer import send_results

def process_hackathon(email, questions, answers):

    scores = []

    # 🔹 Evaluate answers
    for q, ans in zip(questions, answers):
        score = evaluate(q, ans)
        scores.append(score)

    # 🔹 Plagiarism
    plag = check_plagiarism(answers)

    if plag:
        print("Plagiarism detected:", plag)

    # 🔹 Total Score
    total_score = sum(scores)

    # 🔹 Shortlist
    top_students = select_top_students(5)

    # 🔹 Send Results
    send_results(email, top_students)

    return total_score, "Completed"