# Adversarial Text Attacks Against Detection of Computer-Generated Text

Code for loading computer-generated text datasets, training text classification models on these datasets, and evaluating adversarial text attacks against them.

Results to be published in the paper ``Evaluating Adversarial Robustness of Detection of Transformer-Generated Text".

## Install Requirements

`pip install -r requirements.txt`


## Data Dependencies

These experiments rely on several data sources and machine learning models to operate.  You must download these datasets and retrieve these models prior to running the code.

You'll need to run the following code from an environment where you have access to CUDA 11.0.  For example, a server running Jupyter Notebook with CUDA 11

Download the required data into "data" path.

### GPT-2

```
git clone git@github.com:openai/gpt-2-output-dataset.git
cd gpt-2-output-dataset
python download_dataset.py
```

### GPT-3

Download the file "175b_samples.jsonl" from the repo https://github.com/openai/gpt-3 as "gpt3_175b_samples.jsonl"

### Generate Datasets

Run the notebook "Construct_Datasets.ipynb"

This will convert the raw GPT-2 and GPT-3 test datasets into a format that is compatible with the Grover detection model and place them under "classification_data".  These same output datasets will be used for evaluating the statistical SVM models.

### Phrasal Feature Datasets

You'll need the following data files.

idioms.txt
cliche500.txt
archaisms.txt

### Download spacy model
`python -m spacy download en`

### Stanza
Because the coreference resolution is busted.
pip install git@github.com:stanfordnlp/stanza.git@dev



### MAUVE

`pip install mauve-text`

## Running the experiments

Run through the notebooks in order.  Intermediate data files can be used to avoid re-running sections (use data loading commands as appropriate).
