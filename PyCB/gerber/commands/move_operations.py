from PyCB.adt import Vector


def init(router):
    # TODO
    @router.action("X")
    def set_x_position(ctx, x):
        ctx.position = Vector(float(x) / 10**4, ctx.position.y)

    # TODO
    @router.action("Y")
    def set_y_position(ctx, y):
        ctx.position = Vector(ctx.position.x, float(y) / 10 ** 4)

    # TODO
    @router.action("I")
    def set_i_offset(ctx, i):
        pass

    # TODO
    @router.action("J")
    def set_j_offset(ctx, j):
        pass
