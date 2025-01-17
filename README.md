# BERT-legal-argentina (LawBERTarg)

LawBERTarg is a BERT-based model (specifically RoBERTa) pretrained on Argentine legal texts. It is designed for simple tasks such as legal document classification or clause extraction in the context of Argentine law vocabulary.

This model is intended to assist in legal NLP tasks but is still in development. This model is for experimentation purposes only and should not be used for serious applications at this stage.

## Model Overview

- Model architecture: RoBERTa with DistilBERT dimensions.
- Training corpus: Argentine legal texts, including laws, regulations, contracts, among others.
- Tokenizer: ByteLevelBPE, trained on Argentine legal data to handle legal vocabulary and terminology efficiently.

## Status

This model is still in the early stages of development. Fine-tuning hyperparameters and testing have not yet been completed. As a result, the model is not yet optimized for production use.

## Usage

To use the model, install the necessary dependencies via `pip` and import from `transformers` from HugginFace:

```bash
pip install transformers
pip install torch
```

```python
from transformers import BertTokenizer, BertModel
```

then download the model and load it as pretrained:

```python
tokenizer = BertTokenizer.from_pretrained('path/to/LawBERTarg')
model = BertModel.from_pretrained('path/to/LawBERTarg')
```