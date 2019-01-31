class GameStats():
#this will track stats for alien invasion
        
        def __init__(self, ai_settings):
                self.ai_settings = ai_settings
                self.reset_stats()
                #start alien invasion an inactive state
                self.game_active = False
                
                #high score should never be reset
                self.high_score = 0
                
                
        
                
        def reset_stats(self):
                self.ships_left = self.ai_settings.ships_limit
                self.score = 0
                self.level = 1
                
                
                
