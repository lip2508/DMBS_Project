from dataclasses import dataclass
from typing import List, Dict


@dataclass
class RecoveryTechnique:
    name: str
    consistency_score: float
    runtime_perf: float
    recovery_perf: float
    complexity_score: float
    scalability_score: float


def combined_performance(tech: RecoveryTechnique) -> float:
    return (tech.runtime_perf + tech.recovery_perf) / 2


def evaluate_techniques(techniques: List[RecoveryTechnique]) -> Dict[str, Dict[str, float]]:
    evaluation = {}

    for tech in techniques:
        evaluation[tech.name] = {
            "Data consistency & correctness": tech.consistency_score,
            "Performance (runtime + recovery)": combined_performance(tech),
            "Implementation complexity": tech.complexity_score,
            "Scalability": tech.scalability_score,
        }

    return evaluation


def rank_techniques(evaluation: Dict[str, Dict[str, float]]) -> List[tuple]:
    rankings = []

    for name, metrics in evaluation.items():
        score = (
            0.3 * metrics["Data consistency & correctness"] +
            0.3 * metrics["Performance (runtime + recovery)"] +
            0.25 * metrics["Scalability"] -
            0.15 * metrics["Implementation complexity"]
        )
        rankings.append((name, round(score, 2)))

    return sorted(rankings, key=lambda x: x[1], reverse=True)



# Example instantiation (includes NoSQL DBMS)

if __name__ == "__main__":
    techniques = [
        RecoveryTechnique(
            name="ARIES (Relational)",
            consistency_score=9.5,
            runtime_perf=9.0,
            recovery_perf=8.5,
            complexity_score=8.0,
            scalability_score=9.5
        ),
        RecoveryTechnique(
            name="Shadow Paging",
            consistency_score=8.5,
            runtime_perf=6.5,
            recovery_perf=9.0,
            complexity_score=5.5,
            scalability_score=6.5
        ),
        RecoveryTechnique(
            name="Checkpointing",
            consistency_score=8.8,
            runtime_perf=8.0,
            recovery_perf=7.5,
            complexity_score=6.5,
            scalability_score=8.0
        ),
        RecoveryTechnique(
            name="MongoDB (WiredTiger, NoSQL)",
            # WAL + checkpoints + replication-based recovery
            consistency_score=8.8,
            runtime_perf=8.5,
            recovery_perf=8.0,
            complexity_score=6.5,
            scalability_score=9.0
        ),
    ]

    evaluation = evaluate_techniques(techniques)
    rankings = rank_techniques(evaluation)

    print("Comparative Evaluation of Recovery Techniques:\n")
    for tech, metrics in evaluation.items():
        print(f"{tech}:")
        for k, v in metrics.items():
            print(f"  {k}: {v}")
        print()

    print("Overall Ranking:")
    for name, score in rankings:
        print(f"{name}: {score}")
