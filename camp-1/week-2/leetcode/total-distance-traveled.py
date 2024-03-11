class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
    
        if mainTank < 5:
            return 10 * mainTank
        total_km = 0

        while mainTank:
            if mainTank >= 5:
                mainTank -= 5
                total_km += 50
                if additionalTank:
                    mainTank += 1
                    additionalTank -= 1
            else:
                total_km += mainTank * 10
                mainTank -= mainTank
        return total_km
            