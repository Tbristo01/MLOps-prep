from transformers import pipeline,logging


print("TASK : Transformers library: the pipeline() function.")

'''
The most basic object in the 🤗 Transformers library is the pipeline() function. 
It connects a model with its necessary preprocessing and postprocessing steps, allowing us to directly input any text and get an intelligible answer
'''

print("\nModel#1: sentiment-analysis")
# Reduce logging verbosity to hide the warnings
logging.set_verbosity_error()
classifier = pipeline("sentiment-analysis")
result = classifier(
    "I've been waiting for a HuggingFace course my whole life.")
print(result)


print("\nWe can even pass several sentences!")
result = classifier(
    ["I've been waiting for a HuggingFace course my whole life.", "I hate this so much!"]
)
print(result)


print("\nZero-shot classification")
'''
This pipeline is called zero-shot because you don’t need to fine-tune the model on your data to use it.
It can directly return probability scores for any list of labels you want!
'''
classifier = pipeline("zero-shot-classification")
result = classifier(
    "This is a course about the Transformers library",
    candidate_labels=["education", "politics", "business"],
)
print(result)


print("\n Text generation")
'''
Now let’s see how to use a pipeline to generate some text. 
The main idea here is that you provide a prompt and the model will auto-complete it by generating the remaining text. 
This is similar to the predictive text feature that is found on many phones. 
Text generation involves randomness, so it’s normal if you don’t get the same results as shown below.
'''


generator = pipeline("text-generation")
my_text="Testing 1234"
# my_text=input("Enter a sentences: ")
result=generator(f"{my_text}")
print(result)


print("\nUsing any model from the Hub in a pipeline")
generator = pipeline("text-generation", model="distilgpt2")
result= generator(
    "In this course, we will teach you how to",
    max_length=30,
    num_return_sequences=2,
)
print(result)

print("\nMask filling")
'''
The next pipeline you’ll try is fill-mask. 
The idea of this task is to fill in the blanks in a given text

The top_k argument controls how many possibilities you want to be displayed. 
Note that here the model fills in the special <mask> word, which is often referred to as a mask token.
Other mask-filling models might have different mask tokens, so it’s always good to verify the proper mask word when exploring other models. 
One way to check it is by looking at the mask word used in the widget.
'''
unmasker = pipeline("fill-mask")
result = unmasker("This course will teach you all about <mask> models.", top_k=3)
print(result)


print("\nNamed entity recognition")
'''
Named entity recognition (NER) is a task where the model has to find which parts of the input text correspond to entities such as persons, locations, or organizations.
'''

ner = pipeline("ner", aggregation_strategy="simple")
text = "My name is Sarah and I work at Apple in San Francisco."
results = ner(text)
print(results)

print("\nQuestion answering")
'''
The question-answering pipeline answers questions using information from a given context.
'''

question_answerer = pipeline("question-answering")
results=question_answerer(
    question="Where do I work?",
    context="My name is Sylvain and I work at Hugging Face in Brooklyn",
)
print(results)

print("\nSummarization")
'''
Summarization is the task of reducing a text into a shorter text while keeping all (or most) of the important aspects referenced in the text.
'''

summarizer = pipeline("summarization")
result = summarizer(
    """
    America has changed dramatically during recent years. Not only has the number of 
    graduates in traditional engineering disciplines such as mechanical, civil, 
    electrical, chemical, and aeronautical engineering declined, but in most of 
    the premier American universities engineering curricula now concentrate on 
    and encourage largely the study of engineering science. As a result, there 
    are declining offerings in engineering subjects dealing with infrastructure, 
    the environment, and related issues, and greater concentration on high 
    technology subjects, largely supporting increasingly complex scientific 
    developments. While the latter is important, it should not be at the expense 
    of more traditional engineering.

    Rapidly developing economies such as China and India, as well as other 
    industrial countries in Europe and Asia, continue to encourage and advance 
    the teaching of engineering. Both China and India, respectively, graduate 
    six and eight times as many traditional engineers as does the United States. 
    Other industrial countries at minimum maintain their output, while America 
    suffers an increasingly serious decline in the number of engineering graduates 
    and a lack of well-educated engineers.
"""
)

print(result)


print("\nTranslation")
'''
For translation, you can use a default model if you provide a language pair in the task name (such as "translation_en_to_fr").
'''
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")
result = translator("Ce cours est produit par Hugging Face.")
print(result)
