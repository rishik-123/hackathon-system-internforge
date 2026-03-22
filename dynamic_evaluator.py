from google import genai
client = genai.Client(api_key="AIzaSyCyJ7aGfTol-DiixHNXZawItMoZunq1Ml0")

def evaluate(question, student_answer):
    try:
        prompt = f"""
        Question: {question}
        Student Answer: {student_answer}
        Give score from 0 to 10. Only number.
        """

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        text = response.text.strip()
        score = float(text.split()[0])

        return score

    except Exception as e:
        print("AI Failed → Using fallback:", e)

        return fallback_score(question, student_answer)


# 🔥 SMART FALLBACK (BETTER THAN BEFORE)
def fallback_score(question, answer):

    keywords = question.lower().split()
    answer_words = answer.lower().split()

    match = 0
    for word in keywords:
        if word in answer_words:
            match += 1

    length_score = len(answer_words)

    # scoring logic
    score = (match * 2) + (length_score / 10)

    return min(round(score, 2), 10)