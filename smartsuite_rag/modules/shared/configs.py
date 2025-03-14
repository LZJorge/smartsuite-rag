import os

class Configs:
    @staticmethod
    def get(key):
        if key not in os.environ:
            raise ValueError(f"Missing environment variable: {key}")
        
        return os.environ[key]