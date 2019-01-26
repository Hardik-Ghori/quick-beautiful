Programming exercises - tutorial material for work with a beginner. I am searching for exercises that can be solved with a simple code and give properly impressive results.

Code in this repository is a mix of notes, used ideas and materials left as a feedback for the future.

# Exercises

## Hello world
Standard hello world example.

## Mandelbrot visualisation

Generation of beautiful Mandelbrot fractal. Demonstrates one of cases where vast computing power of a computer allows to achieve results unfeasible with human computing power due to a cost differences alone.

![mandelbrot.png](mandelbrot.png)

## Image generation

Making image out of simple shapes. For example group of dwarves in from of their home. Excellent situation to demonstarte why code reuse using functions is useful.

![dwarves.png](dwarves.png)

# Bonus

Materials showing interesting cases where programming is necessary:

* [7 Minutes of Terror: Curiosity Rover's Risky Mars Landing](https://www.youtube.com/watch?v=h2I8AoB1xgU) (bonus: [landing video](https://www.youtube.com/watch?v=svUJdzMHwmM) + [Curiosity rover descending on parachute, photo made by Mars Reconnaissance Orbiter](https://www.jpl.nasa.gov/spaceimages/details.php?id=PIA15978))

# Maintenance commands

## Reformat code to follow Python coding stadards

`autopep8 --in-place --recursive .`

[PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

## Run all Python scripts in one folder

`find . -maxdepth 1 -type f -name "*.py" -exec python3 {} \;`

Command based on one by [Jim Lewis](https://stackoverflow.com/a/10523492/4130619)
