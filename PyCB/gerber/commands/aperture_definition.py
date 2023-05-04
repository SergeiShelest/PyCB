from PyCB.gerber.apertures import CircleAperture, RectangleAperture, ObroundAperture, PolygonAperture
from PyCB.utils import log


def get_by_index(list_, index, default=None):
    return list_[index] if index < len(list_) else default


def create_circle_aperture(sizes):
    return CircleAperture(
        diameter=get_by_index(sizes, 0, 0.0),
        hole_diameter=get_by_index(sizes, 1, 0.0)
    )


def create_rectangle_aperture(sizes):
    return RectangleAperture(
        x_size=get_by_index(sizes, 0, 0.0),
        y_size=get_by_index(sizes, 1, 0.0),
        hole_diameter=get_by_index(sizes, 2, 0.0)
    )


def create_obround_aperture(sizes):
    return ObroundAperture(
        x_size=get_by_index(sizes, 0, 0.0),
        y_size=get_by_index(sizes, 1, 0.0),
        hole_diameter=get_by_index(sizes, 2, 0.0)
    )


def create_polygon_aperture(sizes):
    return PolygonAperture(
        outer_diameter=get_by_index(sizes, 0, 0.0),
        vertices=get_by_index(sizes, 1, 0.0),
        rotation=get_by_index(sizes, 2, 0.0),
        hole_diameter=get_by_index(sizes, 3, 0.0)
    )


def init(router):
    @router.action("%/AD")
    def aperture_definition(ctx, index, shape, sizes):
        sizes = [float(size) for size in sizes.split("X")]

        match shape:
            case "C": aperture = create_circle_aperture(sizes)
            case "R": aperture = create_rectangle_aperture(sizes)
            case "O": aperture = create_obround_aperture(sizes)
            case "P": aperture = create_polygon_aperture(sizes)
            case _:
                log.warning("CMD", f"Unknown aperture shape {shape}. Index {index}.")
                return

        ctx.apertures.update({index: aperture})
