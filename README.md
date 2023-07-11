# GPT Python Script Documentation

This script interacts with OpenAI's GPT-3 or GPT-4 models to generate text completions based on given prompts. It provides options to use pre-defined prompts, files, or command outputs as input. The generated completion and input can be saved for future reference.

## Table of Contents

1. [Installation and Configuration](#installation-and-configuration)
2. [Usage](#usage)
3. [Command Line Arguments](#command-line-arguments)
4. [Adding Custom Prompts](#adding-custom-prompts)
5. [Adding Commands](#adding-commands)

## Installation and Configuration

Before running the script, ensure that you have Python and the `openai` Python package installed.

The script requires a configuration file named `.openai_config` located in your home directory. This file should contain your OpenAI API key, the default model, and temperature in the following format:

```
[DEFAULT]
API_KEY = your_openai_api_key
MODEL = model_name
TEMPERATURE = temperature_value
```

## Usage

To execute the script, navigate to the directory containing the script and run:

```
python gpt.py
```

## Command Line Arguments

The script supports several command line arguments:

- `--file`: Provide one or multiple filenames to use as input.
- `--command-output`: Choose a command to run and use its output.
- `--prompt`: Select a prompt by index.
- `--model`: Model to use for the chat completion.
- `--temperature`: Temperature to use for the chat completion.
- `--confirm-send`: Automatically confirm sending the message without prompt.
- `--model-selection`: Choose the GPT model to use without prompt.
- `--list-saved`: List all saved input-output files and exit.
- `--output`: Provide a custom path for saving the output.

## Adding Custom Prompts

You can add custom prompts by editing the `prompts.example` file in your home directory. The prompts should be in a Python dictionary format, with the keys being the prompt names and the values being the prompt texts.

## Adding Commands

You can add commands to be used with the `--command-output` argument by editing the `commands` dictionary in the script. The keys should be the command names and the values should be the command to run in a list format.

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

## Prompts
```
./gpt
Select a prompt:
0. commit_message_prompt
1. one_shot
2. document
3. debug
4. cover_letter
5. job_classifier
6. job_decider
```


