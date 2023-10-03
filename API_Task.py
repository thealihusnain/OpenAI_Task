import pprint
import google.generativeai as palm

# use the open ai key for the response of the prompt
palm.configure(api_key='AIzaSyBqQykkQPbY8ttnCKfDt8dJdO4fkw50YP0')

models = [
    m
          for m in palm.list_models()
          if 'generateText' in m.supported_generation_methods
          ]
model = models[0].name
print(models)
count = 1
while (0<count):
    prompt = input("Enter the any query: ")
# generate text is a function of generativeai 
    completion = palm.generate_text(
    model=model,
    prompt=prompt,
# The maximum length of the response
    max_output_tokens=80000,)
    prompt_text = completion.result
    print(prompt_text)
    count = int(input("Press '0' Exit, Otherwise Press 1 :"))