from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from app.models.questionModel import Question

model = SentenceTransformer('all-MiniLM-L6-v2')

def find_similar_questions(new_question_title):

    all_questions = Question.get_all_questions()

    if not all_questions:
        return []

    titles = []

    for question in all_questions:
        titles.append(question['title'])

    title_embeddings = model.encode(titles)

    new_embedding = model.encode([new_question_title])

    similarities = cosine_similarity(
        new_embedding,
        title_embeddings
    )[0]

    similar_questions = []

    for index, score in enumerate(similarities):

        if score > 0.20:

            similar_questions.append({
                'question': all_questions[index],
                'score': round(score * 100, 2)
            })

    similar_questions.sort(
        key=lambda x: x['score'],
        reverse=True
    )

    return similar_questions[:5]