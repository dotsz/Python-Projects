import conway.q3 as q3
import conway.ui as ui

def start():
  # Get the initial state of the world
  world = q3.get_world()

  # Initialize the graphical user interface with this world state
  # Here, we pass the evolve function as a value rather than calling it.
  # The init function will call it when it needs to evolve the world.
  # Thus, init is a higher-order function!
  # Using a higher-order function here allows us to keep your code
  # easily separated from the given UI code!
  # We could also easily implement a different function that evolves
  # the world using a different set of rules, and pass that function 
  # here instead without changing any of the UI code!
  # Higher-order functions have many benefits!
  ui.init(world, q3.evolve)