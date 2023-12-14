class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.Token_exp_time = {}
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.Token_exp_time[tokenId] = self.timeToLive + currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.Token_exp_time and self.Token_exp_time[tokenId] > currentTime:
            self.Token_exp_time[tokenId] = self.timeToLive + currentTime

        
    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for token in self.Token_exp_time:
            if self.Token_exp_time[token] > currentTime:
                count += 1
        return count

        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)