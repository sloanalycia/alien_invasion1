class GameStats():
#this will track stats for alien invasion
        
        def __init__(self, ai_settings):
                self.ai_settings = ai_settings
                self.reset_stats()
                
         def reset_stats(self):
                self.ships_left = self.ai_settings.ships_limit
