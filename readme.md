# Gemini-Quicksearch



I found myself opening up the browser a querying Google for simple key-bindings on my journey to learn Vim. I figured it would be much better for my workflow if I could quickly open the terminal in NeoVim and query the motion I needed. So Gemini-Quicksearch was born, a lightweight command-line tool that allows you to query **Gemini 2.5 Flash** directly from your terminal. 

Get concise or detailed responses depending on your preference all without leaving the shell.

It is very simple, we will see if I add to it in the future.

---

## Features

- Query Gemini 2.5 Flash from your terminal quickly.
- Optional `-b` (**brevity**) argument for short, concise responses.
- Easy to install and set up.

---

## Requirements

- Python 3.12+
- `pip` package manager
- Internet connection for querying Gemini 2.5 Flash
- Must have the GEMINI_API_KEY key set as an environment variable
- Only tested on a Linux system

---

## Installation

1. **Clone or download** this repository:

```bash
git clone https://github.com/aaronKilpatrick/gemini.git
cd gemini
```

2. **Install required Python package**:

```bash
pip install -q -U google-genai
```

3. **Make the script executable** (Linux/macOS):

```bash
chmod +x gemini.py
```

4. **Move it to a folder in your PATH** for global access:

```bash
sudo mv gemini.py /usr/local/bin/gemini
```

Now you can run `gemini` from anywhere in your terminal.

---

## Usage

Once installed, you can run `gemini` from your terminal to query Gemini 2.5 Flash.

### Basic Query

Simply type your question or prompt:

```bash
gemini how to delete inbetween braces nvim
```

### Brevity Mode

Use the `-b` flag to get short, concise responses:

```bash
gemini -b how to delete inbetween braces nvim
```

### Examples

```bash
# Detailed response
$ gemini how to delete inbetween braces nvim
To delete content **between** braces in Neovim:

1.  **`di{`**: This deletes the *inner* content, leaving the `{}` braces intact. Position your cursor anywhere inside or on a brace. (Think "delete inner curly brace").

etc...

# Brevity response
$ gemini -b how to delete inbetween braces nvim
To delete text *inbetween* braces `{}` in Neovim, place your cursor anywhere inside or on either of the braces and type `di{`.
```

---

## Arguments

| Flag | Description                          |
| ---- | ------------------------------------ |
| `-b` | Brevity mode: short, quick responses |

---

## License

MIT License – see [LICENSE](LICENSE) for details.

This project is **not affiliated with, endorsed by, or owned by Google**. All trademarks and copyrights belong to their respective owners.

---

## Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork the repo and submit pull requests.

---

## Author

Created by [Aaron Kilpatrick](https://github.com/aaronkilpatrick)

