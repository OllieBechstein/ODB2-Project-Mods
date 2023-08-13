
class PerkLunchtime(GlobalCondition):
    def __init__(self, amount):
        self._amount = amount
    
    def activate(self):
        self.react_to(Trigger.PlanetColonized, self.check)

    def info(self):
        info = CondInfo()
        info.FullDescription = LStr("perk.lunchtime.desc", self._amount)
        return info

    def check(self, data):
        if not data["node"].NodeType.startswith("planet."): return
        triggered = data["node"].IsProducerOf(Resource.All["F"])
        if triggered:
            commands.IssueScriptedConsequence(ConsGrantResources(self._amount, Resource.Cash, data["node"]))
