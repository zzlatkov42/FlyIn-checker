import os
import traceback

#function that return true or false based on the map
from ..parser.utils import parse_file

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

TEST_FOLDERS = {
    "maps/easy": True,
    "maps/medium": True,
    "maps/hard": True,
    "maps/invalid": False,
    "maps/invalid": False,
    "maps/crash": True,
}


def run_tests() -> None:
    """
    Execute automated tests on configuration files.

    Iterates through folders specified in `TEST_FOLDERS`, parses
    each file using `parse_file`, and compares the results against
    the expected outcome.

    Prints detailed test results to the console, including:
        - [OK] for passed tests
        - [FAIL] for failed tests
        - [CRASH] if an exception occurred during parsing

    Also prints a summary of total tests passed vs total tests run.

    Notes:
        - Uses color-coded output constants:
            BOLD, CYAN, GREEN, RED, YELLOW, RESET.
        - Assumes `TEST_FOLDERS` is a dictionary
            mapping folder paths to expected results.
        - `parse_file` is the function responsible
            for parsing and validating individual files.
    """
    total = 0
    passed = 0

    print(f"{BOLD}{CYAN}=== RUNNING TESTS ==={RESET}\n")

    for folder, expected in TEST_FOLDERS.items():
        if not os.path.exists(folder):
            print(f"{YELLOW}[WARNING]{RESET} Folder '{folder}' not found")
            continue

        print(f"{BOLD}Testing folder:{RESET} {folder}")

        for file in os.listdir(folder):
            path = os.path.join(folder, file)

            if not os.path.isfile(path):
                continue

            total += 1

            try:
                data: dict = {}
                result = parse_file(path, data)

                if result == expected:
                    print(f"{GREEN}[OK]{RESET} {file}")
                    passed += 1
                else:
                    print(
                        f"{RED}[FAIL]{RESET} {file} → "
                        f"Expected {expected}, got {result}"
                    )

            except Exception:
                print(f"{RED}{BOLD}[CRASH]{RESET} {file}")
                traceback.print_exc()

        print()

    print(f"{BOLD}======================{RESET}")
    print(f"{CYAN}Passed {passed}/{total}{RESET}")

    if passed == total:
        print(f"{GREEN}{BOLD}✅ ALL TESTS PASSED{RESET}")
    else:
        print(f"{RED}{BOLD}❌ SOME TESTS FAILED{RESET}")


if __name__ == "__main__":
    run_tests()
