import argparse

# First create the argparse with the main help
parser = argparse.ArgumentParser(
  "Main text"
)

# Add multiple arguments
parser.add_argument(
  "multiple_args", 
  nargs='+', 
  type=str, 
  help="List of args"
)

# Add named arguments
parser.add_argument(
  "--named_arg", 
  help="Text to help"
)

# Add optional arguments
parser.add_argument(
    '--default_arg',
    help="Default argument",
    default=None
)

# If you're using LOGGER this is so useful
parser.add_argument(
    '--logger_level',
    help="Logger level, values available: DEBUG, INFO, WARNING, ERROR, CRITICAL",
    default="ERROR"
)

# And finally parse the args
args = vars(parser.parse_args())

# And get the args
multiple_args = args.get("multiple_args")
