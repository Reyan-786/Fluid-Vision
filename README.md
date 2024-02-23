# Fluid Vision Prototype

## Introduction
Fluid Vision is a prototype tool that leverages the power of AI to scrape visual data from web pages. Using a combination of Selenium for taking screenshots and OpenAI's GPT model to analyze and interpret the content, this tool can extract information from any website and present it in a structured JSON format.

## Features
- Take screenshots of web pages automatically.
- Encode images for analysis.
- Utilize OpenAI's Vision GPT model to process and interpret webpage content.
- Present data in a user-friendly JSON format.

## Installation
To get started with Fluid Vision, clone this repository and install the required dependencies.

```bash
git clone https://github.com/Reyan-786/Fluid-Vision/
cd directory
pip install -r requirements.txt
```

## Usage
```bash
streamlit run --server.runOnSave True app.py
```

## Development
This prototype is in the early stages of development. Contributions to improve functionality or add new features are welcome. Please feel free to fork the project, make changes, and submit a pull request.

## License
Fluid Vision is released under the MIT License.

## Acknowledgements
A special thanks to OpenAI for providing the API that powers the core functionality of this scraper.
