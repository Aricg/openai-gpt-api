# GPT OpenAI Chat Completion CLI

This Python script provides a command-line interface (CLI) to interact with the OpenAI GPT models (GPT-3 and GPT-4) for chat completion tasks. It allows users to provide input via text files or command output and select a predefined prompt. The script also supports editing the message using a text editor (Vim) and saving input-output pairs for future reference.

## Table of Contents

1. [Requirements](#requirements)
2. [Configuration](#configuration)
3. [Usage](#usage)
4. [Functions](#functions)

## Requirements

- Python 3.x
- OpenAI Python library

## Configuration

Before using the script, an OpenAI API key and other settings must be configured in a file named `.openai_config` located in the user's home directory. The file should contain the following information:

```
[DEFAULT]
API_KEY = your_openai_api_key
MODEL = gpt-3
TEMPERATURE = 0.8
```

Replace `your_openai_api_key` with your actual OpenAI API key.

## Usage

The script can be run from the command line using the following syntax:

```
python gpt_openai_chat_completion.py [options]
```

Options:

- `--file`: Provide one or multiple filenames to use as input
- `--command-output`: Choose a command to run and use its output as input
- `--model`: Model to use for the chat completion (default: gpt-3)
- `--temperature`: Temperature to use for the chat completion (default: 0.8)
- `--list-saved`: List all saved input-output files and exit

## Functions

The script contains several functions that handle different aspects of the CLI:

1. `read_prompts()`: Reads prompts from a file named `prompts.example` located in the user's home directory and returns a dictionary of prompts.
2. `get_input_or_file_input()`: Parses command-line arguments and returns the input content and argument values.
3. `list_saved_files()`: Lists saved input-output files and returns the name of the selected file.
4. `select_prompt()`: Allows the user to select a prompt from a list of predefined prompts and returns the selected prompt.
5. `edit_message_in_vim(message)`: Opens the provided message in Vim for editing and returns the edited message.
6. `save_input_output(input_content, output_content)`: Saves input and output content to timestamped files in a `.gpt` directory located in the user's home directory.
7. `main()`: Main function that orchestrates the script's workflow.

## Workflow

1. The script reads the prompts from the `prompts.example` file.
2. It parses the command-line arguments and gets the input content.
3. The user selects a prompt.
4. The message is displayed, and the user can choose to send the message, edit it, or cancel the operation.
5. The user selects the GPT model to use (GPT-3 or GPT-4).
6. The script sends the message to the OpenAI API and receives the chat completion output.
7. The input and output content are saved to timestamped files in the `.gpt` directory.
8. The user can choose to exit or continue with another input.


