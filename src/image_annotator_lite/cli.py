import argparse
from image_annotator_lite.core import build_snapshot


def main() -> None:
    parser = argparse.ArgumentParser(description="Utility to catalog image batches, labels, and manual review notes.")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    if args.summary:
        print(build_snapshot())


if __name__ == "__main__":
    main()
