import numpy as np
from uuv_mission.dynamic import Mission, Submarine, ClosedLoop
from uuv_mission.control import PDController

# Load mission data
mission = Mission.from_csv("data/mission.csv")

# Create submarine and controller
submarine = Submarine()
controller = PDController()

# Connect the components
system = ClosedLoop(submarine, controller)

# Simulate without disturbances
disturbances = np.zeros(len(mission.reference))
trajectory = system.simulate(mission, disturbances)

# Test trajectory dimensions
assert trajectory.position.shape == (100, 2)

# Test that all positions are finite
assert np.all(np.isfinite(trajectory.position))

# Test that the submarine actually moves vertically
assert np.any(trajectory.position[:, 1] != 0)

print("All closed-loop tests passed!")

# Visualise the simulation
trajectory.plot_completed_mission(mission)