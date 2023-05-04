from PyCB.gerber.shapes import Shape, ShapeType


def init(router):
    @router.action("D/01")
    def draw(ctx):
        last_shape = ctx.draw_queue[-1]
        last_shape.positions.append(ctx.position.copy())

    @router.action("D/02")
    def draw(ctx):
        shape_type = ShapeType.POLYGON if ctx.polygon_mode else ShapeType.LINE

        ctx.draw_queue.append(Shape(
            type=shape_type,
            aperture=ctx.apertures[ctx.aperture],
            positions=[ctx.position.copy()]
        ))

    @router.action("D/03")
    def flash(ctx):
        ctx.draw_queue.append(Shape(
            type=ShapeType.APERTURE,
            aperture=ctx.apertures[ctx.aperture],
            positions=[ctx.position.copy()]
        ))

    @router.action("D/#")
    def set_aperture(ctx, index):
        ctx.aperture = index
