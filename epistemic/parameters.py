import logging
log = logging.getLogger("parameters")

import copy

class ParametersError(Exception):
    pass

class Parameters(object):
    # Put the default parameters here
    seed = 0
    landscape = None
    max_steps = 100
    # Followers move this often, even when the move is not better
    follower_move_p = .01
    neighbourhood_size = 1

    # Anything above this is the good stuff
    significance_cutoff = .5

    def __init__(self, **kwargs):
        self.agents_to_create = []
        for k, v in kwargs.items():
            if hasattr(self, k):
                log.info("Setting '%s' to %s", k, v)
                setattr(self, k, v)
            else:
                log.warning("'%s' is not a valid parameter (ignoring)", k)

    def add_agents(self, kind, number, placement=None):
        self.agents_to_create.append((kind, number, placement))
