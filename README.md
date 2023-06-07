# OpenAI Chat Commit Helper

## Overview

This Python script utilizes OpenAI's GPT-3 (or GPT-4) language model to generate git commit messages based on provided user instructions and optionally, the standard output and git status information. 

It's a command line tool that interacts with the user, gathering information to feed into the AI model and then displaying the generated output. The user can then approve this output or request another try. If the initial output isn't satisfactory, the script can resend the request using the GPT-4 model.

## Requirements

* Python 3.6 or newer
* OpenAI Python library (`pip install openai`)
* An OpenAI API key

## Setup

1. Clone this repository.
2. Install the OpenAI Python library if not already installed: `pip install openai`
3. Set your OpenAI API key in a `.openai_config` file in the same directory as the script. If the file doesn't exist, the script will create a default one on the first run. The `.openai_config` file should follow this format:

    ```
    [DEFAULT]
    API_KEY = sk-your-api-key
    MODEL = gpt-3.5-turbo
    TEMPERATURE = 0.5
    ```

## Usage

Clone this repository.

Install the OpenAI Python library if not already installed: pip install openai

Set your OpenAI API key in a .openai_config file in the same directory as the script. If the file doesn't exist, the script will create a default one on the first run. The .openai_config file should follow this format:
```
[DEFAULT]
API_KEY = sk-your-api-key
MODEL = gpt-3.5-turbo
TEMPERATURE = 0.5
```
Usage
You can run the script from the command line as follows:

```
python script_name.py [--include-stdout] [--aicommit] [--model MODEL] [--temperature TEMPERATURE]
--include-stdout: If this flag is provided, the script will include the standard output in the chat completion.
--aicommit: If this flag is provided, the script will create a git commit message, including the output of git status -v.
--model: The OpenAI model to use for the chat completion. Defaults to the value in the .openai_config file.
--temperature: The temperature to use for the chat completion. Defaults to the value in the .openai_config file.
```
After running the script, you'll be prompted to enter any additional instructions for the AI. The script will then display the message to be sent to the AI for confirmation. You can choose to send the message, edit it, or cancel the operation.

Once the message is sent and a response received, you'll be asked if you're happy with the response. If you're not, the script will resend the request with the GPT-4 model.

## Contributions
Contributions, issues, and feature requests are welcome!

## License
This project is licensed under the terms of the MIT license. See the LICENSE file for details.

Please note that you need to follow OpenAI's use case policy when using this script.

## Disclaimer
This script is provided as is, and you acknowledge that it may have potential bugs or limitations. By using this script, you acknowledge that you are responsible for compliance with any applicable local laws. The developers of this script are not liable for any damages or losses resulting from your use of the script.

