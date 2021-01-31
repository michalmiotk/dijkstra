class Node():
    def __init__(self, optimistic_cost, est_tot_cost=float('inf'),past_cost=float('inf'), parent_node='None'):
        self.optimistic_cost = optimistic_cost
        self.est_tot_cost = est_tot_cost
        self.past_cost = past_cost
        self.parent_node = parent_node
    
    def __str__(self):
        return "past "+str(self.past_cost)+" parent "+str(self.parent_node)