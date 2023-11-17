#! /bin/env python3

import re

# Dicionário de intenções
intent_patterns = {
    'option1': re.compile(r'Quero mudar minha (.*)'), #testado com 'Quero mudar minha atualização de pagamento'
    'option2': re.compile(r'Quero consultar o (.*)'), #testado com 'Quero consultar o status do pedido'
}

# Dicionário de ações
def responseUpdate(prompt):
    print(f"Entendido, verei a situação da sua {prompt}")

def responseFollow(prompt):
    print(f"Entendido, consultarei o {prompt}")

action_mapping = {
    'option1': responseUpdate,
    'option2': responseFollow,
}

def process_intent(user_input):
    for intent, pattern in intent_patterns.items():
        match = pattern.match(user_input)
        if match:
            return intent, match.group(1)
    return None, None

def execute_action(intent, prompt):
    if intent in action_mapping:
        action = action_mapping[intent]
        action(prompt)
        return True
    return False

def main():
    loop = True

    while loop == True:

        user_input = input(">> ")
        if user_input == "sair":
            loop = False
        else:
            intent, prompt = process_intent(user_input)
            if intent:
                success = execute_action(intent, prompt)
                if success:
                    print('Ligue para a central e será informado, seu problema é grave!')
                else:
                    print('Ação não reconhecida.')
            else:
                print('Comando não compreendido.')

if __name__ == '__main__':
    main()