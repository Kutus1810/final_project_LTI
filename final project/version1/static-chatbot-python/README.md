# Static Chatbot Project

This project is a static chatbot built using Python for the backend and HTML, CSS, and JavaScript for the user interface. The chatbot fetches commands based on keywords provided by the user, utilizing a CSV file as its dataset.

## Project Structure

```
static-chatbot-python
├── src
│   ├── app.py               # Entry point of the application
│   ├── chatbot.py           # Main logic for the chatbot
│   ├── utils.py             # Utility functions for data processing
│   ├── static
│   │   ├── css
│   │   │   └── styles.css    # CSS styles for the user interface
│   │   ├── js
│   │   │   └── main.js       # JavaScript for user interactions
│   │   └── index.html        # Main HTML page for the chatbot interface
│   └── templates
│       └── index.html        # Jinja2 template for rendering the main page
├── data
│   └── keyword_commandsfianl.csv # Dataset mapping keywords to commands
├── tests
│   └── test_chatbot.py       # Unit tests for chatbot functionality
├── requirements.txt           # Project dependencies
├── .gitignore                 # Files and directories to ignore by Git
└── README.md                  # Project documentation
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd static-chatbot-python
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```
   python src/app.py
   ```

5. **Access the chatbot**:
   Open your web browser and navigate to `http://127.0.0.1:5000`.

## Usage

- Enter a query in the chatbot interface and submit it.
- The chatbot will process the query and return the corresponding commands based on the keywords found in the dataset.

## Testing

To run the unit tests for the chatbot functionality, execute the following command:
```
python -m unittest discover -s tests
```

## License

This project is licensed under the MIT License.