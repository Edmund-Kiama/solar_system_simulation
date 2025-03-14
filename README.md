# Solar System Simulation

This project is a simple solar system simulation using Pygame. It models the gravitational interactions between planets and the Sun, displaying their orbits in a 2D space.

## Features
- Simulates planetary orbits based on Newtonian gravity.
- Realistic mass, velocity, and distance scaling.
- Dynamic orbital path visualization.
- Adjustable planet configurations (easily extendable for more planets).

## Requirements
- Python 3.x
- Pygame

## Installation
1. Clone this repository:
   ```sh
   git clone git@github.com:Edmund-Kiama/solar_system_simulation.git
   cd solar_system_simulation
   ```
2. Install dependencies:
   ```sh
   pip install pygame
   ```

## How to Run
Simply execute the Python script:
```sh
python main.py
```

## Controls
- Close the window to exit the simulation.

## Code Overview
- `Planet` class: Represents a celestial body, calculating gravitational forces and updating positions.
- `main()` function: Initializes the Pygame window, creates planets, and runs the simulation loop.

## Future Improvements
- Add more planets (Jupiter, Saturn, Uranus, etc.).
- Implement zooming and panning controls.

## License
This project is open-source and available under the MIT License.

