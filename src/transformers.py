import torch
import numpy as np
from transformers import AutoTokenizer, AutoModelForMultipleChoice

class McqModel:
	def __init__(self, model_path = "model/"):
		self.path = model_path
		self.tokenizer = AutoTokenizer.from_pretrained(model_path)
		self.model = AutoModelForMultipleChoice.from_pretrained(model_path)

	def softmax(self, x):
		return np.exp(x) / np.sum(np.exp(x), axis=0)

	def inference(self, mcq):
		# Change format here
		question = mcq.get("question")
		choice0 = mcq.get("choice0")
		choice1 = mcq.get("choice1")
		choice2 = mcq.get("choice2")
		choice3 = mcq.get("choice3")

		assert question is not None, "Question cannot be empty"
		assert choice0 is not None, "First answer cannot be empty, remember that this is a mcq :)"
		assert choice1 is not None, "Second answer cannot be empty, remember that this is a mcq :)"

		choices = [choice0, choice1, choice2, choice3]
		choices = [choice for choice in choices if choice is not None]
		number_of_answers = sum(filter(None, choices))

		context = [question]*number_of_answers
		choices = choices[:number_of_answers]

		encodings = self.tokenizer(context, choices, truncation=True, padding=True)
		inputs = {k:  torch.tensor([v[i:i+4] for i in range(0, len(v), 4)]) for k, v in encodings.items()}
		output = self.model(**inputs)
		result = self.softmax(output.logits.detach().numpy())
		# Keep this if want to return only the highest probability answer
		# result = np.argmax(result)
		return result