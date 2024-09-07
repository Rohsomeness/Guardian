# Guardian
Smart manager for who enters apartment

## How to use:
Make venv using requirements.txt. Run guardian.py, setting visualize to True if you want visual output and false otherwise like so:

`python guardian.py -v -p`

## How to add people:
1) Add photos to `dataset` folder. Label folder as `<name>_<num>`
2) Run `encode_faces.py` to make embeddings for faces.
3) Add lines in the `encodings.pickle` file mapping `<name>` to list of phrases. See commented out lines in main method on how to do this.
