from PyCB.gerber.enums import UnitSystem, Polarity


def init(router):
    @router.action("%/MO")
    def set_global_unit_imperial(ctx, unit_system):
        match unit_system:
            case "IN":
                ctx.global_unit_system = UnitSystem.IMPERIAL
                ctx.unit_system = UnitSystem.IMPERIAL
            case "MM":
                ctx.global_unit_system = UnitSystem.METRIC
                ctx.unit_system = UnitSystem.METRIC

    @router.action("%/LP")
    def set_polarity(ctx, polarity):
        match polarity:
            case "C": ctx.polarity = Polarity.CLEAR
            case "D": ctx.polarity = Polarity.DARK
