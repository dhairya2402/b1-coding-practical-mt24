import numpy as np
from uuv_mission.dynamic import Mission

mission = Mission.from_csv("data/mission.csv")

# Test 1: Check the number of data points
assert len(mission.reference) == 100
assert len(mission.cave_height) == 100
assert len(mission.cave_depth) == 100
print("Test 1 passed")

# Test 2: Check the first values
assert np.isclose(mission.reference[0], 0.0)
assert np.isclose(mission.cave_height[0], 30.0)
assert np.isclose(mission.cave_depth[0], -30.0)
print("Test 2 passed")

# Test 3: Check the array types
assert isinstance(mission.reference, np.ndarray)
assert isinstance(mission.cave_height, np.ndarray)
assert isinstance(mission.cave_depth, np.ndarray)
print("Test 3 passed")

print("All mission tests passed!")