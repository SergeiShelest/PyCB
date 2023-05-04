import os
import pkgutil

from PyCB.gerber.router import Router


router = Router()

self_path = os.path.dirname(__file__)

for loader, module_name, is_pkg in pkgutil.iter_modules([self_path]):
    module = loader.find_module(module_name).load_module(module_name)
    module.init(router)
