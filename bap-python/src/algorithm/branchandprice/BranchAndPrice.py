# **********************************************************
# * Author        : XXXXXX
# * Email         : X@XXX.com
# * Create time   : 2022/XX/XX X:XX AM
# * Filename      : BranchAndPrice
# * Description   :
# **********************************************************
from queue import PriorityQueue

from src.algorithm.branchandprice.BapNode import BapNode
from src.algorithm.branchandprice.PricingProblem import PricingProblem
from src.algorithm.branchandprice.RestrictedMasterProblem import RestrictedMasterProblem


class BranchAndPrice:

    def __init__(self, silent=True):
        self.silent: bool = silent
        self.opt_flag: bool = False
        self._rmp: RestrictedMasterProblem = None
        self._sp: PricingProblem = None
        # solution information
        self.node_explored: int = 0
        self.total_cg_iteration: int = 0
        self._best_node: BapNode = None
        self.mip_search_gap: float = 0
        self.cpu_time: float = 0
        self.lb: float = 0
        self.ub: float = float('inf')
        self.root_relaxation_val: float = 0
        self._queue = PriorityQueue()
        self._solution_pool = PriorityQueue()

    def print_solution(self):
        """ Print solution. """
        pass

    def solve(self) -> bool:
        """ Solve problem and return whether problem is feasible. """
        pass

    def _branch_and_bound(self) -> None:
        """ Branch and Bound procedure. """
        pass

    def _add_node_to_queue(self):
        """ Run column generation, then add node to queue."""
        pass


