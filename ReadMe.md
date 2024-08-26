# Custom NER Model Training with spaCy

This project is a custom Named Entity Recognition (NER) model training script built with the `spaCy` library. The model is trained to identify and classify specific entities such as "MATERIAL" and "COLOR" in text. 

## Features

- **Custom Entity Recognition:** Identifies "MATERIAL" (e.g., `1234`, `5678`) and "COLOR" (e.g., `Red`, `Blue`) entities in text.
- **Flexible Training Data:** Easily extend the training data with more text examples and entities.
- **Model Export:** Trained model is saved to disk for future use.

## Getting Started

### Prerequisites

- Python 3.6+
- `spaCy` library

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```
2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`   
    ```
3. **Install the required dependencies**
    ```bash
    pip install spacy

    ```