
from cgraph.test.utils import checkf

import cgraph as cg
import cgraph.sdf as sdf

def test_circle():
    x = cg.Symbol('x')
    y = cg.Symbol('y')

    c = sdf.Circle(center=[1,1], radius=1.)
    checkf(c.sdf, {x:2, y:1}, value=0., ngrad={x:1, y:0})
    checkf(c.sdf, {x:0.9, y:0.7}, value=-0.683772, ngrad={x:-0.316228, y:-0.948683})
    checkf(c.sdf, {x:5, y:4}, value=4, ngrad={x:0.8, y:0.6})

def test_halfspace():
    x = cg.Symbol('x')
    y = cg.Symbol('y')

    c = sdf.Halfspace(normal=[0,1], d=1)
    checkf(c.sdf, {x:0, y:0}, value=-1., ngrad={x:0, y:1})
