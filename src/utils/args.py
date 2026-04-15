import argparse

parser = argparse.ArgumentParser(description="Djinni parser")
parser.add_argument(
    "--no-headless",
    action="store_false",
    dest="headless",
    help="Run browser in visible mode (default: headless)",
)
parser.add_argument(
    "--path",
    type=str,
    default="./",
    dest="path",
    metavar="PATH",
    help="Set directory to save the output JSON file (default: ./)",
)
parser.add_argument(
    "--out",
    choices=["file", "print", "both"],
    default="file",
    help="Output mode: save to file, print in terminal, or both (default: file)",
)
parser.add_argument(
    "--limit",
    type=int,
    default=15,
    dest="limit",
    metavar="NUMBER",
    help="Set number of recommended vacancies to return (default: 15). Woks only in recommendation mode.",
)
parser.add_argument(
    "-recs",
    action="store_true",
    dest="recommend",
    help="Recommendations mode: show recommended vacancies based on user preferences. This is the default mode.",
)
parser.add_argument(
    "-stat",
    action="store_true",
    dest="stats",
    help="Statistics mode: show vacancies statistics based on user preferences.",
)


args = parser.parse_args()

ARG_HEADLESS = args.headless
ARG_PATH = args.path
ARG_LIMIT = args.limit
ARG_OUT = args.out
ARG_STATS = args.stats
ARG_RECOMMEND = args.recommend
