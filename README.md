- run command on kali:
    - Set up the environment:
        "python3 -m venv venv"
        "source venv/bin/activate"
        "pip3 install -r requirements.txt"

    - add execute permission to file - "chmod +x scanner_docs.py:"
    - create a symbolic link to the /usr/local/bin/ address - "sudo ln -sf /home/.../prak1_v3/scanner_docs.py /usr/local/bin/scanner_docs
    - run utility - "scanner_docs + 'path file'"

# npak1

- model.ipynb:
    Traning the model: model.ipynb(steps by step)
    - Install the necessary libraries
    - Import the libraries and defines a text preprocessing function( converting all characters to lowercase, removing extra spaces and unnecessary punctuation) . 
    - The data is read from an Excel file 
    - Convert the data from the Excel file into a training dataset. 
    - The train_test_splits split the data with a ratio of 80% for training and 20% for testing. 
    - Perform the vectorization of the text using TF-IDF.
    - Train the classification model using the Logistic Regression algorithm. The model is trained on the vectorized dataset (X_train_vect) with the corresponding labels (y_train). 
    - After the model is trained, evaluate the performance of the model.  
    - Store the trained model and the TF-IDF vectorizer object into files ("model_trained.pkl" and "vectorizer.pkl").



File_processor.py module provides functions to extract text content from various file types such as .txt, .docx, .pdf, .eml, compressed files, or images (using OCR with Tesseract). 

Scanner_docs.py file uses the functions in file_processor to take the text, load the model and vectorizer from the saved files, convert the text to vectors, and use the trained model to predict the label for the document, then print the results to the screen.
