"""Sosw Essential Orchestrator
"""

import logging

from sosw.orchestrator import Orchestrator
from sosw.app import LambdaGlobals, get_lambda_handler

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class EssentialOrchestrator(Orchestrator):
    pass


global_vars = LambdaGlobals()
lambda_handler = get_lambda_handler(EssentialOrchestrator, global_vars)
