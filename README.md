# Community Prediction Model

## Overview
This project aims to predict the community of individuals based on their surnames. The model is designed to work primarily with Indian surnames, with a significant focus on Hindi and Marathi-speaking communities. It leverages machine learning techniques to analyze and provide predictions, though the model is still being fine-tuned to improve accuracy and extend its coverage across diverse Indian communities.

## Features
- **Surname-Based Prediction**: Uses advanced machine learning algorithms to predict community.
- **Language Focus**: Primarily trained on Hindi and Marathi surname datasets.
- **API Integration**: A Flask-based application providing a RESTful API for predictions.
- **Future Enhancements**: Plans to broaden the dataset and improve prediction accuracy for other Indian languages and communities.

## Technologies Used
- **Python**
  - Flask (for web application)
  - Scikit-learn (for model training)
  - Joblib (for model serialization)
- **GitHub LFS**: For handling large model files.
- **Machine Learning**: Random Forest algorithm.

## How It Works
1. **Input**: Users provide a surname.
2. **Processing**: The input is encoded and passed through a pre-trained Random Forest model.
3. **Output**: Predicted community is returned.

## Current Limitations
- The model's accuracy is skewed towards Hindi-Marathi communities due to the current dataset.
- Prediction accuracy may vary for other regional surnames.

## Future Plans
- Expand the dataset to include surnames from diverse Indian states and communities.
- Integrate user feedback to refine predictions.
- Optimize the machine learning pipeline for better accuracy and performance.

## Installation
### Prerequisites
- Python 3.8 or higher
- Pip

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/insightfulMind/predmodel.git
   ```
2. Navigate to the project directory:
   ```bash
   cd predmodel
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```

## Usage
- Access the application via `http://127.0.0.1:5000/`.
- Enter a surname in the input field and click "Predict".
- View the predicted community.

## Contributing
We welcome contributions to improve the model and expand its scope. Please fork the repository, create a feature branch, and submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
If you have any questions or suggestions, feel free to reach out via the Issues tab on GitHub.