# tests/conftest.py

import pytest
from app.calculation import CalculationFactory
from app.calculation import (
    AddCalculation,
    SubtractCalculation,
    MultiplyCalculation,
    DivideCalculation,
)

@pytest.fixture(autouse=True)
def reset_calculation_factory():
    CalculationFactory._calculations.clear()
    CalculationFactory.register_calculation('add')(AddCalculation)
    CalculationFactory.register_calculation('subtract')(SubtractCalculation)
    CalculationFactory.register_calculation('multiply')(MultiplyCalculation)
    CalculationFactory.register_calculation('divide')(DivideCalculation)
