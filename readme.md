# Gantt Diagram Maker

A simple script that construct a Gantt diagram using plotly. It also supports milestones.
The code is provided with a small real example of tasks and deliverables as milestones.

To run the example
```
python main.py tasks.csv --m milestones.csv
```

Also, the same diagram without the milestones
```
python main.py tasks.csv
```

## TODO

1. Add other options to argparser for the name of the columns
2. Allow other date formats, probably through argparser
3. Allow other color configurations
4. Allow option to save to file