# tigera-coding-challenge
Coding challenge for Tigera interview

- Written in python, using Flask
- Approximate time: 4 hours

# Docker container build/run instructions
To build & run the Docker container, enter:
```
sudo ./start.sh
```
After the container builds and runs, it can be accessed via http://127.0.0.1/.

# Unit tests instructions
To run unit tests, install pytest if it's not installed already:
```
pip install pytest
```
Then, enter the following to run the unit tests:
```
cd tests
pytest
```

# Notes
- If the application fails to access either the name generator or joke generator URL, it will display a default name or default joke
