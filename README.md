# 4gRobot

Here is my resolution of the exercice proposed by [4GClinical](https://4gclinical.com/home).

## Client/Server Version

### Installing / Getting started

#### Server
You need python 3.5.2 but you also need to install project dependencies by running :

```bash
pip install -r requirements.txt
```

#### Client

You need angular cli tools, you can get it by running : 

```bash
npm install -g @angular/cli
```

*Be aware that Angular requires Node.js version 8.x or 10.x.
To check your version, run node -v in a terminal/console window.
To get Node.js, go to [nodejs.org](https://nodejs.org).*

Then you can to install the project dependencies by running :
 
```bash
npm install
```

### Run

You need to run the pyramid server :
```bash
python server.py
```

And also the Angular builtin server to launch the client side.
```bash
ng serve --open
```

### Tests

I did no test for this part as I did not have the time...

### Future thoughts

- Make e2e tests in client app
- Make robot name editable in client app
- Make environment editable in client app
- Make the app responsive
- Add comments to the app
- Improve typescript utilisation (I'm still "too" close of javascript I think)

## CLI Version

### Installing / Getting started

You need python 3.5.2, it may work on other versions but I developed and tested it on this version.

### Run

You can execute the `run.py` script which allows you to interact with a robot.
```shell
python run.py -i
```

The script allows multiple "modes" which can be enabled through script options:
- `--interactive` or `-i` : *interactive* mode in which you can send instructions to the robot in real time
- `--file` or `-f filepath` : *file* mode allows you to give the path to a file containing instructions for the robot
(the file `example.txt` is here for you to try) :
```shell
    python run.py -f example.txt
```
- `--execute` or `-x` to give instructions directly in the standard input
```shell
    python run.py -x "PLACE 0,0,NORTH" "MOVE" "REPORT"
```   

Other options are also available to configure the experience :
- `--x-size` : determine the size of the environment on x axis (default 5)
- `--y-size` : determine the size of the environment on y axis (default x-size)
- `--verbose` or `-v` : show information on the robot situation in the environment after each instruction
(except from REPORT)
- `--name` : the name you want to give to the robot (default Alice)

### Tests

Some unit tests are provided, you can run them with following command.

```shell
 python -m unittest discover -s tests
```