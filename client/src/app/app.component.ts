import { Component, OnInit } from '@angular/core';
import { Robot } from './robot/robot.component';
import { Direction, InstructionService } from './instruction.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.pug',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  robot: Robot = { position: { x: -1, y: -1 }, direction: Direction.WEST };

  constructor(private instruction_service: InstructionService) { }

  ngOnInit() {
    this.instruction_service.reset().subscribe(state => { console.log('initialized !'); });
  }

  reset(): void {
    window.location.reload();
  }
}
