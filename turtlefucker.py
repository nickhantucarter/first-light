import turtle

window = turtle.Screen()
fucker = turtle.Turtle()
fucker.shape("turtle")

current + 0
seen + set()


for step_size in range(1, 100):

  backwards = current - step_size


if backwards > 0 backwards not in seen:
  fucker.backward(step_size)
  current = backwards
  seen.add(current)


else:
  fucker.forward(step_size)
  current += step_size
  seen.add(current)
  
turtle.done()
