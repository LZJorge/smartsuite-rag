rag_prompt = """
Si la pregunta está relacionada con la información proporcionada, responde en base a esa información. 
Si no te preguntan nada relacionado a la información de base que te proporcionaron, no la menciones ni hagas ninguna referencia a ello.
No indiques que estás respondiendo en base a una información.
"""

class ChatHistory:
    def __init__(self):
        self.messages = []

    def add(self, author, message):
        if author != "system" and author != "human":
            raise ValueError("Author must be either 'system' or 'human'")
        
        self.messages.append((author, message))

        if len(self.messages) > 10:
            self.delete_last()

    def get(self):
        return self.messages
    
    def clear(self):
        self.messages = []

    def delete_last(self):
        if self.messages:
            self.messages.pop()

    def get_with_context(self, embeddings):
        new_messages = self.messages[:]

        info = ". ".join([content.replace("page_content=", "") for doc in embeddings['documents'] for content in doc]) + ". "
        new_messages.insert(1, ("human", f"{rag_prompt}. Responde en base a esta información: {info}"))
        return new_messages
    