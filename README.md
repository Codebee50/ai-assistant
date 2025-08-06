# AI Assistant

A Gradio-based AI chatbot powered by OpenAI's GPT-4o-mini model with custom tools and functionality.

## Prerequisites

- Python 3.7 or higher
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Codebee50/ai-assistant.git
cd ai-assistant
```



2. Create a virtual environment
```bash
python -m venv venv
```

3. Activate the virtual environment
```bash
python -m venv venv
```


4. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your environment variables:
   - Create a `.env` file in the root directory
   - Add your OpenAI API key:
```
OPENAI_API_KEY=<your-api-key-here>
```

## Usage

Run the application:
```bash
python main.py
```

The application will:
1. Validate your OpenAI API key
2. Launch a Gradio chat interface in your browser
3. Provide an interactive AI assistant experience

## API Key Setup

Make sure your OpenAI API key:
- Has no leading or trailing whitespace
- Is properly set in your `.env` file

If you encounter API key issues, check the troubleshooting guidance provided in the application output.




## Configuration

The application uses GPT-4o-mini by default. You can modify the model in `main.py` if needed:

```python
MODEL = "gpt-4o-mini"  # you can choose to Change this to use a different model
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request


## Troubleshooting

If you encounter issues:
- Ensure your OpenAI API key is valid and properly formatted
- Check that all dependencies are installed correctly
- Verify your Python version meets the requirements


