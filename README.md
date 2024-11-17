# Streaming server

This project is a basic server capable of streaming live video from a capture card

The cctv videos input are displayed in a grid, so some cropping is done to determine which video to display.

Only one cell is streamed at a time to save on costs.

This project also adds some opencv magic to add in people detection

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies

A makefile has been setup for simplicity

```bash
make install
```

## Tests

```bash
make test
```