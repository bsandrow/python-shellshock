
.PHONY: clean

clean:
	find . -iname '*.pyc' -print0 | xargs -r0 rm
