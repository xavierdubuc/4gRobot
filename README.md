# 4gRobot

Here is my resolution of the exercice proposed by [4GClinical](https://4gclinical.com/home).

## Installing / Getting started

You just need python 3.5.2, it may work on other versions but I developed and tested it on this version.

### Run

You can execute the `run.py` script which allows you to interact with a robot.
```shell
python run.py -i
```

The script allows multiple "mode" which can be enabled through script options:
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