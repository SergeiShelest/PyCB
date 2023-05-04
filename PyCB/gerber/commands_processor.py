from PyCB.utils import log

from .context import Context
from .parser import Parser, BaseTokens, AttributesTokens
from .router import ActionNotFound
from .commands import router


class CommandsProcessor:
    def __init__(self, file_path):
        self.context = Context()
        self.parser = Parser(file_path)

    def start(self):
        for token, match in self.parser.parse():
            try:
                match token:
                    case BaseTokens.OPERATION:
                        operation_code, operation_number = match

                        if operation_code in {"X", "Y", "I", "J"}:
                            router.call(operation_code, self.context, operation_number)
                        elif operation_code == "D" and int(operation_number) >= 10:
                            router.call(f"{operation_code}/#", self.context, operation_number)
                        else:
                            router.call(f"{operation_code}/{operation_number}", self.context)

                    case AttributesTokens():
                        attribute_name, *params = match
                        router.call(f"%/{attribute_name}", self.context, *params)

            except ActionNotFound as msg:
                log.warning("PROCESSOR", msg)


if __name__ == "__main__":
    import pprint

    cp = CommandsProcessor("/mnt/hdd1/PyCB/tests/gbr_files/hackrf-one-gerbers/hackrf-one-Front.gtl")
    cp.start()

    pprint.pprint(cp.context.draw_queue, width=100)
