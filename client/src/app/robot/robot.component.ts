import { Component, OnInit, Input } from '@angular/core';
import { Position } from '../instruction.service';

export interface Robot {
  direction: string;
  position: Position;
}

@Component({
  selector: 'robot',
  templateUrl: './robot.component.pug',
  styleUrls: ['./robot.component.scss']
})
export class RobotComponent implements OnInit {
  @Input() robot: Robot;

  constructor() { }

  ngOnInit() {
  }

  get_direction(): string {
    if (!!this.robot && !!this.robot.direction) {
      return this.robot.direction.toLowerCase();
    }
  }

}
