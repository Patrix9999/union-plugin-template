# How to produce symbol file(s)

## With IDA
1. Open Up IDA (9.x)
2. Open up the disassembled `Gothic executable project`
3. File->Script File (pick `generate.py` from this folder)
4. Congratulations, near your `Gothic executable project` should be file named `IDA_PROJECT_NAME.txt`, just copy it here and rename it

## With Gothic API
1. Make sure you have gothic-api fetched as a submodule in `dependencies/union/gothic-api/`
2. Form the template directory run `python -u resources/generate-names.py dependencies/union/gothic-api/ZenGin/<ENGINE>/Names.txt -o <output>.txt` (replace `<ENGINE>` with your engine version - `Gothic_I_Classic`, `Gothic_I_Addon`, `Gothic_II_Classic`, `Gothic_II_Addon` and `<output>` with the desired file name)
3. Congratulations, you should have `<output>.txt` file generated, just copy it here and rename it