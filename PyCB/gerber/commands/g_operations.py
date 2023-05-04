

def init(router):
    @router.action("G/01")
    def set_interpolation_to_linear(_):
        pass

    @router.action("G/02")
    def set_interpolation_to_clockwise_circular(_):
        pass

    @router.action("G/03")
    def set_interpolation_to_counterclockwise_circular(_):
        pass

    @router.action("G/36")
    def set_polygon_mode_enable(ctx):
        ctx.polygon_mode = True

    @router.action("G/37")
    def set_polygon_mode_disable(ctx):
        ctx.polygon_mode = False
