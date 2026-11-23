
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = BASE_DIR / "scripts"

pipeline_steps = [
    "extract.py",
    "transform.py",
    "validate.py",
    "load.py"
]

for step in pipeline_steps:
    script_path = SCRIPTS_DIR / step

    print(f"\nRunning {step}...", flush=True)

    try:
        subprocess.run(
            [sys.executable, str(script_path)],
            cwd=str(BASE_DIR),
            check=True
        )
    except subprocess.CalledProcessError:
        print(f"\nPipeline stopped because {step} failed.")
        raise SystemExit(1)

print("\nETL PIPELINE COMPLETED SUCCESSFULLY!")
