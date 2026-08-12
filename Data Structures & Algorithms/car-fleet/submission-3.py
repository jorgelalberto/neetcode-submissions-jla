class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        targets = [None]*(max(position)+1)
        fleets = 0
        prev_fleet_arrival = 0

        for position_i, speed_i in zip(position, speed):
            targets[position_i] = speed_i

        for i, speed_i in enumerate(reversed(targets)):
            if speed_i == None:
                continue

            position_i = len(targets)-1 - i

            curr_fleet_arrival = (target-position_i)/speed_i
            # same fleet
            if curr_fleet_arrival <= prev_fleet_arrival:
                continue
            # different fleet
            prev_fleet_arrival = max(prev_fleet_arrival, curr_fleet_arrival)
            fleets += 1
        return fleets