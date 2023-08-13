class FoodCreation:
    TRADE_BONUS = 30
    def name(self): return LS("quality.deep_drilling", "Deep Drilling")
    def desc(self): return LS("quality.deep_drilling.desc",
        "Mines on [[ref:planet.mining]] planets produce an additional :O: and yield *{1}%* more income.", self.TRADE_BONUS)

    def sentiment(self): return QualitySentiment.Positive

    def applies(self, node):
        return node.NodeType == "planet.mining" and node.ActuallyProduces(Resource.All["O"]) 

    def effects(self, node): 
        return [
            ChangeProducts.AddOne(Resource.All["O"], "deep_drilling"),
            PercentageBonus.TradeIncome(self.TRADE_BONUS)
        ]