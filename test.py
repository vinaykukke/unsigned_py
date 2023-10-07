
import hou
from collections import Counter
import numpy as np

# To reload all files, use hou.shelves.reloadShelfFiles. 
# To reload a single file, use hou.shelves.loadFile

def create_new_tool():
  unsinged_shelf_set: hou.ShelfSet = hou.shelves.newShelfSet(name="Unsigned", label="Unsigned")
  shelf: hou.Shelf = hou.shelves.newShelf(name="one", label="Test") 
  tool: hou.Tool = hou.shelves.newTool(name="unsigned_default_lighting", label="Lighting")
  unsinged_shelf_set.setShelves([shelf])
  shelf.setTools([tool])

def createFootball():
  parentNode: hou.Node = hou.node('/obj/grid1')
  platonic: hou.Node = parentNode.createNode("platonic")
  polybevel: hou.Node = parentNode.createNode("polybevel::3.0")
  polyextrude: hou.Node = parentNode.createNode("polyextrude::2.0")

  polyextrude.setNextInput(platonic)
  polybevel.setNextInput(polyextrude)

  platonic.parm("type").set(5)
  polyextrude.parm("dist").set(0.092)
  polyextrude.parm("splittype").set("elements")
  polybevel.parm("offset").set(0.023)

  polyextrude.moveToGoodPosition()
  polybevel.moveToGoodPosition()

def getAllNodes():
  parent: hou.Node = hou.node('/obj')
  children: hou.Node = parent.children()
  ## List Comprehension
  nodes = [x.type().name() for x in children]
  print(Counter(nodes))

def numpy_test():
  a = np.array([3, 99, 44], dtype=np.float64)
  print(a)

def createSphere(**kwargs) -> None:
  # Create a sphere with optional keyword arguments
  sphere: hou.Node = hou.node("/obj").createNode("geo").createNode("sphere")
  sphere.parm("type").set(2);

  # Set various properties based on kwargs
  if 'radius' in kwargs:
    sphere.parmTuple("rad").set((2,2,2))
    sphere.parm("rows").set(20)
    sphere.parm("cols").set(20)
    