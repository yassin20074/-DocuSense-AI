#HuggingFace library for running ready-made NLP models 
from transformers import pipeline

#Creating models 
ner_pipeline = pipeline("ner", grouped_entities=True, model="dbmdz/bert-large-cased-finetuned-conll03-english")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

#A function for extracting entities
def extract_entities(text):
    raw_entities = ner_pipeline(text)
    
    #Converting technical symbols into understandable names 
    mapping = {
        "PER": "Person",
        "ORG": "Organization",
        "LOC": "Location",
        "MISC": "Miscellaneous"
    }

    #Create a variable to organize the data for each entity 
    formatted_entities = []
    for ent in raw_entities:
        formatted_entities.append({
            "word": ent['word'],
            "label": mapping.get(ent['entity_group'], ent['entity_group']),
            "score": round(float(ent['score']), 2)
        })
    return formatted_entities

#A function to summarize the text 
def summarize_text(text):
    if len(text.split()) < 30:#Protect the text if it is short 
        return text
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
        return summary[0]['summary_text']
