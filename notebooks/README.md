# Jupyter Notebooks

This folder contains Jupyter notebooks used as laboratory notes for experiments and
analysis.

The canonical experiment protocols remain in `docs/experiments/`. The notebooks are
complementary records for:

- summarizing the experiment context;
- copying validated commands used in external terminals;
- storing observed results and evidence notes;
- adding small analysis cells for logs, CSV files, JSON outputs, or generated data;
- preparing reusable figures or tables for future TFM writing.

## Safety Boundary

Do not use notebooks as the primary control surface for real robot motion.

For Doosan motion experiments, execute ROS 2 launch commands and service calls from
validated terminals or scripts. Use the notebook to document the command, paste the
result, and analyze exported evidence.

## Structure

- `evidence/`: external evidence files referenced by notebooks, organized per experiment.
- `experiments/`: notebooks paired with experiment files in `docs/experiments/`.
- `templates/`: reusable notebook templates.
