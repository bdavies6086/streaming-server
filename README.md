# Streaming server

This project is a basic server capable of streaming live video from a capture card

The cctv videos input are displayed in a grid, so some cropping is done to determine which video to display.

Only one cell is streamed at a time to save on costs.

This project also adds some opencv magic to add in people detection

As you can see the in the files, the project does make quite a bit of use of shared state in the modules. Which is a big no no when a server is handling multiple tenants. In this case its for a personal project and will have 1 user interracting with it at one time, so isn't an issue.

If multiple tenants were to use this server, they'd be competing for which channel to watch (the channels on the 
frontend would also get out of sync without some sort of server sent events configured (but thats overkill for this project.))

A simple way to make this stateless would be to render a stream per camera, but that would cost more £££

Another way to remove state could be to crop on the frontend, and stream all cameras as part of a single stream. But the thought of some horrible css hack to crop videos in the frontend made me feel nauseaous.

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