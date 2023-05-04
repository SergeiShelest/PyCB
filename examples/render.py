import os
import math

from PyCB import CommandsProcessor, Vector, PainterCairo, Render
from PyCB.gerber.shapes import Shape


def get_bounding_box(draw_queue: [Shape]) -> (Vector, Vector):
    star = Vector(math.inf, math.inf)
    end = Vector(-math.inf, -math.inf)

    for s in draw_queue:
        for pos in s.positions:
            if pos.x < star.x:
                star = Vector(pos.x, star.y)

            if pos.y < star.y:
                star = Vector(star.x, pos.y)

            if pos.x > end.x:
                end = Vector(pos.x, end.y)

            if pos.y > end.y:
                end = Vector(end.x, pos.y)

    return star, end


if __name__ == "__main__":
    cp = CommandsProcessor("/mnt/hdd1/PyCB/tests/gbr_files/hackrf-one-gerbers/hackrf-one-Edge_Cuts.gbr")
    cp.start()

    start_pos, end_pos = get_bounding_box(cp.context.draw_queue)

    output_path = "./output/"

    if not os.path.exists(output_path):
        os.mkdir(output_path)

    gerbers = {
        os.path.join(output_path, "edge-cuts.png"): "../tests/gbr_files/hackrf-one-gerbers/hackrf-one-Edge_Cuts.gbr",

        os.path.join(output_path, "f-silks.png"): "../tests/gbr_files/hackrf-one-gerbers/hackrf-one-F_SilkS.gto",
        os.path.join(output_path, "f-paste.png"): "../tests/gbr_files/hackrf-one-gerbers/hackrf-one-F_Paste.gtp",
        os.path.join(output_path, "f-mask.png"): "../tests/gbr_files/hackrf-one-gerbers/hackrf-one-F_Mask.gts",
        os.path.join(output_path, "f-copper.png"): "../tests/gbr_files/hackrf-one-gerbers/hackrf-one-Front.gtl",

        os.path.join(output_path, "i1-copper.png"): "../tests/gbr_files/hackrf-one-gerbers/hackrf-one-Inner3.gbr",
        os.path.join(output_path, "i2-copper.png"): "../tests/gbr_files/hackrf-one-gerbers/hackrf-one-Inner2.gbr",

        os.path.join(output_path, "b-copper.png"): "../tests/gbr_files/hackrf-one-gerbers/hackrf-one-Back.gbl",
        os.path.join(output_path, "b-mask.png"): "../tests/gbr_files/hackrf-one-gerbers/hackrf-one-B_Mask.gbs",
    }

    for png_output_path, grb_input_path in gerbers.items():
        render = Render(
            processor=CommandsProcessor(grb_input_path),
            painter=PainterCairo(png_output_path),

            scale=1000,
            start_pos=start_pos,
            end_pos=end_pos
        )

        render.draw()
