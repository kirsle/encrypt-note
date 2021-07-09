ALL: run

.PHONY: run
run: clean
	./encrypt-note.py

.PHONY: clean
clean:
	if [ -d ./out ]; then rm -rf ./out; fi