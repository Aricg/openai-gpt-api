# OpenAI API Interaction Tool

This Python script serves as a command-line tool to interact with the OpenAI API to perform various tasks, such as generating commit messages, debugging code, and creating documentation.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Configuration](#configuration)
3. [Usage](#usage)
    - [Input Methods](#input-methods)
    - [Prompt Selection](#prompt-selection)
    - [Editing Messages](#editing-messages)
4. [Customization](#customization)
    - [Commands](#commands)
    - [Prompts](#prompts)

## Prerequisites

- Python 3.x
- `openai` Python library
- An OpenAI API key

## Configuration

Before using the tool, create a configuration file called `.openai_config` in your home directory with the following format:

```
[DEFAULT]
API_KEY = your_openai_api_key
MODEL = default_model_name
TEMPERATURE = default_temperature
```

Replace `your_openai_api_key` with your actual OpenAI API key. Set `default_model_name` and `default_temperature` to your preferred default values (e.g., `text-davinci-002` and `0.8`).

## Usage

### Input Methods

The tool provides two input methods:

1. **File**: Use the `--file` option followed by the filename to read the input from a file.
   ```
   python gpt --file input.txt
   ```

2. **Command output**: Use the `--command-output` option followed by a command key to run a predefined command and use its output as input.
   ```
   python gpt --command-output git_commit
   ```

### Prompt Selection

After providing input, the tool will display a list of available prompts. Enter the number corresponding to the desired prompt, and the tool will generate a message to be sent to the OpenAI API.

### Editing Messages

Before sending the message, you have the option to edit it. Enter `edit` when prompted, and the message will open in your default text editor. Save your changes and exit the editor to confirm the message.

## Customization

### Commands

You can add custom commands to the `commands` dictionary in the script. Each key-value pair should have the command key as the key and the command as a list of strings. For example:

```python
commands = {
    "git_commit": ['git', 'status', '-v'],
    "my_custom_command": ['ls', '-la'],
}
```

### Prompts

You can add custom prompts to the `prompts` dictionary in the script. Each key-value pair should have the prompt key as the key and the prompt text as the value. For example:

```python
prompts = {
    "commit_message_prompt": "Given the changes in the provided Git diff...",
    "my_custom_prompt": "Write a brief summary of the following text...",
}
```
