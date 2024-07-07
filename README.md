# Cultural Identity of AI Models

## Overview
This repository contains the work done during my internship at NORA.ai in Norway, focused on discovering and researching the cultural identity of different AI models. The project aimed to analyze how well AI models align with Norwegian culture by comparing responses from models created by the Language Technology Group (LTG) at UIO, GPT-3.5-turbo, and GPT-4.

## Repository Structure

- `questions/`: Contains files with questions used for testing the AI models.
- `results/`: Contains the results of the testing.
- `scripts/`: Python scripts used for various tasks such as data processing and translation.
- `README.md`: This file.

## Project Details

### Models Tested
- **LTG Models**: Developed by the Language Technology Group at the University of Oslo (UIO).
- **GPT-3.5-turbo and GPT-4**: Developed by OpenAI.

### Methodology
1. **Question Formulation**: Questions were based on observations made during my three-month stay in Norway and Norwegian Citizenship practice tests. Each question was categorized by type and generality.
2. **Translation**: Questions were inputted into the models in Norwegian and responses were translated to English using the `BERT_m2m_100` model.
3. **Hardware**: The Norwegian Artificial Intelligence Cloud (NAIC) was utilized for running the models and translations.
4. **Comparison and Analysis**: Responses from the models were compared to evaluate their alignment with Norwegian culture.

### Tools and Technologies
- **NAIC**: For hardware resources.
- **BERT_m2m_100**: For translating Norwegian to English.
- **Python**: For data processing and translation (e.g., translating Excel columns).

## Files

### Questions
Contains various files used for testing the AI models. Each question includes the following attributes:
- **Type**: The category or nature of the question.
- **Generality**: The level of specificity or abstraction of the question.

### Translations
Includes a Python file (`translator.py`) used for translating Excel columns from Norwegian to English.

### Results
This directory holds the results of the AI model testing, including translated responses and analysis.

### Scripts
Python scripts used for various tasks such as:
- Data processing
- Translation of text and Excel columns



## Acknowledgments
- **NORA.ai**: For the internship opportunity.
- **LTG at UIO**: For providing the AI models.
- **OpenAI**: For GPT-3.5-turbo and GPT-4 models.
- **NAIC**: For providing hardware resources.

---
