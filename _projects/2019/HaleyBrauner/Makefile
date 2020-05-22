# Make will run this by default, which checks if any html files need to be updated.
.PHONY:htmls 
	
# Save the names of all the md files in an array
MD_FILES=$(wildcard *.md)

# Generate names of html files corresponding to the md files
HTML_FILES=$(patsubst %.md, %.html, $(MD_FILES))

# This will force Make to check every html file in the list
htmls: $(HTML_FILES)

# This will run each html file that needs to be updated
%.html: %.md
	pandoc -s --mathjax -o $*.html $<

# Clean up - delete all the html files
.PHONY: clean
clean:
	rm *.html
