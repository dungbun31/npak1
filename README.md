python3 -m venv venv

source venv/bin/activate

pip3 install -r requirements.txt


chmod +x scanner_docs.py

sudo ln -sf /home/dungbun/Desktop/prak1_v3/scanner_docs.py /usr/local/bin/scanner_docs
# npak1

- model.ipynb:
First, in the first cell, we install the necessary libraries
Next, the second cell imports the libraries and defines a text preprocessing function. This function takes a text string as input and performs cleaning steps such as converting all characters to lowercase, removing extra spaces and unnecessary punctuation.
In the third cell, the data is read from an Excel file with a relative path. This Excel file contains columns, each column representing a label (e.g. Personal data, HR data, …) and contains a list of corresponding keywords.
The fourth cell focuses on converting the data from the Excel file into a training dataset. This process is done by going through each column of the original DataFrame. For each column, missing values ​​(NaN) are removed, then the keywords are converted to strings and processed using the text_preprocess function. The result is two lists: one containing the processed text and one containing the corresponding labels, which are then merged into a new DataFrame with two columns: "text" and "label".
In the fifth cell, the dataset is split into a training set and a test set. Specifically, the "text" column is stored in the variable X and the "label" column in the variable y. Then, the train_test_split function is used to split the data with a ratio of 80% for training and 20% for testing.
Next, the sixth cell performs the vectorization of the text using TF-IDF. The vectorizer is trained on the training set (X_train) and converts the text samples into numeric vectors, and the test set (X_test) is also converted to vectors using the same trained vectorizer.
The seventh cell is the step of training the classification model using the Logistic Regression algorithm. The model is trained on the vectorized dataset (X_train_vect) with the corresponding labels (y_train).
After the model is trained, the eighth cell evaluates the performance of the model.
Finally, the ninth cell performs the step of storing the trained model and the TF-IDF vectorizer object into files ("model_trained.pkl" and "vectorizer.pkl").


- how the project works:
Your project operates in a continuous and rigorous process, starting with training the classification model in the model.ipynb file. In which, data from the Excel file (categories.xlsx) is processed and converted into (text, label) pairs after preprocessing and vectorization using TF-IDF, then the Logistic Regression model is trained and saved with the vectorizer as a pickle file in the model folder. Next, the file_processor.py module provides functions to extract text content from various file types such as .txt, .docx, .pdf, .eml, compressed files, or images (using OCR with Tesseract). Finally, the scanner_docs.py file serves as the command line interface for the project, where users only need to run the command with the path to the file to be analyzed; This script will use the functions in file_processor to take the text, load the model and vectorizer from the saved files, convert the text to vectors, and use the trained model to predict the label for the document, then print the results to the screen.
