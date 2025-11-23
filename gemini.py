#!/usr/bin/env python3 

from google import genai
from google.genai import types
import sys


def query_api(query):
    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=query,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(
                # Dynamic thinking budget (-1)
                thinking_budget=-1
            )
        ),
    )
    return response.text


def check_if_args(args):
    if len(args) <= 1:
        return False
    return True


def has_brevity_flag(args):
    brevity = "-b"
    if brevity in args:
        return True
    return False


def add_brevity_statement(args):
    flag_index = args.index("-b")
    del args[flag_index]
    return args.insert(0, "Keep your answer to 100 words:")


def stringify_args(args):
    string_args = [str(item) for item in args]
    return " ".join(string_args)


def main():
    args = sys.argv[1:]

    if not check_if_args(args):
        print("No question asked")
        return

    if has_brevity_flag(args):
        add_brevity_statement(args)

    question = stringify_args(args)

    respone = query_api(question)

    print(respone)


if __name__ == "__main__":
    main()
