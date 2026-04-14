class BaseLLM:
    def generate(self, prompt):
        raise NotImplementedError("LLM must implement generate()")
