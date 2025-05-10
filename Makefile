BOARD = qtpy_m0
PORT = /media/$(USER)/CIRCUITPY
SRC = code.py

flash:
	@if [ -d "$(PORT)" ]; then \
		echo "Flashing $(SRC) to $(PORT)..."; \
		cp $(SRC) $(PORT)/; \
	else \
		echo "Error: $(PORT) not found. Is the board connected and running CircuitPython?"; \
		exit 1; \
	fi

tty:
	screen /dev/ttyACM1 115200
