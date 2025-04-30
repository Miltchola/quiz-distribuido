"""
Definição do protocolo comum para interoperabilidade entre clientes e servidores
"""

# Tipos de mensagens do cliente para o servidor
CLIENT_MESSAGES = {
    'CONNECT': 'connect',
    'ANSWER': 'answer',
    'DISCONNECT': 'disconnect'
}

# Tipos de mensagens do servidor para o cliente
SERVER_MESSAGES = {
    'WELCOME': 'welcome',
    'QUESTION': 'question',
    'FEEDBACK': 'feedback',
    'RESULT': 'result',
    'ERROR': 'error'
}

# Estrutura esperada para cada tipo de mensagem
MESSAGE_SCHEMAS = {
    CLIENT_MESSAGES['CONNECT']: {
        'required': ['type', 'player_name'],
        'optional': ['version']
    },
    CLIENT_MESSAGES['ANSWER']: {
        'required': ['type', 'question_id', 'answer'],
        'optional': []
    },
    SERVER_MESSAGES['WELCOME']: {
        'required': ['type', 'status', 'message', 'total_questions'],
        'optional': ['current_players']
    },
    SERVER_MESSAGES['QUESTION']: {
        'required': ['type', 'id', 'text', 'options'],
        'optional': ['time_limit']
    }
}

def validate_message(message, expected_type):
    """Valida se uma mensagem segue o protocolo definido"""
    if not isinstance(message, dict):
        return False
        
    schema = MESSAGE_SCHEMAS.get(expected_type)
    if not schema:
        return False
        
    # Verifica campos obrigatórios
    for field in schema['required']:
        if field not in message:
            return False
            
    # Verifica se o tipo está correto
    if message['type'] != expected_type:
        return False
        
    return True