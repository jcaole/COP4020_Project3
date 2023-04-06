echo run python lisp_fsa_gen.py fsa.txt
python lisp_fsa_gen.py fsa.txt

echo run timeout for 2 seconds
timeout /t 2
echo.

echo Generating Program
xlwin32 part2.lsp