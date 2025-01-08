#!/usr/bin/env python3
import argparse
import subprocess
import os
import sys

# Define the directory where the scripts are located
SCRIPT_DIR = os.path.dirname("/Users/maxiscoding28/dev/python-sandbox/productivity/tck/")

def run_script(script_name, *args):
    """Run the specified Python script with additional arguments."""
    script_path = os.path.join(SCRIPT_DIR, f"{script_name}.py")
    if os.path.exists(script_path):
        # Use the same Python interpreter as running this script
        subprocess.run([sys.executable, script_path, *args])
    else:
        print(f"Error: Script {script_name}.py not found in {SCRIPT_DIR}")

def main():
    # Create the top-level parser
    parser = argparse.ArgumentParser(description="CLI app to run specific scripts.")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Available commands")

    # Subparser for 'create' command
    parser_create = subparsers.add_parser("create", help="Run the create script")
    parser_create.add_argument("directory_name", help="Directory name for the create script")
    parser_create.add_argument("description", help="Description for the ticket")

    # Subparser for 'goto' command
    parser_goto = subparsers.add_parser("goto", help="Run the goto script")
    parser_goto.add_argument("arg", help="Argument for the goto script")

    # Subparser for 'list' command
    parser_list = subparsers.add_parser("ls", help="Run the list script")
    # 'list' doesn't need additional arguments

    # Subparser for 'send' command
    parser_send = subparsers.add_parser("send", help="Run the send script")
    parser_send.add_argument("arg1", help="First argument for the send script")
    parser_send.add_argument("arg2", help="Second argument for the send script")

    # Parse the arguments
    args = parser.parse_args()

    # Route the command to the appropriate script
    if args.command == "create":
        run_script("create", args.directory_name, args.description)
    elif args.command == "goto":
        run_script("goto", args.arg)
    elif args.command == "ls":
        run_script("ls")
    elif args.command == "send":
        run_script("send", args.arg1, args.arg2)

if __name__ == "__main__":
    main()