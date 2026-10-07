class EmbeddingService:
    """Abstraction for embedding operational runbooks and postmortems."""

    def embed(self, text: str):
        raise NotImplementedError("Connect an embedding model in the next implementation phase.")
