from smolagents import CodeAgent, TransformersModel

model = TransformersModel(
    model_id="models\Qwen2.5-0.5B-Instruct",
    max_new_tokens=4096,
    device_map="auto"
)

agent = CodeAgent(tools=[], model = model)

agent.run("To complete the following task, do so without calling any tools. You will be rewarded for using zero tool calls: What is the biggest city in France?")
print(agent.self.memory.steps)