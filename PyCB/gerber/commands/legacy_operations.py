from PyCB.gerber.enums import UnitSystem


def init(router):
    @router.action("G/54")
    def select_aperture(_):
        pass

    @router.action("G/55")
    def prepare_for_flash(_):
        pass

    @router.action("G/70")
    def set_unit_to_imperial(ctx):
        ctx.unit_system = UnitSystem.IMPERIAL

    @router.action("G/71")
    def set_unit_to_metric(ctx):
        ctx.unit_system = UnitSystem.METRIC

    @router.action("G/90")
    def set_coordinate_format_to_absolute(_):
        pass

    @router.action("G/91")
    def set_coordinate_format_to_incremental(_):
        pass

    @router.action("M/00")
    def program_stop(_):
        pass

    @router.action("M/01")
    def optional_stop(_):
        pass
