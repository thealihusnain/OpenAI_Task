import pprint
import google.generativeai as palm


palm.configure(api_key='AIzaSyBqQykkQPbY8ttnCKfDt8dJdO4fkw50YP0')

models = [
    m
          for m in palm.list_models()
          if 'generateText' in m.supported_generation_methods
          ]
model = models[0].name
# print(model)
count = 1
while (0<count):

    prompt = input("Enter the any query: ")
    completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=1.0,
    # The maximum length of the response
    max_output_tokens=80000,)
    prompt_text = completion.result
    print(prompt_text)
    count = int(input("Press '0' Exit, Otherwise any number :"))