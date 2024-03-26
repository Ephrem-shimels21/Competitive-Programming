class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        total_seats = [0] * (n + 1)

        for first, last, seats in bookings:
            total_seats[first - 1] += seats
            total_seats[last] -= seats

        for i in range(1, len(total_seats)):
            total_seats[i] = total_seats[i - 1] + total_seats[i]
        
        return total_seats[:-1]
        