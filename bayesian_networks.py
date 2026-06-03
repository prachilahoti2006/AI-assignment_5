from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define Bayesian Network structure
network = BayesianNetwork([
    ('Rain', 'Traffic'),
    ('Traffic', 'Late')
])

# Probability of Rain
rain_cpd = TabularCPD(
    variable='Rain',
    variable_card=2,
    values=[
        [0.7],
        [0.3]
    ]
)

# Probability of Traffic given Rain
traffic_cpd = TabularCPD(
    variable='Traffic',
    variable_card=2,
    values=[
        [0.8, 0.2],
        [0.2, 0.8]
    ],
    evidence=['Rain'],
    evidence_card=[2]
)

# Probability of being Late given Traffic
late_cpd = TabularCPD(
    variable='Late',
    variable_card=2,
    values=[
        [0.9, 0.1],
        [0.1, 0.9]
    ],
    evidence=['Traffic'],
    evidence_card=[2]
)

# Add CPDs to network
network.add_cpds(
    rain_cpd,
    traffic_cpd,
    late_cpd
)

# Create inference engine
engine = VariableElimination(network)

# Query P(Late | Rain = 1)
query_result = engine.query(
    variables=['Late'],
    evidence={'Rain': 1}
)

print(query_result)
