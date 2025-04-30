import json
import os

def load_questions(category):
    try:
        file_path = os.path.join('questions', f'{category.lower()}.json')
        with open(file_path, 'r', encoding='utf-8') as f:
            questions = json.load(f)
            
        # Adiciona IDs às questões
        for i, question in enumerate(questions):
            question['id'] = i + 1
            
        return questions
    except Exception as e:
        print(f"Erro ao carregar perguntas: {e}")
        return []