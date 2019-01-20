from time import sleep
from wsgiref.simple_server import make_server

from pyramid.config import Configurator
from pyramid.events import NewRequest
from pyramid.view import view_config

from robotic.server_robot_simulation import ServerRobotSimulation
from robotic.talkative_robot import TalkativeRobot

robot = TalkativeRobot()
simulator = ServerRobotSimulation(robot)


def add_cors_headers_response_callback(event):
    def cors_headers(request, response):
        response.headers.update({
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST,GET,DELETE,PUT,OPTIONS',
            'Access-Control-Allow-Headers': 'Origin, Content-Type, Accept, Authorization',
            'Access-Control-Allow-Credentials': 'true',
            'Access-Control-Max-Age': '1728000',
        })

    event.request.add_response_callback(cors_headers)


@view_config(
    route_name='reset',
    renderer='json'
)
def reset(request):
    robot.reset()
    simulator.reset()
    return {'status': 'ok'}


@view_config(
    route_name='home',
    renderer='json'
)
def home(request):
    if request.method == 'POST':
        instructions = request.json_body['instructions']
        simulator.input(instructions)
        out = {'errors': simulator.errors,
               'output': simulator.output.getvalue()}
        if robot.position is not None:
            out['position'] = {
                'x': robot.position[0],
                'y': robot.position[1]
            }
        if robot.direction is not None:
            out['direction'] = robot.direction.name
        sleep(0.2)
        return out


if __name__ == '__main__':
    with Configurator() as config:
        config.add_subscriber(add_cors_headers_response_callback, NewRequest)
        config.add_route('home', '/')
        config.add_route('reset', '/reset')
        config.scan()
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
