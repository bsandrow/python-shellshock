
.PHONY: clean

clean:
	find . -iname '*.pyc' -print0 | xargs -r0 rm
	find . -iname '*.egg-info' -print0 | xargs -r0 rm -r
