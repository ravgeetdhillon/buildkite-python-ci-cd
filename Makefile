freeze: 
	pip freeze | grep -v "pkg_resources" > requirements.txt