from smartsuite_rag.modules.rag.repository import Repository
from smartsuite_rag.modules.rag.seeds.seed import seed

def load_rag():
    repository = Repository()
    is_database_empty = repository.count() == 0
    
    if is_database_empty:
        docs = [seed]

        repository.add(documents=docs)