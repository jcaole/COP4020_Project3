echo run python lisp_fsa_gen.py fsa.txt
python fsa.py fsa.txt

echo run timeout for 2 seconds
timeout /t 2

echo run part 2: generate part2.lsp
xlwin32 part2.lsp