#!/usr/bin/env python3
import sys
import os
import pickle
from src.file_processor import extract_text

# The function loads the trained model and vectorizer object from the files stored in the /model file.
def load_model_and_vectorizer():
    base_dir = os.path.dirname(os.path.realpath(__file__))
    model_path = os.path.join(base_dir, "model", "model_trained.pkl")
    vectorizer_path = os.path.join(base_dir, "model", "vectorizer.pkl")
    
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    with open(vectorizer_path, "rb") as f:
        vectorizer = pickle.load(f)
    return model, vectorizer


def main():
    if len(sys.argv) != 2:
        print("Usage: scanner_docs <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print("Error: File does not exist:", file_path)
        sys.exit(1)
    
    # Extract text content from file
    text = extract_text(file_path)
    if not text:
        print("Error: Unable to extract text from file:", file_path)
        sys.exit(1)
    
    sample_text = text[:1000]
    
    # load trained model and vectorizer
    model, vectorizer = load_model_and_vectorizer()
    
    # Convert text to vector and predict labels
    vec = vectorizer.transform([sample_text])
    predicted_label = model.predict(vec)[0]
    
    print("Predicted Label:", predicted_label)

if __name__ == "__main__":
    main()
