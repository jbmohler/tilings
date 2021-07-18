from PIL import Image, ImageColor, ImageDraw
import transforms


class Polygon:
    # must define BASE_LABELS in derived classes

    def __init__(self, vertices):
        assert len(vertices) == len(self.BASE_LABELS)

        self._vertices = {k: v for k, v in zip(self.BASE_LABELS, vertices)}

    @classmethod
    def enum_edges(cls):
        labels = cls.BASE_LABELS
        offset = labels[1:] + labels[0]
        yield from zip(labels, offset)

    def midpoint(self, edge):
        return transforms.midpoint(self._vertices[edge[0]], self._vertices[edge[1]])

    def spin_reflect_across_edge(self, edge):
        """
        Reflect this Quad across the edge specified by a 2 character string.
        Returns the Quad with corresponding vertices labeled to match.

        Technically this is a 180 degree rotation around the midpoint of the
        specified edge.
        """

        """
        line = transforms.Line(self._vertices[edge[0]], self._vertices[edge[1]])

        # first reflect
        refl_vertices = {}
        for ll, vv in sorted(self._vertices.items()):
            f = lambda x: x if ll in edge else line.reflect
            refl_vertices[ll] = f(vv)

        # then, reflect across perpendicular
        perp = line.rotate_perpendicular()

        final = {}
        for ll, vv in sorted(refl_vertices.items()):
            final[ll] = perp.reflect(vv)
            """

        mid = self.midpoint(edge)

        f = transforms.reflection
        final = {ll: f(mid, vv) for ll, vv in self._vertices.items()}

        return self.__class__([final[ll] for ll in self.BASE_LABELS])

    def shrink_epsilon(self, eps=0.1):
        # for rendering

        center = self.center()
        # shorten all distances to vertices by epsilon factor
        pass

    def render(self, draw, fill, outline):
        vxs = [self._vertices[ll] for ll in self.BASE_LABELS]
        draw.polygon(vxs, fill=fill, outline=outline)

class Quad(Polygon):
    BASE_LABELS = "ABCD"

class Triangle(Polygon):
    BASE_LABELS = "ABC"


if __name__ == "__main__":
    q = Quad([(400, 415), (400, 433), (422, 433), (428, 395)])
    #q = Triangle([(400, 415), (400, 433), (422, 433)])

    im = Image.new("RGB", (1000, 1000), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    q.render(draw, ImageColor.getrgb("blue"), ImageColor.getrgb("black"))

    for edge in q.enum_edges():
        gen2 = q.spin_reflect_across_edge(edge)
        gen2.render( draw, ImageColor.getrgb("magenta"), ImageColor.getrgb("black"))
        for edge1 in q.enum_edges():
            if edge1 != edge:
                gen3 = gen2.spin_reflect_across_edge(edge1)
                gen3.render( draw, ImageColor.getrgb("green"), ImageColor.getrgb("black"))

    im.save("image.png", "PNG")
