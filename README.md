# OpenAI Chat Completion Script

This script interacts with the OpenAI API to generate text completions based on given prompts. It supports reading input from a file or the output of a command, and allows users to select a prompt to use as a basis for the generated completion. Users can also edit the message before sending it to the API and can resend the request with a different model if desired.

## Requirements

* Python 3.6 or newer
* OpenAI Python library (`pip install openai`)
* An OpenAI API key

## Functions

### get_input_or_file_input()

This function parses command-line arguments to determine the source of the input content and returns the content and parsed arguments. It supports two mutually exclusive options:

- `--file`: Provide a filename to use as input.
- `--command-output`: Choose a command to run and use its output.

Additionally, it accepts the following optional arguments:

- `--model`: Model to use for the chat completion (default: value from the config file).
- `--temperature`: Temperature to use for the chat completion (default: value from the config file).

### select_prompt()

This function displays a list of available prompts to the user and asks them to select one by entering its corresponding number. It returns the selected prompt.

### edit_message_in_vim(message)

This function allows the user to edit the message in a text editor (lvim) before sending it to the API. It takes the initial message as input and returns the edited message.

### main()

The main function coordinates the entire process:

1. Get the input content and command-line arguments using `get_input_or_file_input()`.
2. Select a prompt using `select_prompt()`.
3. Display the message to be sent and ask the user for confirmation or editing.
4. If the user chooses to edit the message, use `edit_message_in_vim()` to edit the message.
5. Send the message to the OpenAI API and display the generated completion.
6. Ask the user if they are satisfied with the completion or want to resend the request with a different model (e.g., gpt-4).
7. If the user chooses to resend, update the model and repeat steps 5-6.

## Configuration

The script requires a configuration file located at `~/.openai_config` with the following structure:

```
[DEFAULT]
API_KEY = your_openai_api_key
MODEL = default_model_to_use
TEMPERATURE = default_temperature_to_use
```

## Usage

To use the script, run it with the desired options:

```bash
./openai_chat_completion.py --file input.txt --model gpt-3 --temperature 0.7
```

or

```bash
./openai_chat_completion.py --command-output git_commit
```


## Contributions
Contributions, issues, and feature requests are welcome!

## License
This project is licensed under the terms of the MIT license. See the LICENSE file for details.

Please note that you need to follow OpenAI's use case policy when using this script.

## Disclaimer
This script is provided as is, and you acknowledge that it may have potential bugs or limitations. By using this script, you acknowledge that you are responsible for compliance with any applicable local laws. The developers of this script are not liable for any damages or losses resulting from your use of the script.
