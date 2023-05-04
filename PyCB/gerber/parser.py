import re
import enum

from PyCB.utils import log


def find_by_tokens(string, tokens):
    valid_matches = []

    for token in tokens:
        if matches := re.findall(token.value, string, re.ASCII):
            for match in matches:
                valid_matches.append((token, match))

            break

    return valid_matches


class AttributesTokens(enum.Enum):
    APERTURE_DEFINITION = r"(AD)D(\d+)([A-Z]),\s?((?:\d?\.\d+X?)+)"
    FORMAT_SPECIFICATION = r"(FS)(L|T)(A|I)X(-?\d+)Y(-?\d+)"
    UNIT = r"(MO)(IN|MM)"
    LOAD_POLARITY = r"(LP)(C|D)"
    LOAD_NAME = r"(LN)([A-Z_]+)"


class BaseTokens(enum.Enum):
    COMMENT = r"(G04) (.+)\*"
    ATTRIBUTE = r"(%)(.+)\*%"
    OPERATION = r"([A-Z])(-?\d+)"


class Parser:
    def __init__(self, file_path):
        self.__file_path = file_path

    def parse(self):
        with open(self.__file_path, "rt") as file:
            for line in file:

                matches = find_by_tokens(line, BaseTokens)
                if not matches:
                    continue

                if matches[0][0] == BaseTokens.ATTRIBUTE:
                    attribute = matches[0][1]
                    matches = find_by_tokens(line, AttributesTokens)

                    if not matches:
                        log.warning("PARSER", f"Unknown attribute {attribute}")
                        continue

                for token, match in matches:
                    yield token, match


if __name__ == "__main__":
    import sys

    try:
        gerber_path = sys.argv[1]
        parser = Parser(gerber_path)

        for i, c in enumerate(parser.parse()):
            t, m = c
            log.debug("PARSER", f"{i} {t.name} {m}")

    except IndexError:
        log.error("PARSER", "No input file.")
        exit(1)
