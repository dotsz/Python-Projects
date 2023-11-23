import conway.config as config
import tkinter as tk


def is_live(cell):
  return cell == '*'

def init(world, evolve_func):
  """Initialize a tkinter window to a size the will accomodate the
    given world.
    world must be a non-ragged 2d list of . or * characters"""

  # Calculate the size of the window
  width = len(world[0]) * config.cell_size
  height = len(world) * config.cell_size

  # Initialize the window
  window = tk.Tk()
  window.title("Life")
  window.geometry(str(width) + "x" + str(height))

  # Create a canvas to draw the world on
  canvas = tk.Canvas(window,
                     bg=config.backround_color,
                     height=height,
                     width=width)
  canvas.pack()

  # Yes! You can define functions within functions
  # This function will only be callable from within the init function
  # But all variables defined in the init function will be accessible
  def draw_world(world):
    """Draw the given world (a non-ragged 2d list of . or * characters)
      onto the given tkinter canvas.
      Each space in the world takes up a config.cell_size pixel square.
      Live cells (*) are drawn in the color config.live_color.
    """
    canvas.delete("all")  # Clear the canvas

    x = 0  # The horizontal position of the next cell to be drawn
    y = 0  # The vertical position of the next cell to be drawn
    # (Starting at the top left of the canvas)
    for row in world:
      x = 0  # Reset the horizontal position before drawing the next row
      for cell in row:
        if is_live(cell):
          # Draw a square representing the live cell
          # (Specify corners of the square anti-clockwise from top left)
          canvas.create_polygon(
              x,
              y,
              x,
              y + config.cell_size,
              x + config.cell_size,
              y + config.cell_size,
              x + config.cell_size,
              y,
              # Final argument is color of cell
              fill=config.cell_color)
        # Need to move to the next horizontal position on each iteration
        # of the inner loop
        x += config.cell_size
      # Next vertical position on each iteration of the outer
      y += config.cell_size

  def next_frame(world):
    """This is the main game loop. Draws the given current world state,
      then evolves the world state and schedules the next frame to be 
      drawn
      world must be a non-ragged 2d list of . or * characters
      """

    # Draw the current world state using the function defined above
    draw_world(world)

    # Calculate the next world state
    # Here, we call the function that was passed to the init function
    # (See the note in app.py regarding the call to ui.init)
    next_world_state = evolve_func(world)

    # Here, we set up yet another nested function that will call next_frame
    # using the next world state instead of the current world state.
    def do_next_frame():
      next_frame(next_world_state)

    # Schedule the next frame of the game
    # "After frame_length seconds, call the do_next_frame function"
    window.after(config.frame_length, do_next_frame)

  # Kick things off with an inital call to next_frame...
  next_frame(world)
  # ...and a call to tk.mainloop
  # (which makes the window.after call in next_frame work properly)
  tk.mainloop()
