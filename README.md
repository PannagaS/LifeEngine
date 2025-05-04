# Life Engine Simulation

A cellular-based life simulation inspired by The Life Engine website. This simulation models the evolution of simple organisms through cellular structures and interactions.

## Demo

### Basic Organism Movement
![Basic Movement](docs/gifs/basic_movement.gif)
*An organism with mover cells navigating the environment*

### Evolution in Action
![Evolution](docs/gifs/evolution.gif)
*Organisms evolving their cellular structure over time*

### Predator-Prey Interaction
![Predator-Prey](docs/gifs/predator_prey.gif)
*Killer cells hunting and consuming other organisms*

### Energy Production
![Energy Production](docs/gifs/energy_production.gif)
*Producer cells generating energy from sunlight*

### Cell Mutation
![Cell Mutation](docs/gifs/cell_mutation.gif)
*Cells mutating during reproduction*

> Note: To view these GIFs, run the simulation and use the screen recording feature of your operating system. The GIFs above are placeholders - you can replace them with actual recordings of your simulation in action.

## Features

### Cellular Structure
Organisms are composed of different cell types, each with a specific function:

```
┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
│  Mouth  │ │Producer │ │  Mover  │ │ Killer  │ │  Armor  │ │   Eye   │
│   🔴    │ │   🔵    │ │   🟡    │ │   🟣    │ │   ⚪    │ │   ⚪    │
└─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘
```

- **Mouth** (red): Eats food for energy
- **Producer** (cyan): Generates energy from sunlight
- **Mover** (yellow): Enables movement
- **Killer** (purple): Attacks other organisms
- **Armor** (gray): Provides protection
- **Eye** (white): Increases sight range

Example of a simple organism structure:
```
    [E]
    [M]
[P][B][M][K]
    [A]
```
Where:
- E = Eye
- M = Mover
- P = Producer
- B = Body
- K = Killer
- A = Armor

### Evolution System
- Cells can mutate during reproduction:
  - Add new cells
  - Change cell types
  - Remove existing cells
- Each cell type has specific functions and energy costs
- Organisms evolve by changing their cellular structure

### Environment
```
┌─────────────────────────────────┐
│  🌊  🏔️  🏜️  🌳  🌊  🏔️  🏜️  │
│  🌳  🌊  🏔️  🏜️  🌳  🌊  🏔️  │
│  🏜️  🌳  🌊  🏔️  🏜️  🌳  🌊  │
│  🏔️  🏜️  🌳  🌊  🏔️  🏜️  🌳  │
└─────────────────────────────────┘
```
- Dynamic world with different terrain types:
  - Land (🌳)
  - Water (🌊)
  - Mountains (🏔️)
  - Deserts (🏜️)
- Day/night cycle
- Weather system (clear, rainy, stormy, foggy)
- Temperature variations

### Energy System
```
┌─────────────┐
│  Producer   │
│  Energy +1  │
└─────┬───────┘
      │
┌─────▼───────┐
│    Mouth    │
│  Energy +50 │
└─────┬───────┘
      │
┌─────▼───────┐
│    Killer   │
│  Energy +25 │
└─────────────┘
```
- Producers generate energy from sunlight
- Mouths consume food for energy
- Killers gain energy from successful attacks
- Movers cost extra energy to reproduce
- Food blocks reproduction when present

### Movement and Interaction
```
┌─────────┐
│    ↑    │
│  ← O →  │
│    ↓    │
└─────────┘
```
- Organisms can rotate
- One-touch kill option for attacks
- Look range for finding food/prey
- Cells can't overlap with other organisms

## Requirements
- Python 3.8+
- Pygame
- NumPy

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/life_engine.git
cd life_engine
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Simulation
```bash
python main.py
```

## Controls
```
┌─────────────────────────┐
│        Controls         │
├─────────────────────────┤
│ Space: Pause/Resume     │
│ R: Reset simulation     │
│ Q: Quit simulation      │
│ ↑: Increase speed       │
│ ↓: Decrease speed       │
└─────────────────────────┘
```

The simulation speed can be adjusted in real-time:
- Press ↑ to increase the simulation speed
- Press ↓ to decrease the simulation speed
- The current speed is displayed in the simulation window

## Configuration
The simulation parameters can be adjusted in `core/config.py`:
- World size and grid settings
- Organism settings (initial count, energy, etc.)
- Food settings (spawn rate, energy value)
- Evolution settings (mutation rates, cell probabilities)
- Environment settings (temperature, weather)

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details. 